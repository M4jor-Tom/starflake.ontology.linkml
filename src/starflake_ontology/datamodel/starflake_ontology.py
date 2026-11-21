# Auto generated from starflake_ontology.yaml by pythongen.py version: 0.0.1
# Schema: starflake-ontology
#
# id: https://w3id.org/M4jor-Tom/starflake-ontology
# description: Domain ontology for Starflake, an open-world 3D space explorer.
#
#   A pilot flies a ship through a galaxy of star systems, shoots raiders and
#   asteroids, scoops up the fuel they leave, and jumps to a neighbouring system
#   once the tank holds enough fuel.
#
#   The ontology describes the universe only, in words one of its inhabitants
#   would use. How the game is played, hosted and tuned is specified in the
#   design repository.
#
#   The schema has two layers:
#
#   * **Content** (`Galaxy`): what exists, such as ship classes, weapons,
#     raider and asteroid types, and the star systems.
#   * **State** (`GalaxyState`): what is where at one moment, which references
#     content by identifier.
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


class WeaponTypeId(NamedThingId):
    pass


class ShipClassId(NamedThingId):
    pass


class RaiderTypeId(NamedThingId):
    pass


class AsteroidTypeId(NamedThingId):
    pass


class GalaxyId(NamedThingId):
    pass


class StarSystemId(NamedThingId):
    pass


class GalaxyStateId(extended_str):
    pass


class PilotId(NamedThingId):
    pass


class SpaceEntityId(extended_str):
    pass


class ShipId(SpaceEntityId):
    pass


class PilotShipId(ShipId):
    pass


class RaiderShipId(ShipId):
    pass


class AsteroidId(SpaceEntityId):
    pass


