# Wyrażenia regularne

## Zadanie 1 - Sprawdź poprawność adresu e-mail

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący adres e-mail. Twoim zadaniem jest sprawdzić, czy jest to poprawny adres e-mail zgodnie z następującymi regułami:

- Adres e-mail składa się z identyfikatora użytkownika, znaku `@` oraz nazwy domeny.

- **Identyfikator użytkownika** może zawierać wyłącznie:

  - Małe (a–z) i wielkie (A–Z) litery.
  - Cyfry (0–9).
  - Znaki specjalne: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
  - Kropki `.`, pod warunkiem że nie są pierwszym ani ostatnim znakiem oraz nie występują dwukrotnie po sobie.

- **Nazwa domeny** może zawierać wyłącznie:

  - Małe (a–z) i wielkie (A–Z) litery.
  - Cyfry (0–9).
  - Kropki `.` oraz myślniki `-`, pod warunkiem że nie są pierwszym ani ostatnim znakiem oraz nie występują dwukrotnie po sobie.

### Dane wejściowe

- Jeden napis reprezentujący adres e-mail.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli adres e-mail jest poprawny.
  - **Fałsz**, jeśli adres e-mail nie jest poprawny.

### Przykład

- **Dane wejściowe**:
  ```
  adam@gmail.com
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Możesz użyć wyrażeń regularnych do sprawdzenia poprawności adresu e-mail według podanych reguł.
- Zwróć uwagę na warunki dotyczące kropek i myślników.

---

## Zadanie 2 - Sprawdź poprawność hasła

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący hasło. Twoim zadaniem jest sprawdzić, czy hasło spełnia wszystkie poniższe warunki:

1. Zawiera co najmniej jedną małą literę [a–z].
2. Zawiera co najmniej jedną wielką literę [A–Z].
3. Zawiera co najmniej jedną cyfrę [0–9].
4. Zawiera co najmniej jeden znak specjalny spośród: `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Dane wejściowe

- Jeden napis reprezentujący hasło.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli hasło spełnia wszystkie powyższe warunki.
  - **Fałsz**, jeśli hasło nie spełnia któregokolwiek z warunków.

### Przykład

- **Dane wejściowe**:
  ```
  abc1234
  ```
- **Oczekiwane wyjście**:
  ```
  Fałsz
  ```

### Wskazówki

- Możesz użyć wyrażeń regularnych, aby sprawdzić obecność poszczególnych typów znaków.
- Upewnij się, że hasło spełnia zarówno wymagania dotyczące zawartości, jak i długości.

---

## Zadanie 3 - Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis. Twoim zadaniem jest sprawdzić, czy napis ten składa się wyłącznie z cyfr (znaków od '0' do '9').

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli napis składa się wyłącznie z cyfr.
  - **Fałsz**, jeśli w napisie występują inne znaki niż cyfry.

### Przykład

- **Dane wejściowe**:
  ```
  1234
  ```
- **Oczekiwane wyjście**:
  ```
  Prawda
  ```

### Wskazówki

- Możesz wykorzystać funkcje lub metody sprawdzające, czy wszystkie znaki w napisie są cyframi.
- Zwróć uwagę na ewentualne białe znaki lub inne niedrukowalne znaki.

---

## Zadanie 4 - Sprawdź, czy słowo występuje w zdaniu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwa napisy:

- Pierwszy napis to zdanie.
- Drugi napis to słowo.

Twoim zadaniem jest sprawdzić, czy drugie słowo występuje w pierwszym napisie jako samodzielne słowo, nie będąc częścią innego wyrazu.

### Dane wejściowe

- Dwa napisy:
  1. Zdanie.
  2. Słowo do wyszukania.

### Dane wyjściowe

- Wartość logiczna:
  - **Prawda**, jeśli słowo występuje w zdaniu jako samodzielne słowo.
  - **Fałsz**, jeśli słowo nie występuje lub jest tylko częścią innego wyrazu.

### Przykład

- **Dane wejściowe**:
  ```
  Siała baba mak.
  babcia
  ```
- **Oczekiwane wyjście**:
  ```
  Fałsz
  ```

### Wskazówki

- Możesz podzielić zdanie na słowa i sprawdzić, czy słowo znajduje się wśród nich.
- Zwróć uwagę na znaki interpunkcyjne i wielkość liter.

---

