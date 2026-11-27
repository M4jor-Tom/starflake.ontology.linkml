# Ontology source

Use [`starflake_ontology.yaml`](starflake_ontology.yaml) as the entry point for validation and generation. It imports the galaxy content model and the state model, which share the same catalog and core types.

```text
ontology/src/
├── README.md
├── starflake_ontology.yaml     # Entry point
├── core/
│   ├── identity.yaml           # NamedThing, identifiers and schema subsets
│   ├── quantities.yaml         # Amount, Distance, Speed and radius
│   └── geometry.yaml           # Vector3D and Attitude
├── catalog/
│   ├── materials.yaml          # Solid materials and structural composition
│   ├── ships.yaml              # Hull designs and weapon types
│   └── encounters.yaml         # Raider and asteroid types and their fuel yields
├── galaxy/
│   ├── galaxy.yaml             # Galaxy content root
│   ├── star_systems.yaml       # Stars, spectral classes and jump routes
│   └── regions.yaml            # Asteroid fields and raider packs
└── state/
    ├── entities.yaml           # Physical entities, asteroids and fuel pods
    ├── ships.yaml              # Pilots and individual ships in flight
    └── snapshots.yaml          # GalaxyState and StarSystemState
```

Keep the directory layout intact when copying the schema. Inside a module, use `./` for sibling imports and `../` for imports across directories so all generators resolve the same files. After editing, run `just gen-graph lint test` from the `ontology` dev shell.
