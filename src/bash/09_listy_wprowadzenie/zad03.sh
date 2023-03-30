# Tytul: Rotacja w lewo/prawo.
# Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.
# Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

source ../assert.sh

znajdz_klucz_v1() {

    local n=${#lista[@]}

    for (( i=0; i<n; i++ ))
    do
        if [ ${lista[$i]} -eq $1 ]; then
            echo $i
            return
        fi
    done

    echo -1
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    local a=2
    local wynik=6
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}

test2() {
    local lista=(3 -2 4 9 -3 -40 8 5 -7 -1)
    local a=2
    local wynik=-1
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

