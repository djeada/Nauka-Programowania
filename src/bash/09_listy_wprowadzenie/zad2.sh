# Tytul: Samochody jadace w przeciwnych kierunkach.
# Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy samochody jadace w przeciwnych kierunkach mijaja sie.
# Dane wejsciowe: Lista znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B').
# Dane wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.
# Przyklad:
# Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.

wczytaj() {

    for (( i=0; i<$1; i++ ))
    do
        read liczba
        lista+=("$liczba")
    done

}

zwieksz() {

    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        lista[$i]=$((lista[$i] + 1))
    done
}

pomnoz() {

    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        lista[$i]=$((lista[$i] * $i))
    done
}

zastap() {

    local n=$(( ${#lista[@]}))

    for (( i=1; i<n; i++ ))
    do
        lista[$i]=${lista[0]}
    done
}

wypisz() {

    echo $(IFS=",";echo "${lista[*]// /|}";IFS=$'')

}

main() {

    declare -a lista
    echo "podaj liczbe n:"
    read n

    echo "podaj $n liczb:"
    wczytaj $n
    local kopia=("${lista[@]}")

    echo -e "\nliczby powiekszone o 1:"
    zwieksz
    wypisz

    lista=("${kopia[@]}")

    echo -e "\nliczby pomnozone przez indeks:"
    pomnoz
    wypisz

    lista=("${kopia[@]}")

    echo -e "\npierwsza liczba $n razy:"
    zastap
    wypisz

}

main "$@"

