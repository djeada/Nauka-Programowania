# ZAD-05 — Liczby z przedziału
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `przedziały`, `modulo`
#
# ### Treść
#
# Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:
#
# * `lo = min(a, b)`
# * `hi = max(a, b)`
#
# Następnie:
#
# a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).
#
# b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).
#
# ### Wejście
#
# Dwie liczby naturalne:
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 9
# 5
# ```
#
# **Wyjście:**
#
# ```
# 6
# 7
# 8
# 6
# ```
#
# ### Uwagi o formatowaniu
#
# * Nie wypisuj nagłówków typu „a)” i „b)”.
# * Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
# * Nie dodawaj pustej linii między podpunktami.

main() {

    echo "Podaj dwie liczby:"
    read a
    read b

    if [[ $a -gt $b ]]; then
        echo "swap"
        temp=$a
        a=$b
        b=$temp
    fi

    echo "Liczby naturalne wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for ((i = $(($a + 1)); i < $b; i++)); do
        echo $i
    done

    echo "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for ((i = $(($a + 1)); i < $b; i++)); do
        if [[ $(($i % 3)) -eq 0 ]]; then
            echo $i
        fi
    done
}

main "$@"
