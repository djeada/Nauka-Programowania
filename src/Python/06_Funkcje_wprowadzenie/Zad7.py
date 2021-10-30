"""
Napisz dwie funkcje. Pierwsza powinna prosić użytkownika o podanie nazwy oraz hasła 
oraz zwracać otrzymane dane. Druga powinna otrzymywać dane od pierwszej i ponownie 
prosić o podanie nazwy oraz hasła. Prośba o podanie danych powinna zostać umieszczona 
w pętli. Warunkiem zakończenia pętli jest podanie przez użytkownika danych identycznych 
z tymi przekazanymi przez pierwszą funkcję.
"""

def inicjalizacja_danych():
    nazwa = input("Podaj nazwę: ")
    haslo = input("Podaj hasło: ")
    return nazwa, haslo

def sprawdzenie_danych(nazwa, haslo):

    nazwa2 = None
    haslo2 = None

    while not(nazwa == nazwa2 and haslo == haslo2):
        nazwa2 = input("Podaj nazwę: ")
        haslo2 = input("Podaj hasło: ")

    print("Dane są identyczne")

if __name__ == "__main__":
    
    nazwa, haslo = inicjalizacja_danych()
    sprawdzenie_danych(nazwa, haslo)