"""The committed ontology graph must match the schema."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_graph_is_up_to_date(tmp_path):
    generated = tmp_path / "graph.md"
    subprocess.run(["just", "gen-graph", "--output", generated], cwd=ROOT, check=True)
    committed = ROOT / "docs/generated/ontology-graph.md"
    assert committed.read_bytes() == generated.read_bytes(), "run `just gen-graph`"
