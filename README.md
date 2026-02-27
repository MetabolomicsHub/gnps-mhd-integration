# MetaboLights - MHD Model Integration Framework



## Development Environment


Development environment for linux or mac
```bash

# install python package manager uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# add $HOME/.local/bin to your PATH, either restart your shell or run
export PATH=$HOME/.local/bin:$PATH

# install git from https://git-scm.com/downloads
# Linux command
apt update; apt install git -y

# Mac command
# brew install git

# clone project from github
git clone https://github.com/MetabolomicsHub/gnps-mhd-integration.git

cd gnps-mhd-integration

# install python if it is not installed
uv python install 3.12

# install python dependencies
uv sync

# install pre-commit to check repository integrity and format checking
uv run pre-commit

# open your IDE (vscode, pycharm, etc.) and set python interpreter as .venv/bin/python

```

## Commandline Usage


```bash
# you can use any python version >= 3.12
pip install gnps-mhd-integration

gnps-mhd-cli
####################################################################
# Usage: gnps-mhd-cli [OPTIONS] COMMAND [ARGS]...

#   GNPS/MassIVE - MHD Integration CLI.

#   Use this cli to create MHD model file, convert MHD model file to
#   announcement file, and fetch GNPS/MassIVE params.xml metadata file.

# Options:
#   --version   Show the version and exit.
#   -h, --help  Show this message and exit.

# Commands:
#   create    Create MHD model or annoucenment file.
#   download  Fetch a GNPS/MassIVE study params.xml and convert it to json.
#   validate  Validate MHD model or annoucenment file.
####################################################################


gnps-mhd-cli create mhd
####################################################################
# Usage: gnps-mhd-cli create mhd [OPTIONS] MASSIVE_STUDY_ID MHD_IDENTIFIER

#   Convert a GNPS/MassIVE study to MHD model file.

# Options:
#   --input-file-path TEXT  Input file path of params.xml. If it is not defined,
#                           the params.xml will be fetched from MassIVE.
#   --output-dir TEXT       Output directory for MHD file  [default: outputs]
#   --output-filename TEXT  MHD filename (e.g., MHD000001.mhd.json,
#                           ST000001.mhd.json)
#   --schema_uri TEXT       Target MHD model schema. It defines format of MHD
#                           model structure.  [default:
#                           https://metabolomicshub.github.io/mhd-
#                           model/schemas/v0_1/common-data-
#                           model-v0.1.schema.json]
#   --profile_uri TEXT      Target MHD model profile. It is used to validate MHD
#                           model  [default:
#                           https://metabolomicshub.github.io/mhd-
#                           model/schemas/v0_1/common-data-model-v0.1.legacy-
#                           profile.json]
#   -h, --help              Show this message and exit.
####################################################################

gnps-mhd-cli create mhd MSV000099062 MSV000099062
####################################################################
# MSV000099062 is converted successfully. Output file: outputs/MSV000099062.mhd.json
####################################################################

ls outputs
# MSV000099062.mhd.json


gnps-mhd-cli download

####################################################################
# Usage: gnps-mhd-cli download [OPTIONS] STUDY_ID

#   Download a GNPS/MassIVE study as json file.

# Options:
#   --output-dir TEXT       Output directory for MHD file  [default: outputs]
#   --output-filename TEXT  MHD filename (e.g., MHD000001_mhd.json,
#                           ST000001_mhd.json)
#   -h, --help              Show this message and exit.
####################################################################

gnps-mhd-cli download MSV000099062
# MSV000099062 is downloaded

ls outputs
# MSV000099062.json


gnps-mhd-cli validate mhd MSV000099062 outputs/MSV000099062.mhd.json
####################################################################
# MSV000099062: outputs/MSV000099062.mhd.json MHD file validation started.
# Used schema: https://metabolomicshub.github.io/mhd-model/schemas/v0_1/common-data-model-v0.1.schema.json
# Validation profile: https://metabolomicshub.github.io/mhd-model/schemas/v0_1/common-data-model-v0.1.legacy-profile.json
# MSV000099062: File 'outputs/MSV000099062.mhd.json' is validated successfully.####################################################################

gnps-mhd-cli create announcement

####################################################################
# Usage: gnps-mhd-cli create announcement [OPTIONS] MHD_STUDY_ID
#                                         MHD_MODEL_FILE_PATH
#                                         TARGET_MHD_MODEL_FILE_URL

#   Create announcement file from MHD data model file.

#   Args:

#   mhd_study_id (str): MHD study identifier

#   mhd_model_file_path (str): MHD data model path

#   target_mhd_model_file_url (str): target URL of MHD data model

#   output_dir (str): Output directory of announcement file

#   output_filename (str): Name of MHD announcement file. Default is <repository
#   identifier>.announcement.json

# Options:
#   --output-dir TEXT       Output directory for MHD file  [default: outputs]
#   --output-filename TEXT  MHD announcement filename (e.g.,
#                           MHD000001.announcement.json,
#                           ST000001.announcement.json)
#   -h, --help              Show this message and exit.
####################################################################


# MHD identifier will be reserved for each private study
# Assumption: MSV000099062.mhd.json will be accessible on
# https://www.gnps.org/data?MHD_ID=MHD0123456789
gnps-mhd-cli create announcement MHD0123456789  outputs/MSV000099062.mhd.json "https://www.gnps.org/data?MHD_ID=MHD0123456789"
####################################################################
# MSV000099062 announcement file conversion completed.
####################################################################

ls outputs
####################################################################
# MHD0123456789.announcement.json  MSV000099062.mhd.json
####################################################################

gnps-mhd-cli validate announcement

####################################################################
# Usage: gnps-mhd-cli validate announcement [OPTIONS] MHD_STUDY_ID
#                                         ANNOUNCEMENT_FILE_PATH
#   Validate MHD announcement file.
#   Args:
#   mhd_study_id (str): MHD study id
#   announcement_file_path (str): MHD announcement file path
#   output_path (None | str): If it is defined, validation results are saved in
#   output file path.

# Options:
#   --output-path TEXT  Validation output file path
#   -h, --help          Show this message and exit.
####################################################################

gnps-mhd-cli validate announcement MSV000099062 outputs/MSV000099062.announcement.json

####################################################################
# MHD0123456789: File 'outputs/MSV000099062.announcement.json' is validated successfully.
####################################################################

```
