# Tytul: Z ilu slow sklada sie zdanie?
# Tresc: Zlicz, ile slow sklada sie z podanego zdania. Znaki interpunkcyjne nie sa brane pod uwage jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanego napisu: "gram na pianinie.", powinno zostac zwrocone: 3.

source ../assert.sh

srednia_dlugosc() {

    local zdanie="$1"
    local licznik=0
    local calkowita_dlugosc=0

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                local licznik=$((licznik + 1))
                local calkowita_dlugosc=$(( calkowita_dlugosc + ${#slowo} ))
            fi
        done

        echo $(bc -l <<< "scale=0; $calkowita_dlugosc/$licznik")
    }

    test1() {
        local zdanie="Ile to   ma :  slow w swoim zdaniu na   koniec?"
        local wynik=3
        assertEqual "$(srednia_dlugosc "$zdanie")" "$wynik" $LINENO
    }

    test2() {
        local zdanie="Kaczka lubi wiosne."
        local wynik=5
        assertEqual "$(srednia_dlugosc "$zdanie")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

