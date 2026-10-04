# ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami
#
# **Poziom:** ★★★
# **Tagi:** `binarne`, `binary gap`, `pętle`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).
#
# Jeśli nie ma takiego ciągu — wypisz `0`.
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedna liczba naturalna: długość najdłuższego „gapu”.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 14
# ```
#
# **Wyjście:**
#
# ```
# 0
# ```
#
# ### Uwagi (ważne)
#
# * `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
#   Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

# Uzycie:
#   bash zad12.sh                     - uruchamia testy
#   bash zad12.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca dlugosc najdluzszego ciagu zer otoczonego z obu stron jedynkami.
# Najpierw pomijamy zera na koncu zapisu (nie maja jedynki po prawej), potem
# idziemy od najmlodszego bitu: kazda jedynka zamyka biezacy ciag zer.
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(1)
najdluzsza_przerwa() {
    local n=$1 biezaca=0 najdluzsza=0
    while ((n > 0 && (n & 1) == 0)); do
        ((n >>= 1))
    done
    while ((n > 0)); do
        if ((n & 1)); then
            if ((biezaca > najdluzsza)); then
                najdluzsza=$biezaca
            fi
            biezaca=0
        else
            ((biezaca++))
        fi
        ((n >>= 1))
    done
    echo "$najdluzsza"
}

program() {
    local n
    read -r n
    najdluzsza_przerwa "$n"
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

test_najdluzsza_przerwa() {
    assertEqual "$(najdluzsza_przerwa 0)" 0 $LINENO
    assertEqual "$(najdluzsza_przerwa 15)" 0 $LINENO
    assertEqual "$(najdluzsza_przerwa 32)" 0 $LINENO
    assertEqual "$(najdluzsza_przerwa 9)" 2 $LINENO
    assertEqual "$(najdluzsza_przerwa 529)" 4 $LINENO
    assertEqual "$(najdluzsza_przerwa 1041)" 5 $LINENO
    sprawdz program "14" "0" $LINENO
    sprawdz program "20" "1" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_najdluzsza_przerwa
    fi
}

main "$@"
