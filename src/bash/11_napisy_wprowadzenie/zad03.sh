# Tytul: Usun spacje ze zdania.
# Tresc: Otrzymasz napis reprezentujacy zdanie. Usun spacje ze zdania.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "Alamakota".

source ../assert.sh

liczba_slow_v1() {

    local zdanie="$1"
    local licznik=0

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                local licznik=$((licznik + 1))
            fi
        done

        echo "$licznik"
    }

    test1() {
        local zdanie="Ile to   ma :  slow w swoim zdaniu na   koniec?"
        local wynik=9
        local wynik=9
        assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
    }

    test2() {
        local zdanie="to sa cztery slowa"
        local wynik=4
        local wynik=4
        assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
    }

    test3() {
        local zdanie="31    331 .,,,.,.,brak slow!!!    "
        local wynik=2
        local wynik=2
        assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
        test3
    }

    main "$@"

