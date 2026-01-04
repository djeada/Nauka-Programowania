# ZAD-03 — Minimalny iloczyn trzech liczb
#
# **Poziom:** ★★☆
# **Tagi:** `list`, `min`, `math`
#
# ### Treść
#
# Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech liczb** wybranych z tej listy.
#
# Jeśli lista zawiera mniej niż 3 liczby — wypisz iloczyn wszystkich elementów listy.
#
# ### Wejście
#
# * 1 linia: lista liczb całkowitych `A`
#
# ### Wyjście
#
# * 1 linia: jedna liczba całkowita
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [3, -1, -3, 2, 9, 4]
# ```
#
# **Wyjście:**
#
# ```
# -108
# ```
source ../assert.sh

# Znajduje minimalny iloczyn trzech liczb z listy.
# Złożoność czasowa: O(n log n), gdzie n to liczba elementów
# Złożoność pamięciowa: O(n)
minimalny_iloczyn_trzech() {
    local -n _lista_ref=$1
    local n=${#_lista_ref[@]}

    # Jeśli mniej niż 3 elementy, zwróć iloczyn wszystkich
    if [ $n -lt 3 ]; then
        local iloczyn=1
        for el in "${_lista_ref[@]}"; do
            iloczyn=$((iloczyn * el))
        done
        echo $iloczyn
        return
    fi

    # Sortuj listę
    local posortowane=($(printf '%s\n' "${_lista_ref[@]}" | sort -n))

    # Najmniejszy iloczyn może być:
    # 1. trzy najmniejsze (wszystkie ujemne dają dodatni, ale jeśli jest 1 ujemne to daje ujemny)
    # 2. najmniejsza ujemna i dwie największe dodatnie (ujemna * dodatnia * dodatnia = ujemna duża)
    # 3. trzy największe (wszystkie dodatnie lub ujemne)

    local n=${#posortowane[@]}
    local iloczyn1=$((${posortowane[0]} * ${posortowane[1]} * ${posortowane[2]}))
    local iloczyn2=$((${posortowane[0]} * ${posortowane[$((n - 2))]} * ${posortowane[$((n - 1))]}))
    local iloczyn3=$((${posortowane[$((n - 3))]} * ${posortowane[$((n - 2))]} * ${posortowane[$((n - 1))]}))

    # Znajdź minimum
    local min=$iloczyn1
    [ $iloczyn2 -lt $min ] && min=$iloczyn2
    [ $iloczyn3 -lt $min ] && min=$iloczyn3

    echo $min
}

test_minimalny_iloczyn_trzech() {
    local lista=(3 -1 -3 2 9 4)
    local wynik=$(minimalny_iloczyn_trzech lista)
    assertEqual "$wynik" "-108" $LINENO

    local lista2=(1 2)
    local wynik2=$(minimalny_iloczyn_trzech lista2)
    assertEqual "$wynik2" "2" $LINENO
}

main() {
    test_minimalny_iloczyn_trzech
}

main "$@"
