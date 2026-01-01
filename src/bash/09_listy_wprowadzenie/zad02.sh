# ZAD-02 — Wczytaj, zmodyfikuj i wypisz
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `indeksy`, `modyfikacja`
#
# ### Treść
#
# Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:
#
# a) Zwiększ każdy element o `1`.
# b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
# c) Zastąp wszystkie elementy wartością pierwszego elementu.
#
# Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
#
# ### Wyjście
#
# Trzy linie:
#
# 1. wynik po (a)
# 2. wynik po (b)
# 3. wynik po (c)
#
# Elementy w linii oddzielone przecinkami (bez spacji).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 3
# 9
# 7
# ```
#
# **Wyjście:**
#
# ```
# 4,10,8
# 0,9,14
# 3,3,3
# ```

wczytaj() {

    for ((i = 0; i < $1; i++)); do
        read liczba
        lista+=("$liczba")
    done

}

zwieksz() {

    local n=$((${#lista[@]}))

    for ((i = 0; i < n; i++)); do
        lista[$i]=$((lista[$i] + 1))
    done
}

pomnoz() {

    local n=$((${#lista[@]}))

    for ((i = 0; i < n; i++)); do
        lista[$i]=$((lista[$i] * $i))
    done
}

zastap() {

    local n=$((${#lista[@]}))

    for ((i = 1; i < n; i++)); do
        lista[$i]=${lista[0]}
    done
}

wypisz() {

    echo $(
        IFS=","
        echo "${lista[*]// /|}"
        IFS=$''
    )

}

main() {

    declare -a lista
    read n

    wczytaj $n
    local kopia=("${lista[@]}")

    zwieksz
    wypisz

    lista=("${kopia[@]}")

    pomnoz
    wypisz

    lista=("${kopia[@]}")

    zastap
    wypisz

}

main "$@"
