#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanego napisu oraz znaku,
# znajdz liczbe wystapien znaku w napisie.

policz_znak_v1() {

    local slowo=$1
    local szukany_znak=$2
    local licznik=0

    while IFS= read -n 1 znak ; do
        if [[ "$znak" == "$szukany_znak" ]]; then
            local licznik=$((licznik+1))
        fi
    done <<< "$1"

    echo $licznik

}

policz_znak_v2() {

    local slowo=$1
    local szukany_znak=$2

    grep -o "$szukany_znak" <<<"$slowo" | grep -c .

}

test1() {
    local napis="adam"
    local znak="a"
    local wynik=2
    assertEqual "$(policz_znak_v1 $napis $znak)" "$wynik" $LINENO
}

test2() {
    local napis="adam"
    local znak="a"
    local wynik=2
    assertEqual "$(policz_znak_v2 $napis $znak)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

