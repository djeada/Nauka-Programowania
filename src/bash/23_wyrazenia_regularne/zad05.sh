# ZAD-05 — Wyodrębnij cyfry z tekstu
#
# **Poziom:** ★☆☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).
#
# ### Wejście
#
# Jedna linia:
#
# * `tekst`
#
# ### Wyjście
#
# Jedna linia:
#
# * napis złożony tylko z cyfr z tekstu wejściowego
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Terminator2001
# ```
#
# **Wyjście:**
#
# ```
# 2001
# ```

odfiltruj_cyfry() {
    echo "$1" | grep -o '[0-9]'
}

test_odfiltruj_cyfry() {
    assertEqual $(odfiltruj_cyfry "abc123") "123"
    assertEqual $(odfiltruj_cyfry "abc") ""
    assertEqual $(odfiltruj_cyfry "123") "123"
    assertEqual $(odfiltruj_cyfry "3d4jda2") "342"
}

main() {
    test_odfiltruj_cyfry
}

main "$@"
