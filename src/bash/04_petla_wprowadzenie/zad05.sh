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
    read a
    read b

    # Określ lo i hi
    if [[ $a -gt $b ]]; then
        lo=$b
        hi=$a
    else
        lo=$a
        hi=$b
    fi

    # a) Wypisz liczby z przedziału (lo, hi)
    for ((i = $(($lo + 1)); i < $hi; i++)); do
        echo $i
    done

    # b) Wypisz liczby z przedziału (lo, hi) podzielne przez 3
    suma=0
    for ((i = $(($lo + 1)); i < $hi; i++)); do
        if [[ $(($i % 3)) -eq 0 ]]; then
            echo $i
            suma=$(($suma + $i))
        fi
    done
    
    # Wypisz sumę liczb podzielnych przez 3
    echo "$suma"
}

main "$@"
