# HEPData pyhf extractor

[![GH Actions status][badge-actions-image]][badge-actions-status]
[![Coverage status][badge-coverage-image]][badge-coverage-status]
[![Project license][badge-license-image]][badge-license-ref] 

Python package to extract and summarize information from the [pyhf][pyhf-repository] submissions.


## About
This package aims to define the post-submission computations to summarize the information that pyhf
submissions hold. Its evolution is coupled with the [hepdata-pyhf-visualizer][pyhf-visualizer-repo]
JS package, as this one renders what gets summarized by this component.


## Installation

Via pip:
```sh
pip install hepdata-pyhf-extractor
```

Via GitHub (for developers):
```
git clone https://github.com/HEPData/hepdata-pyhf-extractor
cd hepdata-pyhf-extractor
pip install ".[dev]"
```


## Usage

To extract basic information out of a `pyhf` Pallet file, the summarizers can:

A) Receive a Pallet file path for them to open and read it internally.
```python3
from pyhf_extractor import V1PalletSummarizer

# The provided file can be either .json.gz or .json
pallet_path = "example_pallet.json.gz"
pallet_path = "example_pallet.json"

summarizer = V1PalletSummarizer(pallet_path=pallet_path)
summary = summarizer.summarize()
```

B) Receive an already parsed Pallet file:
```python3
import gzip
import json
from pyhf_extractor import V1PalletSummarizer

pallet_path = "example_pallet.json.gz"

with gzip.open(pallet_path) as file:
    pallet_data = json.load(file)           

summarizer = V1PalletSummarizer(pallet_data=pallet_data)
summary = summarizer.summarize()
```


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

### Testing
The package uses [pytest][pytest-web] to run all the tests:

```sh
make test
```

### Release version
To bump and tag a particular commit to mark a release:

```sh
# Any of the following options
make tag-major
make tag-minor
make tag-patch
```


[badge-actions-image]: https://github.com/HEPData/hepdata-pyhf-extractor/workflows/Continuous%20Integration/badge.svg?branch=main
[badge-actions-status]: https://github.com/HEPData/hepdata-pyhf-extractor/actions?query=workflow%3A%22Continuous%20Integration%22+branch%3Amain
[badge-coverage-image]: https://coveralls.io/repos/github/HEPData/hepdata-pyhf-extractor/badge.svg?branch=main
[badge-coverage-status]: https://coveralls.io/github/HEPData/hepdata-pyhf-extractor?branch=main
[badge-license-image]: https://img.shields.io/badge/License-GPL%20v2-blue.svg
[badge-license-ref]: https://opensource.org/licenses/GPL-2.0
[black-web]: https://black.readthedocs.io/en/stable/
[pre-commit-web]: https://pre-commit.com/
[pyhf-repository]: https://github.com/scikit-hep/pyhf
[pyhf-visualizer-repo]: https://github.com/HEPData/hepdata-pyhf-visualizer
[pytest-web]: https://docs.pytest.org/en/stable/
