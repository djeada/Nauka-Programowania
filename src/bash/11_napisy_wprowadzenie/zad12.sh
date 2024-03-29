# Tytul: Zamien wszystkie male litery na duze.
# Tresc: Otrzymasz napis. Zmien wszystkie male litery na duze.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanego napisu: "Rumcajs", powinien zostac zwrocony napis: "RUMCAJS".

source ../assert.sh

usun_spacje_v1() {

    local zdanie="$1"
    local wynik=""

    while IFS= read -n 1 znak ; do
        if [[ "$znak" != " " ]]; then
            local wynik="${wynik}${znak}"
        fi
    done <<< "$zdanie"

    echo "$wynik"
}

usun_spacje_v2() {

    local zdanie="$1"
    echo "$zdanie" | sed -r 's/[ ]+//g'
}

test1() {
    local zdanie="lezy jezy na wiezy."
    local wynik="lezyjezynawiezy."
    assertEqual "$(usun_spacje_v1 "$zdanie")" "$wynik" $LINENO
}

test2() {
    local zdanie="lezy jezy na wiezy."
    local wynik="lezyjezynawiezy."
    assertEqual "$(usun_spacje_v2 "$zdanie")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

