## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Render the ontology as Mermaid class diagrams, one per subset
[group('model development')]
gen-graph:
  uv run python -m starflake_ontology.graph {{source_schema_path}} > docs/ontology-graph.md
