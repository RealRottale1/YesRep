import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_valid_ticket():
    assert validate_ticket("TK123456") is True


def test_invalid_ticket_extra_legth():
    assert validate_ticket("TK1234567") is False


def test_invalid_ticket_noTK():
    with pytest.raises(TypeError):
        assert validate_ticket(43)


def test_get_ticket_tier_General():
    assert get_ticket_tier("TK323456") == "General"


def test_get_ticket_tier_VIP():
    assert get_ticket_tier("TK623456") == "VIP"


def test_get_ticket_tier_Platinum():
    assert get_ticket_tier("TK923456") == "Platinum"


def test_get_ticket_tier_Invalid():
    with pytest.raises(ValueError):
         get_ticket_tier("TKH23456")

def test_calculate_total_empty():
    with pytest.raises(ValueError):
        calculate_total([], 0.5)

def test_calculate_total_out_of_range():
    with pytest.raises(ValueError):
        calculate_total([20, 30], 99999)

def test_calculate_total_non_list_prices():
    with pytest.raises(TypeError):
        calculate_total("Hello World", 0.5)