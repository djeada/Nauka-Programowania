# Tytul:Wypisz pionowo slowa, z ktorych sklada sie zdanie.
# Tresc: Otrzymasz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Kilka napisow.
# Przyklad:
# Dla otrzymanego napisu: "Ala ma kota", powinno zostac wypisane: "Ala", "ma", "kota".

source ../assert.sh

odleglosc_hamminga() {

    local napis_a="$1"
    local napis_b="$2"
    local n=${#napis_a}
    local m=${#napis_b}

    if [ $n -ne $m ]; then
        echo "-1"
        return
    fi

    local wynik=0
    for((i=0;i<n;i++)); do
        if [[ "${napis_a:$i:1}" != "${napis_b:$i:1}" ]]; then
            local wynik=$((wynik+1))
        fi
    done

    echo "$wynik"

}

test1() {
    local napis_a="xxbab"
    local napis_b="bbabb"
    local wynik=4
    assertEqual "$(odleglosc_hamminga "$napis_a" "$napis_b")" "$wynik" $LINENO
}

test2() {
    local napis_a="test_string"
    local napis_b="test_string_2"
    local wynik="-1"
    assertEqual "$(odleglosc_hamminga "$napis_a" "$napis_b")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

