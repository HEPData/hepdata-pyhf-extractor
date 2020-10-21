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

PATCHSETS_V1_METADATA = {
    "description": "signal patchset for the SUSY EWK 1Lbb analysis",
    "digests": {
        "sha256": "2563672e1a165384faf49f1431e921d88c9c07ec10f150d5045576564f98f820",
    },
    "labels": [
        "m1",
        "m2",
    ],
    "references": {
        "hepdata": "ins1755298",
    },
}

WORKSPACE_V1_CHANNELS = [
    {
        "name": "WREM_cuts",
        "nbins": 1,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "STCREM_cuts",
        "nbins": 1,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "TRHMEM_cuts",
        "nbins": 1,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "TRMMEM_cuts",
        "nbins": 1,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "TRLMEM_cuts",
        "nbins": 1,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "SRHMEM_mct2",
        "nbins": 3,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "vh"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "SRMMEM_mct2",
        "nbins": 3,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
    {
        "name": "SRLMEM_mct2",
        "nbins": 3,
        "samples": [
            {"name": "ttbar"},
            {"name": "singletop"},
            {"name": "wjets"},
            {"name": "diboson"},
            {"name": "multiboson"},
            {"name": "vh"},
            {"name": "zjets"},
            {"name": "tth"},
            {"name": "ttv"},
        ],
    },
]
