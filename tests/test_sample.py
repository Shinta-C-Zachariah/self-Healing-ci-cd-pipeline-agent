def test_addition():
    assert 1 + 1 == 2

def test_flaky():
    import random
    assert random.choice([True, False])  # Simulates a flaky test
