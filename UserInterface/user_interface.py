from Domain.date_proprietar import to_str_cheltuiala
from Logic.general_logic import srv_add_to_list


def show_menu():
    print("1. Adaugati o cheltuiala in lista: ")
    print("a. Afisare lista cheltuieli: ")
    print("x. Iesire - exit")
    print("\n")

def ui_add_cheltuiala(list):
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

    srv_add_to_list(list, nr_ap, suma, data, tip)


def ui_print_cheltuieli(list):
    for cheltuiala in list:
        print(to_str_cheltuiala(cheltuiala))


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
        elif cmd == 'a':
            ui_print_cheltuieli(list)
        else:
            print("Optiune invalida!Reincercati!")
