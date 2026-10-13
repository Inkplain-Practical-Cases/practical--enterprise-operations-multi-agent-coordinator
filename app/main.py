from fastapi import FastAPI
from pydantic import BaseModel, Field
app=FastAPI(title='Enterprise Operations Coordinator')
class WorkRequest(BaseModel):
    request_id:str=Field(min_length=3)
    actor_id:str=Field(min_length=3)
    action:str=Field(pattern='^(prepare|review|approve)$')
@app.post('/work')
def accept_work(req:WorkRequest):
    return {'request_id':req.request_id,'state':'accepted','action':req.action}

# Persist coordinator HTTP operation outcomes independently of simulation state.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
