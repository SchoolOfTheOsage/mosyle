# Building and Publishing

## Local Editable Install

`pip install -e .`

## Version Numbers

In the standard configuration setuptools_scm takes a look at three things:

latest tag (with a version number)
the distance to this tag (e.g. number of revisions since latest tag)
workdir state (e.g. uncommitted changes since latest tag)
and uses roughly the following logic to render the version:

no distance and clean:
{tag}
distance and clean:
{next_version}.dev{distance}+{scm letter}{revision hash}
no distance and not clean:
{tag}+dYYYYMMDD
distance and not clean:
{next_version}.dev{distance}+{scm letter}{revision hash}.dYYYYMMDD
The next version is calculated by adding 1 to the last numeric component of the tag.

For Git projects, the version relies on git describe, so you will see an additional g prepended to the {revision hash}.

Semantic Versioning (SemVer)

Due to the default behavior it's necessary to always include a patch version (the 3 in 1.2.3), or else the automatic guessing will increment the wrong part of the SemVer (e.g. tag 2.0 results in 2.1.devX instead of 2.0.1.devX). So please make sure to tag accordingly.

Note

Future versions of setuptools_scm will switch to SemVer by default hiding the the old behavior as an configurable option.

Create Tag: `git tag -a v0.0.0 -m "Version 0.0.0"`

Push Tag: `git push origin v0.0.0`

## Build

`python -m build`

## Publish

### Test

`twine upload --repository-url=https://test.pypi.org/legacy/ dist/*`

### Production

`twine upload dist/*`
