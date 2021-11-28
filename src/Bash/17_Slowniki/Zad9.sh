#!/usr/bin/env bash

# Otrzymujesz napis. Znajdz w otrzymanym napisie wszystkie znaki 
# powtarzajace sie wiecej niz raz.

znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="$1"
    local -A histogram=()
    for (( i=0; i<${#napis}; i++ )); do
        ((histogram["${napis:$i:1}"]++))
    done
    for litera in ${!histogram[@]}; do
        if [[ "${histogram[$litera]}" -gt 1 ]]; then
            echo "$litera"
        fi
    done
}

test_znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="ababab"
    local wynik=($(znaki_powtarzajace_sie_wiecej_niz_raz "$napis"))
    local oczekiwane=(a b)
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_znaki_powtarzajace_sie_wiecej_niz_raz
}

main "$@"

