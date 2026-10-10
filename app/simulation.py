"""Deterministic multi-role workflow; local fixture not production identity or distributed state."""
from app.planner import plan,ready
from app.execution import Execution
from app.approval import Approval
from app.recovery import run_bounded

def simulate(request_id:str,approval:Approval):
 tasks=plan('prepare');state=Execution(request_id);audit=[]
 while len(state.completed)<len(tasks):
  available=ready(tasks,state.completed)
  if not available:raise RuntimeError('Deadlock')
  task=available[0]
  if task=='approve':approval.require(request_id)
  answer=run_bounded(lambda:{'task':task,'request_id':request_id})
  if answer['status']!='completed':return {'status':'failed','audit':audit}
  state.record(task,{'ok':True,'payload':answer['result']})
  audit.append({'task':task,'status':'completed'})
 return {'status':'completed','audit':audit,'results':state.results}
