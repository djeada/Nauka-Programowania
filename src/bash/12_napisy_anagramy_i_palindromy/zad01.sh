# ZAD-01 — Czy słowo jest palindromem?
#
# **Poziom:** ★☆☆
# **Tagi:** `string`, `palindrom`, `I/O`
#
# ### Treść
#
# Wczytaj jedno słowo i sprawdź, czy jest palindromem (czytane od lewej do prawej i od prawej do lewej jest takie samo).
#
# ### Wejście
#
# * 1. linia: słowo (same litery, bez spacji)
#
# ### Wyjście
#
# Jedna linia:
#
# * `Prawda` — jeśli słowo jest palindromem
# * `Fałsz` — w przeciwnym razie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# kajak
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```
#
# ### Uwagi o formatowaniu
#
# * Jeśli chcesz ignorować wielkość liter, porównuj wersje `lower()`.
source ../assert.sh

# Funkcja sprawdzajaca czy slowo jest palindromem
# Zlozonosc czasowa: O(n), gdzie n to dlugosc slowa
# Zlozonosc pamieciowa: O(n) dla odwroconego slowa
czy_palindrom() {
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

test_czy_palindrom() {
    assertTrue "czy_palindrom 'kajak'"
    assertFalse "czy_palindrom 'kot'"
}

main() {
    test_czy_palindrom
}

main "$@"
