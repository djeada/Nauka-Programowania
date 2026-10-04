# ZAD-10 — Obróć macierz o 90° w prawo
#
# **Poziom:** ★★☆
# **Tagi:** `macierze`, `transpozycja`
#
# ### Treść
#
# Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.
#
# ### Wejście
#
# * 1. linia: `n`
# * następnie `n` wierszy po `n` liczb
#
# ### Wyjście
#
# * `n` wierszy obróconej macierzy
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# ```
#
# **Wyjście:**
#
# ```
# 7 4 1
# 8 5 2
# 9 6 3
# ```

# Uzycie:
#   bash zad10.sh                     - uruchamia testy
#   bash zad10.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Wypisuje macierz n×n (argumenty: n, a potem elementy wierszami) obrocona
# o 90° zgodnie z ruchem wskazowek zegara: wiersz i wyniku to kolumna i
# czytana od dolu do gory, czyli wynik[i][j] = macierz[n-1-j][i].
# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(n^2)
obroc_macierz() {
    local n=$1
    shift
    local -a macierz=("$@") wiersz
    local i j

    for ((i = 0; i < n; i++)); do
        wiersz=()
        for ((j = 0; j < n; j++)); do
            wiersz+=("${macierz[(n - 1 - j) * n + i]}")
        done
        echo "${wiersz[*]}"
    done
}

# Wczytuje n oraz n wierszy macierzy ze stdin i wypisuje wynik.
program() {
    local n i
    local -a macierz=() wiersz
    read -r n
    for ((i = 0; i < n; i++)); do
        read -ra wiersz
        macierz+=("${wiersz[@]}")
    done
    obroc_macierz "$n" "${macierz[@]}"
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

test_obroc_macierz() {
    assertEqual "$(obroc_macierz 2 1 2 3 4)" $'3 1\n4 2' $LINENO
    assertEqual "$(obroc_macierz 1 5)" "5" $LINENO
    assertEqual "$(obroc_macierz 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16)" \
        $'13 9 5 1\n14 10 6 2\n15 11 7 3\n16 12 8 4' $LINENO
}

test_program() {
    sprawdz program $'3\n1 2 3\n4 5 6\n7 8 9' $'7 4 1\n8 5 2\n9 6 3' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_obroc_macierz
        test_program
    fi
}

main "$@"
