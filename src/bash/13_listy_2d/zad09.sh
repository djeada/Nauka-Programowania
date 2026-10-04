# ZAD-09 — Klepsydra o największej sumie
#
# **Poziom:** ★★☆
# **Tagi:** `macierze`, `przeszukiwanie`
#
# ### Treść
#
# Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):
#
# ```
# a b c
#   d
# e f g
# ```
#
# ### Wejście
#
# * 1. linia: `n m`
# * następnie `n` wierszy po `m` liczb całkowitych
#
# ### Wyjście
#
# * 1 linia: maksymalna suma klepsydry
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4 4
# 7 4 2 0
# 4 8 10 8
# 3 6 7 6
# 3 9 19 14
# ```
#
# **Wyjście:**
#
# ```
# 75
# ```

# Uzycie:
#   bash zad09.sh                     - uruchamia testy
#   bash zad09.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca najwieksza sume klepsydry (7 pol z kwadratu 3×3: gorny wiersz, srodek,
# dolny wiersz) w macierzy n×m (argumenty: n, m, a potem elementy wierszami).
# Maksimum zaczynamy od pierwszej klepsydry, a nie od 0 (liczby moga byc ujemne).
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(n*m)
najwieksza_klepsydra() {
    local n=$1 m=$2
    shift 2
    local -a t=("$@")
    local najwieksza="" suma i j

    for ((i = 0; i + 2 < n; i++)); do
        for ((j = 0; j + 2 < m; j++)); do
            suma=$((t[i * m + j] + t[i * m + j + 1] + t[i * m + j + 2] +
                t[(i + 1) * m + j + 1] +
                t[(i + 2) * m + j] + t[(i + 2) * m + j + 1] + t[(i + 2) * m + j + 2]))
            if [[ -z $najwieksza ]] || ((suma > najwieksza)); then
                najwieksza=$suma
            fi
        done
    done

    echo "$najwieksza"
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
    najwieksza_klepsydra "$n" "$m" "${macierz[@]}"
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

test_najwieksza_klepsydra() {
    assertEqual "$(najwieksza_klepsydra 3 3 1 1 1 0 1 0 1 1 1)" 7 $LINENO
    # Same liczby ujemne - wynik tez jest ujemny
    assertEqual "$(najwieksza_klepsydra 3 3 -1 -1 -1 -1 -1 -1 -1 -1 -1)" -7 $LINENO
    # Pole poza klepsydra (srodek lewej kolumny) nie jest liczone
    assertEqual "$(najwieksza_klepsydra 3 4 0 0 0 0 100 0 0 0 0 0 0 1)" 1 $LINENO
}

test_program() {
    sprawdz program $'4 4\n7 4 2 0\n4 8 10 8\n3 6 7 6\n3 9 19 14' "75" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_najwieksza_klepsydra
        test_program
    fi
}

main "$@"
