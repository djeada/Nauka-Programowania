# ZAD-02 — Policz wystąpienia znaku
#
# **Poziom:** ★☆☆
# **Tagi:** `string`, `count`
#
# ### Treść
#
# Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.
#
# ### Wejście
#
# * 1. linia: napis
# * 2. linia: pojedynczy znak
#
# ### Wyjście
#
# * 1. linia: liczba wystąpień
#
# ### Przykład
#
# **Wejście:**
#
# ```
# klamra
# a
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```

source ../assert.sh

# Funkcja liczaca wystapienia znaku w napisie (wersja z petla)
# Zlozonosc czasowa: O(n), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(1)
policz_znak_v1() {

    local slowo=$1
    local szukany_znak=$2
    local licznik=0

    while IFS= read -n 1 znak; do
        if [[ "$znak" == "$szukany_znak" ]]; then
            local licznik=$((licznik + 1))
        fi
    done <<<"$1"

    echo $licznik

}

# Funkcja liczaca wystapienia znaku w napisie (wersja z grep)
# Zlozonosc czasowa: O(n), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(n) dla wyjscia grep
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
