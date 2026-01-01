# ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)
#
# **Poziom:** ★☆☆
# **Tagi:** `files`, `copy`, `png`, `shutil`
#
# ### Treść
#
# Otrzymujesz ścieżkę folderu źródłowego i docelowego. Skopiuj wszystkie pliki `.png` znajdujące się **bezpośrednio** w folderze źródłowym do folderu docelowego.
#
# ### Wejście
#
# * 1 linia: `src_folder`
# * 2 linia: `dst_folder`
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
# C:\Users\Username\Obrazy
# D:\Backup\Obrazy
# ```
#
# **Wyjście:**
# *(brak)*

source ../assert.sh

kopiuj_pliki_png() {
    local folder_1="$1"
    local folder_2="$2"

    find "$folder_1" -name "*.png" -exec cp {} "$folder_2" \;
}

test_kopiuj_pliki_png() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    touch 'test/test1/plik1.png'
    touch 'test/test1/plik1.png'
    touch 'test/test1/plik2.png'

    kopiuj_pliki_png 'test/test1' 'test/test2'
    kopiuj_pliki_png 'test/test1' 'test/test2'

    assertTrue $(if [[ -f 'test/test2/plik1.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test2/plik1.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test2/plik2.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test1/plik1.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test1/plik2.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO

    rm -rf 'test'
    rm -rf 'test'

}

main() {
    test_kopiuj_pliki_png
}

main "$@"
