update-and-push:
	sh ./update-and-push.sh version

nvenv: make-venv

make-venv:
	pip install virtualenv
	python -m virtualenv ~/nvenv --no-site-packages

install-deps: make-venv
	~/nvenv/bin/pip install -Ur requirements.txt
	~/nvenv/bin/pip install coverage nose codacy-coverage

test-unit:
	. ~/nvenv/bin/activate; \
	python -m nose2; \
	mkdir ~/test-results
	mv nose2-junit.xml ~/test-results/noselog$(PYTHON_VERSION).xml; \

upload-coverage:
	. ~/nvenv/bin/activate
	~/nvenv/bin/coverage xml
	~/nvenv/bin/python-codacy-coverage -r coverage.xml

verify-git-tag: make-venv
	. ~/nvenv/bin/activate
	~/nvenv/bin/python setup.py verify

dist:
	# create a source distribution
	~/nvenv/bin/python setup.py sdist

	# create a wheel
	~/nvenv/bin/python setup.py bdist_wheel

upload-to-pypi:
	. ~/nvenv/bin/activate
	~/nvenv/bin/twine upload dist/*