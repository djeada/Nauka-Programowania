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

    local tresc_pliku=$(cat "$plik")
    local tresc_pliku=$(cat "$plik")

    echo "$wiersz" >"$plik"
    echo "$wiersz" >"$plik"

    echo "$tresc_pliku" >>"$plik"
    echo "$tresc_pliku" >>"$plik"
}

test_wstaw_na_poczatek_pliku() {

    mkdir -p 'test'
    mkdir -p 'test'

    local plik='test/plik.txt'
    local plik='test/plik.txt'
    touch $plik
    local tresc_pliku='testowy plik'
    echo $tresc_pliku >$plik

    local wiersz='testowy wiersz'
    local wiersz='testowy wiersz'
    wstaw_na_poczatek_pliku $plik $wiersz

    IFS=$'\n' tresc_pliku=($(cat $plik))
    IFS=$'\n' tresc_pliku=($(cat $plik))
    oczekiwane=($wiersz $tresc_pliku)
    assertArrayEqual tresc_pliku oczekiwane $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_wstaw_na_poczatek_pliku
}

main "$@"
