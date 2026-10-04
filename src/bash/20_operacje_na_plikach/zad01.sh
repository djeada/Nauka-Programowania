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

    touch 'test/test.txt'

    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertFalse "$(czy_sciezka_pliku test)" $LINENO

    rm -rf 'test'
}

test_czy_sciezka_folderu() {

    mkdir 'test'

    assertTrue "$(czy_sciezka_folderu test)" $LINENO

    rm -rf 'test'
}

main() {
    # Testy tworzą i usuwają pliki — pracuj w katalogu tymczasowym, nie w repozytorium.
    local katalog_roboczy
    katalog_roboczy=$(mktemp -d)
    trap 'rm -rf "$katalog_roboczy"' EXIT
    cd "$katalog_roboczy" || exit 1
    test_czy_sciezka_pliku
    test_czy_sciezka_folderu
}

main "$@"