## Zadanie 5 - Wyodrębnij cyfry z tekstu

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis zawierający różne znaki. Twoim zadaniem jest wyodrębnić wszystkie cyfry z tego napisu i zwrócić je jako nowy napis, zachowując kolejność wystąpień.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Napis składający się wyłącznie z cyfr występujących w napisie wejściowym, w kolejności ich pojawienia się.

### Przykład

- **Dane wejściowe**:
  ```
  Terminator2001
  ```
- **Oczekiwane wyjście**:
  ```
  2001
  ```

### Wskazówki

- Możesz iterować przez znaki napisu i wybierać te, które są cyframi.
- Rozważ użycie funkcji sprawdzającej, czy dany znak jest cyfrą.

---

## Zadanie 6 - Wiersze kończące się określonym napisem

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Tekst zawierający wiele wierszy (linijek).
2. Słowo lub fragment napisu.

Twoim zadaniem jest znaleźć i zwrócić listę wierszy z pierwszego napisu, które kończą się drugim napisem. Wiersze mogą być zakończone dowolnym znakiem interpunkcyjnym.

### Dane wejściowe

- Dwa napisy:
  1. Tekst zawierający kilka wierszy, w których poszukasz dopasowań.
  2. Napis, który ma być na końcu wiersza.

### Dane wyjściowe

- Lista napisów zawierających wiersze, które spełniają warunek.

### Przykład

- **Dane wejściowe**:
  ```
  Folgujmy paniom nie sobie, ma rada;
  Milujmy wiernie nie jest w nich przysada.
  Godności trzeba nie za nic tu cnota,
  Miłości pragną nie pragną tu złota.
  ```
  ```
  da
  ```
- **Oczekiwane wyjście**:
  ```
  ['Folgujmy paniom nie sobie, ma rada;', 'Milujmy wiernie nie jest w nich przysada.']
  ```

### Wskazówki

- Możesz podzielić tekst na wiersze (np. używając znaku nowej linii).
- Dla każdego wiersza sprawdź, czy kończy się podanym napisem, uwzględniając ewentualne znaki interpunkcyjne na końcu.

---

## Zadanie 7 - Podziel tekst względem znaków interpunkcyjnych

**Poziom trudności**: ★☆☆

### Treść zadania

Otrzymujesz napis zawierający zdanie lub kilka zdań. Twoim zadaniem jest podzielić ten napis na fragmenty, rozdzielając go w miejscach występowania znaków interpunkcyjnych (np. przecinek, kropka, wykrzyknik, pytajnik itp.). Po podzieleniu należy usunąć ewentualne spacje znajdujące się na początku lub końcu każdego fragmentu.

### Dane wejściowe

- Jeden napis.

### Dane wyjściowe

- Lista napisów będących fragmentami tekstu po podziale.

### Przykład

- **Dane wejściowe**:
  ```
  Ani nie poszedł do kina, ani nie wybrał się do teatru.
  ```
- **Oczekiwane wyjście**:
  ```
  ['Ani nie poszedł do kina', 'ani nie wybrał się do teatru']
  ```

### Wskazówki

- Możesz użyć wyrażeń regularnych do podziału tekstu na podstawie znaków interpunkcyjnych.
- Zwróć uwagę na usunięcie zbędnych spacji.

---

## Zadanie 8 - Cyfry w słowach

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący zdanie. Twoim zadaniem jest wyodrębnić wszystkie ciągi cyfr, które są częścią słów, czyli są bezpośrednio połączone z literami. Nie należy uwzględniać cyfr, które są oddzielone od liter spacjami.

### Dane wejściowe

- Jeden napis zawierający zdanie.

### Dane wyjściowe

- Lista napisów zawierających ciągi cyfr będących częścią słów, w kolejności ich występowania w tekście.

### Przykład

- **Dane wejściowe**:
  ```
  Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
  ```
- **Oczekiwane wyjście**:
  ```
  ['29', '37', '3', '91']
  ```

### Wskazówki

- Możesz użyć wyrażeń regularnych do wyszukania cyfr w obrębie słów.
- Upewnij się, że cyfry otoczone spacjami nie są brane pod uwagę.

---

## Zadanie 9 - Usuń fragment napisu

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz dwa napisy:

1. Tekst składający się z wielu zdań lub wierszy.
2. Słowo klucz.

Twoim zadaniem jest przeszukać tekst i, jeśli wystąpi w nim słowo klucz, usunąć z tekstu całą część od pierwszego wystąpienia tego słowa aż do końca tekstu. Jeśli słowo klucz nie występuje w tekście, zwróć oryginalny tekst.

### Dane wejściowe

