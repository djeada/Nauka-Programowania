# Rozdział 20: Operacje na plikach

Poniższe zadania polegają na wczytywaniu danych ze **standardowego wejścia** (stdin), wykonywaniu operacji na plikach i folderach oraz wypisywaniu wyniku na **standardowe wyjście** (stdout).
**Każde zadanie jest osobnym, niezależnym programem.**

**Konwencje wspólne:**

* Program działa na plikach w **katalogu roboczym**, czyli w folderze, w którym jest uruchamiany. Wszystkie ścieżki na wejściu są **względne** wobec katalogu roboczego i używają `/` jako separatora, np. `dane/raport.txt`. Ścieżki wczytuj jako całe linie — mogą zawierać spacje.
* Sprawdzarka przed każdym testem tworzy nowy katalog roboczy z plikami opisanymi w teście, uruchamia program, a potem sprawdza zarówno wypisany tekst, jak i zawartość plików.
* W przykładach **Pliki przed:** pokazuje zawartość katalogu roboczego przed uruchomieniem programu, a **Pliki po:** — stan wybranych plików po jego zakończeniu. Każda linia to ścieżka pliku, a linie zaczynające się od `| ` to kolejne wiersze jego treści. Ścieżka zakończona `/` to pusty folder, `(rozmiar: N B)` oznacza plik o rozmiarze N bajtów, a `(usunięty)` — plik, którego po zakończeniu programu ma już nie być.
* Pliki tekstowe są zapisane w kodowaniu UTF-8 — otwieraj je przez `open(sciezka, encoding="utf-8")`.
* **Rozszerzenie** to końcówka nazwy pliku od ostatniej kropki (razem z nią), np. `archiwum.tar.gz` ma rozszerzenie `.gz`. Rozszerzenia porównuj **bez względu na wielkość liter** (`.TXT` to też `.txt`).
* Listy plików wypisuj po jednym w linii, jako ścieżki **względem podanego folderu** z separatorem `/` (np. `2024/raport.txt`), posortowane rosnąco tak, jak sortuje napisy funkcja `sorted()`. Na Windowsie ścieżki mają separator `\` — zamień go na `/` (np. metodą `Path.as_posix()`).
* Komunikaty dla przypadków brzegowych wypisuj dokładnie w podanej postaci, np. `Folder nie istnieje.`, `Plik nie istnieje.`, `Brak plików.`
* Program nie wypisuje komunikatów typu „Podaj ścieżkę:”. Tekst podany w `input("…")` jest ignorowany przez sprawdzarkę.

---

## ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Wczytaj ścieżkę i sprawdź, co się pod nią znajduje w katalogu roboczym. Wypisz:

* `plik` — jeśli ścieżka wskazuje istniejący plik,
* `folder` — jeśli ścieżka wskazuje istniejący folder,
* `brak` — jeśli pod tą ścieżką nic nie ma.

### Wejście

* 1. linia: ścieżka (względna, z `/` jako separatorem; może zawierać spacje)

### Wyjście

Jedno słowo: `plik`, `folder` albo `brak`.

### Przykład

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
dane/raport.txt
```

**Wyjście:**

```
plik
```

### Przykład 2

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
dane
```

**Wyjście:**

```
folder
```

### Przykład 3

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
raport.txt
```

**Wyjście:**

```
brak
```

Plik `raport.txt` leży w folderze `dane`, a nie bezpośrednio w katalogu roboczym.

### Uwagi

* Przydatne funkcje: `os.path.isfile()` i `os.path.isdir()` albo metody `Path.is_file()` i `Path.is_dir()` z modułu `pathlib`.

---

## ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Wczytaj ścieżkę folderu i rozszerzenie (np. `.txt`). Wypisz nazwy wszystkich **plików** o tym rozszerzeniu, które leżą **bezpośrednio** w tym folderze. Nie zaglądaj do podfolderów. Foldery pomijaj, nawet jeśli ich nazwa wygląda jak nazwa pliku (np. folder `stare.txt`).

Rozszerzenia porównuj bez względu na wielkość liter, ale nazwy wypisuj dokładnie tak, jak są zapisane.

### Wejście

* 1. linia: ścieżka folderu
* 2. linia: rozszerzenie z kropką, np. `.txt`

