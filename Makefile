all:
	rm -rf dist
	mkdir dist
	python render.py
	cp -r static dist

deploy:
	git subtree push --prefix dist origin gh-pages
	@# Deploy to `gh-pages` from a `dist` folder on the master branch.
	@# Ref https://gist.github.com/cobyism/4730490