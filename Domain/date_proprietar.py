def creeaza_cheltuiala(id: str, nr_ap: int, suma: float, data: str, tip: str) -> tuple:
    """
    Creeaza o noua cheltuiala.
    :param id: Id-ul cheltuielii
    :param nr_ap: Numarul apartamentului
    :param suma:  Suma respectiva
    :param data:  Data la care este adaugata cheltuiala
    :param tip:   Tipul cheltuielii
    :return:      O cheltuiala
    """
    return id, nr_ap, suma, data, tip


def get_id(cheltuiala):
    """
    Getter pentru id-ul cheltuielii
    :param cheltuiala: Id-ul
    :return: Id-ul cheltuielii
    """
    return cheltuiala[0]


def get_nr_ap(cheltuiala):
    """
    Getter pentru numarul apartamentului
    :param cheltuiala: Numarul apartamentului
    :return: Numarul apartamentului din cheltuiala
    """
    return cheltuiala[1]


def get_suma(cheltuiala):
    """
    Getter pentru suma cheltuielilor
    :param cheltuiala: Suma
    :return: Valoarea sumei din cheltuiala
    """
    return cheltuiala[2]


def get_data(cheltuiala):
    """
    Getter pentru data la care se face adaugarea
    :param cheltuiala: Data respectiva
    :return: Data din cheltuiala
    """
    return cheltuiala[3]


def get_tip(cheltuiala):
    """
    Getter pentru tipul cheltuielii
    :param cheltuiala: Tipul respectiv
    :return: Tipul din cheltuiala
    """
    return cheltuiala[4]


def to_str_cheltuiala(cheltuiala):
    """
    Functie care face printing la o cheltuiala
    :param cheltuiala: cheltuiala
    :output: cheltuiala sub forma de string
    """
    return "Id_Factura: " + str(cheltuiala[0]) + " | " + \
           "Apartamentul " + str(cheltuiala[1]) + \
           ": " + str(cheltuiala[2]) + \
           "-RON (" + str(cheltuiala[3]) + \
           ") <" + str(cheltuiala[4]) + ">"
