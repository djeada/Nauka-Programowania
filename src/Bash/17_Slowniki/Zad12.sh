#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. 
# Listy sa nieuporzadkowane. Sprawdz czy slowniki skladaja sie z tych samych par. 
# Dwie listy uznajemy za identyczne jesli zawieraja te same elementy, przy 
# czym kolejnosc elementow moze byc zmieniona.

czy_slowniki_identyczne() {

    # sprawdz czy klucze sa takie same
    if [[ "${!slownik_a[@]}" != "${!slownik_b[@]}" ]]; then
        echo false
        return
    fi

    # sprawdz czy wartosci sa takie same
    for klucz in "${!slownik_a[@]}"; do
        # posortuj listy dla obu slownikow
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

