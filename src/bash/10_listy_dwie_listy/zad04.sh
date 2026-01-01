# ZAD-04 — Iloczyn skalarny dwóch wektorów 3D
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `wektory`, `math`
#
# ### Treść
#
# Wczytaj dwie listy długości 3 (wektory 3D) i oblicz ich **iloczyn skalarny**:
# [
# A_xB_x + A_yB_y + A_zB_z
# ]
#
# ### Wejście
#
# * 1 linia: wektor A (lista 3 liczb całkowitych)
# * 2 linia: wektor B (lista 3 liczb całkowitych)
#
# ### Wyjście
#
# * 1 linia: jedna liczba całkowita — iloczyn skalarny
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [1, 2, 3]
# [3, 1, 2]
# ```
#
# **Wyjście:**
#
# ```
# 11
# ```

source ../assert.sh

mnozenie_skalarne() {

    local n=$((${#lista_a[@]}))
    local wynik=0

    for ((i = 0; i < n; i++)); do
        wynik=$(echo "${lista_a[$i]} * ${lista_b[$i]}+$wynik" | bc -l)

    done
    echo "$wynik"
}

mnozenie_wektorowe() {

    wynik=()
    wynik+=($(echo "${lista_a[1]} * ${lista_b[2]} - ${lista_a[2]} * ${lista_b[1]}" | bc -l))
    wynik+=($(echo "${lista_a[2]} * ${lista_b[0]} - ${lista_a[0]} * ${lista_b[2]}" | bc -l))
    wynik+=($(echo "${lista_a[0]} * ${lista_b[1]} - ${lista_a[1]} * ${lista_b[0]}" | bc -l))
}

test1() {
    local lista_a=(3 -5 4)
    local lista_b=(2 6 5)
    local wynik=-4
    assertEqual "$(mnozenie_skalarne)" "$wynik" $LINENO
}

test2() {
    local lista_a=(3 -5 4)
    local lista_b=(2 6 5)
    local oczekiwane=(-49 -7 28)
    mnozenie_wektorowe
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"
