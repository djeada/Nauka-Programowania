# Tytul: Usuwanie z slownika.
# Tresc: Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza liczbe calkowita. Usun z slownika pary, dla ktorych wartosc jest rowna otrzymanej liczbie.
# Dane wejsciowe: Slownik par napisow i liczb calkowitych oraz liczba calkowita.
# Dane wyjsciowe: Slownik par napisow i liczb calkowitych.
# Przyklad:
# Dla slownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, slownik powinien wygladac nastepujaco: {“abc”: 1, “cba” : 3}.

source ../assert.sh

czy_slowniki_identyczne() {

    if [[ "${!slownik_a[@]}" != "${!slownik_b[@]}" ]]; then
        if [[ "${!slownik_a[@]}" != "${!slownik_b[@]}" ]]; then
            echo false
            return
        fi

        for klucz in "${!slownik_a[@]}"; do
            for klucz in "${!slownik_a[@]}"; do
                local posortowane_wartosci_a=($(echo "${slownik_a[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                local posortowane_wartosci_a=($(echo "${slownik_a[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                local posortowane_wartosci_b=($(echo "${slownik_b[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                if [[ "${posortowane_wartosci_a[@]}" != "${posortowane_wartosci_b[@]}" ]]; then
                    echo false
                    return
                fi
            done

            echo true
        }

        test_czy_slowniki_identyczne() {
            local -A slownik_a=(["a"]="1 2 3" ["b"]="4 5 6")
            local -A slownik_b=(["a"]="3 1 2" ["b"]="5 4 6")
            assertTrue "$(czy_slowniki_identyczne)" $LINENO
        }

        main() {
            test_czy_slowniki_identyczne
        }

        main "$@"

