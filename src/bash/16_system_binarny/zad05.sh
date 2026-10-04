# ZAD-05A — Minimum bez instrukcji warunkowych
#
# **Poziom:** ★★☆
# **Tagi:** `bit-trick`, `min/max`, `bez if`
#
# ### Treść
#
# Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba naturalna: `min(a, b)`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 2
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
#
# ### Uwagi
#
# * Dopuszczalne są operacje arytmetyczne i bitowe.
#
# ZAD-05B — Maksimum bez instrukcji warunkowych
#
# **Poziom:** ★★☆
# **Tagi:** `bit-trick`, `min/max`, `bez if`
#
# ### Treść
#
# Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba naturalna: `max(a, b)`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 2
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie (ZAD-05A) dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bez instrukcji warunkowych: dla d = a - b przesuniecie arytmetyczne d >> 63
# (liczby w Bashu sa 64-bitowe ze znakiem) daje -1 (same jedynki), gdy d < 0,
# i 0, gdy d >= 0. Zatem d & (d >> 63) jest rowne d, gdy a < b, albo 0.
# (Ta sama sztuczka daje maksimum: a - (d & (d >> 63)).)

# ZAD-05A: min(a, b) = b + (d & (d >> 63))
# Zlozonosc czasowa: O(1)
# Zlozonosc pamieciowa: O(1)
minimum() {
    local a=$1 b=$2
    local d=$((a - b))
    echo "$((b + (d & (d >> 63))))"
}

# Wczytuje a i b (kazda w osobnej linii) i wypisuje mniejsza z nich.
program() {
    local a b
    read -r a
    read -r b
    minimum "$a" "$b"
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

test_minimum() {
    assertEqual "$(minimum 2 3)" 2 $LINENO
    assertEqual "$(minimum 4 4)" 4 $LINENO
    assertEqual "$(minimum -5 3)" -5 $LINENO
    assertEqual "$(minimum -1000000000 1000000000)" -1000000000 $LINENO
    assertEqual "$(minimum 1000000000 -1000000000)" -1000000000 $LINENO
    sprawdz program $'3\n2' "2" $LINENO
    sprawdz program $'-7\n-7' "-7" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_minimum
    fi
}

main "$@"
