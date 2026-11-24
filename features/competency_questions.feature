Feature: Facts about space
  Background:
    Given a stellar system

  Scenario: How can stellar heating affect a solid object?
    When a solid object approaches a star
    Then stellar heating will heat the solid object

  Scenario: How can temperature affect a material?
    Given a pure solid at a pressure where its liquid phase is stable
    When it is heated to its melting point
    Then it begins to melt

  # Solar luminosity: https://doi.org/10.3847/0004-6256/152/2/41
  # Iron: https://periodic-table.rsc.org/element/26/iron
  # Water ice: https://iapws.org/relguide/MeltSub.html
  # These are reference temperatures; exposed ice in a vacuum can sublime rather than melt.
  Scenario Outline: How close to Sol does <material> reach its reference melting point?
    Given Sol's nominal luminosity is 3.828e26 W
    And the melting point of <material> at one atmosphere is <temperature_K> K
    And the object is modelled as a uniformly heated blackbody sphere
    When I ask where its radiative equilibrium temperature equals that melting point
    Then the distance from Sol's centre is approximately <million_km> million km

    Examples:
      | material  | temperature_K | million_km |
      | pure iron | 1811          | 3.53       |
      | water ice | 273.15        | 155        |

  Scenario: How can temperature affect a solid object?
    When a solid object has its composing material(s) melting, it can get destroyed
