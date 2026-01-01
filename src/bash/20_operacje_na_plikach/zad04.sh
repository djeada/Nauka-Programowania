# ZAD-04 — Wczytaj i wypisz treść pliku
#
# **Poziom:** ★☆☆
# **Tagi:** `files`, `read`, `encoding`
#
# ### Treść
#
# Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.
#
# ### Wejście
#
# * 1 linia: `file_path`
#
# ### Wyjście
#
# * treść pliku (dokładnie taka jak w pliku)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents\wiadomość.txt
# ```
#
# **Wyjście:**
#
# ```
# Witaj! To jest przykładowa treść pliku tekstowego.
# ```

source ../assert.sh

wypisz_plik() {
    local plik="$1"
    cat "$plik"
}

main() {

    mkdir 'test'
    mkdir 'test'

    echo 'test' >'test/test.txt'
    echo 'test' >'test/test.txt'

    wypisz_plik 'test/test.txt'
    wypisz_plik 'test/test.txt'

    rm -rf 'test'
    rm -rf 'test'
}

main "$@"
