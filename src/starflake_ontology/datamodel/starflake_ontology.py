# Auto generated from starflake_ontology.yaml by pythongen.py version: 0.0.1
# Schema: starflake-ontology
#
# id: https://w3id.org/M4jor-Tom/starflake-ontology
# description: Domain ontology for Starflake, an open-world 3D space explorer.
#
#   The pilot flies a ship through a galaxy of star systems, shoots enemies and
#   asteroids, loots the fuel they drop, and jumps to a neighbouring system once
#   the tank holds enough fuel.
#
#   The schema has two layers:
#
#   * **Content** (`ContentPack`): static, designer-authored definitions such as
#     ship classes, weapons, enemy and asteroid types, and the galaxy map.
#   * **State** (`GameSession`): the persisted, replicable state of one play
#     session, which references content by identifier.
#
#   Units: distances in metres, time in seconds, angles in radians.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.12.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STARFLAKE = CurieNamespace('starflake', 'https://w3id.org/M4jor-Tom/starflake-ontology/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = STARFLAKE


# Types
class Amount(Float):
    """ A non-negative quantity such as hull points, damage or fuel. """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "Amount"
    type_model_uri = STARFLAKE.Amount


class Distance(Float):
    """ A non-negative length in metres. """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "Distance"
    type_model_uri = STARFLAKE.Distance


class Speed(Float):
    """ A non-negative speed in metres per second. """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "Speed"
    type_model_uri = STARFLAKE.Speed


# Class references
class NamedThingId(extended_str):
    pass


class ContentPackId(NamedThingId):
    pass


class WeaponTypeId(NamedThingId):
    pass


class ShipClassId(NamedThingId):
    pass


class EnemyTypeId(NamedThingId):
    pass


class AsteroidTypeId(NamedThingId):
    pass


class GalaxyId(NamedThingId):
    pass


class StarSystemId(NamedThingId):
    pass


class GameSessionId(extended_str):
    pass


class PlayerId(NamedThingId):
    pass


class SpaceEntityId(extended_str):
    pass


class ShipId(SpaceEntityId):
    pass


class PlayerShipId(ShipId):
    pass


class EnemyShipId(ShipId):
    pass


class AsteroidId(SpaceEntityId):
    pass