- Dwa napisy:
  1. Tekst do modyfikacji.
  2. Słowo klucz do wyszukania i usunięcia wraz z resztą tekstu.

### Dane wyjściowe

- Napis będący zmodyfikowanym tekstem po usunięciu odpowiedniego fragmentu.

### Przykład

- **Dane wejściowe**:
  ```
  Turned it up should no valley cousin he.
  Speaking numerous ask did horrible packages set.
  Ashamed herself has distant can studied mrs.
  Led therefore its middleton perpetual fulfilled provision frankness.
  Small he drawn after among every three no.
  All having but you edward genius though remark one.
  Rooms oh fully taken by worse do.
  Points afraid but may end law lasted.
  Was out laughter raptures returned outweigh.
  Luckily cheered colonel me do we attacks on highest enabled.
  Tried law yet style child.
  Bore of true of no be deal.
  Frequently sufficient in be unaffected.
  The furnished she concluded depending procuring concealed.
  ```
  ```
  a
  ```
- **Oczekiwane wyjście**:
  ```
  Turned it up should no v
  Spe
  Ash
  Led therefore its middleton perpetu
  Sm
  All h
  Rooms oh fully t
  Points
  W
  Luckily cheered colonel me do we
  Tried l
  Bore of true of no be de
  Frequently sufficient in be un
  The furnished she concluded depending procuring conce.
  ```

### Wskazówki

- Znajdź pierwsze wystąpienie słowa klucz w tekście.
- Usuń wszystko od tego miejsca do końca tekstu.
- Jeśli słowo klucz nie występuje, tekst pozostaje bez zmian.

---

## Zadanie 10 - Podmień napisy z listy A na napisy z listy B

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz:

- Napis zawierający tekst.
- Dwie listy napisów o tej samej długości:
  - Lista A zawierająca napisy do znalezienia w tekście.
  - Lista B zawierająca napisy, które zastąpią odpowiednie napisy z listy A.

Twoim zadaniem jest w tekście zastąpić wszystkie wystąpienia napisów z listy A odpowiadającymi im napisami z listy B. Zastąpienia należy dokonać dla każdego napisu z listy A, używając odpowiednika z listy B o tym samym indeksie.

### Dane wejściowe

- Napis (tekst do modyfikacji).
- Dwie listy napisów (lista A i lista B), każda o takiej samej długości.

### Dane wyjściowe

- Napis będący zmodyfikowanym tekstem po dokonaniu zastąpień.

### Przykład

- **Dane wejściowe**:

  Tekst:
  ```
  Every mile was tilted at seven or.
  Wished her entire esteem mr oh by.
  He prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on be.
  Warmth his law design says he is a person.
  Pronunciation suspected in belonging conveying ye repulsive.
  ```

  Lista A:
  ```
  ['or', 'be', 'he']
  ```

  Lista B:
  ```
  ['and', 'off', 'she']
  ```

- **Oczekiwane wyjście**:
  ```
  Every mile was tilted at seven and.
  Wished her entire esteem mr oh by.
  She prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on and off.
  Warmth his law design says she is a person.
  Pronunciation suspected in belonging conveying ye repulsive.
  ```

### Wskazówki

- Upewnij się, że zastąpisz wszystkie wystąpienia każdego napisu z listy A.
- Zwróć uwagę na to, by nie zmieniać części innych słów (zastąp tylko całe słowa).
- Możesz użyć wyrażeń regularnych do precyzyjnego dopasowania słów.

---

## Zadanie 11 - Nazwa pliku bez rozszerzenia

**Poziom trudności**: ★★☆

### Treść zadania

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku w systemie plików. Twoim zadaniem jest wyodrębnić nazwę pliku (bez ścieżki) i usunąć z niej rozszerzenie. Zwróć samą nazwę pliku bez rozszerzenia.

### Dane wejściowe

- Jeden napis reprezentujący ścieżkę do pliku.

### Dane wyjściowe

- Napis zawierający nazwę pliku bez rozszerzenia.

### Przykład

- **Dane wejściowe**:
  ```
  C:\my-long\path_directory\file.html
  ```
- **Oczekiwane wyjście**:
  ```
  file
  ```

### Wskazówki

- Rozważ, jak rozdzielić ścieżkę na komponenty katalogów i nazwy pliku.
- Pamiętaj, że rozszerzenie pliku to część po ostatniej kropce w nazwie pliku.
- Upewnij się, że działanie będzie poprawne dla ścieżek z różnymi separatorami katalogów (np. `\` lub `/`).
