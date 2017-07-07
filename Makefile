.PHONY: init test publish clean

init:
	virtualenv -p python3 venv
	./venv/bin/pip install pip --upgrade
	./venv/bin/pip install -r requirements-test.txt
	./venv/bin/pip install -e .

clean:
	rm -rf dist *.egg *.egg-info .cache .coverage MANIFEST

test:
	flake8 notsouid
	py.test

publish:
	pip install twine wheel --upgrade
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
	rm -fr build dist .egg notsouid.egg-info

