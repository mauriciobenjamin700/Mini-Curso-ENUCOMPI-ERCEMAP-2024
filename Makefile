start-doc:
	@sphinx-quickstart docs

generate-doc:
	@sphinx-apidoc -f -o docs/source/ src/

build-doc:
	@sphinx-build -M html docs/source docs/build

build-html:
	cd docs
	make html
	cd ..

open-doc:
	@xdg-open docs/build/index.html