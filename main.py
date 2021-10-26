"""
Scrieți un program pentru gestionarea unei asociații de proprietari. Vor fi suportate operațiile:
1.1. Adăugare / ștergere / modificare cheltuială: se efectuează pe bază de număr de apartament.
        O cheltuială conține număr apartament, suma, data (DD.MM.YYYY)
            și tipul: întreținere, canal, alte cheltuieli.
1.2. Ștergerea tuturor cheltuielilor pentru un apartament dat.
1.3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.
1.4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
1.5. Ordonarea cheltuielilor descrescător după sumă.
1.6. Afișarea sumelor lunare pentru fiecare apartament.
1.7. Undo.
"""
from Tests.tests import run_teste
from UserInterface.user_interface import run


def main():
    run_teste()
    run()


if __name__ == '__main__':
    main()
