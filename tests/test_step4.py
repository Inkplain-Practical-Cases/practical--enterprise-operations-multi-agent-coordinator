from app.approval import Approval
import pytest
def test_approval():
 Approval('req1','manager',True).require('req1')
 with pytest.raises(PermissionError):Approval('req1','',True).require('req1')
