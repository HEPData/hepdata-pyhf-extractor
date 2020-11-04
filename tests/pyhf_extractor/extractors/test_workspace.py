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

from src.pyhf_extractor.extractors import V1WorkspaceExtractor

from .values import WORKSPACE_V1_CHANNELS
from ..helpers import get_file_path


@pytest.fixture(scope="module")
def workspace_v1() -> dict:
    """ Unzips and parses a test Workspace V1 """

    test_file_name = "workspace_v1.json.gz"
    test_file_path = get_file_path(test_file_name)

    with gzip.open(test_file_path) as file:
        return json.load(file)


def test_v1_workspace_extractor_observations(workspace_v1: dict):
    """
    Test the correct info extraction of the observations within a pyhf Workspace V1
    :param workspace_v1: Workspace dictionary
    """

    extractor = V1WorkspaceExtractor()
    obs = extractor.get_observations(workspace_v1)

    assert obs == {
        "WREM_cuts": 1,
        "STCREM_cuts": 1,
        "TRHMEM_cuts": 1,
        "TRMMEM_cuts": 1,
        "TRLMEM_cuts": 1,
        "SRHMEM_mct2": 3,
        "SRMMEM_mct2": 3,
        "SRLMEM_mct2": 3,
    }


def test_v1_workspace_extractor_samples(workspace_v1: dict):
    """
    Test the correct info extraction of the samples within a pyhf Workspace V1
    :param workspace_v1: Workspace dictionary
    """

    extractor = V1WorkspaceExtractor()
    samples = extractor.get_samples(workspace_v1["channels"][0])

    assert samples == [
        {"name": "ttbar"},
        {"name": "singletop"},
        {"name": "wjets"},
        {"name": "diboson"},
        {"name": "multiboson"},
        {"name": "vh"},
        {"name": "zjets"},
        {"name": "tth"},
        {"name": "ttv"},
    ]


def test_v1_workspace_extractor_channels(workspace_v1: dict):
    """
    Test the correct info extraction of the channels within a pyhf Workspace V1
    :param workspace_v1: Workspace dictionary
    """

    extractor = V1WorkspaceExtractor()
    channels = extractor.get_channels(workspace_v1)

    assert channels == WORKSPACE_V1_CHANNELS


def test_v1_workspace_extractor(workspace_v1: dict):
    """
    Test the correct info extraction of a pyhf Workspace V1
    :param workspace_v1: Workspace dictionary
    """

    extractor = V1WorkspaceExtractor()
    info = extractor.extract_info(workspace_v1)

    assert info["version"] == "1.0.0"
    assert info["channels"] == WORKSPACE_V1_CHANNELS
