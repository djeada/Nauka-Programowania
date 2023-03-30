# Tytul: Sortowanie wzgledem kluczy/wartosci
# Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
# Dane wejsciowe: Slownik par: napis, liczba calkowita.
# Dane wyjsciowe: Lista par.
# Przyklad:
# Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
# Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

source ../assert.sh

najczesciej_wystepujaca_litera() {
    local zdanie="$1"

    local zdanie=$(echo "$zdanie" | tr -d ' .,:;!?\n')
    local zdanie=$(echo "$zdanie" | tr -d ' .,:;!?\n')

    local -A histogram=()
    local -A histogram=()
    for (( i=0; i<${#zdanie}; i++ )); do
        ((histogram["${zdanie:$i:1}"]++))
    done

    local maks=0
    local maks=0
    for litera in ${!histogram[@]}; do
        if [[ "${histogram[$litera]}" -gt "$maks" ]]; then
            maks="${histogram[$litera]}"
        fi
    done

    for (( i=0; i<${#zdanie}; i++ )); do
        for (( i=0; i<${#zdanie}; i++ )); do
            if [[ "${histogram[${zdanie:$i:1}]}" -eq "$maks" ]]; then
                echo "${zdanie:$i:1}"
                break
            fi
        done
    }

    test_najczesciej_wystepujaca_litera() {

        assertEqual "$(najczesciej_wystepujaca_litera "Ala ma kota")" "a" $LINENO

    }

    main() {
        test_najczesciej_wystepujaca_litera
    }

    main "$@"