### Wyjście

* Nazwy pasujących plików (same nazwy, bez ścieżki folderu), każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli w folderze nie ma żadnego pasującego pliku.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
dokumenty/lista zakupów.txt
| mleko
| chleb
dokumenty/notatki.TXT
| Zadzwonić do Ani.
dokumenty/zdjęcie.png
dokumenty/stare/archiwum.txt
```

**Wejście:**

```
dokumenty
.txt
```

**Wyjście:**

```
lista zakupów.txt
notatki.TXT
```

Plik `stare/archiwum.txt` leży w podfolderze, więc go pomijamy.

### Przykład 2

**Pliki przed:** *(brak)*

**Wejście:**

```
zdjecia
.png
```

**Wyjście:**

```
Folder nie istnieje.
```

### Uwagi

* Zawartość folderu zwraca `os.listdir()` albo `Path.iterdir()`. Rozszerzenie pliku poda `os.path.splitext()` albo `Path.suffix`.

---

## ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Wczytaj ścieżkę folderu i nazwę pliku (np. `raport.txt`). Przeszukaj ten folder **i wszystkie jego podfoldery** (na dowolnej głębokości) i wypisz ścieżki wszystkich plików o dokładnie takiej nazwie.

* Nazwy porównuj dokładnie — wielkość liter ma znaczenie (`Raport.txt` to inna nazwa niż `raport.txt`).
* Wypisuj tylko pliki. Folder o szukanej nazwie nie jest wynikiem, ale jego wnętrze też przeszukaj.
* Ścieżki wypisuj względem podanego folderu. Folder `.` oznacza cały katalog roboczy.

### Wejście

* 1. linia: ścieżka folderu, w którym zaczynasz szukanie (`.` = cały katalog roboczy)
* 2. linia: nazwa pliku

### Wyjście

* Ścieżki znalezionych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Nie znaleziono.` — jeśli nie ma żadnego pliku o tej nazwie.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
raport.txt
2023/raport.txt
2023/raport.docx
2023/styczeń/raport.txt
2024/Raport.txt
```

**Wejście:**

```
.
raport.txt
```

**Wyjście:**

```
2023/raport.txt
2023/styczeń/raport.txt
raport.txt
```

`2024/Raport.txt` ma inną nazwę (wielka litera), a `2023/raport.docx` — inne rozszerzenie.

### Przykład 2

**Pliki przed:**

```
raport.txt
2023/raport.txt
2023/raport.docx
2023/styczeń/raport.txt
2024/Raport.txt
```

**Wejście:**

```
2023
raport.txt
```

**Wyjście:**

```
raport.txt
styczeń/raport.txt
```

Ścieżki są podane względem folderu `2023`.

### Uwagi

* Wszystkie pliki w folderze i jego podfolderach zwraca `os.walk()` albo `Path.rglob("*")`.

---

## ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Wczytaj ścieżkę pliku tekstowego i wypisz jego treść dokładnie tak, jak jest zapisana w pliku (wiersz po wierszu, razem z pustymi wierszami w środku).

### Wejście

* 1. linia: ścieżka pliku

### Wyjście

* Treść pliku. Pusty plik — nic nie wypisuj.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku (np. wskazuje folder albo nic).

### Przykład

**Pliki przed:**

```
wiadomość.txt
| Witaj!
| To jest przykładowa treść pliku tekstowego.
```

**Wejście:**

```
wiadomość.txt
```

**Wyjście:**

```
Witaj!
To jest przykładowa treść pliku tekstowego.
```

### Przykład 2

**Pliki przed:**

```
wiadomość.txt
| Witaj!
```

**Wejście:**

```
list.txt
```

**Wyjście:**

```
Plik nie istnieje.
```

### Uwagi

* Sprawdzarka ignoruje końcowe spacje w wierszach i puste wiersze na samym końcu wyjścia, więc nie musisz się przejmować tym, czy plik kończy się znakiem nowej linii.

---

## ZAD-05 — Posortuj adresy IP z pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `sort`, `list`

### Treść

Wczytaj ścieżkę pliku tekstowego, w którym każdy niepusty wiersz zawiera jeden adres IPv4 — cztery liczby od 0 do 255 oddzielone kropkami, np. `192.168.1.10`. Wypisz wszystkie adresy posortowane **rosnąco według wartości liczbowych**: najpierw według pierwszej liczby, przy równych — według drugiej, potem trzeciej i czwartej.

Zwykłe porównywanie napisów da złą kolejność: `"192.168.1.10" < "192.168.1.2"`, chociaż $10 > 2$.

### Wejście

* 1. linia: ścieżka pliku z adresami

### Wyjście

* Adresy w kolejności rosnącej, każdy w osobnej linii. Powtarzające się adresy wypisz tyle razy, ile razy występują w pliku.
* `Brak adresów.` — jeśli plik nie zawiera żadnego adresu.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Puste wiersze pomiń. Wiersze z adresami nie zawierają spacji ani innych znaków.

### Przykład

**Pliki przed:**

```
adresy_ip.txt
| 192.168.1.10
| 10.0.0.1
| 192.168.1.2
| 172.16.0.5
```

**Wejście:**

```
adresy_ip.txt
```

**Wyjście:**

```
10.0.0.1
172.16.0.5
192.168.1.2
192.168.1.10
```

### Uwagi

* Wygodnie jest sortować z kluczem: `sorted(adresy, key=...)`, gdzie klucz zamienia adres na krotkę czterech liczb całkowitych.

---

## ZAD-06 — Statystyki pliku tekstowego

**Poziom:** ★★☆
**Tagi:** `files`, `stats`, `dict`

### Treść

Wczytaj ścieżkę pliku tekstowego i oblicz:

1. liczbę wierszy,
2. łączną liczbę słów,
3. średnią długość wiersza (w znakach),
4. średnią liczbę słów w wierszu,
5. ile razy występuje każde słowo.

Definicje:

* **Wiersze** to fragmenty tekstu rozdzielone znakami nowej linii. Znak nowej linii na samym końcu pliku nie tworzy dodatkowego, pustego wiersza (tak działa `str.splitlines()`), ale puste wiersze w środku pliku się liczą.
* **Długość wiersza** to liczba jego znaków (bez znaku nowej linii), łącznie ze spacjami i interpunkcją.
* **Słowo** to najdłuższy ciąg kolejnych liter (także polskich). Wszystkie inne znaki — spacje, cyfry, interpunkcja, myślniki — rozdzielają słowa, np. `Mark-up 2024r.` zawiera słowa `Mark`, `up` i `r`.
* Licząc wystąpienia, nie rozróżniaj wielkości liter: `Ala` i `ala` to to samo słowo.

### Wejście

* 1. linia: ścieżka pliku

### Wyjście

* 1. linia: liczba wierszy,
* 2. linia: liczba słów,
* 3. linia: średnia długość wiersza z dokładnie 2 miejscami po przecinku,
* 4. linia: średnia liczba słów w wierszu z dokładnie 2 miejscami po przecinku,
* dalej: dla każdego różnego słowa jedna linia `słowo: liczba` — słowo małymi literami, w kolejności pierwszego wystąpienia w pliku. Jeśli plik nie zawiera słów, ta część jest pusta.

Przypadki szczególne (wypisz tylko komunikat):

* `Plik jest pusty.` — jeśli plik nie zawiera żadnego znaku,
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Przykład

**Pliki przed:**

```
tekst.txt
| Ala ma kota.
| Kot ma na imię Filemon.
| Filemon lubi mleko, Ala lubi
| kota Filemona!
```

**Wejście:**

```
tekst.txt
```

**Wyjście:**

```
4
15
19.25
3.75
ala: 2
ma: 2
kota: 2
kot: 1
na: 1
imię: 1
filemon: 2
lubi: 2
mleko: 1
filemona: 1
```

Wiersze mają 12, 23, 28 i 14 znaków, więc średnia długość to $\frac{77}{4} = 19.25$, a średnia liczba słów to $\frac{15}{4} = 3.75$.

### Uwagi

* Słowa łatwo wyodrębnić, zamieniając każdy znak, który nie jest literą (`znak.isalpha()`), na spację, a potem dzieląc wiersz metodą `split()`.
* Słownik w Pythonie pamięta kolejność dodawania kluczy.

---

## ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Wczytaj ścieżkę pliku tekstowego i wiersz tekstu. Dopisz ten wiersz na **początku** pliku — jako nowy, pierwszy wiersz. Dotychczasowa treść pliku ma pozostać bez zmian pod nowym wierszem. Pusty plik po zmianie zawiera tylko nowy wiersz.

### Wejście

* 1. linia: ścieżka pliku
* 2. linia: wiersz do dodania (może zawierać spacje)

### Wyjście

* Gdy plik istnieje — nic (wynikiem jest zmieniony plik).
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku. Wtedy nie twórz żadnego pliku.

### Przykład

**Pliki przed:**

```
notatki.txt
| kupić mleko
| zadzwonić do babci
```

**Wejście:**

```
notatki.txt
TODO:
```

**Wyjście:** *(brak)*

**Pliki po:**

```
notatki.txt
| TODO:
| kupić mleko
| zadzwonić do babci
```

### Przykład 2

**Pliki przed:** *(brak)*

**Wejście:**

```
notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**

