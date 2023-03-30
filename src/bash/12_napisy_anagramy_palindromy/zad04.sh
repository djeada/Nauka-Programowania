# Tytul: Wyszukanie wszystkich palindromow w zdaniu.
# Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie wszystkich palindromow w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostac zwrocona lista: ["kajak", "i", "w", "oko"].

source ../assert.sh

czy_palindrom() {
    local slowo="$1"
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

wypisz_slowa() {
    local zdanie="$1"
    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo" | tr '[:upper:]' '[:lower:]'
            fi
        done

    }

    palindromy_w_zdaniu() {
        local zdanie="$1"
        local zdanie="$1"
        local slowa=$(wypisz_slowa "$zdanie")
        for slowo in $slowa; do
            if [ "$(czy_palindrom "$slowo")" == "true" ]; then
                echo "$slowo"
            fi
        done
    }

    test_palindromy_w_zdaniu(){
        local wynik=$(palindromy_w_zdaniu "Tata zbaral kajak na wycieczke i uderzyl sie w oko.")
        local oczekiwane=(kajak i w oko)
        assertIdenticalElements wynik oczekiwane $LINENO
    }

    main() {
        test_palindromy_w_zdaniu
    }

    main "$@"

