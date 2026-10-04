# ZAD-12 — Rotacja w lewo / prawo
#
# **Poziom:** ★★☆
# **Tagi:** `listy`, `rotacja`, `modulo`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych, a następnie:
#
# * `kierunek = 0` → rotacja w lewo,
# * `kierunek = 1` → rotacja w prawo,
#
# o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
# * kolejna linia: `kierunek` (0 lub 1)
# * ostatnia linia: `K` (`K ≥ 0`)
#
# ### Wyjście
#
# Jedna linia: lista po rotacji, elementy oddzielone przecinkami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 5
# 27
# 6
# 2
# 1
# 10
# 8
# 0
# 2
# ```
#
# **Wyjście:**
#
# ```
# 6,2,1,10,8,5,27
# ```
#
# ### Uwagi
#
# * Zredukuj `K` przez `K % N`.
source ../assert.sh

# Obraca globalną tablicę `lista` o `liczba` pozycji w podanym kierunku.
rotacja() {
    local kierunek=$1
    local liczba=$2
    local n=${#lista[@]}

    if ((n == 0)); then
        return
    fi

    for ((i = 0; i < liczba % n; i++)); do
        if [[ $kierunek == "prawo" ]]; then
            lista=("${lista[n - 1]}" "${lista[@]:0:n-1}")
        else
            lista=("${lista[@]:1}" "${lista[0]}")
        fi
    done
}

test1() {
    local lista=(5 27 6 2 1 10 8)
    local wynik=(6 2 1 10 8 5 27)
    local kierunek="lewo"
    local liczba=2
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(9 9 42 47 5 6 19 7)
    local wynik=(6 19 7 9 9 42 47 5)
    local kierunek="prawo"
    local liczba=3
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

test3() {
    local lista=(1 2 3)
    local wynik=(3 1 2)
    rotacja prawo 4
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"
