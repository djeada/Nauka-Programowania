# Tytul: Czy napis sklada sie wylacznie z cyfr?
# Tresc: Masz napis. Sprawdz, czy sklada sie on wylacznie z cyfr.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Wartosc logiczna.
# Przyklad:
# Dla napisu: “1234”, powinna zostac zwrocona wartosc logiczna: Prawda.

source ../assert.sh

nazwa_pliku(){
    local sciezka="$1"
    sciezka="${sciezka//\\//}"
    sciezka="${sciezka%/}"
    sciezka="${sciezka#/}"
    sciezka="${sciezka##*/}"

    while [[ "$sciezka" = *.* ]]; do
        sciezka="${sciezka%.*}"
    done

    echo "$sciezka"
}

test_nazwa_pliku() {
    assertEqual $(nazwa_pliku 'C:\\Windows\\explorer.exe') "explorer" $LINENO
    assertEqual $(nazwa_pliku '/home/user/var/log/syslog') "syslog" $LINENO
    assertEqual $(nazwa_pliku 'test.jpg.png.mp3.mp5.html.txt') "test" $LINENO
    assertEqual $(nazwa_pliku 'test') "test" $LINENO
}

main() {
    test_nazwa_pliku
}

main "$@"

