# Tytul: Konwersja listy na napis
# Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.
# Dane wejsciowe: Lista liczb naturalnych.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo"
            fi
        done

    }

    main() {
        local zdanie="We think in generalities, but we live in details."
        wypisz_slowa "$zdanie"
    }

    main "$@"

