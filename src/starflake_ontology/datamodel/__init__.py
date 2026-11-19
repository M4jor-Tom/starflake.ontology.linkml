"""Data model package for starflake-ontology."""

from pathlib import Path
from .starflake_ontology import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "starflake_ontology.yaml"
