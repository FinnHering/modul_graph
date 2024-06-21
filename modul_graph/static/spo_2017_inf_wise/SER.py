from modul_graph.models.module import Module
from modul_graph.models.study_exam_rules import StudyExamRules
from modul_graph.static.spo_2017_inf_wise._semesters import semesters
import modul_graph.static.spo_2017_inf_wise._modules as _modules



spo_2017_inf_wise = StudyExamRules()
spo_2017_inf_wise.name = "SPO 2017 Informatik (Start Wintersemester)"
spo_2017_inf_wise.save()

for s in semesters:
    spo_2017_inf_wise.specifies_semester.connect(s)

for v in _modules.__dict__.values():
    if isinstance(v, Module):
        v.belongs_to_SER.connect(spo_2017_inf_wise)