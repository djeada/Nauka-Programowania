# Tytul: Konwersja jednostek.
# Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z nastepujacymi instrukcjami:
# a) Pobierz wielkosc w kilogramach i wypisz, ile gramow odpowiada.
# b) Pobierz wielkosc w calach i wypisz, ile centymetrow odpowiada.
# c) Pobierz liczbe sekund i przelicz na godziny.
# d) Pobierz liczbe w euro i wypisz, ile zlotowek odpowiada.
# e) Pobierz miare kata w stopniach i wypisz, ile radianow odpowiada.
# f) Pobierz temperature w stopniach Fahrenheita i wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada.
# Dane wejsciowe: Liczba naturalna we wszystkich podpunktach.
# Dane wyjsciowe:
# * Liczba naturalna dla podpunktow 1 i 3.
# * Liczba zmiennoprzecinkowa dla pozostalych podpunktow.
# Przyklad:
# a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.
# b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.
# c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.
# d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.
# e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.
# f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.

main() {

    echo "Podaj liczbe kg: "
    read kg

    echo "$kg kg to  $(($kg * 1000)) g"

    echo "Podaj liczbe cali: "
    read cal

    echo "$cal cali to  $(bc -l <<< $cal/2.54) cm"

    echo "Podaj liczbe sekund: "
    read s

    echo "$s s to  $(($kg / 3600)) h"

    echo "Podaj liczbe euro: "
    read stopnie
    rad=$(echo "$stopnie*0.0174532" | bc)

    echo "$stopnie stopni to $rad radianow"

    echo "Podaj temperature w Fahrenheitach "
    read F

    C=$((($F - 32) * 5 / 9))
    K=$(($C - 273))

    echo "$F to Farenheitow to $C C i $K K"
}

main "$@"

