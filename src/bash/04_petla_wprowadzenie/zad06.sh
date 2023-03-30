# Tytul: Suma elementow ciagu.
# Tresc: Dla otrzymanej liczby naturalnej n, wypisz sume n pierwszych elementow ciagu danego wzorem:
# $$a_n = n^2 + n + 1$$
# $$a_n = n^2 + 5n$$
# $$a_n = n + 2n$$
# Wynik powinien zostac zaokraglony do najblizszej liczby naturalnej.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# * Dla otrzymanej liczby 2, w podpunkcie a) powinna zostac wypisana liczba 1.
# * Dla otrzymanej liczby 2, w podpunkcie b) powinna zostac wypisana liczba 17.
# * Dla otrzymanej liczby 2, w podpunkcie c) powinna zostac wypisana liczba 6.

main() {

    echo "Podaj liczbe:"
    read n

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(echo "scale=2; $i/$(($i + 1))" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n/(n+1) dla n=$n: $suma"

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(echo "scale=2; $(($n**2 + 5))/$n" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem (n^2 + 5)/n dla n=$n: $suma"

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(($n + 2**$n))
        suma=$(($suma + $a_n))

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n + 2^n dla n=$n: $suma"

}

main "$@"

