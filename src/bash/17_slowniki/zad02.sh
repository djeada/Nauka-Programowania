# ZAD-02 — Słownik z dwóch list (klucze i wartości)
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `listy`
#
# ### Treść
#
# Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
# Jeśli długości są różne, wypisz pusty słownik `{}`.
#
# ### Wejście
#
# * 1 linia: `n`
# * 2 linia: `m`
# * następnie `n` liczb (pierwsza lista)
# * następnie `m` liczb (druga lista)
#
# ### Wyjście
#
# * Słownik albo `{}`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 3
# 3 5 8
# 1 2 -1
# ```
#
# **Wyjście:**
#
# ```
# {3: 1, 5: 2, 8: -1}
# ```
source ../assert.sh

zbuduj_slownik() {
    local -a lista_a=($1)
    local -a lista_b=($2)
    local -A slownik=()
    local n=${#lista_a[@]}

    for ((i = 0; i < n; i++)); do
        slownik[${lista_a[i]}]=${lista_b[i]}
    done

    for k in "${!slownik[@]}"; do
        echo "$k: ${slownik[$k]};"
    done
}

test_zbuduj_slownik() {
    local wynik=($(zbuduj_slownik "1 2 3 4 5" "a b c d e"))
    local oczekiwane=(
        "1: a;"
        "2: b;"
        "3: c;"
        "4: d;"
        "5: e;"
    )
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_zbuduj_slownik
}

main "$@"
