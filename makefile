default: write

write: pelican_env/bin/pelican
	pelican_env/bin/pelican -s pelicanconf.py -t theme -o etc

test: pelican_env/bin/pelican
	pelican_env/bin/pelican -s pelicanconf_test.py -t theme -o etc

clean:
	rm -rf etc/*

# installing pelican and the appropriate dependencies
pelican_env/bin/pelican: 
	python3 -m venv pelican_env
	pelican_env/bin/python3 -m pip install -r requirements.txt