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


class BasePatchsetExtractor(metaclass=ABCMeta):
    """ Interface for the Pyhf patchset information extractors """

    @abstractmethod
    def extract_info(self, patchset: dict) -> dict:
        """
        Extracts the most relevant information of a Pyhf Patchset
        :param patchset: patchset dictionary
        :return: summarized patchset dictionary
        """

        raise NotImplementedError()


class DummyPatchsetExtractor(BasePatchsetExtractor):
    """ Pyhf patchset dummy information extractor """

    def extract_info(self, patchset: dict) -> dict:
        """
        Returns an empty dictionary (useful when versions do not match)
        :param patchset: patchset dictionary
        :return: empty dictionary
        """

        return {}


class V1PatchsetExtractor(BasePatchsetExtractor):
    """ Pyhf patchset V1 information extractor """

    def extract_info(self, patchset: dict) -> dict:
        """
        Extracts the most relevant information of a Pyhf Patchset V1
        :param patchset: patchset dictionary
        :return: summarized patchset dictionary
        """

        return {
            "metadata": patchset["metadata"],
            "version": patchset["version"],
            "npatches": len(patchset["patches"]),
        }
