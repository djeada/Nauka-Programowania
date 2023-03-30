# Tytul: Odleglosc Hamminga.
# Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych napisy maja rozne znaki.
# Dane wejsciowe: Dwa napisy.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanych napisow: “adam” i “axam”, powinna zostac zwrocona liczba: 1.

source ../assert.sh

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

