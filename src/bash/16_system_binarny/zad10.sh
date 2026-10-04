# ZAD-10 — Ile bitów trzeba odwrócić (A → B)
#
# **Poziom:** ★★☆
# **Tagi:** `XOR`, `popcount`, `bitwise`
#
# ### Treść
#
# Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.
#
# ### Wejście
#
# * 1. linia: `A`
# * 2. linia: `B`
#
# ### Wyjście
#
# Jedna liczba naturalna: liczba różniących się bitów.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 34
# 73
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```

# Uzycie:
#   bash zad10.sh                     - uruchamia testy
#   bash zad10.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca liczbe bitow, ktore trzeba odwrocic w a, aby otrzymac b:
# a ^ b ma jedynki dokladnie na pozycjach, na ktorych bity sie roznia.
# Jedynki liczymy, gaszac najmlodsza z nich (x & (x - 1)).
# Zlozonosc czasowa: O(liczba roznych bitow)
# Zlozonosc pamieciowa: O(1)
bity_do_odwrocenia() {
    local roznica=$(($1 ^ $2)) licznik=0
    while ((roznica != 0)); do
        ((roznica &= roznica - 1))
        ((licznik++))
    done
    echo "$licznik"
}

program() {
    local a b
    read -r a
    read -r b
    bity_do_odwrocenia "$a" "$b"
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

test_bity_do_odwrocenia() {
    assertEqual "$(bity_do_odwrocenia 0 0)" 0 $LINENO
    assertEqual "$(bity_do_odwrocenia 7 7)" 0 $LINENO
    assertEqual "$(bity_do_odwrocenia 0 1023)" 10 $LINENO
    assertEqual "$(bity_do_odwrocenia 8 1)" 2 $LINENO
    sprawdz program $'34\n73' "5" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_bity_do_odwrocenia
    fi
}

main "$@"
