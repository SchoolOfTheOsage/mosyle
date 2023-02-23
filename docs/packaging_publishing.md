# Building and Publishing


## Local Install

`pip install .`

## Version Numbers

The build system will fetch the latest tag from the git repository for use as the version number. If there have been commits since the tag, then the tag will be extended to represent development since the tag.

To increment the version number create a new tag on the cli or create a new release on github.

`git tag -a v0.0.0 -m "Version 0.0.0"`

## Build

`python -m build`

## Publish

### Test

`twine upload --repository-url=https://test.pypi.org/legacy/ dist/*`

### Production

`twine upload dist/*`