## Wyrażenia regularne

### Zad 1.  (★★☆)

Tytuł: Sprawdź poprawność adresu e-mail.

Treść: Otrzymujesz napis reprezentujący adres e-mail. Sprawdź jego poprawność.
Pamiętaj, że każdy adres e-mail składa się z identyfikatora użytkownika, znaku @ oraz nazwy domenowej.

Identyfikator użytkownika składa się jedynie z:
Małych (a-z) i wielkich (A-Z) liter.
Cyfr (0-9).
Znaków  ```! # $ % & ' * + — / = ? ^ _ ` { | } ~```.
Kropki `.` pod warunkiem, że nie jest pierwszym bądź ostatnim znakiem i nie występuje dwukrotnie po sobie.

Nazwa domenowa składa się jedynie z:
Małych (a-z) i wielkich (A-Z) liter.
Cyfr (0-9).
Kropki `.` oraz myślnika — pod warunkiem, że nie są pierwszym bądź ostatnim znakiem i nie występują dwukrotnie po sobie.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “adam@gmail.com”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 2.  (★★☆)

Tytuł: Sprawdź poprawność hasła.

Treść: Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia następujące warunki:
1. Hasło musi zawierać przynajmniej jedną małą literę [a-z].
2. Hasło musi zawierać przynajmniej jedną dużą literę [A-Z].
3. Hasło musi zawierać przynajmniej jedną cyfrę [0-9].
4. Hasło musi zawierać przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
5. Minimalna długość hasła to 8 znaków.
6. Maksymalna długość hasła to 20 znaków.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.


Przykład:

Dla otrzymanego napisu: “abc1234”, powinna zostać zwrócona wartość logiczna: Fałsz.

### Zad 3.  (★☆☆)

Tytuł: Czy napis składa się wyłącznie z cyfr?

Treść: Otrzymujesz napis. Sprawdź, czy napis składa się wyłącznie z cyfr.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “1234”, powinna zostać zwrócona wartość logiczna: Prawda.

### Zad 4.  (★☆☆)

Tytuł: Czy słowo należy do zdania?

Treść: Otrzymujesz dwa napisy. Sprawdź, czy drugi napis występuje w pierwszym napisie.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanych napisów: “Siala baba mak.” oraz “babcia”, powinna zostać zwrócona wartość logiczna: Fałsz.

### Zad 5. (★☆☆)

Tytuł: Odfiltruj cyfry z tekstu.

Treść: Otrzymujesz napis. Zwróć napis składający się z cyfr występujących w otrzymanym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: “Terminator2001”, powinien zostać zwrócony napis: “2001”.

### Zad 6. (★☆☆)

Tytuł: Wiersze kończące się napisem.

Treść: Otrzymujesz dwa napisy. Znajdź wiersze w pierwszym napisie kończące się drugim napisem. Wiersz może być zakończony dowolnym znakiem interpunkcyjnym.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanych napisów:

> Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota.

oraz 

> da 

powinna zostać zwrócona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

### Zad 7. (★☆☆)

Tytuł: Podziel względem znaków interpunkcyjnych.

Treść: Otrzymujesz napis. Podziel go względem znaków interpunkcyjnych i zapisz w liście. Usuń spacje występujące na początku lub końcu otrzymanych napisów.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostać zwrócona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

### Zad 8. (★★☆)

Tytuł: Cyfry będące częścią słów.

Treść: Otrzymujesz napis reprezentujący zdanie. Zapisz w liście cyfry będące częścią słów. Cyfry odseparowane od liter spacjami pomiń.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go”, powinna zostać zwrócona lista: [“29”, “37”, “3891”, “3”].

### Zad 9. (★★☆)

Tytuł: Usuń część wiersza. 

Treść: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje tekst, a drugi zakazane słowo. Jeśli w danym wierszu tekstu występuje zakazane słowo, to usuń część wiersza od wystąpienia zakazanego słowa do końca. Zwróć zmodyfikowany tekst.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Napis.

Przykład:
Dla otrzymanych napisów:

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

oraz napisu “a”, powinien zostać zwrócony napis:
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

Treść: Otrzymujesz napis i dwie listy napisów. Podmień w pierwszym napisie, napisy z pierwszej listy na odpowiadające im napisy z drugiej listy.

Dane wejściowe: Napis oraz dwie listy napisów.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanych danych:

> 'Every mile was tilted at seven or. 
Wished her entire esteem mr oh by.
He prevents requests by if in pleased. 
Picture too and concerned was comforting. 
Ten difficult resembled eagerness nor. 
Same park bore on be. 
Warmth his law design says he is a person. 
Pronunciation suspected in belonging conveying ye repulsive.

oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinniśmy otrzymać:

> Every mile was tilted at seven and. 
Wished her entire esteem mr oh by.
She prevents requests by if in pleased. 
Picture too and concerned was comforting. 
Ten difficult resembled eagerness nor. 
Same park bore on and off. 
Warmth his law design says she is a person. 
Pronunciation suspected in belonging conveying ye repulsive.

### Zad 11.  (★★☆)

Tytuł: Nazwa pliku ze ścieżki.

Treść: Otrzymujesz napis reprezentujący ścieżkę pliku. Odfiltruj nazwę pliku ze ścieżki. Zwróć samą nazwę pliku, bez rozszerzeń.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: “C:\\my-long\\path_directory\\file.html”, powinien zostać zwrócony napis: “file.html”.
