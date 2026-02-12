def test_addition():
    assert 1 + 1 == 2

def test_flaky():
    import random
    assert random.choice([True, False])  # Simulates a flaky test
    
def test_fail_example():
    assert 1 == 0  # This will always fail

    

