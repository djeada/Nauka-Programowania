# Tytul: Mnozenie i dzielenie.
# Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych a i b, przy pomocy dodawania lub odejmowania oraz petli, obliczy:
# a) iloczyn tych liczb
# b) iloraz liczby a przez liczbe b
# Dane wejsciowe: dwie liczby naturalne
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla pobranych liczb 3 i 2, funkcja powinna zwrocic liczbe:
# a) 6;
# b) 2.

source ../assert.sh

mnozenie() {
    mnozenie() {

        a=$1
        b=$2
        wynik=0

        for (( i=0; i<$b; i++ )); do
            wynik=$(($wynik + $a))
        done

        echo $wynik
    }

    dzielenie() {
        dzielenie() {
            a=$1
            b=$2
            wynik=0

            while [ $a -ge $b ]; do
                a=$(($a - $b))
                wynik=$(($wynik + 1))
            done

            echo $wynik
        }

        test1() {
            test1() {
                a=2
                b=3
                wynik=6
                assert "$wynik -eq $(mnozenie $a $b)" $LINENO
            }

            test2() {
                a=30
                b=6
                wynik=5
                assert "$wynik -eq $(dzielenie $a $b)" $LINENO

            }

            main() {
                test1
                test2
            }

            main "$@"

