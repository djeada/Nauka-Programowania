# ZAD-06 — Sumowanie elementów ciągu
#
# **Poziom:** ★☆☆
# **Tagi:** `ciągi`, `sumowanie`, `pętle`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:
#
# a) ( \sum_{k=1}^{n} (k^2 + k + 1) )
#
# b) ( \sum_{k=1}^{n} (k^2 + 5k) )
#
# c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))
#
# Wypisz trzy sumy w kolejności a), b), c).
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 1`)
#
# ### Wyjście
#
# Trzy liczby naturalne — każda w oddzielnej linii:
#
# 1. suma dla (a)
# 2. suma dla (b)
# 3. suma dla (c)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# ```
#
# **Wyjście:**
#
# ```
# 10
# 16
# 9
# ```
#
# ### Uwagi o formatowaniu
#
# * Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

main() {
    read n

    # a) suma (k^2 + k + 1) dla k=1..n
    sumaA=0
    for ((k = 1; k <= $n; k++)); do
        sumaA=$(($sumaA + $k * $k + $k + 1))
    done
    echo "$sumaA"

    # b) suma (k^2 + 5k) dla k=1..n
    sumaB=0
    for ((k = 1; k <= $n; k++)); do
        sumaB=$(($sumaB + $k * $k + 5 * $k))
    done
    echo "$sumaB"

    # c) suma (k + 2k) = suma(3k) dla k=1..n
    sumaC=0
    for ((k = 1; k <= $n; k++)); do
        sumaC=$(($sumaC + $k + 2 * $k))
    done
    echo "$sumaC"
}

main "$@"
