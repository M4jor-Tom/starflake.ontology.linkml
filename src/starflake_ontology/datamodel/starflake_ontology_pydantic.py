from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'starflake',
     'default_range': 'string',
     'description': 'Domain ontology for Starflake, an open-world 3D space '
                    'explorer.\n'
                    '\n'
                    'The pilot flies a ship through a galaxy of star systems, '
                    'shoots enemies and\n'
                    'asteroids, loots the fuel they drop, and jumps to a '
                    'neighbouring system once\n'
                    'the tank holds enough fuel.\n'
                    '\n'
                    'The schema has two layers:\n'
                    '\n'
                    '* **Content** (`ContentPack`): static, designer-authored '
                    'definitions such as\n'
                    '  ship classes, weapons, enemy and asteroid types, and the '
                    'galaxy map.\n'
                    '* **State** (`GameSession`): the persisted, replicable state '
                    'of one play\n'
                    '  session, which references content by identifier.\n'
                    '\n'
                    'Units: distances in metres, time in seconds, angles in '
                    'radians.',
     'id': 'https://w3id.org/M4jor-Tom/starflake-ontology',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'starflake-ontology',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'starflake': {'prefix_prefix': 'starflake',
                                'prefix_reference': 'https://w3id.org/M4jor-Tom/starflake-ontology/'}},
     'see_also': ['https://M4jor-Tom.github.io/starflake-ontology'],
     'source_file': 'src/starflake_ontology/schema/starflake_ontology.yaml',
     'subsets': {'content': {'description': 'Static, designer-authored definitions '
                                            'bundled in a ContentPack.',
                             'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                             'name': 'content'},
                 'core': {'description': 'Building blocks shared by content and '
                                         'state.',
                          'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                          'name': 'core'},
                 'state': {'description': 'Persisted and replicated session state, '
                                          'rooted at GameSession.',
                           'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                           'name': 'state'}},
     'title': 'Starflake ontology',
     'types': {'Amount': {'base': 'float',
                          'description': 'A non-negative quantity such as hull '
                                         'points, damage or fuel.',
                          'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                          'minimum_value': 0,
                          'name': 'Amount',
                          'typeof': 'float',
                          'uri': 'xsd:float'},
               'Distance': {'base': 'float',
                            'description': 'A non-negative length in metres.',
                            'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                            'minimum_value': 0,
                            'name': 'Distance',
                            'typeof': 'float',
                            'unit': {'ucum_code': 'm'},
                            'uri': 'xsd:float'},
               'Speed': {'base': 'float',
                         'description': 'A non-negative speed in metres per '
                                        'second.',
                         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                         'minimum_value': 0,
                         'name': 'Speed',
                         'typeof': 'float',
                         'unit': {'ucum_code': 'm/s'},
                         'uri': 'xsd:float'}}} )

class SpectralClass(str, Enum):
    """
    Morgan-Keenan spectral class of a star, hottest to coolest.
    """
    O = "o"
    """
    Blue, above 30,000 K.
    """
    B = "b"
    """
    Blue-white, 10,000 to 30,000 K.
    """
    A = "a"
    """
    White, 7,500 to 10,000 K.
    """
    F = "f"
    """
    Yellow-white, 6,000 to 7,500 K.
    """
    G = "g"
    """
    Yellow, 5,200 to 6,000 K, like the Sun.
    """
    K = "k"
    """
    Orange, 3,700 to 5,200 K.
    """
    M = "m"
    """
    Red, below 3,700 K.
    """


class HostingMode(str, Enum):
    """
    Who runs the authoritative simulation of a session.
    """
    solo = "solo"
    """
    Single player, simulated locally, no network.
    """
    player_hosted = "player_hosted"
    """
    A player's game acts as server for the players they invite.
    """
    dedicated_server = "dedicated_server"
    """
    A server not run by any player hosts the session.
    """



class NamedThing(ConfiguredBaseModel):
    """
    Anything identifiable and named, whether content or state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['core']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Vector3D(ConfiguredBaseModel):
    """
    A 3D vector in metres (position) or metres per second (velocity). Named Vector3D so it does not shadow the engine's own Vector3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['core']})

    x: float = Field(default=..., description="""X component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })
    y: float = Field(default=..., description="""Y component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })
    z: float = Field(default=..., description="""Z component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })


class Attitude(ConfiguredBaseModel):
    """
    The rotation of a body in 3D space, stored as a unit quaternion. Named Attitude (the aerospace term) so it does not clash with the engine's Quaternion type or Godot's Orientation enum.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['core']})

    x: float = Field(default=..., description="""X component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })
    y: float = Field(default=..., description="""Y component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })
    z: float = Field(default=..., description="""Z component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vector3D', 'Attitude']} })
    w: float = Field(default=..., description="""W (scalar) component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Attitude']} })


class ContentPack(NamedThing):
    """
    A versioned bundle of designer-authored content. Everything a session references by identifier is defined here.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'tree_root': True})

    weapon_types: Optional[list[WeaponType]] = Field(default=None, description="""Weapons available to ship classes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    ship_classes: Optional[list[ShipClass]] = Field(default=None, description="""Hull designs available to player and enemy ships.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    enemy_types: Optional[list[EnemyType]] = Field(default=None, description="""Hostile archetypes that can spawn in star systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    asteroid_types: Optional[list[AsteroidType]] = Field(default=None, description="""Asteroid kinds that can spawn in star systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    starting_ship_class: str = Field(default=..., description="""The hull every new player ship is built from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    galaxy: Galaxy = Field(default=..., description="""The map played with this content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ContentPack']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class WeaponType(NamedThing):
    """
    A ship-mounted weapon that fires projectiles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    damage: float = Field(default=..., description="""Hull or integrity points removed per hit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    fire_rate: float = Field(default=..., description="""Shots per second.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType'], 'unit': {'ucum_code': '/s'}} })
    projectile_speed: float = Field(default=..., description="""Speed of a fired projectile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    max_range: float = Field(default=..., description="""Distance after which a projectile despawns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ShipClass(NamedThing):
    """
    A hull design that player and enemy ships are built from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    max_hull: float = Field(default=..., description="""Hull points of an undamaged ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    max_speed: float = Field(default=..., description="""Top linear speed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    acceleration: float = Field(default=..., description="""Linear acceleration under full thrust.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass'], 'unit': {'ucum_code': 'm/s2'}} })
    turn_rate: float = Field(default=..., description="""Maximum angular speed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass'], 'unit': {'ucum_code': 'rad/s'}} })
    fuel_capacity: float = Field(default=..., description="""Maximum fuel the tank holds. Zero for ships that never jump.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    weapons: Optional[list[str]] = Field(default=None, description="""Weapons mounted on every ship of this class.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class EnemyType(NamedThing):
    """
    A hostile AI pilot archetype: which hull it flies, when it engages, and what it drops when destroyed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    ship_class: str = Field(default=..., description="""The hull design.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyType', 'PlayerShip']} })
    fuel_drop: float = Field(default=..., description="""Fuel in the loot drop left when this is destroyed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyType', 'AsteroidType']} })
    detection_range: float = Field(default=..., description="""Distance at which the enemy notices and chases a player ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class AsteroidType(NamedThing):
    """
    A kind of asteroid. Shooting it until its integrity reaches zero breaks it and leaves a fuel loot drop.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'slot_usage': {'radius': {'description': 'Collision radius of the asteroid.',
                                   'name': 'radius'}}})

    radius: float = Field(default=..., description="""Collision radius of the asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'SpawnRegion']} })
    fuel_drop: float = Field(default=..., description="""Fuel in the loot drop left when this is destroyed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyType', 'AsteroidType']} })
    max_integrity: float = Field(default=..., description="""Damage needed to break the asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Galaxy(NamedThing):
    """
    The map of star systems connected by jump routes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    star_systems: list[StarSystem] = Field(default=..., description="""Every star system of the galaxy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    starting_system: str = Field(default=..., description="""Where new player ships spawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StarSystem(NamedThing):
    """
    One playable area around a star. A player ship can jump to any system in jump_targets once it carries at least jump_fuel_cost fuel.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    star_class: SpectralClass = Field(default=..., description="""Spectral class of the star, driving its look.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    bounds_radius: float = Field(default=..., description="""Radius of the playable sphere centred on the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    jump_fuel_cost: float = Field(default=..., description="""Fuel consumed by a jump out of this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    jump_targets: Optional[list[str]] = Field(default=None, description="""Systems reachable by a single jump from this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    asteroid_fields: Optional[list[AsteroidField]] = Field(default=None, description="""Asteroid spawn regions in this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    enemy_groups: Optional[list[EnemyGroup]] = Field(default=None, description="""Enemy spawn regions in this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class SpawnRegion(ConfiguredBaseModel):
    """
    A sphere inside a star system where a number of entities spawn when the system state is first created.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'slot_usage': {'radius': {'description': 'Radius of the spawn sphere.',
                                   'name': 'radius'}}})

    radius: float = Field(default=..., description="""Radius of the spawn sphere.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'SpawnRegion']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })
    spawn_count: int = Field(default=..., description="""Number of entities spawned in the region.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })


class AsteroidField(SpawnRegion):
    """
    A region filled with asteroids of one type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    asteroid_type: str = Field(default=..., description="""The kind of asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidField', 'Asteroid']} })
    radius: float = Field(default=..., description="""Radius of the spawn sphere.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'SpawnRegion']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })
    spawn_count: int = Field(default=..., description="""Number of entities spawned in the region.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })


class EnemyGroup(SpawnRegion):
    """
    A region where enemies of one type spawn.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    enemy_type: str = Field(default=..., description="""The enemy archetype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyGroup', 'EnemyShip']} })
    radius: float = Field(default=..., description="""Radius of the spawn sphere.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'SpawnRegion']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })
    spawn_count: int = Field(default=..., description="""Number of entities spawned in the region.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['SpawnRegion']} })


class GameSession(ConfiguredBaseModel):
    """
    The persisted state of one play session: a save file in solo, the authoritative world on a host or dedicated server in multiplayer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state'],
         'rules': [{'description': 'Solo sessions hold exactly one player.',
                    'postconditions': {'slot_conditions': {'max_players': {'equals_number': 1,
                                                                           'name': 'max_players'}}},
                    'preconditions': {'slot_conditions': {'hosting_mode': {'equals_string': 'solo',
                                                                           'name': 'hosting_mode'}}}},
                   {'description': 'No player hosts a session that runs on a dedicated '
                                   'server.',
                    'postconditions': {'slot_conditions': {'host': {'name': 'host',
                                                                    'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'hosting_mode': {'equals_string': 'dedicated_server',
                                                                           'name': 'hosting_mode'}}}}]})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    content_pack: str = Field(default=..., description="""The content this session was created with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    hosting_mode: HostingMode = Field(default=..., description="""Who runs the authoritative simulation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    host: Optional[str] = Field(default=None, description="""The player hosting the session. Absent on a dedicated server.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    max_players: int = Field(default=..., description="""Maximum number of players allowed at once.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    players: list[Player] = Field(default=..., description="""Everyone who has joined the session.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    player_ships: Optional[list[PlayerShip]] = Field(default=None, description="""The ship of each player.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })
    system_states: Optional[list[StarSystemState]] = Field(default=None, description="""State of the systems visited so far. A system without state has not been generated yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GameSession']} })


class Player(NamedThing):
    """
    A person taking part in a session. Its name is shown to other players.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StarSystemState(ConfiguredBaseModel):
    """
    The world state of one star system within a session: what remains of its asteroids and enemies, and the loot floating there.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    star_system: str = Field(default=..., description="""The star system this state belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    asteroids: Optional[list[Asteroid]] = Field(default=None, description="""Asteroids not broken yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    enemy_ships: Optional[list[EnemyShip]] = Field(default=None, description="""Enemy ships not destroyed yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    loot_drops: Optional[list[LootDrop]] = Field(default=None, description="""Fuel not collected yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })


class SpaceEntity(ConfiguredBaseModel):
    """
    Anything with a physical presence in a star system. The identifier doubles as the network id in multiplayer.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class Ship(SpaceEntity):
    """
    A flying, armed entity that can be destroyed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    hull: float = Field(default=..., description="""Remaining hull points. The ship is destroyed at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ship']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class PlayerShip(Ship):
    """
    A ship flown by a player.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    ship_class: str = Field(default=..., description="""The hull design.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyType', 'PlayerShip']} })
    pilot: str = Field(default=..., description="""The player flying the ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlayerShip']} })
    current_system: str = Field(default=..., description="""The star system the ship is in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlayerShip']} })
    fuel: float = Field(default=..., description="""Fuel in the tank, at most the ship class fuel_capacity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlayerShip']} })
    hull: float = Field(default=..., description="""Remaining hull points. The ship is destroyed at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ship']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class EnemyShip(Ship):
    """
    A hostile AI ship. Its hull design comes from its enemy type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    enemy_type: str = Field(default=..., description="""The enemy archetype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EnemyGroup', 'EnemyShip']} })
    hull: float = Field(default=..., description="""Remaining hull points. The ship is destroyed at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ship']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class Asteroid(SpaceEntity):
    """
    An asteroid that breaks into a fuel loot drop when shot enough.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    asteroid_type: str = Field(default=..., description="""The kind of asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidField', 'Asteroid']} })
    integrity: float = Field(default=..., description="""Remaining integrity. The asteroid breaks at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asteroid']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class LootDrop(SpaceEntity):
    """
    Fuel floating in space, collected by flying a player ship into it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    fuel_amount: float = Field(default=..., description="""Fuel collected by picking up this drop.""", json_schema_extra = { "linkml_meta": {'domain_of': ['LootDrop']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GameSession', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Vector3D.model_rebuild()
Attitude.model_rebuild()
ContentPack.model_rebuild()
WeaponType.model_rebuild()
ShipClass.model_rebuild()
EnemyType.model_rebuild()
AsteroidType.model_rebuild()
Galaxy.model_rebuild()
StarSystem.model_rebuild()
SpawnRegion.model_rebuild()
AsteroidField.model_rebuild()
EnemyGroup.model_rebuild()
GameSession.model_rebuild()
Player.model_rebuild()
StarSystemState.model_rebuild()
SpaceEntity.model_rebuild()
Ship.model_rebuild()
PlayerShip.model_rebuild()
EnemyShip.model_rebuild()
Asteroid.model_rebuild()
LootDrop.model_rebuild()
