import pytest


@pytest.mark.order(2)
def test_method_b(one_time_setup, setup):
    print("This is method B")


@pytest.mark.order(1)
def test_method_c(one_time_setup, setup):
    print("This is method C")


@pytest.mark.order(6)
def test_method_d(one_time_setup, setup):
    print("This is method D")


@pytest.mark.order("first")
def test_method_e(one_time_setup, setup):
    print("This is method E")


@pytest.mark.order(4)
def test_method_f(one_time_setup, setup):
    print("This is method F")


@pytest.mark.order(5)
def test_method_a(one_time_setup, setup):
    print("This is method A")
