"""The committed ontology graph must match the schema."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_graph_is_up_to_date(tmp_path):
    generated = tmp_path / "graph.mmd"
    subprocess.run(["just", "gen-graph", "--output", generated], cwd=ROOT, check=True)
    diagram = generated.read_bytes()
    assert diagram.startswith(b"erDiagram\n")
    committed = ROOT / "docs/generated/ontology-graph.mmd"
    assert committed.read_bytes() == diagram, "run `just gen-graph`"