```
Plik nie istnieje.
```

**Pliki po:**

```
notatki.txt (usunięty)
```

Pliku nie było, więc program niczego nie tworzy.

### Uwagi

* Do pliku nie da się „dopisać na początku” — wczytaj całą treść, a potem zapisz plik od nowa: najpierw nowy wiersz, potem starą treść.

---

## ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `recursive`, `txt`, `csv`

### Treść

Wczytaj ścieżkę folderu i inicjały (np. `A.D.`). W tym folderze **i wszystkich jego podfolderach**:

a) do każdego pliku `.txt` dopisz inicjały jako nowy, **ostatni wiersz**,

b) z każdego pliku `.csv` usuń **środkowy wiersz** — gdy liczba wierszy jest parzysta, usuń **dolny** z dwóch środkowych.

Pozostałych plików nie zmieniaj. Na koniec wypisz ścieżki wszystkich zmienionych plików.

Szczegóły:

* Wiersze liczymy jak w `str.splitlines()`: znak nowej linii na końcu pliku nie tworzy dodatkowego, pustego wiersza.
* Inicjały trafiają bezpośrednio pod dotychczasowy ostatni wiersz, bez pustego wiersza pomiędzy — także wtedy, gdy plik nie kończy się znakiem nowej linii. Pusty plik `.txt` po zmianie zawiera tylko inicjały.
* W pliku `.csv` o $n$ wierszach usuwamy wiersz numer $\lfloor n/2 \rfloor + 1$ (licząc od 1): przy 3 wierszach — 2., przy 4 — 3., przy 1 — jedyny wiersz.

