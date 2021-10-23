#!/usr/bin/env bash

source ../assert.sh

# Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej
# dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne
# znaki.

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

