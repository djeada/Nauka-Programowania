# Tytul: Odwroc slowa w zdaniu.
# Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "ala mak otak".

wypisz_dane() {
    IFS='; ' read -ra wynik <<< "$1"
    echo "Imie: ${wynik[0]}"
    echo "Nazwisko: ${wynik[1]}"
    echo "Miejsce urodzenia: ${wynik[2]}"
    echo "Zawod: ${wynik[3]}"
    echo "Zarobki: ${wynik[4]}"
}

main() {
    local napis="Jan; Kowalski; Warszawa; Programista; 1000"
    wypisz_dane "$napis"
}

main "$@"

