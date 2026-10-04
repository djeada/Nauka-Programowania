# ZAD-08 — Indeks klucza w cyklicznie posortowanej liście
#
# **Poziom:** ★★☆
# **Tagi:** `binary search`, `rotacja`, `list`
#
# ### Treść
#
# Otrzymujesz cyklicznie posortowaną listę liczb całkowitych (lista była rosnąca, ale została przesunięta) oraz klucz. Znajdź indeks **pierwszego** wystąpienia klucza. Jeśli klucza nie ma — wypisz `-1`.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * 2 linia: `N` liczb całkowitych oddzielonych spacjami
# * 3 linia: liczba całkowita `x` (szukany klucz)
#
# ### Wyjście
#
# * 1 linia: indeks pierwszego wystąpienia `x` albo `-1`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 6
# 3 4 5 6 1 2
# 4
# ```
#
# **Wyjście:**
#
# ```
# 1
# ```
#
# ### Ograniczenia / gwarancje
#
# * Lista jest wynikiem rotacji listy posortowanej niemalejąco (mogą wystąpić duplikaty).
source ../assert.sh

# Zwraca indeks punktu obrotu cyklicznie posortowanej listy, czyli indeks
# pierwszego elementu drugiego posortowanego fragmentu (0, gdy lista nie
# została obrócona). Obsługuje duplikaty.
# Złożoność czasowa: O(log n), w najgorszym przypadku (duplikaty) O(n)
# Złożoność pamięciowa: O(1)
znajdz_punkt_obrotu() {
    local -n _lista_obrot_ref="$1"
    local lewo=0
    local prawo=$((${#_lista_obrot_ref[@]} - 1))
    local srodek

    while ((lewo < prawo)); do
        srodek=$(((lewo + prawo) / 2))

        if ((_lista_obrot_ref[srodek] > _lista_obrot_ref[prawo])); then
            lewo=$((srodek + 1))
        elif ((_lista_obrot_ref[srodek] < _lista_obrot_ref[prawo])); then
            prawo=$srodek
        elif ((_lista_obrot_ref[prawo - 1] > _lista_obrot_ref[prawo])); then
            echo $prawo
            return
        else
            prawo=$((prawo - 1))
        fi
    done

    echo $lewo
}

# Wyszukiwanie binarne pierwszego wystąpienia klucza w posortowanym
# fragmencie listy o indeksach [lewo, prawo]. Zwraca -1, gdy klucza nie ma.
# Złożoność czasowa: O(log n)
# Złożoność pamięciowa: O(1)
pierwsze_wystapienie() {
    local -n _lista_szukaj_ref="$1"
    local klucz=$2
    local lewo=$3
    local prawo=$4
    local wynik=-1
    local srodek

    while ((lewo <= prawo)); do
        srodek=$(((lewo + prawo) / 2))

        if ((_lista_szukaj_ref[srodek] < klucz)); then
            lewo=$((srodek + 1))
        else
            if ((_lista_szukaj_ref[srodek] == klucz)); then
                wynik=$srodek
            fi
            prawo=$((srodek - 1))
        fi
    done

    echo $wynik
}

# Zwraca indeks pierwszego wystąpienia klucza w cyklicznie posortowanej
# liście albo -1, jeśli klucza nie ma. Lista składa się z dwóch posortowanych
# fragmentów: [0, punkt_obrotu) oraz [punkt_obrotu, n), a każdy element
# pierwszego fragmentu jest nie mniejszy niż elementy drugiego - dlatego
# najpierw przeszukujemy pierwszy fragment.
# Złożoność czasowa: O(log n), w najgorszym przypadku (duplikaty) O(n)
# Złożoność pamięciowa: O(1)
znajdz_klucz() {
    local -n _lista_klucz_ref="$1"
    local klucz=$2
    local n=${#_lista_klucz_ref[@]}
    local punkt_obrotu
    local wynik

    punkt_obrotu=$(znajdz_punkt_obrotu "$1")
    wynik=$(pierwsze_wystapienie "$1" "$klucz" 0 $((punkt_obrotu - 1)))

    if ((wynik == -1)); then
        wynik=$(pierwsze_wystapienie "$1" "$klucz" "$punkt_obrotu" $((n - 1)))
    fi

    echo $wynik
}

test_znajdz_klucz_przyklad() {
    local lista=(3 4 5 6 1 2)
    assertEqual "$(znajdz_klucz lista 4)" 1 $LINENO
    assertEqual "$(znajdz_klucz lista 1)" 4 $LINENO
    assertEqual "$(znajdz_klucz lista 2)" 5 $LINENO
}

test_znajdz_klucz_obrocona() {
    local lista=(27 31 32 3 5 9 10 15)
    assertEqual "$(znajdz_klucz lista 31)" 1 $LINENO
    assertEqual "$(znajdz_klucz lista 15)" 7 $LINENO
}

test_brak_klucza() {
    local lista=(4 7 12 32 51 90 100 1 2)
    assertEqual "$(znajdz_klucz lista -5)" -1 $LINENO
    assertEqual "$(znajdz_klucz lista 50)" -1 $LINENO

    local pusta=()
    assertEqual "$(znajdz_klucz pusta 1)" -1 $LINENO
}

test_lista_nieobrocona() {
    local lista=(1 2 3 4 5)
    assertEqual "$(znajdz_klucz lista 1)" 0 $LINENO
    assertEqual "$(znajdz_klucz lista 5)" 4 $LINENO
}

test_duplikaty() {
    local lista=(2 2 3 1 2 2)
    assertEqual "$(znajdz_klucz lista 2)" 0 $LINENO
    assertEqual "$(znajdz_klucz lista 1)" 3 $LINENO

    local lista2=(5 6 1 1 1 2)
    assertEqual "$(znajdz_klucz lista2 1)" 2 $LINENO

    local lista3=(1 1 1 0 1)
    assertEqual "$(znajdz_klucz lista3 0)" 3 $LINENO
    assertEqual "$(znajdz_klucz lista3 1)" 0 $LINENO
}

main() {
    test_znajdz_klucz_przyklad
    test_znajdz_klucz_obrocona
    test_brak_klucza
    test_lista_nieobrocona
    test_duplikaty
}

main "$@"
