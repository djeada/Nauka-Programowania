## Wyrażenia regularne

### Zad 1.  (★★☆)
Tytuł: Sprawdź poprawność adresu e-mail.

Treść: Masz napis reprezentujący adres e-mail. Sprawdź, czy jest on poprawny.

Pamiętaj, że każdy adres e-mail składa się z identyfikatora użytkownika, znaku @ oraz nazwy domenowej.

Identyfikator użytkownika składa się tylko z:

* Małych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Znaków ! # $ % & ' * + — / = ? ^ _ ` { | } ~.
* Kropek . pod warunkiem, że nie jest pierwszym lub ostatnim znakiem i nie występuje dwukrotnie po sobie.

Nazwa domenowa składa się tylko z:

* Małych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Kropek . oraz myślnika — pod warunkiem, że nie są pierwszym lub ostatnim znakiem i nie występują dwukrotnie po sobie.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “adam@gmail.com”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 2.  (★★☆)

Tytuł: Sprawdź poprawność hasła.

Treść: Masz napis reprezentujący hasło. Sprawdź, czy hasło spełnia następujące warunki:

1. Hasło musi zawierać przynajmniej jedną małą literę [a-z].
2. Hasło musi zawierać przynajmniej jedną dużą literę [A-Z].
3. Hasło musi zawierać przynajmniej jedną cyfrę [0-9].
4. Hasło musi zawierać przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
5. Minimalna długość hasła to 8 znaków.
6. Maksymalna długość hasła to 20 znaków.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “abc1234”, powinna zostać zwrócona wartość logiczna: Fałsz.

### Zad 3.  (★☆☆)

Tytuł: Czy napis składa się wyłącznie z cyfr?

Treść: Masz napis. Sprawdź, czy składa się on wyłącznie z cyfr.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “1234”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 4.  (★☆☆)

Tytuł: Sprawdź czy słowo występuje w zdaniu.

Treść: Dostajesz dwa napisy. Sprawdź, czy drugi napis występuje w pierwszym jako pojedyncze słowo.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisów: “Siała baba mak.” oraz “babcia”, powinna zostać zwrócona wartość logiczna: Fałsz.

### Zad 5. (★☆☆)

Tytuł: Wyodrębnij cyfry z tekstu.

Treść: Dostajesz napis. Zwróć napis składający się z cyfr występujących w tym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu: “Terminator2001”, powinien zostać zwrócony napis: “2001”.

### Zad 6. (★☆☆)

Tytuł: Wiersze kończące się określonym napisem.

Treść: Dostajesz dwa napisy. Znajdź wiersze w pierwszym napisie kończące się drugim napisem. Wiersz może być zakończony dowolnym znakiem interpunkcyjnym.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisów:

> Folgujmy paniom nie sobie, ma rada;
  Milujmy wiernie nie jest w nich przysada.
  Godności trzeba nie za nic tu cnota,
  Miłości pragną nie pragną tu złota.

oraz

> da

powinna zostać zwrócona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

### Zad 7. (★☆☆)

ytuł: Podziel tekst względem znaków interpunkcyjnych.

Treść: Dostajesz napis. Podziel go względem znaków interpunkcyjnych i zapisz w liście. Usuń spacje występujące na początku lub końcu otrzymanych napisów.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisu: “Ani nie poszedł do kina, ani nie wybrał się do teatru.”, powinna zostać zwrócona lista: [“Ani nie poszedł do kina”, “ani nie wybrał się do teatru”].

### Zad 8. (★★☆)

Tytuł: Cyfry w słowach.

Treść: Dostajesz napis reprezentujący zdanie. Zapisz w liście cyfry, które są częścią słów. Cyfry oddzielone od liter spacją powinny zostać pominięte.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: "Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego", powinna zostać zwrócona lista: ["29", "37", "3891", "3"].

### Zad 9. (★★☆)

Tytuł: Usuń fragment napisu.

Treść: Dostajesz dwa napisy. Pierwszy napis to tekst, a drugi to słowo, które należy usunąć z tekstu. Jeśli w tekście znajduje się słowo do usunięcia, usuń całą część tekstu od słowa do końca. Zwróć zmodyfikowany tekst.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Napis.

Przykład:
Dla podanych napisów:

> Turned it up should no valley cousin he.
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

oraz słowa "a", powinien zostać zwrócony napis:

> Turned it up should no v
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
    
### Zad 10.  (★★☆)

Tytuł: Podmień napisy z listy A na napisy z listy B.

Treść: Dostajesz napis oraz dwie listy napisów. Zastąp napisy z pierwszej listy w pierwszym napisie odpowiadającymi im napisami z drugiej listy.

Dane wejściowe: Napis oraz dwie listy napisów.

Dane wyjściowe: Napis.

Przykład:

Dla podanych danych:

> 'Every mile was tilted at seven or.
  Wished her entire esteem mr oh by.
  He prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on be.
  Warmth his law design says he is a person.
  Pronunciation suspected in belonging conveying ye repulsive.

oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinien zostać zwrócony napis:

> Every mile was tilted at seven and.
  Wished her entire esteem mr oh by.
  She prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on and off.
  Warmth his law design says she is a person.
  Pronunciation suspected in belonging conveying ye repulsive.

### Zad 11.  (★★☆)

Tytuł: Nazwa pliku bez rozszerzenia.

Treść: Otrzymujesz napis reprezentujący ścieżkę pliku. Odfiltruj z niego nazwę pliku wraz z rozszerzeniem. Zwróć samą nazwę pliku bez rozszerzenia.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu "C:\my-long\path_directory\file.html", powinna zostać zwrócona nazwa pliku bez rozszerzenia "file".