### Wejście

* 1. linia: ścieżka folderu
* 2. linia: inicjały

### Wyjście

* Ścieżki zmienionych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli nie ma żadnego pliku `.txt` ani `.csv`.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Ograniczenia

* Każdy plik `.csv` ma co najmniej jeden wiersz.

### Przykład

**Pliki przed:**

```
projekt/opis.txt
| Projekt X
projekt/dane.csv
| a,1
| b,2
| c,3
projekt/main.py
| print("Projekt X")
projekt/2024/raport.txt
| Raport roczny
projekt/2024/wyniki.csv
| x,1
| y,2
| z,3
| w,4
```

**Wejście:**

```
projekt
A.D.
```

**Wyjście:**

```
2024/raport.txt
2024/wyniki.csv
dane.csv
opis.txt
```

**Pliki po:**

```
projekt/opis.txt
| Projekt X
| A.D.
projekt/dane.csv
| a,1
| c,3
projekt/main.py
| print("Projekt X")
projekt/2024/raport.txt
| Raport roczny
| A.D.
projekt/2024/wyniki.csv
| x,1
| y,2
| w,4
```

`dane.csv` ma 3 wiersze, więc traci 2. wiersz; `wyniki.csv` ma 4 wiersze, więc traci 3. wiersz. Plik `main.py` się nie zmienia.

### Uwagi

* Najpierw zbierz listę wszystkich plików (np. `sorted(Path(folder).rglob("*"))`), a dopiero potem je zmieniaj.

---

## ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Wczytaj ścieżkę folderu. Usuń wszystkie pliki większe niż **10 kB**, czyli o rozmiarze **większym niż 10240 bajtów**, z tego folderu **i wszystkich jego podfolderów**. Pliki o rozmiarze dokładnie 10240 bajtów zostają. Foldery zostają, nawet jeśli staną się puste.

