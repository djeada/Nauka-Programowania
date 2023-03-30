# Tytul: Przesun wszystkie pliki CSV do jednego folderu.
# Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Przenies wszystkie pliki CSV z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.
# Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
# Dane wyjsciowe: Brak.

source ../assert.sh

usun_pliki_wieksze_niz_10k() {
    local folder=$1
    find $folder -type f -size +10k-exec rm -f {} \;
}

test_usun_pliki_wieksze_niz() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    sciezki=('test/test1/test1.txt' 'test/test1/test2.txt' 'test/test2/test1.txt' 'test/test2/test2.txt')
    sciezki=('test/test1/test1.txt' 'test/test1/test2.txt' 'test/test2/test1.txt' 'test/test2/test2.txt')
    for plik in ${sciezki[@]}; do
        touch $plik
        for i in {1..10000}; do
            echo 'test' >> $plik
        done
    done

    usun_pliki_wieksze_niz_10k 'test'
    usun_pliki_wieksze_niz_10k 'test'

    for plik in ${sciezki[@]}; do
        for plik in ${sciezki[@]}; do
            assertTrue $(if [[ -f $plik ]]; then echo "true"; else echo "false"; fi) $LINENO
        done

        rm -rf 'test'
        rm -rf 'test'

    }

    main() {
        test_usun_pliki_wieksze_niz
    }

    main "$@"

