<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# starflake-ontology

Domain ontology for the Starflake space exploration game

## Ontology graph

See [docs/ontology-graph.md](docs/ontology-graph.md) (rendered by GitHub), or
run `just testdoc` for the browsable site. Regenerate it with `just gen-graph`;
a test fails when it is out of date.

## Development on NixOS

Run every command inside `nix develop`, for example `nix develop --command just test`.

## Documentation Website

[https://M4jor-Tom.github.io/starflake-ontology](https://M4jor-Tom.github.io/starflake-ontology)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [starflake_ontology](src/starflake_ontology)
    * [schema/](src/starflake_ontology/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/starflake_ontology/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
