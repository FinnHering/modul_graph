from neomodel import StructuredNode, StringProperty, OneOrMore, RelationshipTo, ZeroOrMore, IntegerProperty, One, RelationshipFrom

from models.module import Module
from models.semester import Semester


class StudyExamRules(StructuredNode):
    name = StringProperty(required=True, unique=True)

    # connection to Module
    has_module = RelationshipFrom(Module, 'BELONGS_TO', cardinality=OneOrMore)

    # connection to Semester
    specifies_semester = RelationshipTo(Semester, 'SPECIFIES', cardinality=OneOrMore)