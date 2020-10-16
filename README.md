# HEPData pyhf extractor

Python package to extract and summarize information from the [pyhf][pyhf-repository] submissions.


## About
This package aims to define the post-submission computations to summarize the information that pyhf
submissions hold. Its evolution is coupled with the [hepdata-pyhf-visualizer][pyhf-visualizer-repo]
JS package, as this one renders what gets summarized by this component.


## Development
The package uses [Black][black-web], in addition to [pre-commit][pre-commit-web] to control its style.

To install the pre-commit hook:
```sh
pre-commit install
```

To check for style inconsistencies:
```sh
make check
```


## Testing
The package uses [pytest][pytest-web] to run all the tests:

```sh
make test
```


## Release tagging
To tag a particular commit to mark a release:

```sh
make tag
```


[black-web]: https://black.readthedocs.io/en/stable/
[pre-commit-web]: https://pre-commit.com/
[pyhf-repository]: https://github.com/scikit-hep/pyhf
[pyhf-visualizer-repo]: https://github.com/HEPData/hepdata-pyhf-visualizer
[pytest-web]: https://docs.pytest.org/en/stable/
