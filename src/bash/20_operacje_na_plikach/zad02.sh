# Tytul: Plik z lista adresow IP.
# Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Kazdy wiersz pliku reprezentuje adres IP. Posortuj adresy IP i zapisz je w liscie.
# Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
# Dane wyjsciowe: Lista adresow IP posortowanych alfabetycznie.

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

    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_z_rozszerzeniem 'test' 'txt')
    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_z_rozszerzeniem 'test' 'txt')

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

