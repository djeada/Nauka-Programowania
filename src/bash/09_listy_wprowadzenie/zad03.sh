# ZAD-03 — Pierwsze wystąpienie klucza
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `wyszukiwanie`, `indeksy`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
# Jeśli `klucz` nie występuje — wypisz `-1`.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
# * ostatnia linia: `klucz` (liczba całkowita)
#
# ### Wyjście
#
# Jedna liczba całkowita — indeks (od `0`) lub `-1`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 2
# 9
# -1
# 3
# 8
# -1
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
source ../assert.sh

znajdz_klucz_v1() {

    local n=${#lista[@]}

    for ((i = 0; i < n; i++)); do
        if [ ${lista[$i]} -eq $1 ]; then
            echo $i
            return
        fi
    done

    echo -1
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    local a=2
    local wynik=6
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}

test2() {
    local lista=(3 -2 4 9 -3 -40 8 5 -7 -1)
    local a=2
    local wynik=-1
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"
