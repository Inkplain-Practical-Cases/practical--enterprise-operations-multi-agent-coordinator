from app.recovery import run_bounded
def test_finite_failure():
 assert run_bounded(lambda: (_ for _ in ()).throw(TimeoutError()),2)['attempts']==2
