# ZAD-06 — Histogram znaków w słowie
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.
# 
# ### Wejście
# 
# * 1 linia: napis
# 
# ### Wyjście
# 
# * Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# klasa
# ```
# 
# **Wyjście:**
# 
# ```
# {'k': 1, 'l': 1, 'a': 2, 's': 1}
# ```

source ../assert.sh

histogram_znakow() {
    local napis=$1
    local -A histogram=()
    for (( i=0; i<${#napis}; i++ )); do
        ((histogram["${napis:$i:1}"]++))
    done
    for znak in ${!histogram[@]}; do
        echo "$znak: ${histogram[$znak]};"
    done
}

test_histogram_znakow() {
    local napis="ala ma kota"
    local wynik=($(histogram_znakow "$napis"))
    local oczekiwane=(a:4; l:1; m:1; k:1; o:1; t:1)
    assertIdenticalElements wynik oczekiwane $LINENO
}

main() {
    test_histogram_znakow
}

main "$@"

