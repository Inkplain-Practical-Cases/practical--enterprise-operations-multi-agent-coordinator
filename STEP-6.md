# STEP 6: Audited operations simulation

Install requirements, run `python -m pytest -q` and examine the deterministic three-role audit. No real internal API writes or identity provider are connected.

## Database (Entity) Relations
SQLite records HTTP operations for the coordinator and linked outcomes, not in-memory simulation details. See STEP-6.erd and STEP-6-ERD.
