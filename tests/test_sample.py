# content of test_sample.py
def test_answer(cmdopt):
    """
    I don't care
    """
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0  # to see what was printed
