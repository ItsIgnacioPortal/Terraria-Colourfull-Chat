# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Do not add any dependencies that substantially (x2) increase the size of the end build.

When you're able to build successfully both the ESP and ENG versions, open a pull-request.

Appart from the following error [(why?)](https://github.com/PyCQA/pylint/issues/4584), pylint should return clean without warnings:

``E1101: Module 'requests.packages' has no 'urllib3' member (no-member)``

## Pull Request Process

1. If a new mode was added, or defaults modified, make sure to modify the README.md accordingly.
2. Increase the version numbers in setup.py to the new version that this Pull Request would represent. The versioning scheme we use is [Semantic Versioning](http://semver.org/).
3. The proposed changes must pass the CodeQL scanning CI with no warnings or errors.
4. The builds with proposed changes must pass [VirusTotal](virustotal.com) scanning with a less than 30% false-positive detection rate. 