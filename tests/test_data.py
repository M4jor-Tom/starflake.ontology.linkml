"""Check the YAML fixtures directly against the authored LinkML schema."""

from pathlib import Path

import pytest
from linkml.validator import validate_file

DATA = Path(__file__).parent / "data"
SCHEMA = DATA.parents[1] / "src/starflake_ontology.yaml"


@pytest.mark.parametrize("path", sorted(DATA.glob("*/*.yaml")), ids=lambda path: path.name)
def test_fixture(path):
    target_class = path.stem.split("-", 1)[0]
    report = validate_file(path, str(SCHEMA), target_class)
    assert bool(report.results) == (path.parent.name == "invalid"), report.results
