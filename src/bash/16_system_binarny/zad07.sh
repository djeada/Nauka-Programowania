# ZAD-07 — Zamiana sąsiadujących bitów
#
# **Poziom:** ★☆☆
# **Tagi:** `bitwise`, `maski`, `swap bits`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:
#
# * bit 0 z bitem 1,
# * bit 2 z bitem 3,
# * bit 4 z bitem 5,
# * itd.
#
# Następnie wypisz wynik w systemie dziesiętnym.
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedna liczba naturalna: wynik po zamianie bitów.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 9131
# ```
#
# **Wyjście:**
#
# ```
# 4951
# ```
#
# ### Uwagi
#
# * Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

# Uzycie:
#   bash zad07.sh                     - uruchamia testy
#   bash zad07.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Maska ...0101 wybiera bity o numerach parzystych. Maske bitow nieparzystych
# (...1010) zastepujemy przesunieciem n >> 1, bo 0xAAAA... jest w Bashu liczba
# ujemna (64 bity ze znakiem).
readonly MASKA_PARZYSTYCH=0x5555555555555555

# Zamienia miejscami kazda pare sasiadujacych bitow (0 z 1, 2 z 3, ...).
# Zlozonosc czasowa: O(1)
# Zlozonosc pamieciowa: O(1)
zamien_sasiednie_bity() {
    local n=$1
    echo "$((((n >> 1) & MASKA_PARZYSTYCH) | ((n & MASKA_PARZYSTYCH) << 1)))"
}

program() {
    local n
    read -r n
    zamien_sasiednie_bity "$n"
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

test_zamien_sasiednie_bity() {
    assertEqual "$(zamien_sasiednie_bity 0)" 0 $LINENO
    assertEqual "$(zamien_sasiednie_bity 1)" 2 $LINENO
    assertEqual "$(zamien_sasiednie_bity 2)" 1 $LINENO
    assertEqual "$(zamien_sasiednie_bity 3)" 3 $LINENO
    # 100 -> 1000 (brakujacy bit 3 traktujemy jak zero)
    assertEqual "$(zamien_sasiednie_bity 4)" 8 $LINENO
    assertEqual "$(zamien_sasiednie_bity 10)" 5 $LINENO
    # 1000000000 = 111011100110101100101000000000
    assertEqual "$(zamien_sasiednie_bity 1000000000)" 929416448 $LINENO
    sprawdz program "9131" "4951" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_zamien_sasiednie_bity
    fi
}

main "$@"
