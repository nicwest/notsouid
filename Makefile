.PHONY: init test

init:
	virtualenv -p python3 venv
	./venv/bin/pip install pip --upgrade
	./venv/bin/pip install -r requirements-test.txt
	./venv/bin/pip install -e .

test:
	flake8 notsouid
	py.test
