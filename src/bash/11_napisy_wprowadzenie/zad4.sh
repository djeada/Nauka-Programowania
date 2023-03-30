# Tytul: Znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
# Tresc: Otrzymasz napis. Znajdz znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista znakow.
# Przyklad:
# Dla otrzymanego napisu: "Slon", powinna zostac zwrocona lista: ['o', 'n'].

source ../assert.sh

na_wielkie_v1() {
    awk '{ print toupper($0) }' <<< "$1"
}

na_wielkie_v2() {
    tr a-z A-Z <<< "$1"
}

test1() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v1 "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v2 "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

