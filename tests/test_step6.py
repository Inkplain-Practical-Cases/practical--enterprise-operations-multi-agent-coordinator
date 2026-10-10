from app.simulation import simulate
from app.approval import Approval
import pytest
def test_complete():
 result=simulate('req1',Approval('req1','manager',True));assert result['status']=='completed';assert len(result['audit'])==3
def test_denied():
 with pytest.raises(PermissionError):simulate('req2',Approval('req2','',False))
