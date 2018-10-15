publish:
	rm -rf *.egg-info build/ dist/
	python setup.py bdist_wheel sdist
	twine upload -r pypi dist/*
	rm -rf *.egg-info build/ dist/
