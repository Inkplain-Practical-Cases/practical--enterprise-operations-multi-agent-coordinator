from dataclasses import dataclass
@dataclass(frozen=True)
class Approval:
 request_id:str
 reviewer:str
 approved:bool
 def require(self,request_id:str):
  if self.request_id!=request_id or not self.reviewer or not self.approved:raise PermissionError('Approval required')
