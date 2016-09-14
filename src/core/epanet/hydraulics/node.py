﻿from enum import Enum
from core.coordinate import Coordinate
from core.epanet.patterns import Pattern
from core.epanet.curves import Curve
from core.project_base import Section
from core.metadata import Metadata


class SourceType(Enum):
    """Water Quality Source Type"""
    CONCEN = 1
    MASS = 2
    FLOWPACED = 3
    SETPOINT = 4


class MixingModel(Enum):
    """Mixing Model"""
    MIXED = 1
    TWO_COMP = 2
    FIFO = 3
    LIFO = 4


class Node(Section, Coordinate):
    """A node in an EPANET model"""
    def __init__(self):
        Coordinate.__init__(self)
        Section.__init__(self)
        # self.name, inherited from Coordinate
        """Unique name or number identifying this node"""

        # self.x, self.y, inherited from Coordinate
        """Node location for mapping"""

#         self.description = ""
#         """Optional description of the Node"""

        self.tag = ""
        """Optional label used to categorize or classify the Node"""

        self.initial_quality = 0.0
        """concentration for chemicals, hours for water age, or percent for source tracing"""

#         self.source_quality = Source()
#         """defines characteristics of water quality source"""
#
#         self.report_flag = ""
#         """Indicates whether reporting is desired at this node"""


class Junction(Node):
    """Junction properties"""

    #    attribute, input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",                '', "Name",            '',   '',   '', "User-assigned name of junction"),
        ('x',                   '', "X-Coordinate",    '',   '',   '', "X coordinate of junction on study area map"),
        ('y',                   '', "Y-Coordinate",    '',   '',   '', "Y coordinate of junction on study area map"),
        ('',                    '', "Description",     '',   '',   '', "Optional comment or description"),
        ('tag',                 '', "Tag",             '',   '',   '', "Optional category or classification"),
        ('elevation',           '', "Elevation",       '',   '',   '', "Elevation of junction"),
        ('base_demand_flow',    '', 'Base Demand',       '',  '',   '', "Base demand flow, characteristic of all demands at this node"),
        ('demand_pattern_name', '', 'Demand Pattern',    '',  '',   '', "Demand pattern ID, optional"),
        ('demand_categories',   '', 'Demand Categories', '',  '',   '', "Number of demand categories, click to edit"),
        ('emitter_coefficient', '', 'Emitter Coeff.',    '',  '',   '', "Emitters are used to model flow through sprinkler heads or pipe leaks. Flow out of the emitter equals the product of the flow coefficient and the junction pressure raised to EMITTER EXPONENT, which defaults to 0.5 and can be set in OPTIONS section."),
        ('initial_quality',     '', 'Initial Quality',   '',  '',   '', "Water quality level at the junction at the start of the simulation period"),
        ('source_quality',      '', 'Source Quality',    '',  '',   '', "Quality of any water entering the network at this location, click to edit")))

    def __init__(self):
        Node.__init__(self)

        self.elevation = ''
        """elevation of junction"""

        self.base_demand_flow = ''
        """Base demand flow, characteristic of all demands at this node"""

        self.demand_pattern_name = ''
        """Demand pattern ID, optional"""

        # TODO: sync with EMITTERS section
        self.emitter_coefficient = ''
        """ Emitters are used to model flow through sprinkler heads or pipe leaks. Flow out of the emitter equals
            the product of the flow coefficient and the junction pressure raised to EMITTER EXPONENT, which
            defaults to 0.5 and can be set in OPTIONS section."""


class Reservoir(Node):
    """Reservoir properties"""

    #    attribute, input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",              '', "Name",            '',    '',   '', "User-assigned name of reservior"),
        ('x',                 '', "X-Coordinate",    '',    '',   '', "X coordinate of reservior on study area map"),
        ('y',                 '', "Y-Coordinate",    '',    '',   '', "Y coordinate of reservior on study area map"),
        ('',                  '', "Description",     '',    '',   '', "Optional comment or description"),
        ('tag',               '', "Tag",             '',    '',   '', "Optional category or classification"),
        ('total_head',        '', "Total Head",      '0.0', '',   '', "Hydraulic head (elevation + pressure head) of water in the reservoir"),
        ('head_pattern_name', '', 'Head Pattern',    '',    '',   '', "Head pattern ID, can be used to make the reservoir head vary with time"),
        ('initial_quality',   '', 'Initial Quality', '',    '',   '', "Water quality level at the reservior at the start of the simulation period"),
        ('source_quality',    '', 'Source Quality',  '',    '',   '', "Quality of any water entering the network at this location, click to edit")))

    def __init__(self):
        Node.__init__(self)

        self.total_head = "0.0"
        """Head is the hydraulic head (elevation + pressure head) of water in the reservoir"""

        self.head_pattern_name = ''
        """head pattern can be used to make the reservoir head vary with time"""


