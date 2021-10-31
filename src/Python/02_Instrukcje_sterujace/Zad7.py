"""
Pokaż za pomocą operacji logicznych:

a) Prawo wyłączonego środka.
b) Prawo niesprzeczności.
c) Przemienność koniunkcji.
d) Przemienność alternatywy.
e) Pierwsze prawo de Morgana.
f) Drugie prawo de Morgana.
"""

if __name__ == "__main__":

    print("Prawo wylacznego srodka")
    p = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " wyrazenie p v ~p ma wartosc logiczna",
        p or not p,
    )
    p = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " wyrazenie p v ~p ma wartosc logiczna",
        p or not p,
    )

    print("\nZasada niesprzecznosci")
    p = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna",
        not (p and not p),
    )
    p = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna",
        not (p and not p),
    )

    print("\nPrzemiennosc koniunkcji")
    p = False
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
        (p and q) == (q and p),
    )
    p = True
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
        (p and q) == (q and p),
    )
    p = False
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
        (p and q) == (q and p),
    )
    p = True
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
        (p and q) == (q and p),
    )

    print("\nPrzemiennosc alternatywy")
    p = False
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
        (p or q) == (q or p),
    )
    p = True
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
        (p or q) == (q or p),
    )
    p = False
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
        (p or q) == (q or p),
    )
    p = True
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
        (p or q) == (q or p),
    )

    print("\nPierwsze prawo de Morgana")
    p = False
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
        (not (p and q)) == (not q or not p),
    )
    p = True
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
        (not (p and q)) == (not q or not p),
    )
    p = False
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
        (not (p and q)) == (not q or not p),
    )
    p = True
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
        (not (p and q)) == (not q or not p),
    )

    print("\nDrugie prawo de Morgana")
    p = False
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
        (not (p or q)) == (not q and not p),
    )
    p = True
    q = False
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
        (not (p or q)) == (not q and not p),
    )
    p = False
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
        (not (p or q)) == (not q and not p),
    )
    p = True
    q = True
    print(
        "dla p majacego wartosc logiczna ",
        p,
        " oraz q majacego wartosc logiczna ",
        q,
        " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
        (not (p or q)) == (not q and not p),
    )
