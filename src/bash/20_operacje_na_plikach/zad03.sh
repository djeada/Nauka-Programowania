# ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `walk`, `recursive`, `pathlib`
#
# ### Treść
#
# Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.
#
# ### Wejście
#
# * 1 linia: `filename` (np. `raport.docx`)
#
# ### Wyjście
#
# * 1 linia: lista pełnych ścieżek (napisy)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# raport.docx
# ```
#
# **Wyjście:**
#
# ```
# [
#   'C:\Users\Username\Documents\raport.docx',
#   'D:\Projekty\Raporty\raport.docx',
#   'E:\Backup\raport.docx'
# ]
# ```
#
# ### Uwagi
#
# * W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

source ../assert.sh

znajdz_pliki_o_nazwie() {
    local nazwa=$1
    local lista=()
    local sciezka
    for sciezka in $(find ~ -type f); do
        if [[ $sciezka == *"$nazwa"* ]]; then
            lista+=("$sciezka")
        fi
    done
    echo "${lista[@]}"
}

test_znajdz_pliki_o_nazwie() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    touch 'test/test1/test.txt'
    touch 'test/test1/test.txt'
    touch 'test/test2/test.txt'

    local sciezka_pliku_1=$(pwd)/test/test1/test.txt
    local sciezka_pliku_1=$(pwd)/test/test1/test.txt
    local sciezka_pliku_2=$(pwd)/test/test2/test.txt

    IFS=' ' read -r -a wynik <<<$(znajdz_pliki_o_nazwie 'test.txt')
    IFS=' ' read -r -a wynik <<<$(znajdz_pliki_o_nazwie 'test.txt')

    assert_array_contains wynik "$sciezka_pliku_1" $LINENO
    assert_array_contains wynik "$sciezka_pliku_1" $LINENO
    assert_array_contains wynik "$sciezka_pliku_2" $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_znajdz_pliki_o_nazwie
}

main "$@"
