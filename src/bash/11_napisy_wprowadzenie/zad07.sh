# ZAD-07 — Zamień znaki na kody ASCII
#
# **Poziom:** ★☆☆
# **Tagi:** `ASCII`, `ord`, `string`
#
# ### Treść
#
# Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# * 1. linia: kody ASCII oddzielone `, `
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Robot
# ```
#
# **Wyjście:**
#
# ```
# 82, 111, 98, 111, 116
# ```

source ../assert.sh

# Funkcja pomocnicza konwertujaca znak na kod ASCII
# Zlozonosc czasowa: O(1)
# Zlozonosc pamieciowa: O(1)
ord() {
    LC_CTYPE=C printf '%d' "'$1"
}

# Funkcja zamieniajaca znaki na kody ASCII
# Zlozonosc czasowa: O(n), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(n) dla wyniku
zamien() {

    local napis="$1"
    local n=$((${#napis} - 1))

    # Wypisywanie kodow ASCII wszystkich znakow oprocz ostatniego
    for ((i = 0; i < n; i++)); do
        echo -n "$(ord "${napis:$i:1}"), "
    done

    # Wypisywanie kodu ASCII ostatniego znaku (bez przecinka)
    if [ $n -ne -1 ]; then
        echo "$(ord "${napis:$n:1}")"
    fi
}

test1() {
    local napis="pacZka!"
    local wynik="112, 97, 99, 90, 107, 97, 33"
    assertEqual "$(zamien $napis)" "$wynik" $LINENO
}

test2() {
    local napis=""
    local wynik=""
    assertEqual "$(zamien $napis)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"
