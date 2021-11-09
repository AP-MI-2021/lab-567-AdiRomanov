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
    :param lista: Lista de cheltuieli
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


def sterge_toate_chelt(nr_ap, lista):
    """
    Sterge toate cheltuielile pentru un apartament dat
    :param nr_ap:
    :param lista: lista de cheltuieli
    :return: lista modificata
    """
    return [cheltuiala for cheltuiala in lista if get_nr_ap(cheltuiala) != nr_ap]


def aduna_valoare(lista, data, val):
    """
    Functia aduna o valoare la toate cheltuielile dintr-o dată citită.
    :param val: valoarea dorita
    :param lista: lista de cheltuieli
    :param data: data pentru care se aduna o suma la cheltuiala
    :return: noua lista de cheltuieli
    """
    lista_noua = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            id = get_id(cheltuiala)
            nr_ap = get_nr_ap(cheltuiala)
            suma = get_suma(cheltuiala)
            suma += val
            data = get_data(cheltuiala)
            tip = get_tip(cheltuiala)
            cheltuiala_noua = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
            lista_noua.append(cheltuiala_noua)
        else:
            lista_noua.append(cheltuiala)
    return lista_noua


def cmm_cheltuiala(list) -> tuple:
    """
    Determina cea mai mare cheltuiala pentru fiecare tip
    :param list: lista de cheltuieli
    :return: cele mai mari cheltuieli pentru fiecare tip (intretinere, canal si alte cheltuieli)
    """
    max_i = 0
    max_c = 0
    max_ac = 0

    for cheltuiala in list:
        suma = get_suma(cheltuiala)
        tip = get_tip(cheltuiala)
        if tip == 'intretinere':
            if suma > max_i:
                max_i = suma
        elif tip == 'canal':
            if suma > max_c:
                max_c = suma
        elif tip == 'alte cheltuieli':
            if suma > max_ac:
                max_ac = suma
    return max_i, max_c, max_ac


def ord_desc(list):
    n = len(list)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if get_suma(list[j]) < get_suma(list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def sume_lunare(lista):
    """
    Functia returneaza suma preturilor penru fiecare Nume
    :param lista: lista cu rezervari
    :return: o lista cu suma preturilor pentru fiecare nume
    """
    rezultat = {}
    for cheltuiala in lista:
        nr_ap = get_nr_ap(cheltuiala)
        suma = get_suma(cheltuiala)
        if nr_ap in rezultat:
            rezultat[nr_ap] = rezultat[nr_ap] + suma
        else:
            rezultat[nr_ap] = suma
    return rezultat
