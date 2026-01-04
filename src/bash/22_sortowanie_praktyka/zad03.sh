# ZAD-03 — Sortowanie listy par względem kryterium
#
# **Poziom:** ★☆☆
# **Tagi:** `sort`, `tuple`, `list`
#
# ### Treść
#
# Otrzymujesz listę par `(napis, liczba)`.
#
# a) Posortuj pary rosnąco po liczbie.
# b) Posortuj pary rosnąco po długości napisu.
#
# Wypisz wyniki dla a) i b) w osobnych liniach.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * następnie `N` linii: `napis liczba` (napis bez spacji)
#
# ### Wyjście
#
# * 1 linia: lista par posortowana jak w podpunkcie a)
# * 2 linia: lista par posortowana jak w podpunkcie b)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ab 3
# bca 1
# c 2
# ```
#
# **Wyjście:**
#
# ```
# [('bca', 1), ('c', 2), ('ab', 3)]
# [('c', 2), ('ab', 3), ('bca', 1)]
# ```
source ../assert.sh

# Sortuje listę par względem napisów (pierwszej części pary).
# Złożoność czasowa: O(n log n), gdzie n to liczba par
# Złożoność pamięciowa: O(n)
posortuj_wzgledem_napisow() {
    local _lista_ref=("$@")
    echo "${_lista_ref[@]}" | tr ' ' '\n' | sort -u
}

# Sortuje listę par względem liczb (drugiej części pary).
# Złożoność czasowa: O(n log n), gdzie n to liczba par
# Złożoność pamięciowa: O(n)
posortuj_wzgledem_liczb() {
    local _lista_ref=("$@")
    echo "${_lista_ref[@]}" | tr ' ' '\n' | sort -t ':' -k 2 -n
}

test_posortuj_wzgledem_napisow() {
    local lista_par=('a:2' 'c:1' 'b:3')
    local wynik=($(posortuj_wzgledem_napisow "${lista_par[@]}"))
    local oczekiwane=('a:2' 'b:3' 'c:1')
    assertSetsEqual wynik oczekiwane $LINENO
}

test_posortuj_wzgledem_liczb() {
    local lista_par=('a:2' 'c:1' 'b:3')
    local wynik=($(posortuj_wzgledem_liczb "${lista_par[@]}"))
    local oczekiwane=('c:1' 'a:2' 'b:3')
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_posortuj_wzgledem_napisow
    test_posortuj_wzgledem_liczb
}

main "$@"
