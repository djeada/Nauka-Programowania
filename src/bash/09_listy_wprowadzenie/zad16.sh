# Tytul: Usun klucz.
# Tresc: Dla otrzymanej listy: liczb calkowitych oraz klucza, usun pierwsze wystapienie klucza w liscie.
# Dane wejsciowe: Lista liczb calkowitych i liczba calkowita.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostac zwrocona lista: [6, 2, 1, 27].

source ../assert.sh

znajdz_pary() {

    local n=${#lista[@]}
    local suma=$1

    for (( i=0; i<n; i++ )); do
        for (( j=i+1; j<n; j++ )); do
            if [ $((lista[i] + lista[j])) -eq $suma ]; then
                wynik+=("${lista[$i]}, ${lista[$j]};")
            fi
        done
    done
}

test1() {
    local lista=(0 4 5 6 2 9 2 3)
    local suma=5
    local oczekiwane=('0, 5;' '2, 3;' '2, 3;')
    declare -a wynik;
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

test2() {
    local lista=(1 -1 3 -3 4 5)
    local suma=0
    local oczekiwane=('1, -1;' '3, -3;')
    declare -a wynik;
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

