# ZAD-05 — Co k-ty znak poziomo i pionowo
#
# **Poziom:** ★☆☆
# **Tagi:** `string`, `slicing`, `pętle`
#
# ### Treść
#
# Wczytaj napis i liczbę `k`.
#
# a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
# b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).
#
# ### Wejście
#
# * 1. linia: napis
# * 2. linia: liczba naturalna `k` (k ≥ 1)
#
# ### Wyjście
#
# * (a) 1 linia: znaki oddzielone spacjami
# * (b) wiele linii: każdy znak osobno
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Grzechotnik
# 3
# ```
#
# **Wyjście:**
#
# ```
# z h n
# z
# h
# n
# ```
#
# ### Uwagi o formatowaniu
#
# * Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

# Wypisywanie co k-tego znaku poziomo (z oddzieleniem spacjami)
# Zlozonosc czasowa: O(n/k), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(1)
wypisz_poziomo() {
    local napis="$1"
    local k=$2
    local n=${#napis}
    local wynik=""
    
    # Zbieranie znakow
    for ((i = 0; i < n; i += k)); do
        if [ -z "$wynik" ]; then
            wynik="${napis:$i:1}"
        else
            wynik="$wynik ${napis:$i:1}"
        fi
    done
    
    echo "$wynik"
}

# Wypisywanie co k-tego znaku pionowo (kazdy znak w osobnej linii)
# Zlozonosc czasowa: O(n/k), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(1)
wypisz_pionowo() {
    local napis="$1"
    local k=$2
    local n=${#napis}
    
    for ((i = 0; i < n; i += k)); do
        echo "${napis:$i:1}"
    done
}

main() {
    local napis="hej dzieci jesli chcecie zobaczyc smerfow las"
    local k=3
    
    wypisz_poziomo "$napis" $k
    wypisz_pionowo "$napis" $k
}

main "$@"
