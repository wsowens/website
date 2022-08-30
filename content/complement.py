import re
"""A function to complement FASTA-formatted files implemented in various ways.
Benchmarks are included near the bottom.

See accompanying blogpost: https://ovvens.com/etc/1000x
The E. coli genome "ecoli.fa" was downloaded from NCBI:
https://www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=161521

This requires pytest and pytest-benchmark:
`pip install pytest pytest-benchmark`

To run the tests (including the benchmarks), simply run
`pytest complement.py`
"""

# Original function


def complement_fasta(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    in_file = open(in_name)
    base = in_file.read(1)
    in_comment = False
    while base:
        out_f = open(out_name, 'a')
        if in_comment:
            if base == "\n":
                in_comment = False
            out_f.write(base)
        else:
            if base == ">":
                in_comment = True
                out_f.write(base)
            elif base == "A":
                out_f.write("T")
            elif base == "C":
                out_f.write("G")
            elif base == "G":
                out_f.write("C")
            elif base == "T":
                out_f.write("A")
            else:
                out_f.write(base)
        base = in_file.read(1)


# Fixing the open file every iteration bug


def complement_fasta2(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    in_file = open(in_name)
    out_f = open(out_name, 'w')
    base = in_file.read(1)
    in_comment = False
    while base:
        if in_comment:
            if base == "\n":
                in_comment = False
            out_f.write(base)
        else:
            if base == ">":
                in_comment = True
                out_f.write(base)
            elif base == "A":
                out_f.write("T")
            elif base == "C":
                out_f.write("G")
            elif base == "G":
                out_f.write("C")
            elif base == "T":
                out_f.write("A")
            else:
                out_f.write(base)
        base = in_file.read(1)


# Checking how bad it is to read just one byte when we don't have Python's
# buffering to save us.


def complement_fasta2_unbuffered(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    in_file = open(in_name, buffering=2)
    out_f = open(out_name, 'w', buffering=2)
    base = in_file.read(1)
    in_comment = False
    while base:
        if in_comment:
            if base == "\n":
                in_comment = False
            out_f.write(base)
        else:
            if base == ">":
                in_comment = True
                out_f.write(base)
            elif base == "A":
                out_f.write("T")
            elif base == "C":
                out_f.write("G")
            elif base == "G":
                out_f.write("C")
            elif base == "T":
                out_f.write("A")
            else:
                out_f.write(base)
        out_f.flush()
        base = in_file.read(1)


# Iterating directly over the File objects instead of reading byte-by-byte


def complement_fasta3(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    in_file = open(in_name)
    out_f = open(out_name, 'w')
    for line in in_file:
        if line.startswith(">"):
            out_f.write(line)
        else:
            for base in line:
                if base == "A":
                    out_f.write("T")
                elif base == "C":
                    out_f.write("G")
                elif base == "G":
                    out_f.write("C")
                elif base == "T":
                    out_f.write("A")
                else:
                    out_f.write(base)


# Using str.translate instead of if-elif-else


def complement_fasta4(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    base_complements = str.maketrans({"A": "T", "C": "G", "G": "C", "T": "A"})
    in_file = open(in_name)
    out_f = open(out_name, 'w')
    for line in in_file:
        if line.startswith(">"):
            out_f.write(line)
        else:
            line = line.translate(base_complements)
            out_f.write(line)


# functions 5-7 take advantage of reading the entire file into memory at once
# While this is probably a valid technique in many cases, it doesn't scale
# well when you have multiple gigabyte references files.
# Thus, I've omitted these files from the discussion, but I'm keeping them
# for posterity.
# In particular, complement_fasta7 got an average runtime of only 12 ms,
# which is an over 6000x improvement over our original function.

# Same as above, but read the entire file in, and split with a regex


def complement_fasta5(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    base_complements = str.maketrans({"A": "T", "C": "G", "G": "C", "T": "A"})
    in_data = open(in_name).read()
    out_f = open(out_name, 'w')
    chunks = re.split(r"(>.*\n)", in_data)

    for (index, chunk) in enumerate(chunks):
        if index % 2 == 0:
            out_f.write(chunk.translate(base_complements))
        else:
            out_f.write(chunk)


# Read the entire file in, split with a slightly more intuitive regex


def complement_fasta6(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    base_complements = str.maketrans({"A": "T", "C": "G", "G": "C", "T": "A"})
    in_data = open(in_name).read()
    out_f = open(out_name, 'w')

    # slightly more intuitive way of writing it
    chunks = re.findall(r"(>.*?\n)([^>]*)", in_data)
    for (header, seq) in chunks:
        out_f.write(header)
        out_f.write(seq.translate(base_complements))


# Best method: Simply find the beginning and ends of headers using str.find


def complement_fasta7(in_name, out_name):
    # read FASTA with name [in_name], complement, and write to [out_name]
    base_complements = str.maketrans({"A": "T", "C": "G", "G": "C", "T": "A"})
    in_data = open(in_name).read()
    out_f = open(out_name, 'w')

    header_start = 0
    while (header_start := in_data.find(">", header_start)) != -1:
        header_end = in_data.find("\n", header_start) + 1
        seq_end = in_data.find(">", header_end)
        seq_end = len(in_data) if seq_end == -1 else seq_end
        out_f.write(in_data[header_start:header_end])
        out_f.write(in_data[header_end:seq_end].translate(base_complements))
        header_start = seq_end


# Benchmarks for complement_fasta_functions


def test_complement_fasta(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement1_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    # warning: really slow, consider changing rounds to 1
    benchmark.pedantic(complement_fasta, setup=setup, rounds=10)


def test_complement_fasta2(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement2_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta2, setup=setup, rounds=10)


def test_complement_fasta2_unbuffered(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement2_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta2_unbuffered, setup=setup, rounds=10)


def test_complement_fasta3(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement3_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta3, setup=setup, rounds=10)


def test_complement_fasta4(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement4_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta4, setup=setup, rounds=10)


def test_complement_fasta5(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement5_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta5, setup=setup, rounds=10)


def test_complement_fasta6(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement6_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta5, setup=setup, rounds=10)


def test_complement_fasta7(tmp_path, benchmark):

    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/complement7_{count}.fa"
        count += 1
        return ("ecoli.fa", output), {}

    benchmark.pedantic(complement_fasta7, setup=setup, rounds=10)


# Saving benchmark results as a backup
# ----------------------------------------------------------------------------------------------------- benchmark: 8 tests ----------------------------------------------------------------------------------------------------
# Name (time in ms)                             Min                    Max                   Mean                StdDev                 Median                   IQR            Outliers      OPS            Rounds  Iterations
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_complement_fasta7                    10.7533 (1.0)          13.1810 (1.0)          11.4152 (1.0)          0.7183 (1.14)         11.1734 (1.0)          0.7008 (1.0)           1;1  87.6028 (1.0)          10           1
# test_complement_fasta5                    12.7415 (1.18)         14.5423 (1.10)         13.5407 (1.19)         0.6326 (1.0)          13.4603 (1.20)         1.0289 (1.47)          4;0  73.8516 (0.84)         10           1
# test_complement_fasta6                    13.0391 (1.21)         16.1790 (1.23)         13.6864 (1.20)         0.9514 (1.50)         13.4213 (1.20)         0.8218 (1.17)          1;1  73.0653 (0.83)         10           1
# test_complement_fasta4                    33.0590 (3.07)         35.9166 (2.72)         34.1243 (2.99)         0.8886 (1.40)         33.9598 (3.04)         1.1938 (1.70)          3;0  29.3046 (0.33)         10           1
# test_complement_fasta3                   565.2323 (52.56)       700.0390 (53.11)       594.9941 (52.12)       38.9925 (61.64)       589.5941 (52.77)       25.7267 (36.71)         1;1   1.6807 (0.02)         10           1
# test_complement_fasta2                 1,060.2358 (98.60)     1,129.6039 (85.70)     1,093.7009 (95.81)       25.0882 (39.66)     1,090.1817 (97.57)       49.0786 (70.04)         5;0   0.9143 (0.01)         10           1
# test_complement_fasta2_unbuffered      5,068.5335 (471.34)    5,325.5667 (404.03)    5,164.5275 (452.43)      76.4460 (120.85)    5,159.2483 (461.75)     104.0034 (148.41)        3;0   0.1936 (0.00)         10           1
# test_complement_fasta                 70,049.2282 (>1000.0)  73,838.2762 (>1000.0)  72,181.3647 (>1000.0)  1,357.6790 (>1000.0)  72,451.3550 (>1000.0)  2,524.1025 (>1000.0)       4;0   0.0139 (0.00)         10           1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Open file vs. write one-byte benchmarks


def open_file(fname):
    open(fname, 'a')


def test_open_file(tmp_path, benchmark):
    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/output_file_{count}.fa"
        count += 1
        return (output, ), {}

    benchmark.pedantic(open_file, setup=setup, rounds=10000)


def write_file(file):
    file.write("a")


def test_write_file(tmp_path, benchmark):
    count = 0

    def setup():
        nonlocal count
        output = f"{tmp_path}/output_byte_{count}.fa"
        output = open(output, 'w')
        count += 1
        return (output, ), {}

    benchmark.pedantic(write_file, setup=setup, rounds=10000)


def test_write_file_buffered(tmp_path, benchmark):
    output = f"{tmp_path}/output_byte_buffered.fa"
    output = open(output, 'w')

    def setup():
        nonlocal output
        return (output, ), {}

    benchmark.pedantic(write_file, setup=setup, rounds=10000)
