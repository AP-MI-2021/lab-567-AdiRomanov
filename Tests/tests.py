from Domain.date_proprietar import creeaza_cheltuiala, get_nr_ap, get_suma, get_data, get_tip, get_id
from Logic.general_logic import check_data, add_cheltuiala_to_list, srv_add_to_list, valideaza_cheltuiala, \
    get_cheltuiala_by_id, sterge_cheltuiala


def test_creeaza_cheltuiala():
    id = "1"
    nr_ap = 54
    suma = 473.30
    data = "10.09.2021"
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    assert (get_id(cheltuiala) == "1")
    assert (get_nr_ap(cheltuiala) == 54)
    assert (abs(get_suma(cheltuiala) - suma) < 0.00001)
    assert (get_data(cheltuiala) == "10.09.2021")
    assert (get_tip(cheltuiala) == "intretinere")


def test_valideaza_cheltuiala():
    cheltuiala = creeaza_cheltuiala("1", 54, 400, "10.10.2021", "intretinere")
    valideaza_cheltuiala(cheltuiala)
    assert True
    invalid_chelt = creeaza_cheltuiala("1", -54, 400, "10.10.2021", "intretinere")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Numar apartament invalid!\n")

    invalid_chelt = creeaza_cheltuiala("1", 54, 30, "20.40.1990", "intretinere")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Data invalida!\n")

    invalid_chelt = creeaza_cheltuiala("1", 54, 30, "10.10.2021", "gaz")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Tip invalid!\n")

    invalid_chelt = creeaza_cheltuiala("1", 54, -30, "10.10.2021", "canal")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Suma invalida!\n")


def test_check_data():
    assert check_data("10.10.2021") is True
    assert check_data("10.9.2022") is True
    assert check_data("33.10.2021") is False
    assert check_data("10.60.2021") is False
    assert check_data("10.10.2019") is True


def test_add_cheltuiala_to_list():
    """
    +test pentru functia get_cheltuiala_by_id( , ):
    """
    list = []
    cheltuiala = creeaza_cheltuiala("1", 54, 400, "10.10.2021", "intretinere")
    assert len(list) == 0
    add_cheltuiala_to_list(list, cheltuiala)
    assert len(list) == 1
    assert get_id(get_cheltuiala_by_id("1", list)) == get_id(cheltuiala)
    assert get_nr_ap(get_cheltuiala_by_id("1", list)) == get_nr_ap(cheltuiala)
    assert abs(get_suma(get_cheltuiala_by_id("1", list)) - get_suma(cheltuiala)) < 0.00001
    assert get_data(get_cheltuiala_by_id("1", list)) == get_data(cheltuiala)
    assert get_tip(get_cheltuiala_by_id("1", list)) == get_tip(cheltuiala)
    alta_cheltuiala = creeaza_cheltuiala("1", 54, 300, "10.10.2021", "intretinere")
    try:
        add_cheltuiala_to_list(list, alta_cheltuiala)
        assert False
    except Exception as ex:
        assert str(ex) == "Cheltuiala existenta!\n"


def test_srv_add_to_list():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 400, "10.10.2021", "intretinere")
    try:
        srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
        assert False
    except Exception as ex:
        assert str(ex) == "Cheltuiala existenta!\n"
    try:
        srv_add_to_list(list, "1", -54, -300, "44.10.2021", "retinere")
        assert False
    except Exception as ex:
        assert str(ex) == "Numar apartament invalid!\nSuma invalida!\nData invalida!\nTip invalid!\n"


def test_sterge_cheltuiala():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "intretinere")
    list = sterge_cheltuiala("1", list)

    assert (len(list) == 1)
    assert get_cheltuiala_by_id("1", list) is None
    assert get_cheltuiala_by_id("2", list) is not None

    list = sterge_cheltuiala("3", list)

    assert (len(list) == 1)
    assert get_cheltuiala_by_id("2", list) is not None


def run_teste():
    test_creeaza_cheltuiala()
    test_valideaza_cheltuiala()
    test_check_data()
    test_add_cheltuiala_to_list()
    test_srv_add_to_list()
    test_sterge_cheltuiala()
