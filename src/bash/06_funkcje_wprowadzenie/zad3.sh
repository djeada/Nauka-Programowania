# Tytul:  Sprawdz warunek
# Napisz funkcje, ktora sprawdzi nastepujace warunki dla otrzymanych dwoch liczb:
# a) Czy pierwsza liczba jest wieksza od drugiej liczby?
# b) Czy suma liczb jest mniejsza niz 10?
# c) Czy obie liczby sa nieparzyste?
# d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu?
# Dane wejsciowe: dwie liczby naturalne
# Dane wyjsciowe: cztery wartosci logiczne, odpowiadajace na kazde z pytan
# Przyklad:
# Dla pobranych liczb 3 i 2, funkcja powinna zwrocic nastepujace wartosci logiczne:
# a) Prawda
# b) Prawda
# c) Falsz
# d) Prawda

czyWieksza() {

    if [[ $1 -gt $2 ]] ; then
        echo true
    else
        echo false
    fi
}

czySumaMniejsza() {
    suma=$(($1 + $2))

    if [[ $suma -lt 10 ]] ; then
        echo true
    else
        echo false
    fi
}

czyObieNieparzyste() {
    if [[ $(($1 % 2)) -eq 1 ]] && [[ $(($2 % 2)) -eq 1 ]]; then
        echo true
    else
        echo false
    fi
}

wieksza() {
    if [[ $1 > $2 ]]; then
        return $1
    else
        return $2
    fi
}

czyWiekszaNizKwad() {
    wieksza $1 $2
    wieksza=$?

    if [[ $wieksza -lt $(($1**2)) ]]; then
        echo true
    else
        echo false
    fi
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    wynik=$(czyWieksza $a $b)
    echo "Pierwsza liczba jest wieksza od drugiej: $wynik"

    wynik=$(czySumaMniejsza $a $b)
    echo "Suma liczb jest mniejsza od 10: $wynik"

    wynik=$(czyObieNieparzyste $a $b)
    echo "Obie liczby nieparzyste: $wynik"

    wynik=$(czyWiekszaNizKwad $a $b)
    echo "Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu $wynik"
}

main "$@"

