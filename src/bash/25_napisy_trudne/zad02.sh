# ZAD-02 — Usuń podnapis
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `replace`, `substring`
#
# ### Treść
#
# Dostajesz dwa napisy:
#
# 1. Napis główny,
# 2. Podnapis do usunięcia.
#
# Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.
#
# ### Wejście
#
# * 1 linia: napis `S`
# * 2 linia: napis `T` (do usunięcia)
#
# ### Wyjście
#
# * 1 linia: wynikowy napis po usunięciu wszystkich wystąpień
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Lezy jezy na wiezy
# zy
# ```
#
# **Wyjście:**
#
# ```
# Le je na wie
# ```

source ../assert.sh

# Usuwa wszystkie wystąpienia podnapisu z napisu głównego.
# Złożoność czasowa: O(n*m), gdzie n to długość napisu, m to długość podnapisu
# Złożoność pamięciowa: O(n)
usun_podnapis() {
    local napis="$1"
    local podnapis="$2"
    
    echo "${napis//$podnapis/}"
}

test_usun_podnapis() {
    local wynik=$(usun_podnapis "Lezy jezy na wiezy" "zy")
    assertEqual "$wynik" "Le je na wie" $LINENO
}

main() {
    test_usun_podnapis
}

main "$@"
