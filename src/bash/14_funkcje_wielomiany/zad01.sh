# ZAD-01 — Wartość wielomianu w punkcie
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `wielomiany`, `Horner`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.
#
# ### Wejście (argumenty funkcji)
#
# * `a` — lista współczynników `[a_n, ..., a_0]`
# * `x` — liczba naturalna (lub całkowita)
#
# ### Wyjście (zwracana wartość)
#
# * jedna liczba (całkowita)
#
# ### Przykład
#
# Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
# `6`
#
# ### Uwagi
#
# * Najprościej użyć schematu Hornera.

# Funkcja obliczajaca wartosc wielomianu w punkcie (schemat Hornera)
# Zlozonosc czasowa: O(n), gdzie n to stopien wielomianu
# Zlozonosc pamieciowa: O(1)
wartosc_wielomianu() {
    local x=$1
    shift
    local wspolczynniki=("$@")
    local n=${#wspolczynniki[@]}
    
    # Schemat Hornera: W(x) = (...((a_n * x + a_(n-1)) * x + a_(n-2))... + a_0)
    local wynik=${wspolczynniki[0]}
    for ((i = 1; i < n; i++)); do
        wynik=$((wynik * x + wspolczynniki[i]))
    done
    
    echo $wynik
}

main() {
    # Przyklad: wielomian 3x^2 + 2x + 1 dla x=1
    local wynik=$(wartosc_wielomianu 1 3 2 1)
    echo "Wartosc wielomianu: $wynik"
}

main "$@"
