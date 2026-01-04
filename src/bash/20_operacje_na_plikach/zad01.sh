# ZAD-01 — Czy ścieżka istnieje?
#
# **Poziom:** ★☆☆
# **Tagi:** `files`, `path`, `os`, `pathlib`
#
# ### Treść
#
# Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.
#
# ### Wejście
#
# * 1 linia: `path` (napis — ścieżka)
#
# ### Wyjście
#
# * 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents\plik.txt
# ```
#
# **Wyjście:**
#
# ```
# Prawda
# ```
source ../assert.sh

czy_sciezka_pliku() {
    if [ -f "$1" ]; then
        echo true
    else
        echo false
    fi
}

czy_sciezka_folderu() {
    if [ -d "$1" ]; then
        echo true
    else
        echo false
    fi
}

test_czy_sciezka_pliku() {

    mkdir 'test'
    mkdir 'test'

    touch 'test/test.txt'
    touch 'test/test.txt'

    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertFalse "$(czy_sciezka_pliku test)" $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

test_czy_sciezka_folderu() {

    mkdir 'test'
    mkdir 'test'

    assertTrue "$(czy_sciezka_folderu test)" $LINENO
    assertTrue "$(czy_sciezka_folderu test)" $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_czy_sciezka_pliku
    test_czy_sciezka_folderu
}

main "$@"
