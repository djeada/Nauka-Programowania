#!/usr/bin/env bash

source ../assert.sh

# Odwroc napis.

odwroc_napis_v1() {

    local napis="$1"
    local n=${#napis}

    for((i=$n-1;i>=0;i--)); do
        local odwrocone="$odwrocone${napis:$i:1}"
    done

    echo "$odwrocone"

}

odwroc_napis_v2() {

    echo $1 | rev

}

test1() {
    local napis="adam"
    local wynik="mada"
    assertEqual "$(odwroc_napis_v1 $napis)" "$wynik" $LINENO
}

test2() {
    local napis="adam"
    local wynik="mada"
    assertEqual "$(odwroc_napis_v2 $napis)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

