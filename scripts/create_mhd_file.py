import logging
from pathlib import Path

from mhd_model.model.v0_1.dataset.validation.validator import validate_mhd_file

from gnps2mhd.config import (
    Gnps2MhdConfiguration,
    gnps2mhd_config,
)
from gnps2mhd.convertor_factory import (
    Gnps2MhdConvertorFactory,
)
from scripts.utils import setup_basic_logging_config

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    setup_basic_logging_config()
    study_ids = [
        "MSV000099201",
        "MSV000099062",
        "MSV000099183",
        "MSV000099175",
        "MSV000099174",
        "MSV000099152",
        "MSV000099141",
    ]

    config = Gnps2MhdConfiguration()

    factory = Gnps2MhdConvertorFactory()
    convertor = factory.get_convertor(
        target_mhd_model_schema_uri=gnps2mhd_config.target_mhd_model_schema_uri,
        target_mhd_model_profile_uri=gnps2mhd_config.target_mhd_model_legacy_profile_uri,
    )
    for idx, massive_study_id in enumerate(study_ids):
        # cache_root_path = "tests/gnps_dataset"
        mhd_output_root_path = Path("tests/mhd_dataset/legacy")
        mhd_output_root_path.mkdir(exist_ok=True, parents=True)
        mhd_output_filename = f"{massive_study_id}.mhd.json"
        convertor.convert(
            repository_name="GNPS",
            repository_identifier=massive_study_id,
            mhd_identifier=None,
            mhd_output_folder_path=mhd_output_root_path,
            mhd_output_filename=mhd_output_filename,
            # cache_root_path=cache_root_path,
        )
        file_path = mhd_output_root_path / Path(mhd_output_filename)

        validation_errors = validate_mhd_file(str(file_path))

        if validation_errors:
            logger.error("MHD model validation errors found for %s", massive_study_id)
            for error in validation_errors:
                logger.error(error)
        else:
            logger.info("MHD model validation successful for %s", massive_study_id)
