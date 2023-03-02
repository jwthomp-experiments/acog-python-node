usage:
	@echo "Usage:"
	@echo "make install:        Install deps"

install: export PIPENV_VENV_IN_PROJECT=1
install: 
	pipenv --python 3.9 install --dev

shell:
	pipenv run bash
