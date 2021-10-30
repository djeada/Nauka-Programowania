"""
Dla dwóch pobranych od użytkownika liczb, sprawdź czy liczby są identyczne.
"""

if __name__ == "__main__":
    
    print("podaj dwie liczby")

    a = int(input())
    b = int(input())

    if a == b:
        print("liczby sa jednakowe")
    else:
        print("liczby sa rozne")
