.PHONY: test run build-deb clean

test:
	python3 -m pytest

run:
	PYTHONPATH=src python3 -m lsusers

build-deb:
	dpkg-buildpackage -us -uc -b

clean:
	rm -rf .pytest_cache build dist *.egg-info src/*.egg-info debian/.debhelper debian/lsusers debian/files debian/debhelper-build-stamp
