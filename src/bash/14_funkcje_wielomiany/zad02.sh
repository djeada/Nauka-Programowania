# ZAD-02 — Iloczyn wielomianu przez skalar
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `wielomiany`, `skalar`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.
#
# ### Wejście (argumenty funkcji)
#
# * `a` — lista współczynników `[a_n, ..., a_0]`
# * `k` — liczba (całkowita)
#
# ### Wyjście (zwracana wartość)
#
# * lista współczynników wielomianu `k * P(x)`
#
# ### Przykład
#
# Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
# `[-8, 6, -4]`
mnozenie_przez_skalar() {
    local k=$1
    shift
    local wspolczynniki=("$@")

    # Pomnozenie kazdego wspolczynnika przez k
    for wspolczynnik in "${wspolczynniki[@]}"; do
        echo -n "$((wspolczynnik * k)) "
    done
    echo ""
}

main() {
    # Przyklad: wielomian [4, -3, 2] * -2
    local wynik=$(mnozenie_przez_skalar -2 4 -3 2)
    echo "Wynik: $wynik"
}

main "$@"
