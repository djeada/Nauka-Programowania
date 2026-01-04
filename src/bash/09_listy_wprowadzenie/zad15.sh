# ZAD-15 — Element dominujący
#
# **Poziom:** ★★☆
# **Tagi:** `zliczanie`, `dict`, `majority`
#
# ### Treść
#
# Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby naturalne
#
# ### Wyjście
#
# Jedna liczba naturalna — element dominujący lub `-1`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 4
# 7
# 4
# 4
# 2
# ```
#
# **Wyjście:**
#
# ```
# 4
# ```
source ../assert.sh

element_dominujacy() {
    declare -A histo

    local n=${#lista[@]}

    for liczba in "${lista[@]}"; do
        if [[ -z ${histo["$liczba"]} ]]; then
            histo["$liczba"]=1
        else
            histo["$liczba"]=$((${histo["$liczba"]} + 1))
        fi

    done

    for klucz in "${!histo[@]}"; do
        if [ ${histo[$klucz]} -gt $((n / 2)) ]; then
            unset histo
            echo "$klucz"
            return
        fi
    done

    unset histo
    echo "-1"
}

test1() {
    local lista=(4 7 4 4 2)
    local wynik=4
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

test2() {
    local lista=(1 2 4 5 6)
    local wynik=-1
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"
