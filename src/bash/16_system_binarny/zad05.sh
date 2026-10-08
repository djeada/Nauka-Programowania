# ZAD-05A — Minimum bez instrukcji warunkowych
#
# **Poziom:** ★★☆
# **Tagi:** `bit-trick`, `min/max`, `bez if`
#
# ### Treść
#
# Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).
#
# ### Ograniczenia
#
# * $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**
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
# * Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
# * Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.
#
# ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych
#
# **Poziom:** ★★☆
# **Tagi:** `bit-trick`, `maski`, `bez if`
#
# ### Treść
#
# Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.
#
# ### Wejście
#
# * 1. linia: `x`
#
# ### Wyjście
#
# Jedna liczba naturalna: $|x|$.
#
# ### Ograniczenia
#
# * $-10^9 \le x \le 10^9$ — liczba **może być ujemna**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# -12
# ```
#
# **Wyjście:**
#
# ```
# 12
# ```
#
# ### Uwagi
#
# * Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
# * Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
# * XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

# Uzycie:
#   bash zad05.sh                        - uruchamia testy
#   bash zad05.sh --stdin A|B < dane.txt - rozwiazuje podpunkt A albo B (domyslnie A)

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
# Wartosc bezwzgledna: maska = x >> 63 to -1 dla x < 0 i 0 dla x >= 0
wartosc_bezwzgledna() {
    local x=$1
    local maska=$((x >> 63))
    echo "$(((x ^ maska) - maska))"
}

program() {
    local a b
    read -r a
    read -r b
    minimum "$a" "$b"
}

program_b() {
    local x
    read -r x
    wartosc_bezwzgledna "$x"
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

test_wartosc_bezwzgledna() {
    assertEqual "$(wartosc_bezwzgledna -12)" 12 $LINENO
    assertEqual "$(wartosc_bezwzgledna 0)" 0 $LINENO
    assertEqual "$(wartosc_bezwzgledna 7)" 7 $LINENO
    assertEqual "$(wartosc_bezwzgledna -1000000000)" 1000000000 $LINENO
    sprawdz program_b "-1" "1" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        case ${2:-A} in
            B | b) program_b ;;
            *) program ;;
        esac
    else
        test_minimum
        test_wartosc_bezwzgledna
    fi
}

main "$@"
