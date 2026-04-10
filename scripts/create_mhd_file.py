import logging
from pathlib import Path

import jsonschema
import json
from mhd_model.model.v0_1.dataset.validation.validator import validate_mhd_model

from gnps2mhd.config import Gnps2MhdConfiguration
from gnps2mhd.convertor_factory import Gnps2MhdConvertorFactory
from scripts.utils import setup_basic_logging_config

logger = logging.getLogger(__name__)


def convert_massive_study_to_mhd_legacy(
    massive_study_id: str, gnps2mhd_config: None | Gnps2MhdConfiguration = None
) -> tuple[bool, dict[str, list[jsonschema.ValidationError]]]:
    if not gnps2mhd_config:
        gnps2mhd_config = Gnps2MhdConfiguration()

    factory = Gnps2MhdConvertorFactory()
    convertor = factory.get_convertor(
        target_mhd_model_schema_uri=gnps2mhd_config.target_mhd_model_schema_uri,
        target_mhd_model_profile_uri=gnps2mhd_config.target_mhd_model_legacy_profile_uri,
    )
    mhd_output_root_path = Path("tests/mhd_dataset/legacy")
    mhd_input_root_path = Path("tests/gnps_dataset")
    mhd_output_root_path.mkdir(exist_ok=True, parents=True)
    mhd_output_filename = f"{massive_study_id}.mhd.json"
    input_file_path = mhd_input_root_path / Path(f"{massive_study_id}.params.xml.json")
    convertor.convert(
        repository_name="GNPS",
        repository_identifier=massive_study_id,
        mhd_identifier=None,
        mhd_output_folder_path=mhd_output_root_path,
        mhd_output_filename=mhd_output_filename,
        input_file_path=input_file_path,
    )
    mhd_file_path = mhd_output_root_path / Path(mhd_output_filename)
    params_json = {}
    if not mhd_file_path.exists():
        logger.error("MHD file not found: %s", mhd_file_path)
        return False, {}
    params_json = json.loads(input_file_path.read_text())
    massive_volume = params_json.get("massive_volume", "v10")
    mhd_file_url = (
        f"ftp://massive-ftp.ucsd.edu/{massive_volume}/{massive_study_id}/mhd/{mhd_output_filename}"
    )
    return validate_mhd_model(
        massive_study_id,
        mhd_file_path,
        validate_announcement_file=True,
        mhd_file_url=mhd_file_url,
    )


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    setup_basic_logging_config()
    study_ids = [
        "MSV000100766",
        # "MSV000099201",
        "MSV000099062",
        "MSV000099183",
        "MSV000099175",
        "MSV000099174",
        "MSV000099152",
        "MSV000099141",
    ]
    gnps2mhd_config = Gnps2MhdConfiguration()
    for study_id in study_ids:
        convert_massive_study_to_mhd_legacy(study_id, gnps2mhd_config)
