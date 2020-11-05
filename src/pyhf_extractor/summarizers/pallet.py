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


class BasePalletSummarizer(metaclass=ABCMeta):
    """ Interface for the Pyhf Pallet summarizers """

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
        Summarizes a Pyhf Pallet information
        :return: summarized Pallet information
        """

        raise NotImplementedError()


class V1PalletSummarizer(BasePalletSummarizer):
    """ Pyhf Pallet V1 information summarizer """

    def __init__(self, pallet_path: str = None, pallet_data: dict = None):
        """
        Initializer for the Pyhf Pallet V1 summarizer
        :param pallet_path: path to the Pallet file (optional)
        :param pallet_data: content of the Pallet file (optional)
        """

        # fmt: off
        assert \
            (pallet_path is not None) or \
            (pallet_data is not None), \
            "Either the Pallet path or the Pallet data must be provided"
        # fmt: on

        if pallet_path is not None:
            data = self.__load_initial_data(pallet_path)
        else:
            data = pallet_data

        assert "patchsets" in data
        assert "workspace" in data

        self.pallet_data = data

    @staticmethod
    def __load_initial_data(pallet_path: str):
        """
        Loads the Pallet file content from the specified .gzip or .json file
        :param pallet_path: path to the Pallet file
        :return: Pallet file content
        """

        try:
            file = gzip.open(pallet_path)
            data = json.load(file)
        except OSError:
            file = open(pallet_path)
            data = json.load(file)
        finally:
            file.close()

        return data

    def __get_patchsets_summary(self) -> list:
        """
        Summarizes the information of each Patchset
        :returns list of summarized Patchset information
        """

        patchset_info = []

        for patch in self.pallet_data["patchsets"]:
            version = patch["version"]
            extractor = self.init_patchset_extractor(version)
            patchset_info.append(extractor.extract_info(patch))

        return patchset_info

    def __get_workspace_summary(self) -> dict:
        """
        Summarizes the information of the Workspace
        :returns summarized Workspace information
        """

        workspace = self.pallet_data["workspace"]
        version = workspace["version"]
        extractor = self.init_workspace_extractor(version)

        return extractor.extract_info(workspace)

    def summarize(self) -> dict:
        """
        Summarizes a Pyhf Pallet information
        :return: summarized Pallet information
        """

        return {
            "patchsets": self.__get_patchsets_summary(),
            "workspace": self.__get_workspace_summary(),
        }
