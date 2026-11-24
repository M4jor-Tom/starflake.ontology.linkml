# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="starflake_ontology"
LINKML_SCHEMA_AUTHOR="theta <tom-vautray@hotmail.fr>"
LINKML_SCHEMA_DESCRIPTION="Domain ontology for the Starflake space exploration game"
LINKML_SCHEMA_SOURCE_DIR="src/starflake_ontology/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile=rdfs)
# LINKML_GENERATORS_OWL_ARGS="--no-type-objects --no-metaclasses --metadata-profile=rdfs"
LINKML_GENERATORS_OWL_ARGS=
