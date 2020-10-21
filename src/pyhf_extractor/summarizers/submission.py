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

from abc import ABCMeta
from abc import abstractmethod

from ..extractors import BasePatchsetExtractor
from ..extractors import BaseWorkspaceExtractor
from ..extractors import DummyPatchsetExtractor
from ..extractors import DummyWorkspaceExtractor
from ..extractors import V1PatchsetExtractor
from ..extractors import V1WorkspaceExtractor


class BaseSubmissionSummarizer(metaclass=ABCMeta):
    """ Interface for the Pyhf submission summarizers """

    patchset_extractors = {
        "1.0.0": V1PatchsetExtractor,
    }

    workspace_extractions = {
        "1.0.0": V1WorkspaceExtractor,
    }

    @classmethod
    def init_patchset_extractor(cls, version: str) -> BasePatchsetExtractor:
        """
        Initializes and returns a PatchsetExtractor
        :param version: patchset schema version
        :return: initialized PatchsetExtractor
        """

        try:
            extractor = cls.patchset_extractors[version]
        except KeyError:
            extractor = DummyPatchsetExtractor

        return extractor()

    @classmethod
    def init_workspace_extractor(cls, version: str) -> BaseWorkspaceExtractor:
        """
        Initializes and returns a WorkspaceExtractor
        :param version: workspace schema version
        :return: initialized WorkspaceExtractor
        """

        try:
            extractor = cls.workspace_extractions[version]
        except KeyError:
            extractor = DummyWorkspaceExtractor

        return extractor()

    @abstractmethod
    def summarize(self) -> dict:
        """
        Summarizes a Pyhf submission information
        :return: summarized Submission information
        """

        raise NotImplementedError()


class V1SubmissionSummarizer(BaseSubmissionSummarizer):
    """ Pyhf submission V1 information summarizer """

    def __init__(self, submission_file: str):
        """
        Initializer for the Pyhf submission V1 summarizer
        :param submission_file: path to the submission file
        """

        with gzip.open(submission_file) as file:
            data = json.load(file)

        assert "description" in data
        assert "patchsets" in data
        assert "workspace" in data

        self.submission_data = data

    def __get_patchsets_summary(self) -> list:
        """
        Summarizes the information of each Patchset
        :returns list of summarized Patchset information
        """

        patchset_info = []

        for patch in self.submission_data["patchsets"]:
            version = patch["version"]
            extractor = self.init_patchset_extractor(version)
            patchset_info.append(extractor.extract_info(patch))

        return patchset_info

    def __get_workspace_summary(self) -> dict:
        """
        Summarizes the information of the Workspace
        :returns summarized Workspace information
        """

        workspace = self.submission_data["workspace"]
        version = workspace["version"]
        extractor = self.init_workspace_extractor(version)

        return extractor.extract_info(workspace)

    def summarize(self) -> dict:
        """
        Summarizes a Pyhf submission information
        :return: summarized Submission information
        """

        return {
            "description": self.submission_data["description"],
            "patchsets": self.__get_patchsets_summary(),
            "workspace": self.__get_workspace_summary(),
        }
