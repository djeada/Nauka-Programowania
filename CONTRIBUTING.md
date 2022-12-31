Jeśli chcesz dodać zmiany do swojego repozytorium, postępuj zgodnie z poniższą instrukcją:

## Jakie zmiany są mile widziane?

1. Nowe rozwiązanie do zadania, które jeszcze nie zostało rozwiązane.
1. Alternatywna wersja rozwiązania, która redukuje złożoność czasową lub pamięciową.
1. Alternatywna wersja rozwiązania, która zwiększa czytelność kodu, ale nie redukuje złożoności czasowej ani pamięciowej.
1. Alternatywna wersja rozwiązania, która używa nowszej wersji składni, ale nie redukuje złożoności czasowej ani pamięciowej.
1. Poprawki błędów składni, literówek lub błędów logicznych w istniejących rozwiązaniach.

## Instrukcja techniczna

1. Utwórz "Fork" tego repozytorium na swoim koncie na stronie <a href="https://github.com">github.com</a>.
2. Sklonuj ten projekt na swój komputer, używając następującej komendy:

```bash
git clone https://github.com/djeada/Nauka-programowania.git
```

3. Dodaj nową gałąź, np.:

```bash
git checkout -b nazwa-galezi
```

4. Wprowadź zmiany i opisz je w wiadomości "commit". Przykład: "Dodano rozwiązanie do zadania 6 z wprowadzenia do list - java".
5. Użyj komendy <i>git push</i>:

```bash
git add changed_file
git commit -m "twoj komentarz do wprowadzanych zmian"
git push origin nazwa-galezi
```
6. Zaloguj się na stronę <a href="https://github.com">github.com</a> i stwórz pull request w swoim repozytorium.

## Szablony

Oto przykładowy szablon dla plików z rozwiązaniami:


```python
'''
# Nazwa zadania

## Tresc

[Tutaj opisz problem i jego wymagania, np. wejście, wyjście i oczekiwane działanie.]

## Wejście:
[Tutaj opisz format wejścia danych, np. lista liczb, ciąg znaków itp.]

## Wyjście:
[Tutaj opisz format wyjścia danych, np. liczba, ciąg znaków itp.]

## Objaśnienie wyjścia:
[Tutaj opisz, co oznaczają poszczególne elementy wyjścia.]

---

## Opis rozwiązania 1:
[Tutaj opisz, jak działa Twoje rozwiązanie.]

### Złożoność czasowa: O(X)
### Złożoność pamięciowa: O(X)

## Opis rozwiązania 2:
[Tutaj opisz, jak działa drugie rozwiązanie (jeśli istnieje).]

### Złożoność czasowa: O(X)
### Złożoność pamięciowa: O(X)

'''

## Implementacja rozwiązania 1:

def nazwa_rozwiazania_1(parametry):
    pass

## Implementacja rozwiązania 2:

def nazwa_rozwiazania_2(parametry):
    pass

## Testy

# Test 1
dane_wejsciowe = [1,2,3]
oczekiwany_wynik = 'wynik'
wynik = nazwa_rozwiazania_1(dane_wejsciowe)
assert wynik == oczekiwany_wynik
# Test 2
dane_wejsciowe = [1,2,3]
oczekiwany_wynik = 'wynik'
wynik = nazwa_rozwiazania_2(dane_wejsciowe)
assert wynik == oczekiwany_wynik
```