Rozmiar to liczba bajtów na dysku, a nie liczba znaków w pliku — w kodowaniu UTF-8 litera `ą` zajmuje 2 bajty.

### Wejście

* 1. linia: ścieżka folderu

### Wyjście

* Ścieżki usuniętych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli żaden plik nie został usunięty.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
pobrane/film.mp4 (rozmiar: 50000 B)
pobrane/notatka.txt (rozmiar: 300 B)
pobrane/obrazy/duże.png (rozmiar: 10241 B)
pobrane/obrazy/ikona.png (rozmiar: 10240 B)
```

**Wejście:**

```
pobrane
```

**Wyjście:**

```
film.mp4
obrazy/duże.png
```

**Pliki po:**

```
pobrane/film.mp4 (usunięty)
pobrane/notatka.txt (rozmiar: 300 B)
pobrane/obrazy/duże.png (usunięty)
pobrane/obrazy/ikona.png (rozmiar: 10240 B)
```

`ikona.png` ma dokładnie 10240 bajtów, więc zostaje.

### Uwagi

* Rozmiar pliku w bajtach zwraca `os.path.getsize()` albo `Path.stat().st_size`, a plik usuwa `os.remove()` albo `Path.unlink()`.

---

## ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)

**Poziom:** ★☆☆
**Tagi:** `files`, `copy`, `png`, `shutil`

### Treść

Wczytaj ścieżkę folderu źródłowego i docelowego. Skopiuj do folderu docelowego wszystkie pliki z rozszerzeniem `.png` (bez względu na wielkość liter), które leżą **bezpośrednio** w folderze źródłowym. Pliki w podfolderach pomiń.

* Pliki w folderze źródłowym zostają na miejscu.
* Jeśli folder docelowy nie istnieje, utwórz go (razem z brakującymi folderami nadrzędnymi). Gdy nie ma czego kopiować, nie ma znaczenia, czy go utworzysz.
* Jeśli w folderze docelowym jest już plik o tej samej nazwie, nadpisz go.

### Wejście

* 1. linia: ścieżka folderu źródłowego
* 2. linia: ścieżka folderu docelowego

### Wyjście

* Nazwy skopiowanych plików, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli w folderze źródłowym nie ma żadnego pliku `.png`.
* `Folder nie istnieje.` — jeśli folder źródłowy nie istnieje. Wtedy niczego nie twórz.

### Przykład

**Pliki przed:**

```
obrazy/kot.png
| (obraz kota)
obrazy/pies.PNG
| (obraz psa)
obrazy/opis.txt
| Zdjęcia zwierząt
obrazy/wakacje/morze.png
| (obraz morza)
```

**Wejście:**

```
obrazy
kopia/obrazy
```

**Wyjście:**

```
kot.png
pies.PNG
```

**Pliki po:**

```
kopia/obrazy/kot.png
| (obraz kota)
kopia/obrazy/pies.PNG
| (obraz psa)
kopia/obrazy/opis.txt (usunięty)
kopia/obrazy/morze.png (usunięty)
obrazy/kot.png
| (obraz kota)
obrazy/pies.PNG
| (obraz psa)
```

Program utworzył folder `kopia/obrazy`. Pliku `wakacje/morze.png` nie kopiujemy, bo leży w podfolderze.

### Uwagi

* Kopiowanie: `shutil.copy(zrodlo, cel)`. Folder razem z folderami nadrzędnymi tworzy `os.makedirs(sciezka, exist_ok=True)`.

---

## ZAD-11 — Zamień miejscami treści dwóch plików

**Poziom:** ★★☆
**Tagi:** `files`, `swap`, `read/write`

### Treść

Wczytaj ścieżki dwóch plików A i B. Zamień ich treści miejscami:

* plik A ma mieć dawną treść pliku B,
* plik B ma mieć dawną treść pliku A.

Nazwy plików się nie zmieniają. Jeśli obie ścieżki są takie same, plik pozostaje bez zmian.

### Wejście

* 1. linia: ścieżka pliku A
* 2. linia: ścieżka pliku B

### Wyjście

* Gdy oba pliki istnieją — nic (wynikiem są zmienione pliki).
* `Plik nie istnieje.` — jeśli którakolwiek ścieżka nie wskazuje istniejącego pliku. Wtedy niczego nie zmieniaj i nie twórz.

### Przykład

**Pliki przed:**

```
plik1.txt
| Ala ma kota
dane/plik2.txt
| Kot ma Alę
| i mysz.
```

**Wejście:**

```
plik1.txt
dane/plik2.txt
```

**Wyjście:** *(brak)*

**Pliki po:**

```
plik1.txt
| Kot ma Alę
| i mysz.
dane/plik2.txt
| Ala ma kota
```

### Przykład 2

**Pliki przed:**

```
plik1.txt
| Ala ma kota
```

**Wejście:**

```
plik1.txt
plik2.txt
```

**Wyjście:**

```
Plik nie istnieje.
```

**Pliki po:**

```
plik1.txt
| Ala ma kota
plik2.txt (usunięty)
```

### Uwagi

* Najprościej wczytać obie treści do zmiennych, a dopiero potem zapisać każdy plik od nowa.

---

## ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `move`, `csv`, `recursive`

### Treść

Wczytaj ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki z rozszerzeniem `.csv` (bez względu na wielkość liter) z folderu źródłowego **i wszystkich jego podfolderów** bezpośrednio do folderu docelowego, zachowując ich nazwy.

* Po przeniesieniu pliku nie ma już w starym miejscu. Foldery zostają, nawet jeśli staną się puste.
* Jeśli folder docelowy nie istnieje, utwórz go (razem z brakującymi folderami nadrzędnymi). Gdy nie ma czego przenosić, nie ma znaczenia, czy go utworzysz.

### Wejście

* 1. linia: ścieżka folderu źródłowego
* 2. linia: ścieżka folderu docelowego

### Wyjście

* Dawne ścieżki przeniesionych plików względem folderu źródłowego, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli nie ma żadnego pliku `.csv`.
* `Folder nie istnieje.` — jeśli folder źródłowy nie istnieje. Wtedy niczego nie twórz.

### Ograniczenia

* Nazwy plików `.csv` w całym folderze źródłowym są różne, a w folderze docelowym nie ma plików o takich nazwach.
* Folder docelowy nie leży wewnątrz folderu źródłowego.

### Przykład

**Pliki przed:**

```
projekt/dane.csv
| id,wartość
| 1,10
projekt/opis.txt
| Dane sprzedaży
projekt/2023/styczeń.csv
| 1,120
projekt/2023/q1/luty.CSV
| 2,95
```

**Wejście:**

```
projekt
wyniki/csv
```

**Wyjście:**

```
2023/q1/luty.CSV
2023/styczeń.csv
dane.csv
```

**Pliki po:**

```
wyniki/csv/dane.csv
| id,wartość
| 1,10
wyniki/csv/styczeń.csv
| 1,120
wyniki/csv/luty.CSV
| 2,95
projekt/dane.csv (usunięty)
projekt/2023/styczeń.csv (usunięty)
projekt/2023/q1/luty.CSV (usunięty)
projekt/opis.txt
| Dane sprzedaży
```

Program utworzył folder `wyniki/csv` i przeniósł do niego trzy pliki; `opis.txt` został na miejscu.

### Uwagi

* Plik przenosi `shutil.move(zrodlo, cel)` albo `Path.rename(cel)`.

---

## ZAD-13 — Raport z pliku CSV

**Poziom:** ★★☆
**Tagi:** `files`, `csv`, `dict`

### Treść

Wczytaj ścieżkę pliku CSV z ocenami uczniów. Pierwszy wiersz pliku to nagłówek `imie,przedmiot,ocena`, a każdy kolejny wiersz opisuje jedną ocenę: imię ucznia, przedmiot i ocenę. Pola są oddzielone przecinkami, a pole zawierające przecinek jest ujęte w cudzysłów, np. `Adam,"WOS, rozszerzony",5`.

Dla każdego ucznia oblicz średnią wszystkich jego ocen (ze wszystkich przedmiotów razem) i wypisz wyniki uczniów w kolejności alfabetycznej imion.

### Wejście

* 1. linia: ścieżka pliku CSV

### Wyjście

* Dla każdego ucznia jedna linia `imię: średnia`, średnia z dokładnie 2 miejscami po przecinku. Uczniowie posortowani rosnąco po imieniu (tak jak sortuje `sorted()`).
* `Brak danych.` — jeśli plik zawiera tylko nagłówek.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Oceny to liczby od 1 do 6, całkowite albo z kropką dziesiętną (np. `4.5`).
* Plik nie zawiera pustych wierszy. Imiona porównujemy dokładnie — wielkość liter ma znaczenie.

### Przykład

**Pliki przed:**

```
oceny.csv
| imie,przedmiot,ocena
| Ola,matematyka,5
| Jan,fizyka,3
| Ola,"WOS, rozszerzony",4
| Jan,matematyka,4
| Ewa,historia,6
```

**Wejście:**

```
oceny.csv
```

**Wyjście:**

```
Ewa: 6.00
Jan: 3.50
Ola: 4.50
```

Ola ma oceny 5 i 4, więc jej średnia to $\frac{5 + 4}{2} = 4.5$.

### Uwagi

* Moduł `csv` dzieli wiersze na pola za Ciebie i poprawnie obsługuje cudzysłowy — zwykłe `split(",")` rozbiłoby `"WOS, rozszerzony"` na dwa pola. `csv.DictReader` pomija nagłówek i zwraca każdy kolejny wiersz jako słownik `{nazwa kolumny: wartość}`:

```python
import csv

