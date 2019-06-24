update-and-push:
	sh ./update-and-push.sh version

nvenv: make-venv

make-venv:
	pip install virtualenv; \
	python -m virtualenv ~/nvenv --no-site-packages; \

install-deps: make-venv
	. ~/nvenv/bin/activate; \
	pip install -Ur requirements.txt; \
	pip install coverage nose codacy-coverage; \

test-unit:
	. ~/nvenv/bin/activate; \
	python -m nose2; \
	mkdir ~/test-results
	cp nose2-junit.xml ~/test-results/noselog$(PYTHON_VERSION).xml; \

upload-coverage:
	. ~/nvenv/bin/activate; \
	cd /tmp/workspace/test-results
	coverage xml; \
	python-codacy-coverage -r coverage.xml; \

verify-git-tag: make-venv
	. ~/nvenv/bin/activate; \
	~/nvenv/bin/python setup.py verify; \

dist:
	. ~/nvenv/bin/activate; \
	python setup.py sdist; \
	python setup.py bdist_wheel; \

upload-to-pypi:
	. ~/nvenv/bin/activate; \
	twine upload dist/*; \