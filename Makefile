all:
	@echo "Please run 'make dist' or 'make upload'"

test:
	python ./setup.py test

clean:
	rm -rf ./build
	rm -rf ./dist

dist: clean
	python ./setup.py bdist_wheel

upload: dist
	twine upload ./dist/*
