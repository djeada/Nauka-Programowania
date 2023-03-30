# Tytul: Zmodyfikuj elementy spelniajace warunek.
# Tresc: Otrzymujesz liste liczb calkowitych. W wyniku wykonania ponizszych polecen otrzymasz nowa liste:
# a) Zwieksz o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynaja sie od 0).
# b) Wyzeruj wszystkie elementy bedace wielokrotnosciami liczby 3.
# c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.
# d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
# e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanej listy [5, 7, 9, 4, 2]:
# a) Wynik: [5, 8, 9, 5, 2]
# b) Wynik: [5, 0, 0, 5, 2]
# c) Wynik: [25, 0, 0, 25, 4]
# d) Wynik: [37, 0, 0, 25, 4]
# e) Wynik: [2592, 0, 0, 36, 1080]

source ../assert.sh

znajdz_maks() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -nr | head -n1
}

znajdz_min() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -n | head -n1
}

suma_ciagu_art() {
    local n=${#lista[@]}
    min=$(znajdz_min)
    maks=$(znajdz_maks)
    echo $(bc -l <<< "scale=0; ($n+1)*($min+$maks)/2")
}

znajdz_brakujacy_element() {

    suma_listy=$(IFS=+; echo "$((${lista[*]}))")
    suma_przedzialu=$(suma_ciagu_art)

    return $((suma_przedzialu - suma_listy))
}

test1() {
    local lista=(6 8 4 10 14 2)
    local wynik=12
    znajdz_brakujacy_element
    assertEqual $? $wynik $LINENO
}

test2() {
    local lista=(1 2 4 5 6)
    local wynik=3
    znajdz_brakujacy_element
    assertEqual $? $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

