# Tytul: Znalezienie wszystkich par elementow listy o sumie rownej podanej liczbie.
# Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz wszystkie pary elementow listy, ktorych suma jest rowna x.
# Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
# Dane wyjsciowe: Lista par liczb calkowitych.
# Przyklad:
# Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostana zwrocone wszystkie pary elementow o sumie rownej 5: [(1, 4), (2, 3)].

source ../assert.sh

usun() {
    local klucz=$1
    local pom=()
    for liczba in "${lista[@]}"
    do
        [ $liczba -ne $klucz ] && pom+=($liczba)
    done
    lista=("${pom[@]}")
    unset pom
}

test1() {
    local lista=(6 7 2 1 8)
    local wynik=(6 7 1 8)
    local klucz=2
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(1 1 1 1)
    local wynik=()
    local klucz=1
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

