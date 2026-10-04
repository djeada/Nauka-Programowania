# ZAD-05 — k-ta pochodna wielomianu
#
# **Poziom:** ★★☆
# **Tagi:** `funkcje`, `pochodna`, `wielomiany`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.
#
# ### Wejście (argumenty funkcji)
#
# * `a` — lista `[a_n, ..., a_0]`
# * `k` — liczba naturalna
#
# ### Wyjście (zwracana wartość)
#
# * lista współczynników wielomianu po zróżniczkowaniu `k` razy
#
# ### Przykład
#
# Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
# `[8, -3]`
#
# ### Uwagi
#
# * Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca wspolczynniki k-tej pochodnej wielomianu podanego jako napis ze
# wspolczynnikami od najwyzszej potegi (np. "4 -3 2"). Pochodna wielomianu
# [c_d, ..., c_1, c_0] to [d*c_d, (d-1)*c_(d-1), ..., 1*c_1]; pochodna stalej to [0].
# Zlozonosc czasowa: O(k*n)
# Zlozonosc pamieciowa: O(n)
pochodna() {
    local -a wspolczynniki nowe
    read -ra wspolczynniki <<<"$1"
    local k=$2 stopien i

    for ((; k > 0; k--)); do
        stopien=$((${#wspolczynniki[@]} - 1))
        if ((stopien == 0)); then
            wspolczynniki=(0)
            break
        fi
        nowe=()
        for ((i = 0; i < stopien; i++)); do
            nowe+=("$((wspolczynniki[i] * (stopien - i)))")
        done
        wspolczynniki=("${nowe[@]}")
    done

    echo "${wspolczynniki[*]}"
}

# Wczytuje wielomian (stopien i wspolczynniki) oraz k ze stdin i wypisuje pochodna.
program() {
    local wspolczynniki k
    read -r _
    read -r wspolczynniki
    read -r k
    pochodna "$wspolczynniki" "$k"
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

test_pochodna() {
    assertEqual "$(pochodna "4 -3 2" 2)" "8" $LINENO
    assertEqual "$(pochodna "4 -3 2" 3)" "0" $LINENO
    assertEqual "$(pochodna "1 0 0 0" 2)" "6 0" $LINENO
    assertEqual "$(pochodna "5" 1)" "0" $LINENO
    assertEqual "$(pochodna "2 1 -7 3 1" 1)" "8 3 -14 3" $LINENO
    assertEqual "$(pochodna "1 1" 12)" "0" $LINENO
}

test_program() {
    sprawdz program $'2\n4 -3 2\n1' "8 -3" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_pochodna
        test_program
    fi
}

main "$@"
