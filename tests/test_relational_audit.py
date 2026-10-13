"""Validate coordinator HTTP request/outcome foreign-key integrity."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_coordinator_request_relations(tmp_path):
    db=str(tmp_path/"operations.sqlite3")
    rid=provider_record_request_audit("POST","/work",200,3.4,db)
    with sqlite3.connect(db) as connection:
        assert connection.execute("SELECT COUNT(*) FROM operations_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert connection.execute("SELECT COUNT(*) FROM operations_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert connection.execute("PRAGMA foreign_key_check").fetchall()==[]