with open("oceny.csv", encoding="utf-8", newline="") as plik:
    for wiersz in csv.DictReader(plik):
        print(wiersz["imie"], wiersz["przedmiot"], wiersz["ocena"])
```

* Wartości z pliku CSV są napisami — ocenę zamień na liczbę przez `float()`. Sumy i liczby ocen zbieraj w słownikach, których kluczem jest imię.

---

## ZAD-14 — Edycja konfiguracji JSON

**Poziom:** ★★☆
**Tagi:** `files`, `json`, `dict`

### Treść

Plik konfiguracyjny w formacie JSON zawiera obiekt (w Pythonie: słownik), w którym mogą być zagnieżdżone kolejne obiekty. Wczytaj ścieżkę pliku, klucz i nową wartość. Klucz jest zapisany w **notacji kropkowej**: `baza.port` oznacza klucz `port` wewnątrz obiektu zapisanego pod kluczem `baza`.

Klucz **istnieje**, jeśli każda jego część poza ostatnią prowadzi do obiektu, a ostatnia część jest kluczem w tym obiekcie. Jeśli klucz istnieje:

1. wypisz jego dotychczasową wartość,
2. ustaw nową wartość — jako **liczbę całkowitą**, jeśli wczytany napis składa się z samych cyfr, ewentualnie poprzedzonych znakiem `-` (np. `8080`, `-5`); w przeciwnym razie jako **napis** (np. `3.5`, `true`, `localhost`),
3. zapisz cały plik od nowa poleceniem `json.dump(dane, plik, indent=2, ensure_ascii=False)`.

Dzięki takiemu zapisowi plik ma wcięcia po 2 spacje, klucze zostają w dotychczasowej kolejności, a polskie litery nie są zamieniane na kody `\u…`. Sprawdzarka porównuje plik po zmianie dokładnie z tym formatem (ignoruje tylko końcowe spacje i puste wiersze).

### Wejście

* 1. linia: ścieżka pliku
* 2. linia: klucz w notacji kropkowej
* 3. linia: nowa wartość

### Wyjście

* Dotychczasowa wartość klucza: napis bez cudzysłowów, liczba jako liczba.
* `Brak klucza: K` — gdzie `K` to wczytany klucz — jeśli klucz nie istnieje. Plik pozostaje wtedy bez zmian.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku.

### Ograniczenia

* Plik zawiera poprawny JSON, którego główną wartością jest obiekt.
* Wartość pod istniejącym kluczem jest napisem albo liczbą całkowitą. Pozostałe wartości w pliku mogą być dowolne (listy, `true`, `null` …).
* Części klucza nie zawierają kropek.

### Przykład

**Pliki przed:**

```
config.json
| {
|   "nazwa": "Sklep",
|   "baza": {
|     "host": "localhost",
|     "port": 5432
|   },
|   "wersja": "1.0"
| }
```

**Wejście:**

```
config.json
baza.port
6543
```

**Wyjście:**

```
5432
```

**Pliki po:**

```
config.json
| {
|   "nazwa": "Sklep",
|   "baza": {
|     "host": "localhost",
|     "port": 6543
|   },
|   "wersja": "1.0"
| }
```

### Przykład 2

**Pliki przed:**

```
config.json
| {"nazwa": "Sklep", "baza": {"host": "localhost"}}
```

**Wejście:**

```
config.json
baza.port
6543
```

**Wyjście:**

```
Brak klucza: baza.port
```

**Pliki po:**

```
config.json
| {"nazwa": "Sklep", "baza": {"host": "localhost"}}
```

W obiekcie `baza` nie ma klucza `port`, więc plik się nie zmienia.

### Uwagi

* Moduł `json` zamienia tekst JSON na słowniki, listy, napisy i liczby Pythona i z powrotem:

```python
import json

