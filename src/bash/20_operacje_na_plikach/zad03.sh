# Tytul: Statystyki dla pliku tekstowego.
# Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Oblicz:
# a) Liczbe wierszy w pliku.
# b) Liczbe slow w pliku (slowa oddzielone sa spacjami i moga skladac sie wylacznie z liter).
# c) Srednia dlugosc wiersza.
# d) Srednia liczbe slow na wiersz.
# e) Czestosc wystepowania kazdego ze slow w pliku.
# Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
# Dane wyjsciowe:
# a) Liczba naturalna reprezentujaca liczbe wierszy.
# b) Liczba naturalna reprezentujaca liczbe slow.
# c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza.
# d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz.
# e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa).
# Przyklad:
# Dla otrzymanego napisu: "C:\Users\Username\Documents\text_file.txt" powinno zostac zwrocone:
# a) Liczba naturalna reprezentujaca liczbe wierszy, np. 6
# b) Liczba naturalna reprezentujaca liczbe slow, np. 25
# c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza, np. 41.5
# d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz, np. 4.2
# e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania slowa): {'The': 2, 'quick': 2, 'brown': 2, 'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1, 'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1, 'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1, 'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1, 'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1, 'ten': 1, 'lines': 1, 'and': 1, 'words.': 1}
# Tekst pliku:
# "The quick brown fox jumped over the lazy dog.
# The quick brown cat sat on the mat.
# Foxes are known for their cunning and intelligence.
# Dogs are known for their loyalty and kindness.
# Cats are independent animals but can be affectionate.
# This text file contains six lines and 25 words."

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

    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_o_nazwie 'test.txt')
    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_o_nazwie 'test.txt')

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

