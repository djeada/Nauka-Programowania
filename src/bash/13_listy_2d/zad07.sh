# ZAD-07 — Zerowanie macierzy
#
# **Poziom:** ★★☆
# **Tagi:** `macierze`, `indeksy`
#
# ### Treść
#
# Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).
#
# ### Wejście
#
# * 1. linia: `n m`
# * następnie `n` wierszy po `m` liczb
#
# ### Wyjście
#
# * `n` wierszy zmodyfikowanej macierzy
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3 3
# 1 2 3
# 4 0 6
# 7 8 9
# ```
#
# **Wyjście:**
#
# ```
# 1 0 3
# 0 0 0
# 7 0 9
# ```

# Uzycie:
#   bash zad07.sh                     - uruchamia testy
#   bash zad07.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zeruje wiersz i kolumne kazdego zera macierzy n×m (argumenty: n, m, a potem
# elementy wierszami) i wypisuje wynikowa macierz.
# Najpierw zapamietujemy wiersze i kolumny z zerami, dopiero potem zerujemy.
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(n + m) (poza sama macierza)
wyzeruj_macierz() {
    local n=$1 m=$2
    shift 2
    local -a macierz=("$@") wiersze_z_zerem=() kolumny_z_zerem=() wiersz
    local i j

    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < m; j++)); do
            if ((macierz[i * m + j] == 0)); then
                wiersze_z_zerem[i]=1
                kolumny_z_zerem[j]=1
            fi
        done
    done

    for ((i = 0; i < n; i++)); do
        wiersz=()
        for ((j = 0; j < m; j++)); do
            if [[ -n ${wiersze_z_zerem[i]:-} || -n ${kolumny_z_zerem[j]:-} ]]; then
                wiersz+=(0)
            else
                wiersz+=("${macierz[i * m + j]}")
            fi
        done
        echo "${wiersz[*]}"
    done
}

# Wczytuje "n m" oraz n wierszy macierzy ze stdin i wypisuje wynik.
program() {
    local n m i
    local -a macierz=() wiersz
    read -r n m
    for ((i = 0; i < n; i++)); do
        read -ra wiersz
        macierz+=("${wiersz[@]}")
    done
    wyzeruj_macierz "$n" "$m" "${macierz[@]}"
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

test_wyzeruj_macierz() {
    assertEqual "$(wyzeruj_macierz 3 4 0 1 2 0 3 4 5 2 1 3 1 5)" \
        $'0 0 0 0\n0 4 5 0\n0 3 1 0' $LINENO
    assertEqual "$(wyzeruj_macierz 2 2 1 2 3 4)" $'1 2\n3 4' $LINENO
    assertEqual "$(wyzeruj_macierz 1 1 0)" "0" $LINENO
    assertEqual "$(wyzeruj_macierz 2 3 -1 0 2 3 4 5)" $'0 0 0\n3 0 5' $LINENO
}

test_program() {
    sprawdz program $'3 3\n1 2 3\n4 0 6\n7 8 9' $'1 0 3\n0 0 0\n7 0 9' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_wyzeruj_macierz
        test_program
    fi
}

main "$@"
