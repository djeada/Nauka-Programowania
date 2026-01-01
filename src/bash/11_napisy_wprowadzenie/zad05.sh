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

wypisz_poziomo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for ((i = 0; i < n; i += k)); do
        echo -n "${napis:$i:1} "
    done
    echo ""
}

wypisz_pionowo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for ((i = 0; i < n; i += k)); do
        echo "${napis:$i:1} "
    done
}

main() {
    local napis="hej dzieci jesli chcecie zobaczyc smerfow las"
    local k=3

    wypisz_poziomo "$napis" $k
    wypisz_pionowo "$napis" $k
}

main "$@"
