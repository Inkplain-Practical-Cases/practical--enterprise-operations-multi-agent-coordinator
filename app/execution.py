from dataclasses import dataclass,field
@dataclass
class Execution:
 request_id:str
 completed:set[str]=field(default_factory=set)
 results:dict=field(default_factory=dict)
 def record(self,task:str,result:dict):
  if result.get('ok') is not True or not isinstance(result.get('payload'),dict):raise ValueError('Invalid tool result')
  if task in self.completed:raise ValueError('Duplicate completion')
  self.results[task]=result['payload'];self.completed.add(task)
