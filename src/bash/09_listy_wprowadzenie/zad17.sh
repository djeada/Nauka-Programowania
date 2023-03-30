# Tytul: Usun duplikaty.
# Tresc: Otrzymujesz liste liczb naturalnych. Usun z niej wszystkie duplikaty, tak aby kazda liczba pozostala tylko raz.
# Dane wejsciowe: Lista liczb naturalnych.
# Dane wyjsciowe: Lista liczb naturalnych.
# Przyklad:
# Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostac zwrocona lista: [3, 2, 1].

source ../assert.sh

suma_dwoch() {
    local n=${#lista[@]}
    local liczba=$1

    for (( i=0; i<n; i++ )); do
        for (( j=i+1; j<n; j++ )); do
            if [ $((lista[i] + lista[j])) -eq $liczba ]; then
                echo "($i, $j)"
                return
            fi
        done
    done

    echo "(-1, -1)"
}

test1() {
    local lista=(1 3 4 5 2)
    local liczba=5
    local wynik="(0, 2)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

test2() {
    local lista=(2 -6 10 21 8)
    local liczba=7
    local wynik="(-1, -1)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

