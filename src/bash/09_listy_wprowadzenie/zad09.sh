# ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `duplikaty`, `set`
#
# ### Treść
#
# Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby naturalne
#
# ### Wyjście
#
# Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 6
# 3
# 2
# 1
# 3
# 2
# 2
# ```
#
# **Wyjście:**
#
# ```
# 3,2,1
# ```

source ../assert.sh

usun_duplikaty() {
    local pom=()
    declare -A histo

    for liczba in "${lista[@]}"; do
        if [[ -z ${histo["$liczba"]} ]]; then
            pom+=("$liczba")
            histo["$liczba"]=1
        fi
    done
    lista=("${pom[@]}")
    unset histo
    unset pom
}

test1() {
    local lista=(3 5 3 3 2)
    local wynik=(3 5 2)
    usun_duplikaty
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
}

main "$@"
