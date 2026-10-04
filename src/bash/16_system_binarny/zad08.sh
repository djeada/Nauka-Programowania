# ZAD-08 — Najbliższa potęga dwójki (>= n)
#
# **Poziom:** ★☆☆
# **Tagi:** `potęgi 2`, `bitwise`, `pętle`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedna liczba naturalna: najmniejsze `2^k ≥ n`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 111
# ```
#
# **Wyjście:**
#
# ```
# 128
# ```
#
# ### Uwagi
#
# * Dla `n = 0` przyjmij wynik `1`.

# Uzycie:
#   bash zad08.sh                     - uruchamia testy
#   bash zad08.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca najmniejsza potege dwojki >= n (dla n = 0 i n = 1 jest to 2^0 = 1).
# Kolejne potegi otrzymujemy przesunieciem w lewo.
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(1)
najblizsza_potega_dwojki() {
    local n=$1 potega=1
    while ((potega < n)); do
        ((potega <<= 1))
    done
    echo "$potega"
}

program() {
    local n
    read -r n
    najblizsza_potega_dwojki "$n"
}

# Uruchamia funkcje $1 z wejsciem $2 i porownuje jej wyjscie (dokladnie, wraz
# z koncowym znakiem nowej linii) z $3. ${x@Q} wymusza porownanie napisow.
sprawdz() {
    local funkcja=$1 wejscie=$2 oczekiwane=$3 linia=$4 wynik
    wynik=$("$funkcja" <<<"$wejscie"; printf x)
    wynik=${wynik%x}
    if [[ -n $oczekiwane ]]; then
        oczekiwane+=$'\n'
    fi
    assertEqual "${wynik@Q}" "${oczekiwane@Q}" "$linia"
}

test_najblizsza_potega_dwojki() {
    assertEqual "$(najblizsza_potega_dwojki 0)" 1 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 1)" 1 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 2)" 2 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 3)" 4 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 64)" 64 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 65)" 128 $LINENO
    assertEqual "$(najblizsza_potega_dwojki 1000000000)" 1073741824 $LINENO
    sprawdz program "111" "128" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_najblizsza_potega_dwojki
    fi
}

main "$@"
