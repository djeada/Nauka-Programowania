# Tytul: Znalezienie w folderze wszystkich plikow z danym rozszerzeniem
# Tresc: Otrzymujesz dwa napisy. Pierwszy napis to sciezka folderu, a drugi to rozszerzenie szukanych plikow. Znajdz w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liscie.
# Dane wejsciowe: Dwa napisy
# Dane wyjsciowe: Lista napisow

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

