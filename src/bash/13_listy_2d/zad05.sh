# ZAD-05 — Czy macierz jest magiczna?
#
# **Poziom:** ★★☆
# **Tagi:** `macierze`, `suma`, `warunki`
#
# ### Treść
#
# Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.
#
# ### Wejście
#
# * 1. linia: `n`
# * następnie `n` wierszy po `n` liczb
#
# ### Wyjście
#
# * `Prawda` albo `Fałsz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 6 7 2
# 1 5 9
# 8 3 4
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Sprawdza, czy macierz n×n (argumenty: n, a potem elementy wierszami) jest
# kwadratem magicznym. Wypisuje "Prawda" albo "Fałsz".
# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(n^2)
czy_kwadrat_magiczny() {
    local n=$1
    shift
    local -a macierz=("$@")
    local wzorzec=0 przekatna=0 antyprzekatna=0 suma_wiersza suma_kolumny i j

    # Suma pierwszego wiersza jest wzorcem dla pozostalych sum
    for ((j = 0; j < n; j++)); do
        ((wzorzec += macierz[j]))
    done

    for ((i = 0; i < n; i++)); do
        suma_wiersza=0
        suma_kolumny=0
        for ((j = 0; j < n; j++)); do
            ((suma_wiersza += macierz[i * n + j]))
            ((suma_kolumny += macierz[j * n + i]))
        done
        if ((suma_wiersza != wzorzec || suma_kolumny != wzorzec)); then
            echo "Fałsz"
            return
        fi
        ((przekatna += macierz[i * n + i]))
        ((antyprzekatna += macierz[i * n + n - 1 - i]))
    done

    if ((przekatna == wzorzec && antyprzekatna == wzorzec)); then
        echo "Prawda"
    else
        echo "Fałsz"
    fi
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
    czy_kwadrat_magiczny "$n" "${macierz[@]}"
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

test_czy_kwadrat_magiczny() {
    assertEqual "$(czy_kwadrat_magiczny 3 6 7 2 1 5 9 8 3 4)" "Prawda" $LINENO
    assertEqual "$(czy_kwadrat_magiczny 4 16 3 2 13 5 10 11 8 9 6 7 12 4 15 14 1)" "Prawda" $LINENO
    assertEqual "$(czy_kwadrat_magiczny 2 2 2 2 2)" "Prawda" $LINENO
    assertEqual "$(czy_kwadrat_magiczny 1 7)" "Prawda" $LINENO
    assertEqual "$(czy_kwadrat_magiczny 2 1 2 3 4)" "Fałsz" $LINENO
    # Wiersze, kolumny i glowna przekatna maja sume 6, druga przekatna 9
    assertEqual "$(czy_kwadrat_magiczny 3 1 2 3 2 3 1 3 1 2)" "Fałsz" $LINENO
}

test_program() {
    sprawdz program $'3\n6 7 2\n1 5 9\n8 3 4' "Prawda" $LINENO
    sprawdz program $'2\n1 2\n3 4' "Fałsz" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_czy_kwadrat_magiczny
        test_program
    fi
}

main "$@"
