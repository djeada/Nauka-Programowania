# ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `dir`, `listdir`, `pathlib`
#
# ### Treść
#
# Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.
#
# ### Wejście
#
# * 1 linia: `folder_path`
# * 2 linia: `ext` (np. `.txt`)
#
# ### Wyjście
#
# * 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents
# .txt
# ```
#
# **Wyjście:**
#
# ```
# ['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
# ```
#
# ### Uwagi o formatowaniu
#
# * Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

source ../assert.sh

znajdz_pliki_z_rozszerzeniem() {
    local folder="$1"
    local rozszerzenie="$2"
    local pliki=()
    for plik in $(find $folder -maxdepth 10 -type f); do
        if [[ "$plik" == *"$rozszerzenie" ]]; then
            pliki+=("$plik")
        fi
    done
    echo "${pliki[@]}"
}

test_znajdz_pliki_z_rozszerzeniem() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    touch 'test/test1/test1.txt'
    touch 'test/test1/test1.txt'
    touch 'test/test1/test2.txt'
    touch 'test/test2/test1.txt'
    touch 'test/test2/test2.txt'

    IFS=' ' read -r -a wynik <<<$(znajdz_pliki_z_rozszerzeniem 'test' 'txt')
    IFS=' ' read -r -a wynik <<<$(znajdz_pliki_z_rozszerzeniem 'test' 'txt')

    assert_array_contains wynik 'test/test1/test1.txt' $LINENO
    assert_array_contains wynik 'test/test1/test1.txt' $LINENO
    assert_array_contains wynik 'test/test1/test2.txt' $LINENO
    assert_array_contains wynik 'test/test2/test1.txt' $LINENO
    assert_array_contains wynik 'test/test2/test2.txt' $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_znajdz_pliki_z_rozszerzeniem
}

main "$@"
