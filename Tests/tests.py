from Domain.date_proprietar import creeaza_cheltuiala, get_nr_ap, get_suma, get_data, get_tip
from Logic.general_logic import check_data, add_cheltuiala_to_list, srv_add_to_list, valideaza_cheltuiala


def test_creeaza_cheltuiala():
    nr_ap = 54
    suma = 473.30
    data = "10.09.2021"
    tip = "intretinere"
    cheltuiala = creeaza_cheltuiala(nr_ap, suma, data, tip)
    assert (get_nr_ap(cheltuiala) == 54)
    assert (abs(get_suma(cheltuiala) - suma) < 0.00001)
    assert (get_data(cheltuiala) == "10.09.2021")
    assert (get_tip(cheltuiala) == "intretinere")


def test_valideaza_cheltuiala():
    cheltuiala = creeaza_cheltuiala(54, 400, "10.10.2021", "intretinere")
    valideaza_cheltuiala(cheltuiala)
    assert True
    invalid_chelt = creeaza_cheltuiala(-54, 400, "10.10.2021", "intretinere")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Numar apartament invalid!\n")

    invalid_chelt = creeaza_cheltuiala(54, 30, "20.40.1990", "intretinere")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Data invalida!\n")

    invalid_chelt = creeaza_cheltuiala(54, 30, "10.10.2021", "gaz")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Tip invalid!\n")

    invalid_chelt = creeaza_cheltuiala(54, -30, "10.10.2021", "canal")
    try:
        valideaza_cheltuiala(invalid_chelt)
        assert False
    except Exception as ex:
        assert (str(ex) == "Suma invalida!\n")


def test_check_data():
    assert check_data("10.10.2021") is True
    assert check_data("10.9.2022") is False
    assert check_data("33.10.2021") is False
    assert check_data("10.60.2021") is False
    assert check_data("10.10.2019") is False


def test_add_cheltuiala_to_list():
    l = []
    cheltuiala = creeaza_cheltuiala(54, 400, "10.10.2021", "intretinere")
    assert len(l) == 0
    add_cheltuiala_to_list(l, cheltuiala)
    assert len(l) == 1
    assert get_nr_ap(l[0]) == get_nr_ap(cheltuiala)
    assert abs(get_suma(l[0]) - get_suma(cheltuiala)) < 0.00001
    assert get_data(l[0]) == get_data(cheltuiala)
    assert get_tip(l[0]) == get_tip(cheltuiala)
    alta_cheltuiala = creeaza_cheltuiala(54, 300, "10.10.2021", "intretinere")
    try:
        add_cheltuiala_to_list(l, alta_cheltuiala)
        assert False
    except Exception as ex:
        assert str(ex) == "Cheltuiala existenta!\n"


def test_srv_add_to_list():
    l = []
    assert (len(l) == 0)
    srv_add_to_list(l, 54, 400, "10.10.2021", "intretinere")
    try:
        srv_add_to_list(l, 54, 300, "10.10.2021", "intretinere")
        assert False
    except Exception as ex:
        assert str(ex) == "Cheltuiala existenta!\n"
    try:
        srv_add_to_list(l, -54, -300, "44.10.2021", "retinere")
        assert False
    except Exception as ex:
        assert str(ex) == "Numar apartament invalid!\nSuma invalida!\nData invalida!\nTip invalid!\n"


def run_teste():
    test_creeaza_cheltuiala()
    test_valideaza_cheltuiala()
    test_check_data()
    test_add_cheltuiala_to_list()
    test_srv_add_to_list()
