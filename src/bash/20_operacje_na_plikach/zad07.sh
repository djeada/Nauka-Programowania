# ZAD-07 — Dodaj wiersz na początku pliku
#
# **Poziom:** ★☆☆
# **Tagi:** `files`, `write`, `prepend`
#
# ### Treść
#
# Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.
#
# ### Wejście
#
# * 1 linia: `file_path`
# * 2 linia: `line_to_add` (może zawierać spacje)
#
# ### Wyjście
#
# Brak.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents\notatki.txt
# To jest nowy wiersz dodany na początku pliku.
# ```
#
# **Wyjście:**
# *(brak)*
source ../assert.sh

wstaw_na_poczatek_pliku() {
    local plik="$1"
    local wiersz="$2"
    local plik_tymczasowy="$plik.tmp"

    {
        echo "$wiersz"
        cat "$plik"
    } >"$plik_tymczasowy" && mv "$plik_tymczasowy" "$plik"
}

test_wstaw_na_poczatek_pliku() {

    mkdir -p 'test'

    local plik='test/plik.txt'
    local tresc_pliku='testowy plik'
    echo "$tresc_pliku" >"$plik"

    local wiersz='testowy wiersz'
    wstaw_na_poczatek_pliku "$plik" "$wiersz"

    local wynik
    mapfile -t wynik <"$plik"
    local oczekiwane=("$wiersz" "$tresc_pliku")
    assertArrayEqual wynik oczekiwane $LINENO

    rm -rf 'test'
}

main() {
    # Testy tworzą i usuwają pliki — pracuj w katalogu tymczasowym, nie w repozytorium.
    local katalog_roboczy
    katalog_roboczy=$(mktemp -d)
    trap 'rm -rf "$katalog_roboczy"' EXIT
    cd "$katalog_roboczy" || exit 1
    test_wstaw_na_poczatek_pliku
}

main "$@"
