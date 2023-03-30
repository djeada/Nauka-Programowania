# Tytul: Odwroc napis.
# Tresc: Zmien otrzymany napis, tak aby zapisany byl on od tylu.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "barszcz", powinien zostac zwrocony napis: "zczsrab".

source ../assert.sh

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

