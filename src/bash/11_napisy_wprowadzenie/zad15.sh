# Tytul: Zamien znaki na kody ASCII.
# Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".

source ../assert.sh

wypisz_slowa() {

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

    test1() {
        local napis="We think in generalities, but we live in details"
        local oczekiwane=('we' 'think' 'in' 'generalities' 'but' 'we' 'live' 'in' 'details')
        readarray -t wynik <<< "$(wypisz_slowa "$napis")"
        assertArrayEqual wynik oczekiwane $LINENO
    }

    test2() {
        local napis=""
        local wynik=""
        assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

