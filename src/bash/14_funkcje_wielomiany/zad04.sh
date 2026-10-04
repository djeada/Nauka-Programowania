# ZAD-04 — Mnożenie wielomianów
#
# **Poziom:** ★★☆
# **Tagi:** `funkcje`, `wielomiany`, `konwolucja`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.
#
# ### Wejście (argumenty funkcji)
#
# * `a` — lista `[a_n, ..., a_0]`
# * `b` — lista `[b_m, ..., b_0]`
#
# ### Wyjście (zwracana wartość)
#
# * lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)
#
# ### Przykład
#
# Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
# `[5, 10, 30, 26, 52, 24]`

# Uzycie:
#   bash zad04.sh                     - uruchamia testy
#   bash zad04.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca wspolczynniki iloczynu dwoch wielomianow. Wielomiany podajemy jako
# napisy ze wspolczynnikami od najwyzszej potegi, np. "5 0 10 6".
# Kazdy wyraz a[i] mnozymy przez kazdy wyraz b[j] i dodajemy do pozycji i+j.
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(n+m)
iloczyn_wielomianow() {
    local -a a b wynik=()
    read -ra a <<<"$1"
    read -ra b <<<"$2"
    local dlugosc=$((${#a[@]} + ${#b[@]} - 1)) i j

    for ((i = 0; i < dlugosc; i++)); do
        wynik[i]=0
    done
    for ((i = 0; i < ${#a[@]}; i++)); do
        for ((j = 0; j < ${#b[@]}; j++)); do
            ((wynik[i + j] += a[i] * b[j]))
        done
    done

    echo "${wynik[*]}"
}

# Wczytuje dwa wielomiany (stopien i wspolczynniki) ze stdin i wypisuje iloczyn.
program() {
    local a b
    read -r _
    read -r a
    read -r _
    read -r b
    iloczyn_wielomianow "$a" "$b"
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

test_iloczyn_wielomianow() {
    assertEqual "$(iloczyn_wielomianow "1 1" "1 -1")" "1 0 -1" $LINENO
    assertEqual "$(iloczyn_wielomianow "2" "3")" "6" $LINENO
    assertEqual "$(iloczyn_wielomianow "0" "1 2 3")" "0 0 0" $LINENO
    assertEqual "$(iloczyn_wielomianow "1 2 1" "1 2 1")" "1 4 6 4 1" $LINENO
    assertEqual "$(iloczyn_wielomianow "-2 0 3" "4 -1")" "-8 2 12 -3" $LINENO
}

test_program() {
    sprawdz program $'3\n5 0 10 6\n2\n1 2 4' "5 10 30 26 52 24" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_iloczyn_wielomianow
        test_program
    fi
}

main "$@"
