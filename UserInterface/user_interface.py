from Domain.date_proprietar import to_str_cheltuiala
from Logic.general_logic import srv_add_to_list, sterge_cheltuiala, modifica_cheltuiala, sterge_toate_chelt, \
    aduna_valoare, cmm_cheltuiala, ord_desc


def show_menu():
    print("1. Adaugati o cheltuiala in lista. ")
    print("2. Stergeti o cheltuiala din lista. ")
    print("3. Modificati o cheltuiala din lista. ")
    print("4. Șterge toate cheltuielile pentru un apartament dat. ")
    print("5. Aduna o valoare la toate cheltuielile dintr o data citita.")
    print("6. Afiseaza cea mai mare cheltuiala pentru fiecare tip. ")
    print("7. Ordoneaza in ordine descrescatoare cheltuielile dupa pret. ")
    print("a. Afisare lista cheltuieli: ")
    print("x. Iesire - exit")
    print("\n")


def ui_add_cheltuiala(list):
    id = input("Introduceti id-ul cheltuielii: ")
    try:
        nr_ap = int(input("Introduceti numarul apartamentului: "))
    except ValueError:
        print("Valoare numerica invalida pentru apartament!\n")
        return
    try:
        suma = float(input("Introduceti valoarea facturii(cu zecimale daca este cazul): "))
    except ValueError:
        print("Valoare numerica invalida pentru factura!\n")
        return
    data = input("Introduceti data sub forma DD.MM.YYYY: ")
    tip = input("Introducetil tipul facturii(intretinere, canal, alte cheltuieli): ")

    srv_add_to_list(list, id, nr_ap, suma, data, tip)


def ui_sterge_cheltuiala(list):
    id = input("Dati id-ul cheltuielii pe care doriti sa o stergeti din lista: ")
    return sterge_cheltuiala(id, list)


def ui_modifica_cheltuiala(list):
    print("Modificare cheltuiala. Introduceti datele de modificat")
    id = input("Introduceti id-ul cheltuielii: ")
    try:
        nr_ap = int(input("Introduceti numarul apartamentului: "))
    except ValueError:
        print("Valoare numerica invalida pentru apartament!\n")
        return
    try:
        suma = float(input("Introduceti valoarea facturii(cu zecimale daca este cazul): "))
    except ValueError:
        print("Valoare numerica invalida pentru factura!\n")
        return
    data = input("Introduceti data sub forma DD.MM.YYYY: ")
    tip = input("Introducetil tipul facturii(intretinere, canal, alte cheltuieli): ")
    return modifica_cheltuiala(list, id, nr_ap, suma, data, tip)


def ui_sterge_toate_chelt(list):
    nr_ap = int(input("Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: "))
    return sterge_toate_chelt(nr_ap, list)


def ui_print_cheltuieli(list):
    for cheltuiala in list:
        print(to_str_cheltuiala(cheltuiala))


def ui_adauga_valoare(list):
    val = float(input("Introduceti suma dorita pentru adaugare(cu zecimale daca este cazul): "))
    data = input("Introduceti data pentru care cheltuielile vor fi schimbate: ")
    return aduna_valoare(list, data, val)


def ui_cmm_cheltuiala(list):
    rez = cmm_cheltuiala(list)
    print("Intretinere: ", rez[0])
    print("Canal: ", rez[1])
    print("Alte cheltuieli: ", rez[2])


def ui_ord_desc(list):
    return ord_desc(list)


def run():
    list = []
    while True:
        show_menu()
        cmd = input("Introduceti optiunea: ")
        if cmd == 'x':
            print("Inchidere program...")
            return
        if cmd == "":
            continue
        if cmd == '1':
            try:
                ui_add_cheltuiala(list)
            except Exception as ex:
                print(ex)
        elif cmd == '2':
            try:
                list = ui_sterge_cheltuiala(list)
            except Exception as ex:
                print(ex)
        elif cmd == '3':
            try:
                list = ui_modifica_cheltuiala(list)
            except Exception as ex:
                print(ex)
        elif cmd == '4':
            try:
                list = ui_sterge_toate_chelt(list)
            except Exception as ex:
                print(ex)
        elif cmd == '5':
            try:
                list = ui_adauga_valoare(list)
            except Exception as ex:
                print(ex)
        elif cmd == '6':
            ui_cmm_cheltuiala(list)
        elif cmd == '7':
            try:
                list = ui_ord_desc(list)
            except Exception as ex:
                print(ex)
        elif cmd == 'a':
            ui_print_cheltuieli(list)
        else:
            print("Optiune invalida! Reincercati!")
