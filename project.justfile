# Generate a Mermaid entity-relationship diagram including classes outside the tree root
[group('model development')]
[arg("output", long)]
gen-graph $output="docs/generated/ontology-graph.mmd":
  #!/usr/bin/env bash
  set -euo pipefail
  diagram=$(gen-erdiagram --format mermaid --no-structural "{{source_schema_path}}")
  sed 's/[[:blank:]]*$//' <<< "$diagram" > "$output"
