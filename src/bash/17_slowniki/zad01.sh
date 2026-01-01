# ZAD-01 — Słownik: liczby i ich kwadraty
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `pętla`
# 
# ### Treść
# 
# Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.
# 
# ### Wejście
# 
# * 1 linia: `n` (n ≥ 1)
# 
# ### Wyjście
# 
# * Słownik w postaci: `{1: 1, 2: 4, ...}`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 5
# ```
# 
# **Wyjście:**
# 
# ```
# {1: 1, 2: 4, 3: 9, 4: 16}
# ```

source ../assert.sh

zbuduj_slownik() {
    local liczba=$1
    local -A slownik=()
    for ((i=0; i<liczba; i++)); do
        slownik[$i]=$((i*i))
    done
    for k in "${!slownik[@]}"; do
        for k in "${!slownik[@]}"; do
            echo "$k: ${slownik[$k]};"
        done
    }

    test_zbuduj_slownik() {
        local wynik=($(zbuduj_slownik 10))
        local oczekiwane=("0: 0;" "1: 1;" "2: 4;" "3: 9;" "4: 16;" "5: 25;" "6: 36;" "7: 49;" "8: 64;" "9: 81;")
        assertArrayEqual wynik oczekiwane $LINENO
    }

    main() {
        test_zbuduj_slownik
    }

    main "$@"

