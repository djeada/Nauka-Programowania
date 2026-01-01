# ZAD-03 — Sprawdzanie warunków logicznych
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `bool`, `warunki`
#
# ### Treść
#
# Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:
#
# a) Czy `a > b`?
# b) Czy `a + b < 10`?
# c) Czy obie liczby są nieparzyste?
# d) Czy `max(a, b) < a^2`?
#
# ### Wejście
#
# Dwa argumenty funkcji:
#
# * `a` (liczba całkowita, `a ≥ 0`)
# * `b` (liczba całkowita, `b ≥ 0`)
#
# ### Wyjście
#
# Cztery wartości logiczne w kolejności a), b), c), d).
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# A, B, C, D = sprawdz_warunki(3, 2)
# print(A)
# print(B)
# print(C)
# print(D)
# ```
#
# **Wyjście:**
#
# ```
# True
# True
# False
# True
# ```

czyWieksza() {

    if [[ $1 -gt $2 ]]; then
        echo true
    else
        echo false
    fi
}

czySumaMniejsza() {
    suma=$(($1 + $2))

    if [[ $suma -lt 10 ]]; then
        echo true
    else
        echo false
    fi
}

czyObieNieparzyste() {
    if [[ $(($1 % 2)) -eq 1 ]] && [[ $(($2 % 2)) -eq 1 ]]; then
        echo true
    else
        echo false
    fi
}

wieksza() {
    if [[ $1 > $2 ]]; then
        return $1
    else
        return $2
    fi
}

czyWiekszaNizKwad() {
    wieksza $1 $2
    wieksza=$?

    if [[ $wieksza -lt $(($1 ** 2)) ]]; then
        echo true
    else
        echo false
    fi
}

main() {
    read a
    read b

    wynik=$(czyWieksza $a $b)

    wynik=$(czySumaMniejsza $a $b)

    wynik=$(czyObieNieparzyste $a $b)

    wynik=$(czyWiekszaNizKwad $a $b)
    echo "Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu $wynik"
}

main "$@"
