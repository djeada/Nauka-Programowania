# Tytul: Napis skladajacy sie z liczb od 1 do n.
# Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

wypisz_poziomo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for((i=0;i<n;i+=k)); do
        echo -n "${napis:$i:1} "
    done
    echo ""
}

wypisz_pionowo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for((i=0;i<n;i+=k)); do
        echo "${napis:$i:1} "
    done
}

main() {
    local napis="hej dzieci jesli chcecie zobaczyc smerfow las"
    local k=3

    wypisz_poziomo "$napis" $k
    wypisz_pionowo "$napis" $k
}

main "$@"

