# ZAD-02 — Iloczyn wielomianu przez skalar
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `wielomiany`, `skalar`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

# Funkcja mnozaca wielomian przez skalar
# Zlozonosc czasowa: O(n), gdzie n to stopien wielomianu
# Zlozonosc pamieciowa: O(n)
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
