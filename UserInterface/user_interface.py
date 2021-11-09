from Domain.date_proprietar import to_str_cheltuiala, creeaza_cheltuiala
from Logic.general_logic import srv_add_to_list, sterge_cheltuiala, modifica_cheltuiala, sterge_toate_chelt, \
    aduna_valoare, cmm_cheltuiala, ord_desc, sume_lunare, valideaza_cheltuiala
from UserInterface.command_line_console import show_menu_interfata, start_nou


def show_menu():
    print("1. Adaugati o cheltuiala in lista. ")
    print("2. Stergeti o cheltuiala din lista. ")
    print("3. Modificati o cheltuiala din lista. ")
    print("4. Șterge toate cheltuielile pentru un apartament dat. ")
    print("5. Aduna o valoare la toate cheltuielile dintr o data citita.")
    print("6. Afiseaza cea mai mare cheltuiala pentru fiecare tip. ")
    print("7. Ordoneaza in ordine descrescatoare cheltuielile dupa pret. ")
    print("8. Afiseaza sumele pentru fiecare apartament. ")
    print("u. Undo. ")
    print("r. Redo. ")
    print("a. Afisare lista cheltuieli: ")
    print("x. Iesire - exit")
    print("\n")


def ui_add_cheltuiala(list, undo_list, redo_list):
    try:
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
        cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
        valideaza_cheltuiala(cheltuiala)

        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()

        srv_add_to_list(list, id, nr_ap, suma, data, tip)
    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_sterge_cheltuiala(list, undo_list, redo_list):
    try:
        id = input("Dati id-ul cheltuielii pe care doriti sa o stergeti din lista: ")
        rez = sterge_cheltuiala(id, list)

        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()
        return rez

    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_modifica_cheltuiala(list, undo_list, redo_list):
    try:
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
        rez = modifica_cheltuiala(list, id, nr_ap, suma, data, tip)

        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()
        return rez

    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_sterge_toate_chelt(list, undo_list, redo_list):
    try:
        nr_ap = int(input("Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile: "))
        rez = sterge_toate_chelt(nr_ap, list)

        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()
        return rez

    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_print_cheltuieli(list):
    for cheltuiala in list:
        print(to_str_cheltuiala(cheltuiala))


def ui_adauga_valoare(list, undo_list, redo_list):
    try:
        val = float(input("Introduceti suma dorita pentru adaugare(cu zecimale daca este cazul): "))
        data = input("Introduceti data pentru care cheltuielile vor fi schimbate: ")
        rez = aduna_valoare(list, data, val)

        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()
        return rez

    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_cmm_cheltuiala(list):
    rez = cmm_cheltuiala(list)
    print("Intretinere: ", rez[0])
    print("Canal: ", rez[1])
    print("Alte cheltuieli: ", rez[2])


def ui_ord_desc(list, undo_list, redo_list):
    try:
        rez = ord_desc(list)
        rezultat = list[:]
        undo_list.append(rezultat)
        redo_list.clear()
        return rez

    except Exception as ve:
        print("Eroare: {}".format(ve))
        return list


def ui_sume_lunare(list):
    print(sume_lunare(list))


def start():
    list = []
    undo_list = []
    redo_list = []
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
                ui_add_cheltuiala(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '2':
            try:
                list = ui_sterge_cheltuiala(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '3':
            try:
                list = ui_modifica_cheltuiala(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '4':
            try:
                list = ui_sterge_toate_chelt(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '5':
            try:
                list = ui_adauga_valoare(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '6':
            ui_cmm_cheltuiala(list)
        elif cmd == '7':
            try:
                list = ui_ord_desc(list, undo_list, redo_list)
            except Exception as ex:
                print(ex)
        elif cmd == '8':
            ui_sume_lunare(list)
        elif cmd == 'u':
            if len(undo_list) > 0:
                redo_list.append(list)
                list = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif cmd == 'r':
            if len(redo_list) > 0:
                undo_list.append(list)
                list = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif cmd == 'a':
            ui_print_cheltuieli(list)
        else:
            print("Optiune invalida! Reincercati!")


def run():
    while True:
        show_menu_interfata()
        option = input("Introduceti optiunea: ")
        if option == 'x':
            print("Inchidere program...")
            return
        if option == "":
            continue

        if option == '1':
            start()
        elif option == '2':
            start_nou()
        else:
            print("Optiune invalida! Reincercati!")
