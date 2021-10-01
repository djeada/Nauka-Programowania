#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Zamien wszystkie znaki napisu
# na odpowiadajace im numery w tablicy ASCII. Podmien
# otrzymany napis na uzyskane numery oddzielone przecinkami.

ord() {
    LC_CTYPE=C printf '%d' "'$1"
}

zamien() {

    local napis="$1"
    local n=$(( ${#napis} - 1 ))

    for ((i = 0; i < n; i++)); do
        echo -n "$(ord "${napis:$i:1}"), "
    done

    if [ $n -ne -1 ]; then
        echo "$(ord "${napis:$n:1}")"
    fi
}

test1() {
    local napis="pacZka!"
    local wynik="112, 97, 99, 90, 107, 97, 33"
    assertEqual "$(zamien $napis)" "$wynik" $LINENO
}

test2() {
    local napis=""
    local wynik=""
    assertEqual "$(zamien $napis)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

