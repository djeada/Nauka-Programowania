# Tytul: Wyszukanie wszystkich palindromow w zdaniu.
# Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie wszystkich palindromow w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: "Tata zabral kajak na wycieczke i uderzyl sie w oko", powinna zostac zwrocona lista: ["kajak", "i", "w", "oko"].

source ../assert.sh

# Funkcja sprawdzajaca czy slowo jest palindromem
# Zlozonosc czasowa: O(n), gdzie n to dlugosc slowa
# Zlozonosc pamieciowa: O(n)
czy_palindrom() {
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

# Funkcja wypisujaca slowa ze zdania (po usnieciu interpunkcji)
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n)
wypisz_slowa() {
    local zdanie="$1"

    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo" | tr '[:upper:]' '[:lower:]'
        fi
    done

}

# Funkcja znajdujaca wszystkie palindromy w zdaniu
# Zlozonosc czasowa: O(n * m), gdzie n to liczba slow, m to srednia dlugosc slowa
# Zlozonosc pamieciowa: O(n)
palindromy_w_zdaniu() {
    local zdanie="$1"
    local slowa=$(wypisz_slowa "$zdanie")
    for slowo in $slowa; do
        if [ "$(czy_palindrom "$slowo")" == "true" ]; then
            echo "$slowo"
        fi
    done
}

test_palindromy_w_zdaniu(){
    local wynik=($(palindromy_w_zdaniu "Tata zbaral kajak na wycieczke i uderzyl sie w oko."))
    local oczekiwane=(kajak i w oko)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_palindromy_w_zdaniu
}

main "$@"
