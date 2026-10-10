"""Bounded deterministic task graph."""
def plan(action:str):
 if action not in {'prepare','review','approve'}:raise ValueError('Unsupported action')
 return [{'id':'prepare','role':'analyst','requires':[]},{'id':'validate','role':'auditor','requires':['prepare']},{'id':'approve','role':'manager','requires':['validate']}]
def ready(tasks,completed):
 return [t['id'] for t in tasks if t['id'] not in completed and set(t['requires'])<=completed]
