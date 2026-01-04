# ZAD-11 — Samochody jadące w przeciwnych kierunkach
#
# **Poziom:** ★★☆
# **Tagi:** `listy`, `zliczanie`, `string`
#
# ### Treść
#
# Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:
#
# * `A` oznacza samochód jadący na wschód,
# * `B` oznacza samochód jadący na zachód.
#
# Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)
#
# ### Wyjście
#
# Jedna liczba naturalna — liczba mijających się par.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# ABABB
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```
source ../assert.sh

policz_samochody() {
    local licznik=0
    local pom=0

    for litera in "${lista[@]}"; do
        if [[ $litera == 'A' ]]; then
            pom=$((pom + 1))
        elif [[ $litera == 'B' ]]; then
            licznik=$((licznik + pom))
        fi
    done

    return $licznik
}

test1() {
    local lista=('A' 'B' 'A' 'B' 'B')
    local wynik=5
    policz_samochody
    assertEqual $? $wynik $LINENO
}

test2() {
    local lista=('A' 'A' 'A' 'B' 'B' 'A' 'B' 'A' 'B' 'A' 'A' 'A')
    local wynik=15
    policz_samochody
    assertEqual $? $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"