class FuelPodId(SpaceEntityId):
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
    A hull design that pilot and raider ships are built from.
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
    scoop_radius: Union[float, Distance] = None
    tractor_range: Union[float, Distance] = None
    tractor_speed: Union[float, Speed] = None
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

        if self._is_empty(self.scoop_radius):
            self.MissingRequiredField("scoop_radius")
        if not isinstance(self.scoop_radius, Distance):
            self.scoop_radius = Distance(self.scoop_radius)

        if self._is_empty(self.tractor_range):
            self.MissingRequiredField("tractor_range")
        if not isinstance(self.tractor_range, Distance):
            self.tractor_range = Distance(self.tractor_range)

        if self._is_empty(self.tractor_speed):
            self.MissingRequiredField("tractor_speed")
        if not isinstance(self.tractor_speed, Speed):
            self.tractor_speed = Speed(self.tractor_speed)

        if not isinstance(self.weapons, list):
            self.weapons = [self.weapons] if self.weapons is not None else []
        self.weapons = [v if isinstance(v, WeaponTypeId) else WeaponTypeId(v) for v in self.weapons]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RaiderType(NamedThing):
    """
    A raider archetype: which hull it flies, when it engages, how close it fights, and what it leaves when destroyed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["RaiderType"]
    class_class_curie: ClassVar[str] = "starflake:RaiderType"
    class_name: ClassVar[str] = "RaiderType"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.RaiderType

    id: Union[str, RaiderTypeId] = None
    name: str = None
    ship_class: Union[str, ShipClassId] = None
    fuel_yield: Union[float, Amount] = None
    detection_range: Union[float, Distance] = None
    keep_distance: Union[float, Distance] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RaiderTypeId):
            self.id = RaiderTypeId(self.id)

        if self._is_empty(self.ship_class):
            self.MissingRequiredField("ship_class")
        if not isinstance(self.ship_class, ShipClassId):
            self.ship_class = ShipClassId(self.ship_class)

        if self._is_empty(self.fuel_yield):
            self.MissingRequiredField("fuel_yield")
        if not isinstance(self.fuel_yield, Amount):
            self.fuel_yield = Amount(self.fuel_yield)

        if self._is_empty(self.detection_range):
            self.MissingRequiredField("detection_range")
        if not isinstance(self.detection_range, Distance):
            self.detection_range = Distance(self.detection_range)

        if self._is_empty(self.keep_distance):
            self.MissingRequiredField("keep_distance")
        if not isinstance(self.keep_distance, Distance):
            self.keep_distance = Distance(self.keep_distance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsteroidType(NamedThing):
    """
    A kind of asteroid. Shooting it until its integrity reaches zero breaks it and leaves a fuel pod.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["AsteroidType"]
    class_class_curie: ClassVar[str] = "starflake:AsteroidType"
    class_name: ClassVar[str] = "AsteroidType"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.AsteroidType

    id: Union[str, AsteroidTypeId] = None
    name: str = None
    radius: Union[float, Distance] = None
    fuel_yield: Union[float, Amount] = None
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

        if self._is_empty(self.fuel_yield):
            self.MissingRequiredField("fuel_yield")
        if not isinstance(self.fuel_yield, Amount):
            self.fuel_yield = Amount(self.fuel_yield)

        if self._is_empty(self.max_integrity):
            self.MissingRequiredField("max_integrity")
        if not isinstance(self.max_integrity, Amount):
            self.max_integrity = Amount(self.max_integrity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Galaxy(NamedThing):
    """
    Star systems connected by jump routes, and the kinds of ships, weapons, raiders and asteroids found among them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Galaxy"]
    class_class_curie: ClassVar[str] = "starflake:Galaxy"
    class_name: ClassVar[str] = "Galaxy"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Galaxy

    id: Union[str, GalaxyId] = None
    name: str = None
    star_systems: Union[dict[Union[str, StarSystemId], Union[dict, "StarSystem"]], list[Union[dict, "StarSystem"]]] = empty_dict()
    weapon_types: Optional[Union[dict[Union[str, WeaponTypeId], Union[dict, WeaponType]], list[Union[dict, WeaponType]]]] = empty_dict()
    ship_classes: Optional[Union[dict[Union[str, ShipClassId], Union[dict, ShipClass]], list[Union[dict, ShipClass]]]] = empty_dict()
    raider_types: Optional[Union[dict[Union[str, RaiderTypeId], Union[dict, RaiderType]], list[Union[dict, RaiderType]]]] = empty_dict()
    asteroid_types: Optional[Union[dict[Union[str, AsteroidTypeId], Union[dict, AsteroidType]], list[Union[dict, AsteroidType]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GalaxyId):
            self.id = GalaxyId(self.id)

        if self._is_empty(self.star_systems):
            self.MissingRequiredField("star_systems")
        self._normalize_inlined_as_list(slot_name="star_systems", slot_type=StarSystem, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="weapon_types", slot_type=WeaponType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ship_classes", slot_type=ShipClass, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="raider_types", slot_type=RaiderType, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="asteroid_types", slot_type=AsteroidType, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StarSystem(NamedThing):
    """
    The space around one star. A pilot ship can jump to any system in jump_targets once it carries at least
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
    raider_packs: Optional[Union[Union[dict, "RaiderPack"], list[Union[dict, "RaiderPack"]]]] = empty_list()

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

        self._normalize_inlined_as_list(slot_name="raider_packs", slot_type=RaiderPack, key_name="radius", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Region(YAMLRoot):
    """
    A sphere inside a star system that holds a number of bodies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Region"]
    class_class_curie: ClassVar[str] = "starflake:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Region

    radius: Union[float, Distance] = None
    center: Union[dict, Vector3D] = None
    count: int = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.radius):
            self.MissingRequiredField("radius")
        if not isinstance(self.radius, Distance):
            self.radius = Distance(self.radius)

        if self._is_empty(self.center):
            self.MissingRequiredField("center")
        if not isinstance(self.center, Vector3D):
            self.center = Vector3D(**as_dict(self.center))

        if self._is_empty(self.count):
            self.MissingRequiredField("count")
        if not isinstance(self.count, int):
            self.count = int(self.count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsteroidField(Region):
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
    count: int = None
    asteroid_type: Union[str, AsteroidTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.asteroid_type):
            self.MissingRequiredField("asteroid_type")
        if not isinstance(self.asteroid_type, AsteroidTypeId):
            self.asteroid_type = AsteroidTypeId(self.asteroid_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RaiderPack(Region):
    """
    A region that raiders of one type hold.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["RaiderPack"]
    class_class_curie: ClassVar[str] = "starflake:RaiderPack"
    class_name: ClassVar[str] = "RaiderPack"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.RaiderPack

    radius: Union[float, Distance] = None
    center: Union[dict, Vector3D] = None
    count: int = None
    raider_type: Union[str, RaiderTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.raider_type):
            self.MissingRequiredField("raider_type")
        if not isinstance(self.raider_type, RaiderTypeId):
            self.raider_type = RaiderTypeId(self.raider_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GalaxyState(YAMLRoot):
    """
    What is where in a galaxy at one moment: its pilots, their ships, and the state of the star systems visited so far.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["GalaxyState"]
    class_class_curie: ClassVar[str] = "starflake:GalaxyState"
    class_name: ClassVar[str] = "GalaxyState"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.GalaxyState

    id: Union[str, GalaxyStateId] = None
    galaxy: Union[str, GalaxyId] = None
    pilots: Union[dict[Union[str, PilotId], Union[dict, "Pilot"]], list[Union[dict, "Pilot"]]] = empty_dict()
    pilot_ships: Optional[Union[dict[Union[str, PilotShipId], Union[dict, "PilotShip"]], list[Union[dict, "PilotShip"]]]] = empty_dict()
    system_states: Optional[Union[Union[dict, "StarSystemState"], list[Union[dict, "StarSystemState"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GalaxyStateId):
            self.id = GalaxyStateId(self.id)

        if self._is_empty(self.galaxy):
            self.MissingRequiredField("galaxy")
        if not isinstance(self.galaxy, GalaxyId):
            self.galaxy = GalaxyId(self.galaxy)

        if self._is_empty(self.pilots):
            self.MissingRequiredField("pilots")
        self._normalize_inlined_as_list(slot_name="pilots", slot_type=Pilot, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pilot_ships", slot_type=PilotShip, key_name="id", keyed=True)

        if not isinstance(self.system_states, list):
            self.system_states = [self.system_states] if self.system_states is not None else []
        self.system_states = [v if isinstance(v, StarSystemState) else StarSystemState(**as_dict(v)) for v in self.system_states]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pilot(NamedThing):
    """
    A person who flies a ship. Other pilots know them by name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["Pilot"]
    class_class_curie: ClassVar[str] = "starflake:Pilot"
    class_name: ClassVar[str] = "Pilot"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.Pilot

    id: Union[str, PilotId] = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PilotId):
            self.id = PilotId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StarSystemState(YAMLRoot):
    """
    The state of one star system: what remains of its asteroids and raiders, and the fuel pods floating there.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["StarSystemState"]
    class_class_curie: ClassVar[str] = "starflake:StarSystemState"
    class_name: ClassVar[str] = "StarSystemState"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.StarSystemState

    star_system: Union[str, StarSystemId] = None
    asteroids: Optional[Union[dict[Union[str, AsteroidId], Union[dict, "Asteroid"]], list[Union[dict, "Asteroid"]]]] = empty_dict()
    raider_ships: Optional[Union[dict[Union[str, RaiderShipId], Union[dict, "RaiderShip"]], list[Union[dict, "RaiderShip"]]]] = empty_dict()
    fuel_pods: Optional[Union[dict[Union[str, FuelPodId], Union[dict, "FuelPod"]], list[Union[dict, "FuelPod"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.star_system):
            self.MissingRequiredField("star_system")
        if not isinstance(self.star_system, StarSystemId):
            self.star_system = StarSystemId(self.star_system)

        self._normalize_inlined_as_list(slot_name="asteroids", slot_type=Asteroid, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="raider_ships", slot_type=RaiderShip, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fuel_pods", slot_type=FuelPod, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpaceEntity(YAMLRoot):
    """
    Anything with a physical presence in a star system.
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
class PilotShip(Ship):
    """
    A ship flown by a pilot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["PilotShip"]
    class_class_curie: ClassVar[str] = "starflake:PilotShip"
    class_name: ClassVar[str] = "PilotShip"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.PilotShip

    id: Union[str, PilotShipId] = None
    position: Union[dict, Vector3D] = None
    hull: Union[float, Amount] = None
    ship_class: Union[str, ShipClassId] = None
    pilot: Union[str, PilotId] = None
    current_system: Union[str, StarSystemId] = None
    fuel: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PilotShipId):
            self.id = PilotShipId(self.id)

        if self._is_empty(self.ship_class):
            self.MissingRequiredField("ship_class")
        if not isinstance(self.ship_class, ShipClassId):
            self.ship_class = ShipClassId(self.ship_class)

        if self._is_empty(self.pilot):
            self.MissingRequiredField("pilot")
        if not isinstance(self.pilot, PilotId):
            self.pilot = PilotId(self.pilot)

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
class RaiderShip(Ship):
    """
    A hostile ship. Its hull design comes from its raider type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["RaiderShip"]
    class_class_curie: ClassVar[str] = "starflake:RaiderShip"
    class_name: ClassVar[str] = "RaiderShip"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.RaiderShip

    id: Union[str, RaiderShipId] = None
    position: Union[dict, Vector3D] = None
    hull: Union[float, Amount] = None
    raider_type: Union[str, RaiderTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RaiderShipId):
            self.id = RaiderShipId(self.id)

        if self._is_empty(self.raider_type):
            self.MissingRequiredField("raider_type")
        if not isinstance(self.raider_type, RaiderTypeId):
            self.raider_type = RaiderTypeId(self.raider_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Asteroid(SpaceEntity):
    """
    An asteroid that breaks into a fuel pod when shot enough.
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
class FuelPod(SpaceEntity):
    """
    Fuel floating in space, scooped up by a pilot ship that flies into it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STARFLAKE["FuelPod"]
    class_class_curie: ClassVar[str] = "starflake:FuelPod"
    class_name: ClassVar[str] = "FuelPod"
    class_model_uri: ClassVar[URIRef] = STARFLAKE.FuelPod

    id: Union[str, FuelPodId] = None
    position: Union[dict, Vector3D] = None
    fuel_amount: Union[float, Amount] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FuelPodId):
            self.id = FuelPodId(self.id)

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

slots.fuel_yield = Slot(uri=STARFLAKE.fuel_yield, name="fuel_yield", curie=STARFLAKE.curie('fuel_yield'),
                   model_uri=STARFLAKE.fuel_yield, domain=None, range=Union[float, Amount])

slots.ship_class = Slot(uri=STARFLAKE.ship_class, name="ship_class", curie=STARFLAKE.curie('ship_class'),
                   model_uri=STARFLAKE.ship_class, domain=None, range=Union[str, ShipClassId])

slots.asteroid_type = Slot(uri=STARFLAKE.asteroid_type, name="asteroid_type", curie=STARFLAKE.curie('asteroid_type'),
                   model_uri=STARFLAKE.asteroid_type, domain=None, range=Union[str, AsteroidTypeId])

slots.raider_type = Slot(uri=STARFLAKE.raider_type, name="raider_type", curie=STARFLAKE.curie('raider_type'),
                   model_uri=STARFLAKE.raider_type, domain=None, range=Union[str, RaiderTypeId])

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

slots.shipClass__scoop_radius = Slot(uri=STARFLAKE.scoop_radius, name="shipClass__scoop_radius", curie=STARFLAKE.curie('scoop_radius'),
                   model_uri=STARFLAKE.shipClass__scoop_radius, domain=None, range=Union[float, Distance])

slots.shipClass__tractor_range = Slot(uri=STARFLAKE.tractor_range, name="shipClass__tractor_range", curie=STARFLAKE.curie('tractor_range'),
                   model_uri=STARFLAKE.shipClass__tractor_range, domain=None, range=Union[float, Distance])

slots.shipClass__tractor_speed = Slot(uri=STARFLAKE.tractor_speed, name="shipClass__tractor_speed", curie=STARFLAKE.curie('tractor_speed'),
                   model_uri=STARFLAKE.shipClass__tractor_speed, domain=None, range=Union[float, Speed])

slots.shipClass__weapons = Slot(uri=STARFLAKE.weapons, name="shipClass__weapons", curie=STARFLAKE.curie('weapons'),
                   model_uri=STARFLAKE.shipClass__weapons, domain=None, range=Optional[Union[Union[str, WeaponTypeId], list[Union[str, WeaponTypeId]]]])

slots.raiderType__detection_range = Slot(uri=STARFLAKE.detection_range, name="raiderType__detection_range", curie=STARFLAKE.curie('detection_range'),
                   model_uri=STARFLAKE.raiderType__detection_range, domain=None, range=Union[float, Distance])

slots.raiderType__keep_distance = Slot(uri=STARFLAKE.keep_distance, name="raiderType__keep_distance", curie=STARFLAKE.curie('keep_distance'),
                   model_uri=STARFLAKE.raiderType__keep_distance, domain=None, range=Union[float, Distance])

slots.asteroidType__max_integrity = Slot(uri=STARFLAKE.max_integrity, name="asteroidType__max_integrity", curie=STARFLAKE.curie('max_integrity'),
                   model_uri=STARFLAKE.asteroidType__max_integrity, domain=None, range=Union[float, Amount])

slots.galaxy__weapon_types = Slot(uri=STARFLAKE.weapon_types, name="galaxy__weapon_types", curie=STARFLAKE.curie('weapon_types'),
                   model_uri=STARFLAKE.galaxy__weapon_types, domain=None, range=Optional[Union[dict[Union[str, WeaponTypeId], Union[dict, WeaponType]], list[Union[dict, WeaponType]]]])

slots.galaxy__ship_classes = Slot(uri=STARFLAKE.ship_classes, name="galaxy__ship_classes", curie=STARFLAKE.curie('ship_classes'),
                   model_uri=STARFLAKE.galaxy__ship_classes, domain=None, range=Optional[Union[dict[Union[str, ShipClassId], Union[dict, ShipClass]], list[Union[dict, ShipClass]]]])

slots.galaxy__raider_types = Slot(uri=STARFLAKE.raider_types, name="galaxy__raider_types", curie=STARFLAKE.curie('raider_types'),
                   model_uri=STARFLAKE.galaxy__raider_types, domain=None, range=Optional[Union[dict[Union[str, RaiderTypeId], Union[dict, RaiderType]], list[Union[dict, RaiderType]]]])

slots.galaxy__asteroid_types = Slot(uri=STARFLAKE.asteroid_types, name="galaxy__asteroid_types", curie=STARFLAKE.curie('asteroid_types'),
                   model_uri=STARFLAKE.galaxy__asteroid_types, domain=None, range=Optional[Union[dict[Union[str, AsteroidTypeId], Union[dict, AsteroidType]], list[Union[dict, AsteroidType]]]])

slots.galaxy__star_systems = Slot(uri=STARFLAKE.star_systems, name="galaxy__star_systems", curie=STARFLAKE.curie('star_systems'),
                   model_uri=STARFLAKE.galaxy__star_systems, domain=None, range=Union[dict[Union[str, StarSystemId], Union[dict, StarSystem]], list[Union[dict, StarSystem]]])

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

slots.starSystem__raider_packs = Slot(uri=STARFLAKE.raider_packs, name="starSystem__raider_packs", curie=STARFLAKE.curie('raider_packs'),
                   model_uri=STARFLAKE.starSystem__raider_packs, domain=None, range=Optional[Union[Union[dict, RaiderPack], list[Union[dict, RaiderPack]]]])

slots.region__center = Slot(uri=STARFLAKE.center, name="region__center", curie=STARFLAKE.curie('center'),
                   model_uri=STARFLAKE.region__center, domain=None, range=Union[dict, Vector3D])

slots.region__count = Slot(uri=STARFLAKE.count, name="region__count", curie=STARFLAKE.curie('count'),
                   model_uri=STARFLAKE.region__count, domain=None, range=int)

slots.galaxyState__galaxy = Slot(uri=STARFLAKE.galaxy, name="galaxyState__galaxy", curie=STARFLAKE.curie('galaxy'),
                   model_uri=STARFLAKE.galaxyState__galaxy, domain=None, range=Union[str, GalaxyId])

slots.galaxyState__pilots = Slot(uri=STARFLAKE.pilots, name="galaxyState__pilots", curie=STARFLAKE.curie('pilots'),
                   model_uri=STARFLAKE.galaxyState__pilots, domain=None, range=Union[dict[Union[str, PilotId], Union[dict, Pilot]], list[Union[dict, Pilot]]])

slots.galaxyState__pilot_ships = Slot(uri=STARFLAKE.pilot_ships, name="galaxyState__pilot_ships", curie=STARFLAKE.curie('pilot_ships'),
                   model_uri=STARFLAKE.galaxyState__pilot_ships, domain=None, range=Optional[Union[dict[Union[str, PilotShipId], Union[dict, PilotShip]], list[Union[dict, PilotShip]]]])

slots.galaxyState__system_states = Slot(uri=STARFLAKE.system_states, name="galaxyState__system_states", curie=STARFLAKE.curie('system_states'),
                   model_uri=STARFLAKE.galaxyState__system_states, domain=None, range=Optional[Union[Union[dict, StarSystemState], list[Union[dict, StarSystemState]]]])

slots.starSystemState__star_system = Slot(uri=STARFLAKE.star_system, name="starSystemState__star_system", curie=STARFLAKE.curie('star_system'),
                   model_uri=STARFLAKE.starSystemState__star_system, domain=None, range=Union[str, StarSystemId])

slots.starSystemState__asteroids = Slot(uri=STARFLAKE.asteroids, name="starSystemState__asteroids", curie=STARFLAKE.curie('asteroids'),
                   model_uri=STARFLAKE.starSystemState__asteroids, domain=None, range=Optional[Union[dict[Union[str, AsteroidId], Union[dict, Asteroid]], list[Union[dict, Asteroid]]]])

slots.starSystemState__raider_ships = Slot(uri=STARFLAKE.raider_ships, name="starSystemState__raider_ships", curie=STARFLAKE.curie('raider_ships'),
                   model_uri=STARFLAKE.starSystemState__raider_ships, domain=None, range=Optional[Union[dict[Union[str, RaiderShipId], Union[dict, RaiderShip]], list[Union[dict, RaiderShip]]]])

slots.starSystemState__fuel_pods = Slot(uri=STARFLAKE.fuel_pods, name="starSystemState__fuel_pods", curie=STARFLAKE.curie('fuel_pods'),
                   model_uri=STARFLAKE.starSystemState__fuel_pods, domain=None, range=Optional[Union[dict[Union[str, FuelPodId], Union[dict, FuelPod]], list[Union[dict, FuelPod]]]])

slots.spaceEntity__position = Slot(uri=STARFLAKE.position, name="spaceEntity__position", curie=STARFLAKE.curie('position'),
                   model_uri=STARFLAKE.spaceEntity__position, domain=None, range=Union[dict, Vector3D])

slots.spaceEntity__velocity = Slot(uri=STARFLAKE.velocity, name="spaceEntity__velocity", curie=STARFLAKE.curie('velocity'),
                   model_uri=STARFLAKE.spaceEntity__velocity, domain=None, range=Optional[Union[dict, Vector3D]])

slots.spaceEntity__orientation = Slot(uri=STARFLAKE.orientation, name="spaceEntity__orientation", curie=STARFLAKE.curie('orientation'),
                   model_uri=STARFLAKE.spaceEntity__orientation, domain=None, range=Optional[Union[dict, Attitude]])

slots.ship__hull = Slot(uri=STARFLAKE.hull, name="ship__hull", curie=STARFLAKE.curie('hull'),
                   model_uri=STARFLAKE.ship__hull, domain=None, range=Union[float, Amount])

slots.pilotShip__pilot = Slot(uri=STARFLAKE.pilot, name="pilotShip__pilot", curie=STARFLAKE.curie('pilot'),
                   model_uri=STARFLAKE.pilotShip__pilot, domain=None, range=Union[str, PilotId])

slots.pilotShip__current_system = Slot(uri=STARFLAKE.current_system, name="pilotShip__current_system", curie=STARFLAKE.curie('current_system'),
                   model_uri=STARFLAKE.pilotShip__current_system, domain=None, range=Union[str, StarSystemId])

slots.pilotShip__fuel = Slot(uri=STARFLAKE.fuel, name="pilotShip__fuel", curie=STARFLAKE.curie('fuel'),
                   model_uri=STARFLAKE.pilotShip__fuel, domain=None, range=Union[float, Amount])

slots.asteroid__integrity = Slot(uri=STARFLAKE.integrity, name="asteroid__integrity", curie=STARFLAKE.curie('integrity'),
                   model_uri=STARFLAKE.asteroid__integrity, domain=None, range=Union[float, Amount])

slots.fuelPod__fuel_amount = Slot(uri=STARFLAKE.fuel_amount, name="fuelPod__fuel_amount", curie=STARFLAKE.curie('fuel_amount'),
                   model_uri=STARFLAKE.fuelPod__fuel_amount, domain=None, range=Union[float, Amount])

slots.AsteroidType_radius = Slot(uri=STARFLAKE.radius, name="AsteroidType_radius", curie=STARFLAKE.curie('radius'),
                   model_uri=STARFLAKE.AsteroidType_radius, domain=AsteroidType, range=Union[float, Distance])

slots.Region_radius = Slot(uri=STARFLAKE.radius, name="Region_radius", curie=STARFLAKE.curie('radius'),
                   model_uri=STARFLAKE.Region_radius, domain=Region, range=Union[float, Distance])
