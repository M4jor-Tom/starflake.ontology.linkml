<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# starflake-ontology

Domain ontology for the Starflake space exploration game

## Ontology graph

See the [ontology graph](docs/generated/ontology-graph.md) (rendered by GitHub), or
run `just testdoc` for the browsable site. Regenerate it with `just gen-graph`;
a test fails when it is out of date.

## Where does a Gherkin scenario belong?

Put a [competency question](features/competency_questions.feature) here if its
answer is a fact you can read or infer from the model and its data without
running the game. For example, “Which systems are one jump from Sol?” needs
only the [example galaxy](tests/data/valid/Galaxy-001.yaml). “Which objects can
be destroyed by melting?” asks about a vulnerability, not whether a particular
object is destroyed. The current schema does not yet model that vulnerability.

“What happens when the pilot attempts that jump without enough fuel?” belongs in
[design/features/jump.feature](https://github.com/M4jor-Tom/starflake.design/blob/master/features/jump.feature):
it specifies what the game does. If a statement only names a field or its type,
keep it in the LinkML schema instead of restating it in Gherkin.

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
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Reporting a problem

Report problems and ideas for any part of Starflake in one place:
<https://github.com/M4jor-Tom/starflake/issues/new/choose>.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
