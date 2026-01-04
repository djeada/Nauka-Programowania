# ZAD-08 — Usuń klucz
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `remove`, `wyszukiwanie`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie `klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii, elementy oddzielone przecinkami.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
# * ostatnia linia: `klucz` (liczba całkowita)
#
# ### Wyjście
#
# Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 6
# 2
# 1
# 4
# 27
# 4
# ```
#
# **Wyjście:**
#
# ```
# 6,2,1,27
# ```
#
# ### Uwagi
#
# * Jeśli `klucz` nie występuje, wypisz listę bez zmian.
source ../assert.sh

usun() {
    local klucz=$1
    local pom=()
    for liczba in "${lista[@]}"; do
        [ $liczba -ne $klucz ] && pom+=($liczba)
    done
    lista=("${pom[@]}")
    unset pom
}

test1() {
    local lista=(6 7 2 1 8)
    local wynik=(6 7 1 8)
    local klucz=2
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(1 1 1 1)
    local wynik=()
    local klucz=1
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"
