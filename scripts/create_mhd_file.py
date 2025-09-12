import logging
from pathlib import Path

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
    study_ids = ["MSV000099062"]

    config = Gnps2MhdConfiguration()

    factory = Gnps2MhdConvertorFactory()
    convertor = factory.get_convertor(
        target_mhd_model_schema_uri=gnps2mhd_config.target_mhd_model_schema_uri,
        target_mhd_model_profile_uri=gnps2mhd_config.target_mhd_model_legacy_profile_uri,
    )
    for massive_study_id in study_ids:
        mhd_output_root_path = Path("tests/mhd_dataset")
        mhd_output_root_path.mkdir(exist_ok=True, parents=True)
        file_path = Path(f"tests/gnps_dataset/{massive_study_id}.json")
        convertor.convert(
            repository_name="GNPS",
            repository_identifier=massive_study_id,
            mhd_identifier=None,
            mhd_output_folder_path=mhd_output_root_path,
        )
