from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_valid():
 assert c.post('/work',json={'request_id':'req1','actor_id':'user1','action':'prepare'}).status_code==200
def test_invalid():
 assert c.post('/work',json={'request_id':'req1','actor_id':'user1','action':'delete'}).status_code==422
