# Tytul: Znajdz i zmodyfikuj pliki spelniajace warunek.
# Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu.
# a) Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych sie w podanym folderze i jego podfolderach.
# b) Usun srodkowy wiersz z kazdego pliku CSV znajdujacego sie w podanym folderze i jego podfolderach.
# Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
# Dane wyjsciowe: Brak.

source ../assert.sh

sortuj_adresy_ip() {
    sort -t . -g -k1,1 -k2,2 -k3,3 -k4,4 $1
}

test_sortuj_adresy_ip() {

    mkdir -p 'test'
    mkdir -p 'test'

    local plik='test/test.txt'
    local plik='test/test.txt'
    touch $plik
    echo "123.4.245.23"  > $plik
    echo "104.244.253.29"  >> $plik
    echo "1.198.3.93" >> $plik
    echo "32.183.93.40" >> $plik
    echo "104.30.244.2" >> $plik
    echo "104.244.4.1" >> $plik

    IFS=$'\n'
    IFS=$'\n'
    wynik=($(sortuj_adresy_ip 'test/test.txt'))

    local oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.244.4.1 104.244.253.29 123.4.245.23)
    local oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.244.4.1 104.244.253.29 123.4.245.23)
    assertArrayEqual wynik oczekiwane $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_sortuj_adresy_ip
}

main "$@"

