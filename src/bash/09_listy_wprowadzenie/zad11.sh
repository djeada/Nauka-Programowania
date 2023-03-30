# Tytul: Pierwsze wystapienie klucza.
# Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
# Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.
# Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.
# Przyklad:
# Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.

source ../assert.sh

policz_samochody() {
    local licznik=0
    local pom=0

    for litera in "${lista[@]}"; do
        if [[ $litera == 'A' ]]; then
            pom=$((pom+1))
        elif [[ $litera == 'B' ]]; then
            licznik=$((licznik+pom))
        fi
    done

    return $licznik
}

test1() {
    local lista=('A' 'B' 'A' 'B' 'B')
    local wynik=5
    policz_samochody
    assertEqual $? $wynik $LINENO
}

test2() {
    local lista=('A' 'A' 'A' 'B' 'B' 'A' 'B' 'A' 'B' 'A' 'A' 'A')
    local wynik=15
    policz_samochody
    assertEqual $? $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

