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

import pytest

from src.pyhf_extractor.extractors import *
from src.pyhf_extractor.summarizers import *

from .values import SUBMISSION_V1_DESCRIPTION
from .values import SUBMISSION_V1_PATCHSETS
from .values import SUBMISSION_V1_WORKSPACE
from ..helpers import get_file_path


@pytest.fixture(scope="module")
def submission_v1_path() -> str:
    """ Generates the path to the test Submission V1 """

    test_file_name = "submission_v1.json.gz"
    test_file_path = get_file_path(test_file_name)

    return test_file_path


def test_base_submission_summarizer_valid_init():
    """
    Test the correct initialization of extractors given a
    set of invalid Patchsets and Workspace versions
    """

    summarizer = BaseSubmissionSummarizer

    p_extractor = summarizer.init_patchset_extractor("X.Y.Z")
    w_extractor = summarizer.init_workspace_extractor("X.Y.Z")

    assert p_extractor.__class__ == DummyPatchsetExtractor
    assert w_extractor.__class__ == DummyWorkspaceExtractor


def test_base_submission_summarizer_invalid_init():
    """
    Test the correct initialization of extractors given a
    set of valid Patchsets and Workspace versions
    """

    summarizer = BaseSubmissionSummarizer

    p_extractor = summarizer.init_patchset_extractor("1.0.0")
    w_extractor = summarizer.init_workspace_extractor("1.0.0")

    assert p_extractor.__class__ == V1PatchsetExtractor
    assert w_extractor.__class__ == V1WorkspaceExtractor


def test_v1_submission_summarizer(submission_v1_path: str):
    """
    Test the correct generation of a summary from a pyhf Submission V1
    :param submission_v1_path: Submission file path
    """

    summarizer = V1SubmissionSummarizer(submission_v1_path)

    info = summarizer.summarize()

    assert info["description"] == SUBMISSION_V1_DESCRIPTION
    assert info["patchsets"] == SUBMISSION_V1_PATCHSETS
    assert info["workspace"] == SUBMISSION_V1_WORKSPACE
