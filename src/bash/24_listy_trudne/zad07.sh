# ZAD-07 — Pojemność wody między słupkami
#
# **Poziom:** ★★★
# **Tagi:** `two pointers`, `prefix`, `trapping rain water`
#
# ### Treść
#
# Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.
#
# ### Wejście
#
# * 1 linia: lista wysokości `H`
#
# ### Wyjście
#
# * 1 linia: jedna liczba naturalna — ilość wody
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [3, 0, 1, 0, 2]
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```
source ../assert.sh

# Oblicza ilość wody zatrzymanej między słupkami.
# Złożoność czasowa: O(n), gdzie n to liczba słupków
# Złożoność pamięciowa: O(n)
pojemnosc_wody() {
    local -n _wysokosci_ref=$1
    local n=${#_wysokosci_ref[@]}

    if [ $n -le 2 ]; then
        echo 0
        return
    fi

    # Znajdź maksymalne wysokości z lewej dla każdego słupka
    local lewy_max=()
    lewy_max[0]=${_wysokosci_ref[0]}
    for ((i = 1; i < n; i++)); do
        if [ ${_wysokosci_ref[$i]} -gt ${lewy_max[$((i - 1))]} ]; then
            lewy_max[$i]=${_wysokosci_ref[$i]}
        else
            lewy_max[$i]=${lewy_max[$((i - 1))]}
        fi
    done

    # Znajdź maksymalne wysokości z prawej dla każdego słupka
    local prawy_max=()
    prawy_max[$((n - 1))]=${_wysokosci_ref[$((n - 1))]}
    for ((i = n - 2; i >= 0; i--)); do
        if [ ${_wysokosci_ref[$i]} -gt ${prawy_max[$((i + 1))]} ]; then
            prawy_max[$i]=${_wysokosci_ref[$i]}
        else
            prawy_max[$i]=${prawy_max[$((i + 1))]}
        fi
    done

    # Oblicz wodę
    local woda=0
    for ((i = 0; i < n; i++)); do
        local min_wysokosc=${lewy_max[$i]}
        [ ${prawy_max[$i]} -lt $min_wysokosc ] && min_wysokosc=${prawy_max[$i]}

        local woda_tutaj=$((min_wysokosc - ${_wysokosci_ref[$i]}))
        # Upewnij się że woda nie jest ujemna
        [ $woda_tutaj -lt 0 ] && woda_tutaj=0
        woda=$((woda + woda_tutaj))
    done

    echo $woda
}

test_pojemnosc_wody() {
    local wysokosci=(3 0 1 0 2)
    local wynik=$(pojemnosc_wody wysokosci)
    assertEqual "$wynik" "5" $LINENO
}

main() {
    test_pojemnosc_wody
}

main "$@"
