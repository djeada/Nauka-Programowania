# ZAD-05 — Obliczenie średniej ważonej
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `float`
#
# ### Treść
#
# Wczytaj dwie listy liczb zmiennoprzecinkowych tej samej długości:
#
# * lista wartości,
# * lista wag.
#
# Oblicz średnią ważoną:
# [
# \frac{\sum (wartość_i \cdot waga_i)}{\sum waga_i}
# ]
#
# ### Wejście
#
# * 1 linia: lista wartości (float)
# * 2 linia: lista wag (float)
#
# ### Wyjście
#
# * 1 linia: jedna liczba zmiennoprzecinkowa — średnia ważona **z dokładnością do 2 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [0.2, 0.4, 0.1, 0.2, 0.1]
# [2.0, 5.0, 0.0, 2.0, 1.0]
# ```
#
# **Wyjście:**
#
# ```
# 0.29
# ```
source ../assert.sh

srednia_wazona() {
    local n=${#wartosci[@]}
    local suma=0
    local suma_iloczynow=0

    for ((i = 0; i < n; i++)); do
        suma=$(echo "${wartosci[$i]} + $suma" | bc -l)
        suma_iloczynow=$(echo "${wartosci[$i]} * ${wagi[$i]} + $suma_iloczynow" | bc -l)
    done

    echo $(bc -l <<<"scale=2; $suma_iloczynow/$suma")
}

test1() {
    local wartosci=(0 -23 -5 2 -3 4 9)
    local wagi=(1 2 3 4 5 6 7)
    local wynik=-1.18
    assertEqual "$(srednia_wazona)" "$wynik" $LINENO
}

test2() {
    local wartosci=(2 5 0 2 1)
    local wagi=(0.2 0.4 0.1 0.2 0.1)
    local wynik=.29
    assertEqual "$(srednia_wazona)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"
