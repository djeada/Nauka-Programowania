# ZAD-01 — Wartość wielomianu w punkcie
#
# **Poziom:** ★☆☆
# **Tagi:** `wielomiany`, `Horner`, `I/O`
#
# ### Treść
#
# Wczytaj współczynniki wielomianu ( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 ) oraz liczbę ( x ). Oblicz wartość wielomianu w punkcie ( x ).

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
    local stopien=2
    local wspolczynniki=(3 2 1)
    local x=1
    local wynik=$(wartosc_wielomianu $x "${wspolczynniki[@]}")
    echo "$wynik"
}

main "$@"
