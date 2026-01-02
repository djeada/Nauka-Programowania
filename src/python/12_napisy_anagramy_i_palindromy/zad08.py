"""
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

"""


def czy_wyjatkowy_palindrom(s):
    """
    Sprawdza czy podciąg jest wyjątkowym palindromem.
    
    Wyjątkowy palindrom to:
    1. wszystkie znaki są identyczne (np. 'aaa'), lub
    2. wszystkie znaki poza środkowym są identyczne (np. 'cbc')
    
    Złożoność czasowa: O(n), gdzie n to długość podciągu
    Złożoność pamięciowa: O(1)
    """
    if len(s) == 0:
        return False
    
    # Przypadek 1: wszystkie znaki identyczne
    if len(set(s)) == 1:
        return True
    
    # Przypadek 2: wszystkie znaki poza środkowym identyczne
    # (ma sens tylko dla nieparzystej długości >= 3)
    if len(s) >= 3 and len(s) % 2 == 1:
        srodek = len(s) // 2
        # Sprawdzenie czy wszystkie znaki poza środkowym są takie same
        znaki_bez_srodka = s[:srodek] + s[srodek+1:]
        if len(set(znaki_bez_srodka)) == 1:
            # Dodatkowo musi być palindromem
            return s == s[::-1]
    
    return False


def znajdz_wyjatkowe_palindromy(slowo):
    """
    Znajduje wszystkie unikalne wyjątkowe palindromy w słowie.
    
    Złożoność czasowa: O(n^3), gdzie n to długość słowa
    Złożoność pamięciowa: O(n^2) dla przechowania wyników
    """
    znalezione = set()
    
    # Iteracja przez wszystkie możliwe podciągi
    for i in range(len(slowo)):
        for j in range(i + 1, len(slowo) + 1):
            podciag = slowo[i:j]
            
            # Sprawdzenie czy podciąg jest wyjątkowym palindromem
            if czy_wyjatkowy_palindrom(podciag):
                znalezione.add(podciag)
    
    # Sortowanie wyników według długości, a następnie alfabetycznie
    return sorted(znalezione, key=lambda x: (len(x), x))


if __name__ == "__main__":
    # Wczytanie słowa z wejścia
    slowo = input().strip()
    
    # Znalezienie wszystkich wyjątkowych palindromów
    palindromy = znajdz_wyjatkowe_palindromy(slowo)
    
    # Wypisanie każdego palindromu w osobnej linii
    for palindrom in palindromy:
        print(palindrom)
