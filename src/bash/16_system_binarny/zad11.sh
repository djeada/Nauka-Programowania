# ZAD-11 — Palindrom w systemie binarnym
#
# **Poziom:** ★★☆
# **Tagi:** `binarne`, `palindrom`, `string`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.
#
# Wypisz:
#
# * `Prawda` — jeśli tak,
# * `Fałsz` — jeśli nie.
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedno słowo: `Prawda` lub `Fałsz`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 26
# ```
#
# **Wyjście:**
#
# ```
# Fałsz
# ```
#
# ### Uwagi (ważne)
#
# * `26` ma zapis binarny `11010`, który **nie** jest palindromem.
#   (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

# Uzycie:
#   bash zad11.sh                     - uruchamia testy
#   bash zad11.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Sprawdza, czy zapis binarny n (bez zer wiodacych) jest palindromem.
# Budujemy liczbe o odwroconej kolejnosci bitow: zapis jest palindromem
# dokladnie wtedy, gdy odwrocona liczba jest rowna n.
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(1)
czy_binarny_palindrom() {
    local n=$1 reszta=$1 odwrocona=0
    while ((reszta > 0)); do
        odwrocona=$(((odwrocona << 1) | (reszta & 1)))
        ((reszta >>= 1))
    done
    if ((odwrocona == n)); then
        echo "Prawda"
    else
        echo "Fałsz"
    fi
}

program() {
    local n
    read -r n
    czy_binarny_palindrom "$n"
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

test_czy_binarny_palindrom() {
    assertEqual "$(czy_binarny_palindrom 0)" "Prawda" $LINENO
    assertEqual "$(czy_binarny_palindrom 1)" "Prawda" $LINENO
    assertEqual "$(czy_binarny_palindrom 9)" "Prawda" $LINENO
    assertEqual "$(czy_binarny_palindrom 27)" "Prawda" $LINENO
    assertEqual "$(czy_binarny_palindrom 10)" "Fałsz" $LINENO
    assertEqual "$(czy_binarny_palindrom 6)" "Fałsz" $LINENO
    sprawdz program "26" "Fałsz" $LINENO
    sprawdz program "585" "Prawda" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_czy_binarny_palindrom
    fi
}

main "$@"
