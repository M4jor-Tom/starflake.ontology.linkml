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
                    'A pilot flies a ship through a galaxy of star systems, shoots '
                    'raiders and\n'
                    'asteroids, scoops up the fuel they leave, and jumps to a '
                    'neighbouring system\n'
                    'once the tank holds enough fuel.\n'
                    '\n'
                    'The ontology describes the universe only, in words one of its '
                    'inhabitants\n'
                    'would use. How the game is played, hosted and tuned is '
                    'specified in the\n'
                    'design repository.\n'
                    '\n'
                    'The schema has two layers:\n'
                    '\n'
                    '* **Content** (`Galaxy`): what exists, such as ship classes, '
                    'weapons,\n'
                    '  raider and asteroid types, and the star systems.\n'
                    '* **State** (`GalaxyState`): what is where at one moment, '
                    'which references\n'
                    '  content by identifier.\n'
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
     'subsets': {'content': {'description': 'What exists in a galaxy, rooted at '
                                            'Galaxy.',
                             'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                             'name': 'content'},
                 'core': {'description': 'Building blocks shared by content and '
                                         'state.',
                          'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
                          'name': 'core'},
                 'state': {'description': 'What is where at one moment, rooted at '
                                          'GalaxyState.',
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



class NamedThing(ConfiguredBaseModel):
    """
    Anything identifiable and named, whether content or state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'schema:Thing',
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['core']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
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


class WeaponType(NamedThing):
    """
    A ship-mounted weapon that fires projectiles.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    damage: float = Field(default=..., description="""Hull or integrity points removed per hit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    fire_rate: float = Field(default=..., description="""Shots per second.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType'], 'unit': {'ucum_code': '/s'}} })
    projectile_speed: float = Field(default=..., description="""Speed of a fired projectile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    max_range: float = Field(default=..., description="""Distance after which a projectile dissipates.""", json_schema_extra = { "linkml_meta": {'domain_of': ['WeaponType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class ShipClass(NamedThing):
    """
    A hull design that pilot and raider ships are built from.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    max_hull: float = Field(default=..., description="""Hull points of an undamaged ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    max_speed: float = Field(default=..., description="""Top linear speed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    acceleration: float = Field(default=..., description="""Linear acceleration under full thrust.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass'], 'unit': {'ucum_code': 'm/s2'}} })
    turn_rate: float = Field(default=..., description="""Maximum angular speed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass'], 'unit': {'ucum_code': 'rad/s'}} })
    fuel_capacity: float = Field(default=..., description="""Maximum fuel the tank holds. Zero for ships that never jump.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    scoop_radius: float = Field(default=..., description="""Distance within which the fuel scoop takes in a fuel pod. Zero for ships without a scoop.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    tractor_range: float = Field(default=..., description="""Distance within which the ship pulls fuel pods toward itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    tractor_speed: float = Field(default=..., description="""Speed at which a pulled fuel pod moves toward the ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    weapons: Optional[list[str]] = Field(default=None, description="""Weapons mounted on every ship of this class.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ShipClass']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class RaiderType(NamedThing):
    """
    A raider archetype: which hull it flies, when it engages, how close it fights, and what it leaves when destroyed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    ship_class: str = Field(default=..., description="""The hull design.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType', 'PilotShip']} })
    fuel_yield: float = Field(default=..., description="""Fuel in the pod left when this is destroyed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType', 'AsteroidType']} })
    detection_range: float = Field(default=..., description="""Distance within which the raider notices and chases a pilot ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType']} })
    keep_distance: float = Field(default=..., description="""Distance from its target at which the raider stops closing in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class AsteroidType(NamedThing):
    """
    A kind of asteroid. Shooting it until its integrity reaches zero breaks it and leaves a fuel pod.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'slot_usage': {'radius': {'description': 'Collision radius of the asteroid.',
                                   'name': 'radius'}}})

    radius: float = Field(default=..., description="""Collision radius of the asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'Region']} })
    fuel_yield: float = Field(default=..., description="""Fuel in the pod left when this is destroyed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType', 'AsteroidType']} })
    max_integrity: float = Field(default=..., description="""Damage needed to break the asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Galaxy(NamedThing):
    """
    Star systems connected by jump routes, and the kinds of ships, weapons, raiders and asteroids found among them.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'tree_root': True})

    weapon_types: Optional[list[WeaponType]] = Field(default=None, description="""Weapons that ship classes mount.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    ship_classes: Optional[list[ShipClass]] = Field(default=None, description="""Hull designs that pilot and raider ships are built from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    raider_types: Optional[list[RaiderType]] = Field(default=None, description="""Raider archetypes that roam the star systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    asteroid_types: Optional[list[AsteroidType]] = Field(default=None, description="""Asteroid kinds found in the star systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    star_systems: list[StarSystem] = Field(default=..., description="""Every star system of the galaxy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Galaxy']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StarSystem(NamedThing):
    """
    The space around one star. A pilot ship can jump to any system in jump_targets once it carries at least jump_fuel_cost fuel.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    star_class: SpectralClass = Field(default=..., description="""Spectral class of the star, driving its look.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    bounds_radius: float = Field(default=..., description="""Radius of the navigable sphere centred on the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    jump_fuel_cost: float = Field(default=..., description="""Fuel consumed by a jump out of this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    jump_targets: Optional[list[str]] = Field(default=None, description="""Systems reachable by a single jump from this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    asteroid_fields: Optional[list[AsteroidField]] = Field(default=None, description="""Asteroid fields of this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    raider_packs: Optional[list[RaiderPack]] = Field(default=None, description="""Raider packs of this system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystem']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class Region(ConfiguredBaseModel):
    """
    A sphere inside a star system that holds a number of bodies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content'],
         'slot_usage': {'radius': {'description': 'Radius of the region.',
                                   'name': 'radius'}}})

    radius: float = Field(default=..., description="""Radius of the region.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'Region']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })
    count: int = Field(default=..., description="""Number of bodies the region holds.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })


class AsteroidField(Region):
    """
    A region filled with asteroids of one type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    asteroid_type: str = Field(default=..., description="""The kind of asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidField', 'Asteroid']} })
    radius: float = Field(default=..., description="""Radius of the region.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'Region']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })
    count: int = Field(default=..., description="""Number of bodies the region holds.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })


class RaiderPack(Region):
    """
    A region that raiders of one type hold.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['content']})

    raider_type: str = Field(default=..., description="""The raider archetype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderPack', 'RaiderShip']} })
    radius: float = Field(default=..., description="""Radius of the region.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidType', 'Region']} })
    center: Vector3D = Field(default=..., description="""Centre of the region, relative to the star.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })
    count: int = Field(default=..., description="""Number of bodies the region holds.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['Region']} })


class GalaxyState(ConfiguredBaseModel):
    """
    What is where in a galaxy at one moment: its pilots, their ships, and the state of the star systems visited so far.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    galaxy: str = Field(default=..., description="""The galaxy this is the state of.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GalaxyState']} })
    pilots: list[Pilot] = Field(default=..., description="""Everyone who flies a ship in the galaxy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GalaxyState']} })
    pilot_ships: Optional[list[PilotShip]] = Field(default=None, description="""The ship of each pilot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GalaxyState']} })
    system_states: Optional[list[StarSystemState]] = Field(default=None, description="""State of the systems visited so far. A system without state has not been visited yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GalaxyState']} })


class Pilot(NamedThing):
    """
    A person who flies a ship. Other pilots know them by name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    name: str = Field(default=..., description="""A human-readable name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""A human-readable description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'], 'slot_uri': 'schema:description'} })


class StarSystemState(ConfiguredBaseModel):
    """
    The state of one star system: what remains of its asteroids and raiders, and the fuel pods floating there.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    star_system: str = Field(default=..., description="""The star system this state belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    asteroids: Optional[list[Asteroid]] = Field(default=None, description="""Asteroids not broken yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    raider_ships: Optional[list[RaiderShip]] = Field(default=None, description="""Raider ships not destroyed yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })
    fuel_pods: Optional[list[FuelPod]] = Field(default=None, description="""Fuel pods not scooped up yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StarSystemState']} })


class SpaceEntity(ConfiguredBaseModel):
    """
    Anything with a physical presence in a star system.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
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
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class PilotShip(Ship):
    """
    A ship flown by a pilot.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    ship_class: str = Field(default=..., description="""The hull design.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderType', 'PilotShip']} })
    pilot: str = Field(default=..., description="""The pilot flying the ship.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PilotShip']} })
    current_system: str = Field(default=..., description="""The star system the ship is in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PilotShip']} })
    fuel: float = Field(default=..., description="""Fuel in the tank, at most the ship class fuel_capacity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PilotShip']} })
    hull: float = Field(default=..., description="""Remaining hull points. The ship is destroyed at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ship']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class RaiderShip(Ship):
    """
    A hostile ship. Its hull design comes from its raider type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    raider_type: str = Field(default=..., description="""The raider archetype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['RaiderPack', 'RaiderShip']} })
    hull: float = Field(default=..., description="""Remaining hull points. The ship is destroyed at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ship']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class Asteroid(SpaceEntity):
    """
    An asteroid that breaks into a fuel pod when shot enough.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    asteroid_type: str = Field(default=..., description="""The kind of asteroid.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AsteroidField', 'Asteroid']} })
    integrity: float = Field(default=..., description="""Remaining integrity. The asteroid breaks at zero.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Asteroid']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


class FuelPod(SpaceEntity):
    """
    Fuel floating in space, scooped up by a pilot ship that flies into it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/M4jor-Tom/starflake-ontology',
         'in_subset': ['state']})

    fuel_amount: float = Field(default=..., description="""Fuel the pod holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FuelPod']} })
    id: str = Field(default=..., description="""A unique identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing', 'GalaxyState', 'SpaceEntity'],
         'slot_uri': 'schema:identifier'} })
    position: Vector3D = Field(default=..., description="""Position relative to the star of the current system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    velocity: Optional[Vector3D] = Field(default=None, description="""Linear velocity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })
    orientation: Optional[Attitude] = Field(default=None, description="""Facing of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpaceEntity']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
Vector3D.model_rebuild()
Attitude.model_rebuild()
WeaponType.model_rebuild()
ShipClass.model_rebuild()
RaiderType.model_rebuild()
AsteroidType.model_rebuild()
Galaxy.model_rebuild()
StarSystem.model_rebuild()
Region.model_rebuild()
AsteroidField.model_rebuild()
RaiderPack.model_rebuild()
GalaxyState.model_rebuild()
Pilot.model_rebuild()
StarSystemState.model_rebuild()
SpaceEntity.model_rebuild()
Ship.model_rebuild()
PilotShip.model_rebuild()
RaiderShip.model_rebuild()
Asteroid.model_rebuild()
FuelPod.model_rebuild()
