# ZAD-08 — Najdłuższy wspólny przedrostek
#
# **Poziom:** ★★★
# **Tagi:** `string`, `prefix`, `list`
#
# ### Treść
#
# Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.
#
# ### Wejście
#
# * 1 linia: `n` — liczba napisów
# * kolejne `n` linii: napisy
#
# ### Wyjście
#
# * 1 linia: najdłuższy wspólny przedrostek (może być pusty)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# Remolada
# Remux
# Remmy
# ```
#
# **Wyjście:**
#
# ```
# Rem
# ```
source ../assert.sh

# Znajduje najdłuższy wspólny przedrostek dla listy napisów.
# Złożoność czasowa: O(n*m), gdzie n to liczba napisów, m to długość najkrótszego
# Złożoność pamięciowa: O(m)
najdluzszy_wspolny_prefix() {
    local -n _napisy_ref=$1

    if [ ${#_napisy_ref[@]} -eq 0 ]; then
        echo ""
        return
    fi

    local prefix="${_napisy_ref[0]}"

    for ((i = 1; i < ${#_napisy_ref[@]}; i++)); do
        local napis="${_napisy_ref[$i]}"
        local nowy_prefix=""

        for ((j = 0; j < ${#prefix} && j < ${#napis}; j++)); do
            if [ "${prefix:$j:1}" = "${napis:$j:1}" ]; then
                nowy_prefix="$nowy_prefix${prefix:$j:1}"
            else
                break
            fi
        done

        prefix="$nowy_prefix"

        if [ -z "$prefix" ]; then
            break
        fi
    done

    echo "$prefix"
}

test_najdluzszy_wspolny_prefix() {
    local napisy=("Remolada" "Remux" "Remmy")
    local wynik=$(najdluzszy_wspolny_prefix napisy)
    assertEqual "$wynik" "Rem" $LINENO
}

main() {
    test_najdluzszy_wspolny_prefix
}

main "$@"
