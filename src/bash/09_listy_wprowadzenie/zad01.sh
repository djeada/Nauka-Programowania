# ZAD-01 — Wczytaj i wypisz
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `I/O`, `odwracanie`
#
# ### Treść
#
# Wczytaj `N`, następnie `N` liczb całkowitych do listy.
#
# a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
# b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone przecinkami (bez spacji).
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
#
# ### Wyjście
#
# a) `N` linii — elementy w kolejności wczytania.
# b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 8
# 12
# 7
# ```
#
# **Wyjście:**
#
# ```
# 8
# 12
# 7
# 7,12,8
# ```
#
# ### Uwagi o formatowaniu
#
# * W podpunkcie (b) nie dodawaj przecinka na końcu.

wczytaj() {

    for ((i = 0; i < $1; i++)); do
        read liczba
        lista+=("$liczba")
    done

}

wypisz_od_poczatku() {

    for liczba in "${lista[@]}"; do
        echo "$liczba"
    done
}

wypisz_od_konca() {
    local n=$((${#lista[@]} - 1))
    
    # Wypisz w jednej linii z przecinkami
    for ((i = n; i >= 0; i--)); do
        echo -n "${lista[$i]}"
        if [[ $i -gt 0 ]]; then
            echo -n ","
        fi
    done
    echo ""
}

main() {

    declare -a lista
    read n

    wczytaj $n

    wypisz_od_poczatku

    wypisz_od_konca

}

main "$@"
