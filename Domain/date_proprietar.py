


def creeaza_cheltuiala(nr_ap: int, suma: float, data: str, tip: str):
    """
    Creeaza o noua cheltuiala.
    :param nr_ap: Numarul apartamentului
    :param suma:  Suma respectiva
    :param data:  Data la care este adaugata cheltuiala
    :param tip:   Tipul cheltuielii
    :return:      O cheltuiala
    """
    return {"nr_ap": nr_ap,
            "suma": suma,
            "data": data,
            "tip": tip
            }


def get_nr_ap(cheltuiala):
    """
    Getter pentru numarul apartamentului
    :param cheltuiala: Numarul apartamentului
    :return: Numarul apartamentului din cheltuiala
    """
    return cheltuiala["nr_ap"]


def get_suma(cheltuiala):
    """
    Getter pentru suma cheltuielilor
    :param cheltuiala: Suma
    :return: Valoarea sumei din cheltuiala
    """
    return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    Getter pentru data la care se face adaugarea
    :param cheltuiala: Data respectiva
    :return: Data din cheltuiala
    """
    return cheltuiala["data"]


def get_tip(cheltuiala):
    """
    Getter pentru tipul cheltuielii
    :param cheltuiala: Tipul respectiv
    :return: Tipul din cheltuiala
    """
    return cheltuiala["tip"]


def to_str_cheltuiala(cheltuiala):
    """
    Functie care face printing la o cheltuiala
    :param cheltuiala: cheltuiala
    :output: cheltuiala sub forma de string
    """
    return "Apartamentul "+str(cheltuiala["nr_ap"])+": "+str(cheltuiala["suma"])+"-RON ("+str(cheltuiala["data"])+") <"+str(cheltuiala["tip"])+">"