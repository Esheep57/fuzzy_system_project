# src/models.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Shape:
    type: str  # e.g., 'TrapezoidShape', 'TriangularShape', 'GaussianShape', etc.

@dataclass
class TrapezoidShape(Shape):
    param1: float
    param2: float
    param3: float
    param4: float

@dataclass
class TriangularShape(Shape):
    param1: float
    param2: float
    param3: float

@dataclass
class GaussianShape(Shape):
    mean: float
    sigma: float

@dataclass
class LeftGaussianShape(Shape):
    mean: float
    sigma: float

@dataclass
class RightGaussianShape(Shape):
    mean: float
    sigma: float

@dataclass
class FuzzyTerm:
    name: str
    complement: bool
    shape: Shape

@dataclass
class FuzzyVariable:
    name: str
    scale: str
    domain_left: float
    domain_right: float
    var_type: str  # 'input' or 'output'
    accumulation: str
    defuzzifier: str
    default_value: float
    terms: List[FuzzyTerm] = field(default_factory=list)

@dataclass
class Clause:
    variable: str
    term: str

@dataclass
class Consequent:
    variable: str
    term: str

@dataclass
class Rule:
    name: str
    connector: str
    weight: float
    antecedents: List[Clause]
    consequent: Consequent

@dataclass
class FuzzySystemModel:
    name: str
    network_address: str
    fuzzy_variables: List[FuzzyVariable] = field(default_factory=list)
    rules: List[Rule] = field(default_factory=list)

@dataclass
class TrainingSample:
    KUWA_score: float
    BCI_weighted: float
    JenPin_score: float
    Student_level: str  # 例如: 'Beginner', 'Basic', 'Intermediate', 'Advanced', 'Proficient'
