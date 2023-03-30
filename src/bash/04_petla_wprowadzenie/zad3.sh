# Tytul: Liczba pi.
# Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi tyle razy, ile wynosi ta liczba, z dokladnoscia do tylu miejsc po przecinku, ile wynosi otrzymana liczba.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanej liczby 2, powinno zostac wypisane:
# 3,14
# 3,14

main() {

    echo "Podaj liczbe:"
    read a

    echo "scale=$a; 4*a(1)" | bc -l
}

main "$@"

