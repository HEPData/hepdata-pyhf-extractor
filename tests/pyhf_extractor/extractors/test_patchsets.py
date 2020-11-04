# -*- coding: utf-8 -*-
#
# This file is part of HEPData.
# Copyright (C) 2020 CERN.
#
# HEPData is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# HEPData is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HEPData; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

import gzip
import json
import pytest

from src.pyhf_extractor.extractors import V1PatchsetExtractor

from .values import PATCHSETS_V1_METADATA
from ..helpers import get_file_path


@pytest.fixture(scope="module")
def patchsets_v1() -> dict:
    """ Unzips and parses a test Patchsets V1 """

    test_file_name = "patchsets_v1.json.gz"
    test_file_path = get_file_path(test_file_name)

    with gzip.open(test_file_path) as file:
        return json.load(file)


def test_v1_patchset_extractor(patchsets_v1: dict):
    """
    Test the correct info extraction of a pyhf Patchset V1
    :param patchsets_v1: Patchsets dictionary
    """

    extractor = V1PatchsetExtractor()
    info = extractor.extract_info(patchsets_v1[0])

    assert info["metadata"] == PATCHSETS_V1_METADATA
    assert info["version"] == "1.0.0"
    assert info["npatches"] == 125
