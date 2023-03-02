PY=./venv/bin/python3

usage:
	@echo "Usage:"
	@echo "make install:        Install deps"

install: export PIPENV_VENV_IN_PROJECT=1
install:
	virtualenv .venv
	.venv/bin/pip3 install -r requirements.txt


run:
	${PY} main.py

shell: source ./venv/bin/activate
shell:
	bash

clean:
	rm -rf .venv
	