from Domain.date_proprietar import to_str_cheltuiala, creeaza_cheltuiala, get_id, get_nr_ap, get_suma, get_data, get_tip
from Logic.general_logic import srv_add_to_list, sterge_cheltuiala, modifica_cheltuiala, sterge_toate_chelt, \
    aduna_valoare, cmm_cheltuiala, ord_desc, valideaza_cheltuiala


def show_menu_interfata():
    print("1. Interfata veche.")
    print("2. Interfata noua.")
    print("x. Exit.")


def show_menu_nou():
    print("1. Adaugati o cheltuiala in lista. ")
    print("add,id,nr_ap,suma,data,tip")
    print("2. Stergeti o cheltuiala din lista. ")
    print("delete,id")
    print("3. Modificati o cheltuiala din lista. ")
    print("mod,id,nr_ap,suma,data,tip")
    print("4. Șterge toate cheltuielile pentru un apartament dat. ")
    print("delete_chelt,nr_ap")
    print("5. Aduna o valoare la toate cheltuielile dintr o data citita.")
    print("add_chelt,val,data")
    print("6. Afiseaza cea mai mare cheltuiala pentru fiecare tip. ")
    print("show_highest")
    print("7. Ordoneaza in ordine descrescatoare cheltuielile dupa pret. ")
    print("ord_desc")
    print("a. Afisare lista cheltuieli: ")
    print("show_all")
    print("x. Iesire - exit")
    print("exit")
    print("\n")


def ui_add_cheltuiala(list, rez):
    cheltuiala = creeaza_cheltuiala(list[1], int(list[2]), float(list[3]), list[4], list[5])

    id = get_id(cheltuiala)
    nr_ap = get_nr_ap(cheltuiala)
    suma = get_suma(cheltuiala)
    data = get_data(cheltuiala)
    tip = get_tip(cheltuiala)
    valideaza_cheltuiala(cheltuiala)
    srv_add_to_list(rez, id, nr_ap, suma, data, tip)


def ui_sterge_cheltuiala(list, rez):
    id = get_id(list[1])
    return sterge_cheltuiala(id, list)


def ui_modifica_cheltuiala(list, rez):
    cheltuiala = creeaza_cheltuiala(list[1], int(list[2]), float(list[3]), list[4], list[5])

    id = get_id(cheltuiala)
    nr_ap = get_nr_ap(cheltuiala)
    suma = get_suma(cheltuiala)
    data = get_data(cheltuiala)
    tip = get_tip(cheltuiala)
    valideaza_cheltuiala(cheltuiala)
    return modifica_cheltuiala(rez, id, nr_ap, suma, data, tip)


def ui_sterge_toate_chelt(list, rez):
    nr_ap = get_nr_ap(list[1])
    return sterge_toate_chelt(nr_ap, rez)


def ui_print_cheltuieli(list):
    for cheltuiala in list:
        print(to_str_cheltuiala(cheltuiala))


def ui_adauga_valoare(list, rez):
    val = list[1]
    data = get_data(list[2])
    return aduna_valoare(rez, data, val)


def ui_cmm_cheltuiala(list):
    rez = cmm_cheltuiala(list)
    print("Intretinere: ", rez[0])
    print("Canal: ", rez[1])
    print("Alte cheltuieli: ", rez[2])


def ui_ord_desc(list):
    return ord_desc(list)


def get_command(cmd):
    list = []
    rez = []

    lst_str = cmd
    lst_str_split = lst_str.split(',')

    for nr_str in lst_str_split:
        list.append(nr_str)
    print(len(list))

    if list[0] == 'add':
        try:
            ui_add_cheltuiala(list, rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'delete':
        try:
            rez = ui_sterge_cheltuiala(list, rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'mod':
        try:
            rez = ui_modifica_cheltuiala(list, rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'delete_chelt':
        try:
            rez = ui_sterge_toate_chelt(list, rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'add_chelt':
        try:
            rez = ui_adauga_valoare(list, rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'show_highest':
        ui_cmm_cheltuiala(rez)
    elif list[0] == 'ord_desc':
        try:
            rez = ui_ord_desc(rez)
        except Exception as ex:
            print(ex)
    elif list[0] == 'show_all':
        ui_print_cheltuieli(rez)
    elif list[0] == 'exit':
        pass
    else:
        print("Optiune invalida! Reincercati!")


def start_nou():
    list = []
    while True:
        show_menu_nou()
        cmd = input("Introduceti comanda: ")
        if cmd == 'x':
            break
        get_command(cmd)
