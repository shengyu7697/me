all:
	rm -rf dist
	mkdir dist
	python render.py
	cp -r static dist
