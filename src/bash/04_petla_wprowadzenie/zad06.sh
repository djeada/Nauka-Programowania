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

    echo "Podaj liczbe:"
    read n

    suma=0

    for ((i = 1; i <= $n; i++)); do
        a_n=$(echo "scale=2; $i/$(($i + 1))" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n/(n+1) dla n=$n: $suma"

    suma=0

    for ((i = 1; i <= $n; i++)); do
        a_n=$(echo "scale=2; $(($n ** 2 + 5))/$n" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem (n^2 + 5)/n dla n=$n: $suma"

    suma=0

    for ((i = 1; i <= $n; i++)); do
        a_n=$(($n + 2 ** $n))
        suma=$(($suma + $a_n))

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n + 2^n dla n=$n: $suma"

}

main "$@"
