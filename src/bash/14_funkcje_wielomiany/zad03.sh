# ZAD-03 — Suma wielomianów
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `wielomiany`, `listy`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` (mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

# Funkcja dodajaca dwa wielomiany
# Zlozonosc czasowa: O(max(n, m))
# Zlozonosc pamieciowa: O(max(n, m))
suma_wielomianow() {
    local rozmiar_a=$1
    shift
    local wspolczynniki_a=()
    for ((i = 0; i < rozmiar_a; i++)); do
        wspolczynniki_a+=("$1")
        shift
    done
    
    local rozmiar_b=$1
    shift
    local wspolczynniki_b=()
    for ((i = 0; i < rozmiar_b; i++)); do
        wspolczynniki_b+=("$1")
        shift
    done
    
    # Wyrownanie dlugosci - dodanie zer na poczatku krotszej listy
    local maks_rozmiar=$((rozmiar_a > rozmiar_b ? rozmiar_a : rozmiar_b))
    local roznica_a=$((maks_rozmiar - rozmiar_a))
    local roznica_b=$((maks_rozmiar - rozmiar_b))
    
    # Dodanie wiodacych zer do krotszej listy
    for ((i = 0; i < roznica_a; i++)); do
        wspolczynniki_a=("0" "${wspolczynniki_a[@]}")
    done
    for ((i = 0; i < roznica_b; i++)); do
        wspolczynniki_b=("0" "${wspolczynniki_b[@]}")
    done
    
    # Dodawanie wspolczynnikow
    for ((i = 0; i < maks_rozmiar; i++)); do
        echo -n "$((wspolczynniki_a[i] + wspolczynniki_b[i])) "
    done
    echo ""
}

main() {
    # Przyklad: [3, 5, 2] + [2, -8, 1]
    local wynik=$(suma_wielomianow 3 3 5 2 3 2 -8 1)
    echo "Wynik: $wynik"
}

main "$@"
