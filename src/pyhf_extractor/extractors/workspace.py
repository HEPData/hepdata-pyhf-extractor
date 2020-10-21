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

from abc import ABCMeta
from abc import abstractmethod


class BaseWorkspaceExtractor(metaclass=ABCMeta):
    """ Interface for the Pyhf workspace information extractors """

    @abstractmethod
    def extract_info(self, workspace: dict) -> dict:
        """
        Extracts the most relevant information of a Pyhf Workspace
        :param workspace: workspace dictionary
        :return: summarized workspace dictionary
        """

        raise NotImplementedError()


class DummyWorkspaceExtractor(BaseWorkspaceExtractor):
    """ Pyhf workspace dummy information extractor """

    def extract_info(self, workspace: dict) -> dict:
        """
        Returns an empty dictionary (useful when versions do not match)
        :param workspace: workspace dictionary
        :return: empty dictionary
        """

        return {}


class V1WorkspaceExtractor(BaseWorkspaceExtractor):
    """ Pyhf workspace V1 information extractor """

    @staticmethod
    def get_observations(workspace: dict) -> dict:
        """
        Extracts the dictionary of summarized observations
        :param workspace: workspace dictionary
        :return: summarized observations dictionary
        """

        return {obs["name"]: len(obs["data"]) for obs in workspace["observations"]}

    @staticmethod
    def get_samples(channel: dict) -> list:
        """
        Extracts the list of summarized samples
        :param channel: channel dictionary
        :return: list of samples summarized information
        """

        return [{"name": sample["name"]} for sample in channel["samples"]]

    def get_channels(self, workspace: dict) -> list:
        """
        Extracts the list of summarized channels
        :param workspace: workspace dictionary
        :return: list of channels summarized information
        """

        obs = self.get_observations(workspace)

        return [
            {
                "name": channel["name"],
                "nbins": obs[channel["name"]],
                "samples": self.get_samples(channel),
            }
            for channel in workspace["channels"]
        ]

    def extract_info(self, workspace: dict) -> dict:
        """
        Extracts the most relevant information of a Pyhf Workspace V1
        :param workspace: workspace dictionary
        :return: summarized workspace dictionary
        """

        return {
            "version": workspace["version"],
            "channels": self.get_channels(workspace),
        }
