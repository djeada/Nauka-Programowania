# ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach
# 
# **Poziom:** ★☆☆
# **Tagi:** `sort`, `dict`
# 
# ### Treść
# 
# Wczytaj `n` par `klucz wartość`.
# a) Wypisz listę par posortowaną rosnąco po kluczach.
# b) Wypisz listę par posortowaną rosnąco po wartościach.
# 
# ### Wejście
# 
# * 1 linia: `n`
# * następnie `n` linii: `klucz wartość`
# 
# ### Wyjście
# 
# * 1 linia: lista par dla a)
# * 2 linia: lista par dla b)
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 4
# c 3
# x 5
# a -2
# b 4
# ```
# 
# **Wyjście:**
# 
# ```
# [('a', -2), ('b', 4), ('c', 3), ('x', 5)]
# [('a', -2), ('c', 3), ('b', 4), ('x', 5)]
# ```

source ../assert.sh

posortuj_wzgledem_napisow() {

    local klucze=($(echo "${!slownik[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

    for klucz in "${klucze[@]}"; do
        echo "$klucz ${slownik[$klucz]};"
    done
}

posortuj_wzgledem_liczb() {

    for klucz in "${!slownik[@]}"; do
        echo "$klucz ${slownik[$klucz]};"
    done | sort -n -k2
}

test_posortuj_wzgledem_napisow() {
    local -A slownik=([a]=2 [c]=1 [b]=3)
    local wynik=($(posortuj_wzgledem_napisow))
    local oczekiwane=(a 2; b 3; c 1;)
    assertElementsEqual wynik oczekiwane $LINENO
}

test_posortuj_wzgledem_liczb() {
    local -A slownik=([a]=2 [c]=1 [b]=3)
    local wynik=($(posortuj_wzgledem_liczb))
    local oczekiwane=(c 1; a 2; b 3;)
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_posortuj_wzgledem_napisow
    test_posortuj_wzgledem_liczb
}

main "$@"