with open("config.json", encoding="utf-8") as plik:
    dane = json.load(plik)          # np. {"baza": {"port": 5432}}

dane["baza"]["port"] = 6543

with open("config.json", "w", encoding="utf-8") as plik:
    json.dump(dane, plik, indent=2, ensure_ascii=False)
```

* Do zagnieżdżonego obiektu dojdziesz pętlą po `klucz.split(".")`: w każdym kroku sprawdź, czy bieżąca wartość jest słownikiem (`isinstance(obiekt, dict)`) i czy zawiera kolejną część klucza.

---

## ZAD-15 — Liczba wierszy z obsługą błędów

**Poziom:** ★☆☆
**Tagi:** `files`, `exceptions`, `try/except`

### Treść

Wczytaj `k` ścieżek. Dla każdej z nich wypisz w osobnej linii:

* liczbę wierszy pliku — jeśli ścieżka wskazuje istniejący plik,
* `To jest folder: X` — jeśli ścieżka wskazuje folder,
* `Brak pliku: X` — jeśli pod ścieżką nic nie ma,

gdzie `X` to ścieżka dokładnie w takiej postaci, w jakiej ją wczytano.

Wiersze liczymy jak w `str.splitlines()`: pusty plik ma 0 wierszy, a znak nowej linii na końcu pliku nie tworzy dodatkowego wiersza.

Rozwiąż zadanie w stylu „najpierw spróbuj, potem obsłuż błąd”: otwórz plik w bloku `try` i przechwyć wyjątki zgłaszane przez `open()` (zob. Uwagi).

### Wejście

* 1. linia: `k` — liczba ścieżek
* kolejne `k` linii: ścieżki

### Wyjście

`k` linii — wynik dla każdej ścieżki, w kolejności wczytywania.

### Ograniczenia

* $1 \le k \le 20$
* Żadna ścieżka nie prowadzi „przez” plik (np. `notatki.txt/a`).

### Przykład

**Pliki przed:**

```
notatki.txt
| kupić mleko
| zadzwonić do babci
dane/
```

**Wejście:**

```
3
notatki.txt
dane
raport.txt
```

**Wyjście:**

```
2
To jest folder: dane
Brak pliku: raport.txt
```

### Uwagi

* Gdy coś pójdzie nie tak, `open()` zgłasza **wyjątek**: `FileNotFoundError`, gdy pliku nie ma, i `IsADirectoryError`, gdy ścieżka wskazuje folder (na Windowsie zamiast niego pojawia się `PermissionError`). Wyjątek przechwytuje blok `try`/`except`:

```python
try:
    with open(sciezka, encoding="utf-8") as plik:
        tresc = plik.read()
except FileNotFoundError:
    print("Brak pliku:", sciezka)
```

* W ZAD-01 najpierw sprawdzaliśmy, co jest pod ścieżką (`os.path.isfile()`), a dopiero potem działaliśmy — to styl LBYL („patrz, zanim skoczysz”). Tutaj od razu próbujemy otworzyć plik i obsługujemy ewentualny błąd — to styl EAFP („łatwiej prosić o wybaczenie niż o pozwolenie”), typowy dla Pythona. Jest odporny na sytuację, w której plik zniknie między sprawdzeniem a otwarciem.
