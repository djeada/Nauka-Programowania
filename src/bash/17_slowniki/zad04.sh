# ZAD-04 — Usuń pary ze słownika na podstawie wartości
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `filtrowanie`
#
# ### Treść
#
# Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.
#
# ### Wejście
#
# * 1 linia: `n`
# * następnie `n` linii: `klucz wartość`
# * ostatnia linia: `k`
#
# ### Wyjście
#
# * Słownik po usunięciu par
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4
# aaa 5
# abc 1
# xxx 5
# cba 3
# 5
# ```
#
# **Wyjście:**
#
# ```
# {'abc': 1, 'cba': 3}
# ```

source ../assert.sh

usun_ze_slownika() {
    local klucz="$1"

    for k in "${!slownik[@]}"; do
        if [[ ${slownik["$k"]} == "$klucz" ]]; then
            unset slownik["$k"]
        fi
    done
}

test_usun_ze_slownika() {
    local -A slownik=([a]=1 [b]=2 [c]=3 [d]=1)
    local -A oczekiwane_wartosci=([b]=2 [c]=3)
    usun_ze_slownika 1
    assertArrayEqual slownik oczekiwane_wartosci
}

main() {
    test_usun_ze_slownika
}

main "$@"
