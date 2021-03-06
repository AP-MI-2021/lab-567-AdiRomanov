from Domain.date_proprietar import creeaza_cheltuiala, get_nr_ap, get_suma, get_data, get_tip, get_id
from Logic.general_logic import check_data, add_cheltuiala_to_list, srv_add_to_list, valideaza_cheltuiala, \
    get_cheltuiala_by_id, sterge_cheltuiala, modifica_cheltuiala, sterge_toate_chelt, aduna_valoare, cmm_cheltuiala, \
    ord_desc, sume_lunare


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
    list = []
    cheltuiala = creeaza_cheltuiala("1", 54, 400, "10.10.2021", "intretinere")
    assert len(list) == 0
    add_cheltuiala_to_list(list, cheltuiala)
    assert len(list) == 1
    assert get_id(list[0]) == get_id(cheltuiala)
    assert get_nr_ap(list[0]) == get_nr_ap(cheltuiala)
    assert abs(get_suma(list[0]) - get_suma(cheltuiala)) < 0.00001
    assert get_data(list[0]) == get_data(cheltuiala)
    assert get_tip(list[0]) == get_tip(cheltuiala)
    alta_cheltuiala = creeaza_cheltuiala("1", 54, 300, "10.10.2021", "intretinere")
    try:
        add_cheltuiala_to_list(list, alta_cheltuiala)
        assert False
    except Exception as ex:
        assert str(ex) == "Cheltuiala existenta!\n"


def test_get_cheltuiala_by_id():
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


def test_modifica_cheltuiala():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "intretinere")
    list = modifica_cheltuiala(list, "2", 58, 450, "10.11.2021", "canal")
    assert get_id(get_cheltuiala_by_id("2", list)) == "2"
    assert get_nr_ap(get_cheltuiala_by_id("2", list)) == 58
    assert get_suma(get_cheltuiala_by_id("2", list)) == 450
    assert get_data(get_cheltuiala_by_id("2", list)) == "10.11.2021"
    assert get_tip(get_cheltuiala_by_id("2", list)) == "canal"


def test_sterge_toate_chelt():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "3", 57, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "5", 58, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "4", 57, 400, "10.10.2021", "intretinere")
    list = sterge_toate_chelt(57, list)
    assert get_cheltuiala_by_id("2", list) is None
    assert get_cheltuiala_by_id("3", list) is None
    assert get_cheltuiala_by_id("4", list) is None


def test_aduna_valoare():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "intretinere")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "intretinere")
    srv_add_to_list(list, "5", 57, 350, "10.10.2021", "intretinere")

    list = aduna_valoare(list, "10.10.2021", 20)
    assert get_suma(get_cheltuiala_by_id("1", list)) == 320
    assert get_suma(get_cheltuiala_by_id("2", list)) == 420
    assert get_suma(get_cheltuiala_by_id("3", list)) == 400
    assert get_suma(get_cheltuiala_by_id("4", list)) == 400
    assert get_suma(get_cheltuiala_by_id("5", list)) == 370


def test_cmm_cheltuiala():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "intretinere")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "intretinere")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "intretinere")
    srv_add_to_list(list, "5", 57, 350, "10.10.2021", "intretinere")
    rez = cmm_cheltuiala(list)
    assert rez[0] == 400
    assert rez[1] == 0
    assert rez[2] == 0

    list = []

    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "canal")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "intretinere")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "alte cheltuieli")
    srv_add_to_list(list, "5", 57, 350, "10.10.2021", "intretinere")
    rez = cmm_cheltuiala(list)
    assert rez[0] == 400
    assert rez[1] == 400
    assert rez[2] == 400

    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "canal")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "canal")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "canal")
    srv_add_to_list(list, "5", 57, 350, "10.10.2021", "canal")
    rez = cmm_cheltuiala(list)
    assert rez[0] == 300
    assert rez[1] == 400
    assert rez[2] == 0


def test_ord_desc():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "canal")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "canal")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "canal")
    srv_add_to_list(list, "5", 57, 350, "10.10.2021", "canal")

    list = ord_desc(list)
    assert get_suma(list[0]) == 400
    assert get_suma(list[1]) == 400
    assert get_suma(list[2]) == 400
    assert get_suma(list[3]) == 350
    assert get_suma(list[4]) == 300

    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 100, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 200, "10.10.2021", "canal")
    srv_add_to_list(list, "3", 57, 300, "10.12.2021", "canal")
    srv_add_to_list(list, "4", 58, 400, "10.11.2021", "canal")
    srv_add_to_list(list, "5", 57, 500, "10.10.2021", "canal")

    list = ord_desc(list)
    assert get_suma(list[0]) == 500
    assert get_suma(list[1]) == 400
    assert get_suma(list[2]) == 300
    assert get_suma(list[3]) == 200
    assert get_suma(list[4]) == 100


def test_sume_lunare():
    list = []
    assert (len(list) == 0)
    srv_add_to_list(list, "1", 54, 300, "10.10.2021", "intretinere")
    srv_add_to_list(list, "2", 57, 400, "10.10.2021", "canal")
    srv_add_to_list(list, "3", 57, 400, "10.12.2021", "canal")
    assert sume_lunare(list) == {54: 300, 57: 800}


def test_undoredo():
    redo_list = []
    lista = []
    undo_list = []

    cheltuiala = creeaza_cheltuiala("1", 54, 300, "10.10.2021", "intretinere")
    valideaza_cheltuiala(cheltuiala)

    rezultat = lista[:]
    undo_list.append(rezultat)
    redo_list.clear()

    srv_add_to_list(lista, "1", 54, 300, "10.10.2021", "intretinere")
    lista = undo_list.pop()
    assert len(lista) == 0

    cheltuiala = creeaza_cheltuiala("2", 54, 300, "10.10.2021", "intretinere")
    valideaza_cheltuiala(cheltuiala)

    rezultat = lista[:]
    undo_list.append(rezultat)
    redo_list.clear()

    srv_add_to_list(lista, "2", 54, 300, "10.10.2021", "intretinere")
    assert len(lista) == 1
    assert lista == [('2', 54, 300, '10.10.2021', 'intretinere')]

    cheltuiala = creeaza_cheltuiala("3", 57, 400, "10.12.2021", "canal")
    valideaza_cheltuiala(cheltuiala)

    rezultat = lista[:]
    undo_list.append(rezultat)
    redo_list.clear()

    srv_add_to_list(lista, "3", 57, 400, "10.12.2021", "canal")
    assert len(lista) == 2
    assert lista == [('2', 54, 300, '10.10.2021', 'intretinere'), ("3", 57, 400, "10.12.2021", "canal")]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    assert len(lista) == 2
    assert lista == [('2', 54, 300, '10.10.2021', 'intretinere'), ("3", 57, 400, "10.12.2021", "canal")]

    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    assert len(lista) == 1
    assert lista == [('2', 54, 300, '10.10.2021', 'intretinere')]


def run_teste():
    test_creeaza_cheltuiala()
    test_valideaza_cheltuiala()
    test_check_data()
    test_add_cheltuiala_to_list()
    test_srv_add_to_list()
    test_sterge_cheltuiala()
    test_get_cheltuiala_by_id()
    test_modifica_cheltuiala()
    test_sterge_toate_chelt()
    test_aduna_valoare()
    test_cmm_cheltuiala()
    test_ord_desc()
    test_sume_lunare()
    test_undoredo()
