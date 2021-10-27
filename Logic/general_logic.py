from Domain.date_proprietar import get_nr_ap, get_data, get_tip, creeaza_cheltuiala, get_suma, get_id


def check_data(data):
    """
    Verifica daca data introdusa este valida
    :param data: O data de tip string de forma DD/MM/YYYY separate prin " . " sau " / "
    :return: True daca data este valida, False in caz contrar
    """
    lst = []

    lst_str = data
    lst_str_split = lst_str.split('.')

    for nr_str in lst_str_split:
        lst.append(int(nr_str))

    if 1 > lst[0] or lst[0] > 31:
        return False
    if 1 > lst[1] or lst[1] > 12:
        return False
    if 2000 > lst[2] or lst[2] > 2030:
        return False

    return True


def valideaza_cheltuiala(verif):
    """
    Functie care valideaza o cheltuiala
    :param verif: verif de tip cheltuiala
    :return: -
    :raises: Exception cu textul:
            "Numar apartament invalid!\n", daca nr_ap < 0
            "Suma invalida!\n", daca suma < 0
            "Data invalida!\n", daca data introdusa nu se regaseste in calendar.
            "Tip invalid!\n", daca tipul specificat este diferit de: intretinere, canal sau alte cheltuieli.
    """
    err = ""
    if get_nr_ap(verif) < 0:
        err += "Numar apartament invalid!\n"
    if get_suma(verif) < 0:
        err += "Suma invalida!\n"
    if check_data(get_data(verif)) is False:
        err += "Data invalida!\n"
    if get_tip(verif) != "intretinere" and get_tip(verif) != "canal" and get_tip(verif) != "alte cheltuieli":
        err += "Tip invalid!\n"

    if len(err) > 0:
        raise Exception(err)


def add_cheltuiala_to_list(lista, cheltuiala):
    """
    Functie care adauga o cheltuiala (unica) in lista de cheltuieli
    :param lista: lista de cheltuieli
    :param cheltuiala: o cheltuiala
    :return: - , lista' = l U {cheltuiala}, daca nu exista deja o cheltuiala pe acelasi ap
    :raises: Exception cu textul
                "Cheltuiala existenta!\n", daca exista deja cheltuiala
    """
    for _cheltuiala in lista:
        if sunt_egale_cheltuielile(cheltuiala, _cheltuiala):
            raise Exception("Cheltuiala existenta!\n")
    lista.append(cheltuiala)


def sunt_egale_cheltuielile(c1, c2):
    """
    Functie care verifica daca doua cheltuieli sunt egale
    :param c1: cheltuieli
    :param c2: cheltuieli
    :return: True daca cheltuiala1 si cheltuiala2 au acelasi nr de apartament, data si tip
             False in caz contrar
    """
    if get_id(c1) == get_id(c2):
        return True

    return False


def srv_add_to_list(list, id, nr_ap, suma, data, tip):
    """
    Functie care creeaza o cheltuiala pe baza nr_ap, suma, data si tip
    Valideaza aceasta cheltuiala si daca este valida o adauga in lista list de cheltuieli unica /
    doar daca nu exista deja acea cheltuiala in lista
    :param id: Id-ul cheltuielii
    :param list: lista de cheltuieli unice prin nr_ap, data si tip
    :param nr_ap: numarul apartamentului
    :param suma: suma
    :param data: data de emitere
    :param tip: tipul cheltuielii
    :return: - , daca totul se desfasoara cu succes
    :raises: Exception cu textul ...
    """
    cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    valideaza_cheltuiala(cheltuiala)
    add_cheltuiala_to_list(list, cheltuiala)


def get_cheltuiala_by_id(id: str, lista):
    """
    Selecteaza chletuiala cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu id-ul dat din lista sau None, daca nu exista
    """
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def sterge_cheltuiala(id, lista):
    """
    Sterge o cheltuiala din lista
    :param id: id_ul cheltuielii
    :param lista: lista de cheltuieli
    :return: lista rezultata dupa stergerea cheltuielii dorite
    """
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def modifica_cheltuiala(lista, id, nr_ap, suma, data, tip):
    """
    Modifica o cheltuiala dupa id
    :param list: Lista de cheltuieli
    :param id: Id-ul cheltuielii
    :param nr_ap: Nr apartamentului
    :param suma: Valoarea facturii
    :param data: Data emiterii
    :param tip: Tipul facturii
    :return: Cheltuiala dupa modificarile aferente
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua
    #need test


def sterge_toate_chelt(nr_ap, lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param lista: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lista if get_nr_ap(cheltuiala) != nr_ap]

    #need test
