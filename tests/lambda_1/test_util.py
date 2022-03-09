from lambda_1.src import util

def test_get_db():
    assert util.get_db() is not None