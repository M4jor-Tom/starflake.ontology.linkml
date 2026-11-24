"""The committed ontology graph must match the schema."""

from pathlib import Path

from starflake_ontology.graph import render

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src/starflake_ontology/schema/starflake_ontology.yaml"


def test_graph_is_up_to_date():
    committed = (ROOT / "docs/generated/ontology-graph.md").read_text()
    assert committed == render(str(SCHEMA)), "run `just gen-graph`"
