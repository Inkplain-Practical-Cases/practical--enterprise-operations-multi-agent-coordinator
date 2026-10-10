# Enterprise Operations Multi-Agent Coordinator

Junior FDE practical case for a deterministic, bounded, multi-role business coordination workflow. The final code has typed FastAPI ingress, task graph, execution state and validated results, explicit manager approval, timeout recovery and a local simulation with audit records.

**Learning code only:** The example does not implement enterprise SSO, persistent database state, a deployed MCP server or production internal APIs. It is intentionally safe/offline.

## Study
- STEP-1: [Define multi-role workflow contracts](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-01-define-multi-role-workflow-contracts)
- STEP-2: [Delegate tasks through controlled graph](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-02-delegate-tasks-through-controlled-graph)
- STEP-3: [Track execution state and validate results](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-03-track-execution-state-and-validate-resul)
- STEP-4: [Enforce human approval and authorization](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-04-enforce-human-approval-and-authorization)
- STEP-5: [Recover failures and bound completion](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-05-recover-failures-and-bound-completion)
- STEP-6: [Simulate audited enterprise operations](https://github.com/Inkplain-Practical-Cases/practical--enterprise-operations-multi-agent-coordinator/tree/step-06-simulate-audited-enterprise-operations)

Each branch contains STEP-N.crd and STEP-N.md. Run `python -m pip install -r requirements.txt`, then `python -m pytest -q` and `uvicorn app.main:app --reload`. Main contains FINAL.crd and the six-tab Simulator artifact after Stage 3.
