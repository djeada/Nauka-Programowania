#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis i dwie listy napisow. Podmien w pierwszym napisie, 
# napisy z pierwszej listy na odpowiadajace im napisy z drugiej listy.

podmien_napisy() {
    local tekst="$1"

    for i in "${!lista_a[@]}"; do
        tekst="${tekst//${lista_a[$i]}/${lista_b[$i]}}"
    done

    echo "$tekst"
}

test_podmien_napisy() {
    local tekst='Whole every miles as tiled at seven or. 
Wished he entire esteem mr oh by.
He prevent request by if in pleased. 
Picture too and concern has was comfort. 
Ten difficult resembled eagerness nor. 
Same park bore on be. 
Warmth his law design say are person. 
Pronounce suspected in belonging conveying ye repulsive.'
    local lista_a=(or be he)
    local lista_b=(and off she)
    local wynik="$(podmien_napisy "$tekst")"
    local oczekiwane='Whole every miles as tiled at seven and. 
Wished she entire esteem mr oh by.
He prevent request by if in pleased. 
Picture too and concern has was comfort. 
Ten difficult resembled eagerness nor. 
Same park bore on off. 
Warmth his law design say are person. 
Pronounce suspected in belonging conveying ye repulsive.'
    assertEqual "$wynik" "$oczekiwane"
}

main() {
    test_podmien_napisy
}


main "$@"

