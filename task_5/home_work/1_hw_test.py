def test_hw_1():
    assert ('home', 'work') == ('home', 'work')


def test_hw_2():
    assert not 'QA' == 'QC'


def test_hw_3():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)
