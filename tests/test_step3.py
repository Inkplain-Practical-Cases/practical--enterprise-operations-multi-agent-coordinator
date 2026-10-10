from app.execution import Execution
import pytest
def test_validation():
 e=Execution('req1');e.record('prepare',{'ok':True,'payload':{'id':'1'}})
 assert 'prepare' in e.completed
 with pytest.raises(ValueError):e.record('validate',{'ok':False,'payload':{}})
