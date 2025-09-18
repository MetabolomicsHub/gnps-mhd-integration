import sys
from pathlib import Path

import click
from mhd_model import __version__
from mhd_model.commands.create.announcement import create_announcement_file_task

from gnps2mhd.commands.create_mhd_file import create_mhd_file
from gnps2mhd.commands.fetch_gnps_study import fetch_gnps_study


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__)
def cli():
    """GNPS/MassIVE - MHD Integration CLI.

    Use this cli to create MHD model file,
    convert MHD model file to announcement file,
    and fetch GNPS/MassIVE params.xml metadata file.
    """
    pass


cli.add_command(create_mhd_file)
cli.add_command(fetch_gnps_study)
cli.add_command(create_announcement_file_task)

if __name__ == "__main__":
    sys.path.insert(0, str(Path.cwd()))
    if len(sys.argv) == 1:
        cli(["--help"])
    else:
        cli()
