# ZAD-07 — Średnia dwóch największych liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `max`, `sortowanie`, `float`
#
# ### Treść
#
# Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 2`)
# * kolejne `N` linii: liczby naturalne
#
# ### Wyjście
#
# Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 6
# 9
# 2
# 3
# 2
# 1
# 7
# ```
#
# **Wyjście:**
#
# ```
# 8.0
# ```

source ../assert.sh

wieksza() {
    local n=${#lista[@]}

    if [ $n -eq 0 ]; then
        echo "0.00"
        return
    fi

    if [ $n -eq 1 ]; then
        echo $((lista[0] - 1))
        return
    fi

    local maks="$((1 << 63))"
    local maks2="$((1 << 63))"

    for liczba in "${lista[@]}"; do

        if [ $liczba -gt $maks ]; then
            maks2=$maks
            maks=$liczba
        elif [ $liczba -gt $maks ]; then
            maks2=$liczba
        fi
    done

    echo $(bc -l <<<"scale=2; ($maks+$maks2)/2")
}

main() {
    local lista=(3 5 -7 4 9 -11 2)
    echo $(wieksza)
}

main "$@"
