# ZAD-05 — Sortowanie listy miast
#
# **Poziom:** ★☆☆
# **Tagi:** `class`, `sort`, `obiekty`
#
# ### Treść
#
# Masz klasę `Miasto` z polami:
#
# * `nazwa` (napis),
# * `liczba_mieszkancow` (liczba naturalna).
#
# Otrzymujesz listę miast.
#
# a) Posortuj miasta alfabetycznie po nazwie.
# b) Posortuj miasta rosnąco po liczbie mieszkańców.
#
# Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.
#
# ### Wejście
#
# * 1 linia: liczba naturalna `N`
# * następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)
#
# ### Wyjście
#
# * 1 linia: lista miast po sortowaniu a)
# * 2 linia: lista miast po sortowaniu b)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# Paris 2150000
# Berlin 3800000
# New_York 8400000
# ```
#
# **Wyjście:**
#
# ```
# [Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
# [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
# ```
#
# ### Uwagi o formatowaniu
#
# * Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.
source ../assert.sh

# Miasto reprezentujemy jako napis "nazwa:liczba_mieszkancow"
# (nazwa nie zawiera spacji ani dwukropków).

# Tworzy miasto o podanej nazwie i liczbie mieszkańców.
miasto() {
    echo "$1:$2"
}

# Zamienia miasto na napis w formacie Miasto("NAZWA", LICZBA).
miasto_na_napis() {
    local nazwa="${1%:*}"
    local liczba_mieszkancow="${1##*:}"
    printf 'Miasto("%s", %s)' "$nazwa" "$liczba_mieszkancow"
}

# Zamienia listę miast na napis w formacie [Miasto("A", 1), Miasto("B", 2)].
lista_miast_na_napis() {
    local -n _miasta_napis_ref="$1"
    local wynik="["
    local i

    for ((i = 0; i < ${#_miasta_napis_ref[@]}; i++)); do
        if ((i > 0)); then
            wynik+=", "
        fi
        wynik+="$(miasto_na_napis "${_miasta_napis_ref[$i]}")"
    done

    echo "$wynik]"
}

# Sortuje miasta alfabetycznie po nazwie.
# Złożoność czasowa: O(n log n), gdzie n to liczba miast
# Złożoność pamięciowa: O(n)
sortuj_po_nazwie() {
    local -n _miasta_nazwa_ref="$1"

    if ((${#_miasta_nazwa_ref[@]} == 0)); then
        return
    fi

    mapfile -t _miasta_nazwa_ref < <(printf '%s\n' "${_miasta_nazwa_ref[@]}" | LC_ALL=C sort -s -t ':' -k1,1)
}

# Sortuje miasta rosnąco po liczbie mieszkańców.
# Złożoność czasowa: O(n log n), gdzie n to liczba miast
# Złożoność pamięciowa: O(n)
sortuj_po_liczbie_mieszkancow() {
    local -n _miasta_liczba_ref="$1"

    if ((${#_miasta_liczba_ref[@]} == 0)); then
        return
    fi

    mapfile -t _miasta_liczba_ref < <(printf '%s\n' "${_miasta_liczba_ref[@]}" | LC_ALL=C sort -s -t ':' -k2,2n)
}

test_sortuj_po_nazwie() {
    local miasta=("$(miasto Paris 2150000)" "$(miasto Berlin 3800000)" "$(miasto New_York 8400000)")
    local oczekiwane=("Berlin:3800000" "New_York:8400000" "Paris:2150000")
    sortuj_po_nazwie miasta
    assertArrayEqual miasta oczekiwane $LINENO
}

test_sortuj_po_liczbie_mieszkancow() {
    local miasta=("$(miasto Paris 2150000)" "$(miasto Berlin 3800000)" "$(miasto New_York 8400000)" "$(miasto Rzym 999)")
    local oczekiwane=("Rzym:999" "Paris:2150000" "Berlin:3800000" "New_York:8400000")
    sortuj_po_liczbie_mieszkancow miasta
    assertArrayEqual miasta oczekiwane $LINENO
}

test_lista_miast_na_napis() {
    local miasta=("Paris:2150000" "Berlin:3800000" "New_York:8400000")
    local oczekiwane='[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]'
    assertEqual "$(lista_miast_na_napis miasta)" "$oczekiwane" $LINENO

    local puste=()
    assertEqual "$(lista_miast_na_napis puste)" "[]" $LINENO
}

test_przyklad() {
    local miasta=("Paris:2150000" "Berlin:3800000" "New_York:8400000")
    local po_nazwie=("${miasta[@]}")
    local po_liczbie=("${miasta[@]}")
    sortuj_po_nazwie po_nazwie
    sortuj_po_liczbie_mieszkancow po_liczbie

    assertEqual "$(lista_miast_na_napis po_nazwie)" \
        '[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]' $LINENO
    assertEqual "$(lista_miast_na_napis po_liczbie)" \
        '[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]' $LINENO
}

main() {
    test_sortuj_po_nazwie
    test_sortuj_po_liczbie_mieszkancow
    test_lista_miast_na_napis
    test_przyklad
}

main "$@"
