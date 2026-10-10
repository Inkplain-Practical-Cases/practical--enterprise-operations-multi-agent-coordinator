# STEP 5: Finite retry

Run python -m pytest -q. Only TimeoutError is eligible for bounded repeat; irreversible writes require idempotency.
