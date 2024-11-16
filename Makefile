generate-doc:
	@sphinx-apidoc -f -o docs/source/ src/

build-doc:
	@sphinx-build -b html docs/source docs/build

open-doc:
	@xdg-open docs/build/index.html