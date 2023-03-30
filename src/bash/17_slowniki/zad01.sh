# Tytul: Slownik z kluczami bedacymi liczbami naturalnymi i wartosciami ich kwadratami.
# Tresc: Dostajesz liczbe naturalna. Stworz slownik, w ktorym kluczami beda kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartosciami beda ich kwadraty.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami naturalnymi.
# Przyklad:
# Dla liczby 5, slownik powinien wygladac nastepujaco: {1: 1, 2: 4, 3: 9, 4: 16}.

source ../assert.sh

zbuduj_slownik() {
    local liczba=$1
    local -A slownik=()
    for ((i=0; i<liczba; i++)); do
        slownik[$i]=$((i*i))
    done
    for k in "${!slownik[@]}"; do
        for k in "${!slownik[@]}"; do
            echo "$k: ${slownik[$k]};"
        done
    }

    test_zbuduj_slownik() {
        local wynik=($(zbuduj_slownik 10))
        local oczekiwane=("0: 0;" "1: 1;" "2: 4;" "3: 9;" "4: 16;" "5: 25;" "6: 36;" "7: 49;" "8: 64;" "9: 81;")
        assertArrayEqual wynik oczekiwane $LINENO
    }

    main() {
        test_zbuduj_slownik
    }

    main "$@"

