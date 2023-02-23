# Building and Publishing

## Build

`pip -m build . --wheel`

## Publish

### Test

`twine upload --repository-url=https://test.pypi.org/legacy/ dist/*`

### Production

`twine upload dist/*`