# Tytul: Zamien litery "a" na znaki zapytania.
# Tresc: Otrzymasz napis. Zmien litery "a" na znaki zapytania.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "Latarnik", powinien zostac zwrocony napis: "L?t?rnik".

source ../assert.sh

liczby() {

    local n="$1"
    local wynik=""

    for((i=1;i<=n;i++)); do
        local wynik="$wynik$i"
    done

    echo "$wynik"

}

test1() {
    local n=5
    local wynik="12345"
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

test2() {
    local n="-1"
    local wynik=""
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

