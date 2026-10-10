from app.planner import plan,ready
def test_dependencies():
 tasks=plan('prepare');assert ready(tasks,set())==['prepare'];assert ready(tasks,{'prepare'})==['validate']
