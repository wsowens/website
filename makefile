default: write

write: 
	pelican -s pelicanconf.py -t theme -o etc

test:
	pelican -s pelicanconf_test.py -t theme -o etc

clean:
	rm -rf etc/*
