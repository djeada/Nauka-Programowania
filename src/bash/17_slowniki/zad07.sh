# Tytul: Anagramy w tekscie
# Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezienie wszystkich slow, w ktorych te same znaki wystepuja te sama liczbe razy. Innymi slowy, szukasz anagramow w tekscie. Nalezy zignorowac roznice miedzy malymi i wielkimi literami. Pamietaj, ze slowa skladaja sie wylacznie z liter.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista list napisow.
# Przyklad:
# Dla otrzymanego napisu:
# "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia jak bandzior i jego arbuz.",
# powinna zostac zwrocona lista:
# [["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]].

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

    histogram_slow_w_tekscie() {
        local tekst="$1"
        local -A histogram=()
        for slowo in $(wypisz_slowa "$tekst"); do
            ((histogram["$slowo"]++))
        done
        for slowo in ${!histogram[@]}; do
            echo "$slowo: ${histogram[$slowo]};"
        done
    }

    test_histogram_slow_w_tekscie() {
        local tekst="Ala ma kota."
        local wynik=($(histogram_slow_w_tekscie "$tekst"))
        local oczekiwane=('ala: 1;' 'ma: 1;' 'kota: 1;')
        assertIdenticalElements wynik oczekiwane $LINENO
    }

    main() {
        test_histogram_slow_w_tekscie
    }

    main "$@"