class Tank(Node):
    """Tank properties"""

    #    attribute, input_name, label,         default, english, metric, hint
    metadata = Metadata((
        ("name",            '', "Name",            '',    '',   '', "User-assigned name of tank"),
        ('x',               '', "X-Coordinate",    '',    '',   '', "X coordinate of tank on study area map"),
        ('y',               '', "Y-Coordinate",    '',    '',   '', "Y coordinate of tank on study area map"),
        ('',                '', "Description",     '',    '',   '', "Optional comment or description"),
        ('tag',             '', "Tag",             '',    '',   '', "Optional category or classification"),
        ('elevation',       '', "Elevation",       '0.0', '',   '', "Elevation of tank"),
        ('initial_level',   '', "Initial Level",   '0.0', '',   '', "Height of the water surface above the bottom elevation of the tank at the start of the simulation."),
        ('minimum_level',   '', "Minimum Level",   '0.0', '',   '', "Minimum height in feet (meters) of the water surface above the bottom elevation that will be maintained."),
        ('maximum_level',   '', "Maximum Level",   '0.0', '',   '', "Maximum height in feet (meters) of the water surface above the bottom elevation that will be maintained."),
        ('diameter',        '', "Diameter",        '0.0', '',   '', "The diameter of the tank"),
        ('minimum_volume',  '', "Minimum Volume",  '0.0', '',   '', "The volume of water in the tank when it is at its minimum level"),
        ('volume_curve',    '', "Volume Curve",    '',    '',   '', "The ID label of a curve used to describe the relation between tank volume and water level"),
        ('mixing_model',    '', "Mixing Model",    '',    '',   '', "The type of water quality mixing that occurs within the tank"),
        ('mixing_fraction', '', "Mixing Fraction", '0.0', '',   '', "The fraction of the tank's total volume that comprises the inlet-outlet compartment of the two-compartment (2COMP) mixing model"),
        ('reaction_coeff',  '', "Reaction Coeff.", '',    '',   '', "Tank-specific reaction coefficient"),
        ('initial_quality', '', 'Initial Quality', '0.0', '',   '', "Water quality level in the tank at the start of the simulation period"),
        ('source_quality',  '', 'Source Quality',  '',    '',   '', "Quality of any water entering the network at this location, click to edit")))

    def __init__(self):
        Node.__init__(self)

        self.elevation = "0.0"
        """Bottom elevation, ft (m)"""

        self.initial_level = "0.0"
        """Initial water level, ft (m)"""

        self.minimum_level = "0.0"
        """Minimum water level, ft (m)"""

        self.maximum_level = "0.0"
        """Maximum water level, ft (m)"""

        self.diameter = "0.0"
        """Nominal diameter, ft (m)"""

        self.minimum_volume = "0.0"
        """Minimum volume, cubic ft (cubic meters)"""

        self.volume_curve = ''
        """If a volume curve is supplied the diameter value can be any non-zero number"""

        # refer to [REACTIONS] section for reaction coefficient


class Mixing(Section):
    """Mixing model and volume fraction of a Tank"""

    def __init__(self):
        Section.__init__(self)
        self.name = ''
        """node identifier/name"""

        self.mixing_model = MixingModel.MIXED
        """Mixing models include:
            Completely Mixed (MIXED)
            Two-Compartment Mixing (2COMP)
            Plug Flow (FIFO)
            Stacked Plug Flow (LIFO)"""

        self.mixing_fraction = "0.0"
        """fraction of the total tank volume devoted to the inlet/outlet compartment"""


class Source(Node):
    """Defines locations of water quality sources"""

    def __init__(self):
        Node.__init__(self)

        self.source_type = SourceType.CONCEN # TRATION
        """Source type (CONCEN, MASS, FLOWPACED, or SETPOINT)"""

        self.baseline_strength = '0.0'                  # real, stored as string
        """Baseline source strength"""

        self.pattern_name = ""                          # string
        """Time pattern ID (optional)"""


class Demand(Section):
    """Define multiple water demands at junction nodes"""

    def __init__(self):
        Section.__init__(self)

        self.junction_name = ''
        """Junction this demand applies to"""

        self.base_demand = "0.0"     # real, stored as string
        """Base demand (flow units)"""

        self.demand_pattern = ''     # string
        """Demand pattern ID (optional)"""

        self.category = ''           # string
        """Name of demand category preceded by a semicolon (optional)"""
