# This file is necessary to be able to launch pytest by running "pytest"

import sys
from pathlib import Path

# Get the sources folder absolute path
project_path = Path(__file__).parent.parent
sources_path = project_path.joinpath("src")

# Necessary for pytest to allow imports from packaged source folders
sys.path.append(str(sources_path))
