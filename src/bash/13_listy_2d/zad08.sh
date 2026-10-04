# ZAD-08 — Wypisanie elementów macierzy spiralnie
#
# **Poziom:** ★★☆
# **Tagi:** `macierze`, `spirala`
#
# ### Treść
#
# Wczytaj macierz `n×m` i wypisz jej elementy spiralnie (zgodnie z ruchem wskazówek zegara), startując z lewego górnego rogu.
#
# ### Wejście
#
# * 1. linia: `n m`
# * następnie `n` wierszy po `m` liczb
#
# ### Wyjście
#
# * 1 linia: elementy spiralnie, oddzielone spacjami
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# ```
#
# **Wyjście:**
#
# ```
# 1 2 3 6 9 8 7 4 5
# ```

# Uzycie:
#   bash zad08.sh                     - uruchamia testy
#   bash zad08.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Wypisuje elementy macierzy n×m (argumenty: n, m, a potem elementy wierszami)
# spiralnie, zgodnie z ruchem wskazowek zegara.
# Zawezamy cztery granice: gora, dol, lewo, prawo.
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(n*m)
spirala() {
    local n=$1 m=$2
    shift 2
    local -a macierz=("$@") wynik=()
    local gora=0 dol=$((n - 1)) lewo=0 prawo=$((m - 1)) i j

    while ((gora <= dol && lewo <= prawo)); do
        for ((j = lewo; j <= prawo; j++)); do
            wynik+=("${macierz[gora * m + j]}")
        done
        ((gora++))

        for ((i = gora; i <= dol; i++)); do
            wynik+=("${macierz[i * m + prawo]}")
        done
        ((prawo--))

        if ((gora <= dol)); then
            for ((j = prawo; j >= lewo; j--)); do
                wynik+=("${macierz[dol * m + j]}")
            done
            ((dol--))
        fi

        if ((lewo <= prawo)); then
            for ((i = dol; i >= gora; i--)); do
                wynik+=("${macierz[i * m + lewo]}")
            done
            ((lewo++))
        fi
    done

    echo "${wynik[*]}"
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
    spirala "$n" "$m" "${macierz[@]}"
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

test_spirala() {
    assertEqual "$(spirala 3 4 1 2 3 4 5 6 7 8 9 10 11 12)" "1 2 3 4 8 12 11 10 9 5 6 7" $LINENO
    assertEqual "$(spirala 4 3 1 2 3 4 5 6 7 8 9 10 11 12)" "1 2 3 6 9 12 11 10 7 4 5 8" $LINENO
    assertEqual "$(spirala 1 4 1 2 3 4)" "1 2 3 4" $LINENO
    assertEqual "$(spirala 4 1 1 2 3 4)" "1 2 3 4" $LINENO
    assertEqual "$(spirala 2 2 1 2 3 4)" "1 2 4 3" $LINENO
    assertEqual "$(spirala 1 1 5)" "5" $LINENO
}

test_program() {
    sprawdz program $'3 3\n1 2 3\n4 5 6\n7 8 9' "1 2 3 6 9 8 7 4 5" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_spirala
        test_program
    fi
}

main "$@"
