# ZAD-12 — Usuń spacje ze zdania
#
# **Poziom:** ★☆☆
# **Tagi:** `replace`, `string`
#
# ### Treść
#
# Wczytaj zdanie i usuń z niego wszystkie spacje.
#
# ### Wejście
#
# * 1. linia: zdanie
#
# ### Wyjście
#
# * 1. linia: zdanie bez spacji
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Ala ma kota
# ```
#
# **Wyjście:**
#
# ```
# Alamakota
# ```
source ../assert.sh

# Funkcja usuwajaca spacje ze zdania (wersja z petla)
# Zlozonosc czasowa: O(n), gdzie n to dlugosc zdania
# Zlozonosc pamieciowa: O(n) dla wyniku
usun_spacje_v1() {

    local zdanie="$1"
    local wynik=""

    # Iteracja przez wszystkie znaki
    while IFS= read -n 1 znak; do
        if [[ "$znak" != " " ]]; then
            local wynik="${wynik}${znak}"
        fi
    done <<<"$zdanie"

    echo "$wynik"
}

# Funkcja usuwajaca spacje ze zdania (wersja z sed)
# Zlozonosc czasowa: O(n), gdzie n to dlugosc zdania
# Zlozonosc pamieciowa: O(n) dla wyniku
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
