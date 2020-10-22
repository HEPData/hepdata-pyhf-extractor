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

PALLET_V1_DESCRIPTION = (
    ""
    "# JSON Likelihoods for 1Lbb Analysis"
    "\n\n"
    "The JSON likelihoods are serialized in this folder. "
    "This is done by providing a background-only workspace containing "
    "the signal/control channels at `BkgOnly.json` as well as patch files for each "
    "mass point on the signal phase-space explored in the analysis."
    "\n\n"
    "All [jsonpatches](http://jsonpatch.com/) are contained in the file `patchset.json`. "
    "Each patch is identified in `patchset.json` by the metadata field "
    '`"name": "C1N2_Wh_hbb_[m1]_[m2]"` where `m1` is the mass of both the lightest chargino '
    "and the next-to-lightest neutralino (which are assumed to be nearly mass degenerate), "
    "and `m2` is the mass of the lightest neutralino."
    "\n\n"
    "## Producing signal workspaces"
    "\n\n"
    "As an example, we use [python jsonpatch](https://python-json-patch.readthedocs.io/en/latest/) "
    "to make the full json likelihood workspace for the signal point `C1N2_Wh_hbb_700_400`:"
    "\n\n"
    "```"
    '\njsonpatch BkgOnly.json <(pyhf patchset extract patchset.json --name "C1N2_Wh_hbb_700_400") > C1N2_Wh_hbb_700_400.json\n'
    "```"
    "\n\n"
    "## Computing signal workspaces"
    "\n\n"
    "For example, with [pyhf](https://scikit-hep.org/pyhf/), you can do any of the following:"
    "\n\n"
    "```"
    '\npyhf cls BkgOnly.json --patch <(pyhf patchset extract patchset.json --name "C1N2_Wh_hbb_700_400")'
    "\n\n"
    'jsonpatch BkgOnly.json <(pyhf patchset extract patchset.json --name "C1N2_Wh_hbb_700_400") | pyhf cls'
    "\n\n"
    "pyhf cls C1N2_Wh_hbb_700_400.json\n"
    "```"
    "\n\n"
)

PALLET_V1_PATCHSETS = [
    {
        "metadata": {
            "description": "signal patchset for the SUSY EWK 1Lbb analysis",
            "digests": {
                "sha256": "2563672e1a165384faf49f1431e921d88c9c07ec10f150d5045576564f98f820",
            },
            "labels": ["m1", "m2"],
            "references": {"hepdata": "ins1755298"},
        },
        "version": "1.0.0",
        "npatches": 125,
    },
]

PALLET_V1_WORKSPACE = {
    "version": "1.0.0",
    "channels": [
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
    ],
}
