# Tytul: Liczby z okreslonego przedzialu.
# Tresc: Dla otrzymanych dwoch liczb naturalnych wypisz:
# a) Wszystkie liczby naturalne wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
# b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Kilka liczb naturalnych.
# Przyklad:
# Dla otrzymanych liczb 9 i 5 powinny zostac wypisane liczby 6, 7 i 8.

main() {

    echo "Podaj dwie liczby:"
    read a
    read b

    if [[ $a -gt $b ]]; then
        echo "swap"
        temp=$a
        a=$b
        b=$temp
    fi

    echo "Liczby naturalne wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        echo $i
    done

    echo "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        if [[ $(($i % 3)) -eq 0 ]]; then
            echo $i
        fi
    done
}

main "$@"