class LootDropId(SpaceEntityId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    Anything identifiable and named, whether content or state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.NamedThing

    id: Union[str, NamedThingId] = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vector3D(YAMLRoot):
    """
    A 3D vector in metres (position) or metres per second (velocity). Named Vector3D so it does not shadow the
    engine's own Vector3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Vector3D"]
    class_class_curie: ClassVar[str] = "starflake:Vector3D"
    class_name: ClassVar[str] = "Vector3D"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Vector3D

    x: float = None
    y: float = None
    z: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attitude(YAMLRoot):
    """
    The rotation of a body in 3D space, stored as a unit quaternion. Named Attitude (the aerospace term) so it does
    not clash with the engine's Quaternion type or Godot's Orientation enum.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Attitude"]
    class_class_curie: ClassVar[str] = "starflake:Attitude"
    class_name: ClassVar[str] = "Attitude"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Attitude

    x: float = None
    y: float = None
    z: float = None
    w: float = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.x):
            self.MissingRequiredField("x")
        if not isinstance(self.x, float):
            self.x = float(self.x)

        if self._is_empty(self.y):
            self.MissingRequiredField("y")
        if not isinstance(self.y, float):
            self.y = float(self.y)

        if self._is_empty(self.z):
            self.MissingRequiredField("z")
        if not isinstance(self.z, float):
            self.z = float(self.z)

        if self._is_empty(self.w):
            self.MissingRequiredField("w")
        if not isinstance(self.w, float):
            self.w = float(self.w)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContentPack(NamedThing):
    """
    A versioned bundle of designer-authored content. Everything a session references by identifier is defined here.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["ContentPack"]
    class_class_curie: ClassVar[str] = "starflake:ContentPack"
    class_name: ClassVar[str] = "ContentPack"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.ContentPack

    id: Union[str, ContentPackId] = None
    name: str = None
    starting_ship_class: Union[str, ShipClassId] = None
    galaxy: Union[dict, "Galaxy"] = None
    weapon_types: Optional[Union[dict[Union[str, WeaponTypeId], Union[dict, "WeaponType"]], list[Union[dict, "WeaponType"]]]] = empty_dict()
    ship_classes: Optional[Union[dict[Union[str, ShipClassId], Union[dict, "ShipClass"]], list[Union[dict, "ShipClass"]]]] = empty_dict()
    enemy_types: Optional[Union[dict[Union[str, EnemyTypeId], Union[dict, "EnemyType"]], list[Union[dict, "EnemyType"]]]] = empty_dict()
    asteroid_types: Optional[Union[dict[Union[str, AsteroidTypeId], Union[dict, "AsteroidType"]], list[Union[dict, "AsteroidType"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContentPackId):
            self.id = ContentPackId(self.id)

        if self._is_empty(self.starting_ship_class):
            self.MissingRequiredField("starting_ship_class")
        if not isinstance(self.starting_ship_class, ShipClassId):
            self.starting_ship_class = ShipClassId(self.starting_ship_class)

        if self._is_empty(self.galaxy):
            self.MissingRequiredField("galaxy")
        if not isinstance(self.galaxy, Galaxy):
            self.galaxy = Galaxy(**as_dict(self.galaxy))

        self._normalize_inlined_as_list(slot_name="weapon_types", slot_type=WeaponType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ship_classes", slot_type=ShipClass, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="enemy_types", slot_type=EnemyType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="asteroid_types", slot_type=AsteroidType, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WeaponType(NamedThing):
    """
    A ship-mounted weapon that fires projectiles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["WeaponType"]
    class_class_curie: ClassVar[str] = "starflake:WeaponType"
    class_name: ClassVar[str] = "WeaponType"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.WeaponType

    id: Union[str, WeaponTypeId] = None
    name: str = None
    damage: Union[float, Amount] = None
    fire_rate: Union[float, Amount] = None
    projectile_speed: Union[float, Speed] = None
    max_range: Union[float, Distance] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WeaponTypeId):
            self.id = WeaponTypeId(self.id)

        if self._is_empty(self.damage):
            self.MissingRequiredField("damage")
        if not isinstance(self.damage, Amount):
            self.damage = Amount(self.damage)

        if self._is_empty(self.fire_rate):
            self.MissingRequiredField("fire_rate")
        if not isinstance(self.fire_rate, Amount):
            self.fire_rate = Amount(self.fire_rate)

        if self._is_empty(self.projectile_speed):
            self.MissingRequiredField("projectile_speed")
        if not isinstance(self.projectile_speed, Speed):
            self.projectile_speed = Speed(self.projectile_speed)

        if self._is_empty(self.max_range):
            self.MissingRequiredField("max_range")
        if not isinstance(self.max_range, Distance):
            self.max_range = Distance(self.max_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ShipClass(NamedThing):
    """
    A hull design that player and enemy ships are built from.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["ShipClass"]
    class_class_curie: ClassVar[str] = "starflake:ShipClass"
    class_name: ClassVar[str] = "ShipClass"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.ShipClass

    id: Union[str, ShipClassId] = None
    name: str = None
    max_hull: Union[float, Amount] = None
    max_speed: Union[float, Speed] = None
    acceleration: Union[float, Amount] = None
    turn_rate: Union[float, Amount] = None
    fuel_capacity: Union[float, Amount] = None
    weapons: Optional[Union[Union[str, WeaponTypeId], list[Union[str, WeaponTypeId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShipClassId):
            self.id = ShipClassId(self.id)

        if self._is_empty(self.max_hull):
            self.MissingRequiredField("max_hull")
        if not isinstance(self.max_hull, Amount):
            self.max_hull = Amount(self.max_hull)

        if self._is_empty(self.max_speed):
            self.MissingRequiredField("max_speed")
        if not isinstance(self.max_speed, Speed):
            self.max_speed = Speed(self.max_speed)

        if self._is_empty(self.acceleration):
            self.MissingRequiredField("acceleration")
        if not isinstance(self.acceleration, Amount):
            self.acceleration = Amount(self.acceleration)

        if self._is_empty(self.turn_rate):
            self.MissingRequiredField("turn_rate")
        if not isinstance(self.turn_rate, Amount):
            self.turn_rate = Amount(self.turn_rate)

        if self._is_empty(self.fuel_capacity):
            self.MissingRequiredField("fuel_capacity")
        if not isinstance(self.fuel_capacity, Amount):
            self.fuel_capacity = Amount(self.fuel_capacity)

        if not isinstance(self.weapons, list):
            self.weapons = [self.weapons] if self.weapons is not None else []
        self.weapons = [v if isinstance(v, WeaponTypeId) else WeaponTypeId(v) for v in self.weapons]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnemyType(NamedThing):
    """
    A hostile AI pilot archetype: which hull it flies, when it engages, and what it drops when destroyed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["EnemyType"]
    class_class_curie: ClassVar[str] = "starflake:EnemyType"
    class_name: ClassVar[str] = "EnemyType"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.EnemyType

    id: Union[str, EnemyTypeId] = None
    name: str = None
    ship_class: Union[str, ShipClassId] = None
    fuel_drop: Union[float, Amount] = None
    detection_range: Union[float, Distance] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnemyTypeId):
            self.id = EnemyTypeId(self.id)

        if self._is_empty(self.ship_class):
            self.MissingRequiredField("ship_class")
        if not isinstance(self.ship_class, ShipClassId):
            self.ship_class = ShipClassId(self.ship_class)

        if self._is_empty(self.fuel_drop):
            self.MissingRequiredField("fuel_drop")
        if not isinstance(self.fuel_drop, Amount):
            self.fuel_drop = Amount(self.fuel_drop)

        if self._is_empty(self.detection_range):
            self.MissingRequiredField("detection_range")
        if not isinstance(self.detection_range, Distance):
            self.detection_range = Distance(self.detection_range)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsteroidType(NamedThing):
    """
    A kind of asteroid. Shooting it until its integrity reaches zero breaks it and leaves a fuel loot drop.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["AsteroidType"]
    class_class_curie: ClassVar[str] = "starflake:AsteroidType"
    class_name: ClassVar[str] = "AsteroidType"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.AsteroidType

    id: Union[str, AsteroidTypeId] = None
    name: str = None
    radius: Union[float, Distance] = None
    fuel_drop: Union[float, Amount] = None
    max_integrity: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AsteroidTypeId):
            self.id = AsteroidTypeId(self.id)

        if self._is_empty(self.radius):
            self.MissingRequiredField("radius")
        if not isinstance(self.radius, Distance):
            self.radius = Distance(self.radius)

        if self._is_empty(self.fuel_drop):
            self.MissingRequiredField("fuel_drop")
        if not isinstance(self.fuel_drop, Amount):
            self.fuel_drop = Amount(self.fuel_drop)

        if self._is_empty(self.max_integrity):
            self.MissingRequiredField("max_integrity")
        if not isinstance(self.max_integrity, Amount):
            self.max_integrity = Amount(self.max_integrity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Galaxy(NamedThing):
    """
    The map of star systems connected by jump routes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Galaxy"]
    class_class_curie: ClassVar[str] = "starflake:Galaxy"
    class_name: ClassVar[str] = "Galaxy"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Galaxy

    id: Union[str, GalaxyId] = None
    name: str = None
    star_systems: Union[dict[Union[str, StarSystemId], Union[dict, "StarSystem"]], list[Union[dict, "StarSystem"]]] = empty_dict()
    starting_system: Union[str, StarSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GalaxyId):
            self.id = GalaxyId(self.id)

        if self._is_empty(self.star_systems):
            self.MissingRequiredField("star_systems")
        self._normalize_inlined_as_list(slot_name="star_systems", slot_type=StarSystem, key_name="id", keyed=True)

        if self._is_empty(self.starting_system):
            self.MissingRequiredField("starting_system")
        if not isinstance(self.starting_system, StarSystemId):
            self.starting_system = StarSystemId(self.starting_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StarSystem(NamedThing):
    """
    One playable area around a star. A player ship can jump to any system in jump_targets once it carries at least
    jump_fuel_cost fuel.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["StarSystem"]
    class_class_curie: ClassVar[str] = "starflake:StarSystem"
    class_name: ClassVar[str] = "StarSystem"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.StarSystem

    id: Union[str, StarSystemId] = None
    name: str = None
    star_class: Union[str, "SpectralClass"] = None
    bounds_radius: Union[float, Distance] = None
    jump_fuel_cost: Union[float, Amount] = None
    jump_targets: Optional[Union[Union[str, StarSystemId], list[Union[str, StarSystemId]]]] = empty_list()
    asteroid_fields: Optional[Union[Union[dict, "AsteroidField"], list[Union[dict, "AsteroidField"]]]] = empty_list()
    enemy_groups: Optional[Union[Union[dict, "EnemyGroup"], list[Union[dict, "EnemyGroup"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StarSystemId):
            self.id = StarSystemId(self.id)

        if self._is_empty(self.star_class):
            self.MissingRequiredField("star_class")
        if not isinstance(self.star_class, SpectralClass):
            self.star_class = SpectralClass(self.star_class)

        if self._is_empty(self.bounds_radius):
            self.MissingRequiredField("bounds_radius")
        if not isinstance(self.bounds_radius, Distance):
            self.bounds_radius = Distance(self.bounds_radius)

        if self._is_empty(self.jump_fuel_cost):
            self.MissingRequiredField("jump_fuel_cost")
        if not isinstance(self.jump_fuel_cost, Amount):
            self.jump_fuel_cost = Amount(self.jump_fuel_cost)

        if not isinstance(self.jump_targets, list):
            self.jump_targets = [self.jump_targets] if self.jump_targets is not None else []
        self.jump_targets = [v if isinstance(v, StarSystemId) else StarSystemId(v) for v in self.jump_targets]

        self._normalize_inlined_as_list(slot_name="asteroid_fields", slot_type=AsteroidField, key_name="radius", keyed=False)

        self._normalize_inlined_as_list(slot_name="enemy_groups", slot_type=EnemyGroup, key_name="radius", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpawnRegion(YAMLRoot):
    """
    A sphere inside a star system where a number of entities spawn when the system state is first created.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["SpawnRegion"]
    class_class_curie: ClassVar[str] = "starflake:SpawnRegion"
    class_name: ClassVar[str] = "SpawnRegion"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.SpawnRegion

    radius: Union[float, Distance] = None
    center: Union[dict, Vector3D] = None
    spawn_count: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.radius):
            self.MissingRequiredField("radius")
        if not isinstance(self.radius, Distance):
            self.radius = Distance(self.radius)

        if self._is_empty(self.center):
            self.MissingRequiredField("center")
        if not isinstance(self.center, Vector3D):
            self.center = Vector3D(**as_dict(self.center))

        if self._is_empty(self.spawn_count):
            self.MissingRequiredField("spawn_count")
        if not isinstance(self.spawn_count, int):
            self.spawn_count = int(self.spawn_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsteroidField(SpawnRegion):
    """
    A region filled with asteroids of one type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["AsteroidField"]
    class_class_curie: ClassVar[str] = "starflake:AsteroidField"
    class_name: ClassVar[str] = "AsteroidField"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.AsteroidField

    radius: Union[float, Distance] = None
    center: Union[dict, Vector3D] = None
    spawn_count: int = None
    asteroid_type: Union[str, AsteroidTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.asteroid_type):
            self.MissingRequiredField("asteroid_type")
        if not isinstance(self.asteroid_type, AsteroidTypeId):
            self.asteroid_type = AsteroidTypeId(self.asteroid_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnemyGroup(SpawnRegion):
    """
    A region where enemies of one type spawn.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["EnemyGroup"]
    class_class_curie: ClassVar[str] = "starflake:EnemyGroup"
    class_name: ClassVar[str] = "EnemyGroup"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.EnemyGroup

    radius: Union[float, Distance] = None
    center: Union[dict, Vector3D] = None
    spawn_count: int = None
    enemy_type: Union[str, EnemyTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.enemy_type):
            self.MissingRequiredField("enemy_type")
        if not isinstance(self.enemy_type, EnemyTypeId):
            self.enemy_type = EnemyTypeId(self.enemy_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GameSession(YAMLRoot):
    """
    The persisted state of one play session: a save file in solo, the authoritative world on a host or dedicated
    server in multiplayer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["GameSession"]
    class_class_curie: ClassVar[str] = "starflake:GameSession"
    class_name: ClassVar[str] = "GameSession"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.GameSession

    id: Union[str, GameSessionId] = None
    content_pack: Union[str, ContentPackId] = None
    hosting_mode: Union[str, "HostingMode"] = None
    max_players: int = None
    players: Union[dict[Union[str, PlayerId], Union[dict, "Player"]], list[Union[dict, "Player"]]] = empty_dict()
    host: Optional[Union[str, PlayerId]] = None
    player_ships: Optional[Union[dict[Union[str, PlayerShipId], Union[dict, "PlayerShip"]], list[Union[dict, "PlayerShip"]]]] = empty_dict()
    system_states: Optional[Union[Union[dict, "StarSystemState"], list[Union[dict, "StarSystemState"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GameSessionId):
            self.id = GameSessionId(self.id)

        if self._is_empty(self.content_pack):
            self.MissingRequiredField("content_pack")
        if not isinstance(self.content_pack, ContentPackId):
            self.content_pack = ContentPackId(self.content_pack)

        if self._is_empty(self.hosting_mode):
            self.MissingRequiredField("hosting_mode")
        if not isinstance(self.hosting_mode, HostingMode):
            self.hosting_mode = HostingMode(self.hosting_mode)

        if self._is_empty(self.max_players):
            self.MissingRequiredField("max_players")
        if not isinstance(self.max_players, int):
            self.max_players = int(self.max_players)

        if self._is_empty(self.players):
            self.MissingRequiredField("players")
        self._normalize_inlined_as_list(slot_name="players", slot_type=Player, key_name="id", keyed=True)

        if self.host is not None and not isinstance(self.host, PlayerId):
            self.host = PlayerId(self.host)

        self._normalize_inlined_as_list(slot_name="player_ships", slot_type=PlayerShip, key_name="id", keyed=True)

        if not isinstance(self.system_states, list):
            self.system_states = [self.system_states] if self.system_states is not None else []
        self.system_states = [v if isinstance(v, StarSystemState) else StarSystemState(**as_dict(v)) for v in self.system_states]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Player(NamedThing):
    """
    A person taking part in a session. Its name is shown to other players.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Player"]
    class_class_curie: ClassVar[str] = "starflake:Player"
    class_name: ClassVar[str] = "Player"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Player

    id: Union[str, PlayerId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlayerId):
            self.id = PlayerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StarSystemState(YAMLRoot):
    """
    The world state of one star system within a session: what remains of its asteroids and enemies, and the loot
    floating there.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["StarSystemState"]
    class_class_curie: ClassVar[str] = "starflake:StarSystemState"
    class_name: ClassVar[str] = "StarSystemState"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.StarSystemState

    star_system: Union[str, StarSystemId] = None
    asteroids: Optional[Union[dict[Union[str, AsteroidId], Union[dict, "Asteroid"]], list[Union[dict, "Asteroid"]]]] = empty_dict()
    enemy_ships: Optional[Union[dict[Union[str, EnemyShipId], Union[dict, "EnemyShip"]], list[Union[dict, "EnemyShip"]]]] = empty_dict()
    loot_drops: Optional[Union[dict[Union[str, LootDropId], Union[dict, "LootDrop"]], list[Union[dict, "LootDrop"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.star_system):
            self.MissingRequiredField("star_system")
        if not isinstance(self.star_system, StarSystemId):
            self.star_system = StarSystemId(self.star_system)

        self._normalize_inlined_as_list(slot_name="asteroids", slot_type=Asteroid, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="enemy_ships", slot_type=EnemyShip, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="loot_drops", slot_type=LootDrop, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpaceEntity(YAMLRoot):
    """
    Anything with a physical presence in a star system. The identifier doubles as the network id in multiplayer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["SpaceEntity"]
    class_class_curie: ClassVar[str] = "starflake:SpaceEntity"
    class_name: ClassVar[str] = "SpaceEntity"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.SpaceEntity

    id: Union[str, SpaceEntityId] = None
    position: Union[dict, Vector3D] = None
    velocity: Optional[Union[dict, Vector3D]] = None
    orientation: Optional[Union[dict, Attitude]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpaceEntityId):
            self.id = SpaceEntityId(self.id)

        if self._is_empty(self.position):
            self.MissingRequiredField("position")
        if not isinstance(self.position, Vector3D):
            self.position = Vector3D(**as_dict(self.position))

        if self.velocity is not None and not isinstance(self.velocity, Vector3D):
            self.velocity = Vector3D(**as_dict(self.velocity))

        if self.orientation is not None and not isinstance(self.orientation, Attitude):
            self.orientation = Attitude(**as_dict(self.orientation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ship(SpaceEntity):
    """
    A flying, armed entity that can be destroyed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Ship"]
    class_class_curie: ClassVar[str] = "starflake:Ship"
    class_name: ClassVar[str] = "Ship"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Ship

    id: Union[str, ShipId] = None
    position: Union[dict, Vector3D] = None
    hull: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.hull):
            self.MissingRequiredField("hull")
        if not isinstance(self.hull, Amount):
            self.hull = Amount(self.hull)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlayerShip(Ship):
    """
    A ship flown by a player.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["PlayerShip"]
    class_class_curie: ClassVar[str] = "starflake:PlayerShip"
    class_name: ClassVar[str] = "PlayerShip"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.PlayerShip

    id: Union[str, PlayerShipId] = None
    position: Union[dict, Vector3D] = None
    hull: Union[float, Amount] = None
    ship_class: Union[str, ShipClassId] = None
    pilot: Union[str, PlayerId] = None
    current_system: Union[str, StarSystemId] = None
    fuel: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlayerShipId):
            self.id = PlayerShipId(self.id)

        if self._is_empty(self.ship_class):
            self.MissingRequiredField("ship_class")
        if not isinstance(self.ship_class, ShipClassId):
            self.ship_class = ShipClassId(self.ship_class)

        if self._is_empty(self.pilot):
            self.MissingRequiredField("pilot")
        if not isinstance(self.pilot, PlayerId):
            self.pilot = PlayerId(self.pilot)

        if self._is_empty(self.current_system):
            self.MissingRequiredField("current_system")
        if not isinstance(self.current_system, StarSystemId):
            self.current_system = StarSystemId(self.current_system)

        if self._is_empty(self.fuel):
            self.MissingRequiredField("fuel")
        if not isinstance(self.fuel, Amount):
            self.fuel = Amount(self.fuel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnemyShip(Ship):
    """
    A hostile AI ship. Its hull design comes from its enemy type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["EnemyShip"]
    class_class_curie: ClassVar[str] = "starflake:EnemyShip"
    class_name: ClassVar[str] = "EnemyShip"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.EnemyShip

    id: Union[str, EnemyShipId] = None
    position: Union[dict, Vector3D] = None
    hull: Union[float, Amount] = None
    enemy_type: Union[str, EnemyTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnemyShipId):
            self.id = EnemyShipId(self.id)

        if self._is_empty(self.enemy_type):
            self.MissingRequiredField("enemy_type")
        if not isinstance(self.enemy_type, EnemyTypeId):
            self.enemy_type = EnemyTypeId(self.enemy_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Asteroid(SpaceEntity):
    """
    An asteroid that breaks into a fuel loot drop when shot enough.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Asteroid"]
    class_class_curie: ClassVar[str] = "starflake:Asteroid"
    class_name: ClassVar[str] = "Asteroid"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Asteroid

    id: Union[str, AsteroidId] = None
    position: Union[dict, Vector3D] = None
    asteroid_type: Union[str, AsteroidTypeId] = None
    integrity: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AsteroidId):
            self.id = AsteroidId(self.id)

        if self._is_empty(self.asteroid_type):
            self.MissingRequiredField("asteroid_type")
        if not isinstance(self.asteroid_type, AsteroidTypeId):
            self.asteroid_type = AsteroidTypeId(self.asteroid_type)

        if self._is_empty(self.integrity):
            self.MissingRequiredField("integrity")
        if not isinstance(self.integrity, Amount):
            self.integrity = Amount(self.integrity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LootDrop(SpaceEntity):
    """
    Fuel floating in space, collected by flying a player ship into it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["LootDrop"]
    class_class_curie: ClassVar[str] = "starflake:LootDrop"
    class_name: ClassVar[str] = "LootDrop"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.LootDrop

    id: Union[str, LootDropId] = None
    position: Union[dict, Vector3D] = None
    fuel_amount: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LootDropId):
            self.id = LootDropId(self.id)

        if self._is_empty(self.fuel_amount):
            self.MissingRequiredField("fuel_amount")
        if not isinstance(self.fuel_amount, Amount):
            self.fuel_amount = Amount(self.fuel_amount)

        super().__post_init__(**kwargs)


# Enumerations
class SpectralClass(EnumDefinitionImpl):
    """
    Morgan-Keenan spectral class of a star, hottest to coolest.
    """
    o = PermissibleValue(
        text="o",
        title="O",
        description="Blue, above 30,000 K.")
    b = PermissibleValue(
        text="b",
        title="B",
        description="Blue-white, 10,000 to 30,000 K.")
    a = PermissibleValue(
        text="a",
        title="A",
        description="White, 7,500 to 10,000 K.")
    f = PermissibleValue(
        text="f",
        title="F",
        description="Yellow-white, 6,000 to 7,500 K.")
    g = PermissibleValue(
        text="g",
        title="G",
        description="Yellow, 5,200 to 6,000 K, like the Sun.")
    k = PermissibleValue(
        text="k",
        title="K",
        description="Orange, 3,700 to 5,200 K.")
    m = PermissibleValue(
        text="m",
        title="M",
        description="Red, below 3,700 K.")

    _defn = EnumDefinition(
        name="SpectralClass",
        description="Morgan-Keenan spectral class of a star, hottest to coolest.",
    )

class HostingMode(EnumDefinitionImpl):
    """
    Who runs the authoritative simulation of a session.
    """
    solo = PermissibleValue(
        text="solo",
        description="Single player, simulated locally, no network.")
    player_hosted = PermissibleValue(
        text="player_hosted",
        description="A player's game acts as server for the players they invite.")
    dedicated_server = PermissibleValue(
        text="dedicated_server",
        description="A server not run by any player hosts the session.")

    _defn = EnumDefinition(
        name="HostingMode",
        description="Who runs the authoritative simulation of a session.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=STARFLAKE.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=STARFLAKE.name, domain=None, range=str)

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=STARFLAKE.description, domain=None, range=Optional[str])

slots.x = Slot(uri=STARFLAKE.x, name="x", curie=STARFLAKE.curie('x'),
                   model_uri=STARFLAKE.x, domain=None, range=float)

slots.y = Slot(uri=STARFLAKE.y, name="y", curie=STARFLAKE.curie('y'),
                   model_uri=STARFLAKE.y, domain=None, range=float)

slots.z = Slot(uri=STARFLAKE.z, name="z", curie=STARFLAKE.curie('z'),
                   model_uri=STARFLAKE.z, domain=None, range=float)

slots.w = Slot(uri=STARFLAKE.w, name="w", curie=STARFLAKE.curie('w'),
                   model_uri=STARFLAKE.w, domain=None, range=float)

slots.radius = Slot(uri=STARFLAKE.radius, name="radius", curie=STARFLAKE.curie('radius'),
                   model_uri=STARFLAKE.radius, domain=None, range=Union[float, Distance])

slots.fuel_drop = Slot(uri=STARFLAKE.fuel_drop, name="fuel_drop", curie=STARFLAKE.curie('fuel_drop'),
                   model_uri=STARFLAKE.fuel_drop, domain=None, range=Union[float, Amount])

slots.ship_class = Slot(uri=STARFLAKE.ship_class, name="ship_class", curie=STARFLAKE.curie('ship_class'),
                   model_uri=STARFLAKE.ship_class, domain=None, range=Union[str, ShipClassId])

slots.asteroid_type = Slot(uri=STARFLAKE.asteroid_type, name="asteroid_type", curie=STARFLAKE.curie('asteroid_type'),
                   model_uri=STARFLAKE.asteroid_type, domain=None, range=Union[str, AsteroidTypeId])

slots.enemy_type = Slot(uri=STARFLAKE.enemy_type, name="enemy_type", curie=STARFLAKE.curie('enemy_type'),
                   model_uri=STARFLAKE.enemy_type, domain=None, range=Union[str, EnemyTypeId])

slots.contentPack__weapon_types = Slot(uri=STARFLAKE.weapon_types, name="contentPack__weapon_types", curie=STARFLAKE.curie('weapon_types'),
                   model_uri=STARFLAKE.contentPack__weapon_types, domain=None, range=Optional[Union[dict[Union[str, WeaponTypeId], Union[dict, WeaponType]], list[Union[dict, WeaponType]]]])

slots.contentPack__ship_classes = Slot(uri=STARFLAKE.ship_classes, name="contentPack__ship_classes", curie=STARFLAKE.curie('ship_classes'),
                   model_uri=STARFLAKE.contentPack__ship_classes, domain=None, range=Optional[Union[dict[Union[str, ShipClassId], Union[dict, ShipClass]], list[Union[dict, ShipClass]]]])

slots.contentPack__enemy_types = Slot(uri=STARFLAKE.enemy_types, name="contentPack__enemy_types", curie=STARFLAKE.curie('enemy_types'),
                   model_uri=STARFLAKE.contentPack__enemy_types, domain=None, range=Optional[Union[dict[Union[str, EnemyTypeId], Union[dict, EnemyType]], list[Union[dict, EnemyType]]]])

slots.contentPack__asteroid_types = Slot(uri=STARFLAKE.asteroid_types, name="contentPack__asteroid_types", curie=STARFLAKE.curie('asteroid_types'),
                   model_uri=STARFLAKE.contentPack__asteroid_types, domain=None, range=Optional[Union[dict[Union[str, AsteroidTypeId], Union[dict, AsteroidType]], list[Union[dict, AsteroidType]]]])

slots.contentPack__starting_ship_class = Slot(uri=STARFLAKE.starting_ship_class, name="contentPack__starting_ship_class", curie=STARFLAKE.curie('starting_ship_class'),
                   model_uri=STARFLAKE.contentPack__starting_ship_class, domain=None, range=Union[str, ShipClassId])

slots.contentPack__galaxy = Slot(uri=STARFLAKE.galaxy, name="contentPack__galaxy", curie=STARFLAKE.curie('galaxy'),
                   model_uri=STARFLAKE.contentPack__galaxy, domain=None, range=Union[dict, Galaxy])

slots.weaponType__damage = Slot(uri=STARFLAKE.damage, name="weaponType__damage", curie=STARFLAKE.curie('damage'),
                   model_uri=STARFLAKE.weaponType__damage, domain=None, range=Union[float, Amount])

slots.weaponType__fire_rate = Slot(uri=STARFLAKE.fire_rate, name="weaponType__fire_rate", curie=STARFLAKE.curie('fire_rate'),
                   model_uri=STARFLAKE.weaponType__fire_rate, domain=None, range=Union[float, Amount])

slots.weaponType__projectile_speed = Slot(uri=STARFLAKE.projectile_speed, name="weaponType__projectile_speed", curie=STARFLAKE.curie('projectile_speed'),
                   model_uri=STARFLAKE.weaponType__projectile_speed, domain=None, range=Union[float, Speed])

slots.weaponType__max_range = Slot(uri=STARFLAKE.max_range, name="weaponType__max_range", curie=STARFLAKE.curie('max_range'),
                   model_uri=STARFLAKE.weaponType__max_range, domain=None, range=Union[float, Distance])

slots.shipClass__max_hull = Slot(uri=STARFLAKE.max_hull, name="shipClass__max_hull", curie=STARFLAKE.curie('max_hull'),
                   model_uri=STARFLAKE.shipClass__max_hull, domain=None, range=Union[float, Amount])

slots.shipClass__max_speed = Slot(uri=STARFLAKE.max_speed, name="shipClass__max_speed", curie=STARFLAKE.curie('max_speed'),
                   model_uri=STARFLAKE.shipClass__max_speed, domain=None, range=Union[float, Speed])

slots.shipClass__acceleration = Slot(uri=STARFLAKE.acceleration, name="shipClass__acceleration", curie=STARFLAKE.curie('acceleration'),
                   model_uri=STARFLAKE.shipClass__acceleration, domain=None, range=Union[float, Amount])

slots.shipClass__turn_rate = Slot(uri=STARFLAKE.turn_rate, name="shipClass__turn_rate", curie=STARFLAKE.curie('turn_rate'),
                   model_uri=STARFLAKE.shipClass__turn_rate, domain=None, range=Union[float, Amount])

slots.shipClass__fuel_capacity = Slot(uri=STARFLAKE.fuel_capacity, name="shipClass__fuel_capacity", curie=STARFLAKE.curie('fuel_capacity'),
                   model_uri=STARFLAKE.shipClass__fuel_capacity, domain=None, range=Union[float, Amount])

slots.shipClass__weapons = Slot(uri=STARFLAKE.weapons, name="shipClass__weapons", curie=STARFLAKE.curie('weapons'),
                   model_uri=STARFLAKE.shipClass__weapons, domain=None, range=Optional[Union[Union[str, WeaponTypeId], list[Union[str, WeaponTypeId]]]])

slots.enemyType__detection_range = Slot(uri=STARFLAKE.detection_range, name="enemyType__detection_range", curie=STARFLAKE.curie('detection_range'),
                   model_uri=STARFLAKE.enemyType__detection_range, domain=None, range=Union[float, Distance])

slots.asteroidType__max_integrity = Slot(uri=STARFLAKE.max_integrity, name="asteroidType__max_integrity", curie=STARFLAKE.curie('max_integrity'),
                   model_uri=STARFLAKE.asteroidType__max_integrity, domain=None, range=Union[float, Amount])

slots.galaxy__star_systems = Slot(uri=STARFLAKE.star_systems, name="galaxy__star_systems", curie=STARFLAKE.curie('star_systems'),
                   model_uri=STARFLAKE.galaxy__star_systems, domain=None, range=Union[dict[Union[str, StarSystemId], Union[dict, StarSystem]], list[Union[dict, StarSystem]]])

slots.galaxy__starting_system = Slot(uri=STARFLAKE.starting_system, name="galaxy__starting_system", curie=STARFLAKE.curie('starting_system'),
                   model_uri=STARFLAKE.galaxy__starting_system, domain=None, range=Union[str, StarSystemId])

slots.starSystem__star_class = Slot(uri=STARFLAKE.star_class, name="starSystem__star_class", curie=STARFLAKE.curie('star_class'),
                   model_uri=STARFLAKE.starSystem__star_class, domain=None, range=Union[str, "SpectralClass"])

slots.starSystem__bounds_radius = Slot(uri=STARFLAKE.bounds_radius, name="starSystem__bounds_radius", curie=STARFLAKE.curie('bounds_radius'),
                   model_uri=STARFLAKE.starSystem__bounds_radius, domain=None, range=Union[float, Distance])

slots.starSystem__jump_fuel_cost = Slot(uri=STARFLAKE.jump_fuel_cost, name="starSystem__jump_fuel_cost", curie=STARFLAKE.curie('jump_fuel_cost'),
                   model_uri=STARFLAKE.starSystem__jump_fuel_cost, domain=None, range=Union[float, Amount])

slots.starSystem__jump_targets = Slot(uri=STARFLAKE.jump_targets, name="starSystem__jump_targets", curie=STARFLAKE.curie('jump_targets'),
                   model_uri=STARFLAKE.starSystem__jump_targets, domain=None, range=Optional[Union[Union[str, StarSystemId], list[Union[str, StarSystemId]]]])

slots.starSystem__asteroid_fields = Slot(uri=STARFLAKE.asteroid_fields, name="starSystem__asteroid_fields", curie=STARFLAKE.curie('asteroid_fields'),
                   model_uri=STARFLAKE.starSystem__asteroid_fields, domain=None, range=Optional[Union[Union[dict, AsteroidField], list[Union[dict, AsteroidField]]]])

slots.starSystem__enemy_groups = Slot(uri=STARFLAKE.enemy_groups, name="starSystem__enemy_groups", curie=STARFLAKE.curie('enemy_groups'),
                   model_uri=STARFLAKE.starSystem__enemy_groups, domain=None, range=Optional[Union[Union[dict, EnemyGroup], list[Union[dict, EnemyGroup]]]])

slots.spawnRegion__center = Slot(uri=STARFLAKE.center, name="spawnRegion__center", curie=STARFLAKE.curie('center'),
                   model_uri=STARFLAKE.spawnRegion__center, domain=None, range=Union[dict, Vector3D])

slots.spawnRegion__spawn_count = Slot(uri=STARFLAKE.spawn_count, name="spawnRegion__spawn_count", curie=STARFLAKE.curie('spawn_count'),
                   model_uri=STARFLAKE.spawnRegion__spawn_count, domain=None, range=int)

slots.gameSession__content_pack = Slot(uri=STARFLAKE.content_pack, name="gameSession__content_pack", curie=STARFLAKE.curie('content_pack'),
                   model_uri=STARFLAKE.gameSession__content_pack, domain=None, range=Union[str, ContentPackId])

slots.gameSession__hosting_mode = Slot(uri=STARFLAKE.hosting_mode, name="gameSession__hosting_mode", curie=STARFLAKE.curie('hosting_mode'),
                   model_uri=STARFLAKE.gameSession__hosting_mode, domain=None, range=Union[str, "HostingMode"])

slots.gameSession__host = Slot(uri=STARFLAKE.host, name="gameSession__host", curie=STARFLAKE.curie('host'),
                   model_uri=STARFLAKE.gameSession__host, domain=None, range=Optional[Union[str, PlayerId]])

slots.gameSession__max_players = Slot(uri=STARFLAKE.max_players, name="gameSession__max_players", curie=STARFLAKE.curie('max_players'),
                   model_uri=STARFLAKE.gameSession__max_players, domain=None, range=int)

slots.gameSession__players = Slot(uri=STARFLAKE.players, name="gameSession__players", curie=STARFLAKE.curie('players'),
                   model_uri=STARFLAKE.gameSession__players, domain=None, range=Union[dict[Union[str, PlayerId], Union[dict, Player]], list[Union[dict, Player]]])

slots.gameSession__player_ships = Slot(uri=STARFLAKE.player_ships, name="gameSession__player_ships", curie=STARFLAKE.curie('player_ships'),
                   model_uri=STARFLAKE.gameSession__player_ships, domain=None, range=Optional[Union[dict[Union[str, PlayerShipId], Union[dict, PlayerShip]], list[Union[dict, PlayerShip]]]])

slots.gameSession__system_states = Slot(uri=STARFLAKE.system_states, name="gameSession__system_states", curie=STARFLAKE.curie('system_states'),
                   model_uri=STARFLAKE.gameSession__system_states, domain=None, range=Optional[Union[Union[dict, StarSystemState], list[Union[dict, StarSystemState]]]])

slots.starSystemState__star_system = Slot(uri=STARFLAKE.star_system, name="starSystemState__star_system", curie=STARFLAKE.curie('star_system'),
                   model_uri=STARFLAKE.starSystemState__star_system, domain=None, range=Union[str, StarSystemId])

slots.starSystemState__asteroids = Slot(uri=STARFLAKE.asteroids, name="starSystemState__asteroids", curie=STARFLAKE.curie('asteroids'),
                   model_uri=STARFLAKE.starSystemState__asteroids, domain=None, range=Optional[Union[dict[Union[str, AsteroidId], Union[dict, Asteroid]], list[Union[dict, Asteroid]]]])

slots.starSystemState__enemy_ships = Slot(uri=STARFLAKE.enemy_ships, name="starSystemState__enemy_ships", curie=STARFLAKE.curie('enemy_ships'),
                   model_uri=STARFLAKE.starSystemState__enemy_ships, domain=None, range=Optional[Union[dict[Union[str, EnemyShipId], Union[dict, EnemyShip]], list[Union[dict, EnemyShip]]]])

slots.starSystemState__loot_drops = Slot(uri=STARFLAKE.loot_drops, name="starSystemState__loot_drops", curie=STARFLAKE.curie('loot_drops'),
                   model_uri=STARFLAKE.starSystemState__loot_drops, domain=None, range=Optional[Union[dict[Union[str, LootDropId], Union[dict, LootDrop]], list[Union[dict, LootDrop]]]])

slots.spaceEntity__position = Slot(uri=STARFLAKE.position, name="spaceEntity__position", curie=STARFLAKE.curie('position'),
                   model_uri=STARFLAKE.spaceEntity__position, domain=None, range=Union[dict, Vector3D])

slots.spaceEntity__velocity = Slot(uri=STARFLAKE.velocity, name="spaceEntity__velocity", curie=STARFLAKE.curie('velocity'),
                   model_uri=STARFLAKE.spaceEntity__velocity, domain=None, range=Optional[Union[dict, Vector3D]])

slots.spaceEntity__orientation = Slot(uri=STARFLAKE.orientation, name="spaceEntity__orientation", curie=STARFLAKE.curie('orientation'),
                   model_uri=STARFLAKE.spaceEntity__orientation, domain=None, range=Optional[Union[dict, Attitude]])

slots.ship__hull = Slot(uri=STARFLAKE.hull, name="ship__hull", curie=STARFLAKE.curie('hull'),
                   model_uri=STARFLAKE.ship__hull, domain=None, range=Union[float, Amount])

slots.playerShip__pilot = Slot(uri=STARFLAKE.pilot, name="playerShip__pilot", curie=STARFLAKE.curie('pilot'),
                   model_uri=STARFLAKE.playerShip__pilot, domain=None, range=Union[str, PlayerId])

slots.playerShip__current_system = Slot(uri=STARFLAKE.current_system, name="playerShip__current_system", curie=STARFLAKE.curie('current_system'),
                   model_uri=STARFLAKE.playerShip__current_system, domain=None, range=Union[str, StarSystemId])

slots.playerShip__fuel = Slot(uri=STARFLAKE.fuel, name="playerShip__fuel", curie=STARFLAKE.curie('fuel'),
                   model_uri=STARFLAKE.playerShip__fuel, domain=None, range=Union[float, Amount])

slots.asteroid__integrity = Slot(uri=STARFLAKE.integrity, name="asteroid__integrity", curie=STARFLAKE.curie('integrity'),
                   model_uri=STARFLAKE.asteroid__integrity, domain=None, range=Union[float, Amount])

slots.lootDrop__fuel_amount = Slot(uri=STARFLAKE.fuel_amount, name="lootDrop__fuel_amount", curie=STARFLAKE.curie('fuel_amount'),
                   model_uri=STARFLAKE.lootDrop__fuel_amount, domain=None, range=Union[float, Amount])

slots.AsteroidType_radius = Slot(uri=STARFLAKE.radius, name="AsteroidType_radius", curie=STARFLAKE.curie('radius'),
                   model_uri=STARFLAKE.AsteroidType_radius, domain=AsteroidType, range=Union[float, Distance])

slots.SpawnRegion_radius = Slot(uri=STARFLAKE.radius, name="SpawnRegion_radius", curie=STARFLAKE.curie('radius'),
                   model_uri=STARFLAKE.SpawnRegion_radius, domain=SpawnRegion, range=Union[float, Distance])
