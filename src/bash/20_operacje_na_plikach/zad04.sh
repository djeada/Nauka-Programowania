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
    # Testy tworzą i usuwają pliki — pracuj w katalogu tymczasowym, nie w repozytorium.
    local katalog_roboczy
    katalog_roboczy=$(mktemp -d)
    trap 'rm -rf "$katalog_roboczy"' EXIT
    cd "$katalog_roboczy" || exit 1

    mkdir 'test'

    echo 'test' >'test/test.txt'

    wypisz_plik 'test/test.txt'

    rm -rf 'test'
}

main "$@"
