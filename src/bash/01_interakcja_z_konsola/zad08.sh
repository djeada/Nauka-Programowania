# Tytul: Obliczenie ceny podlogi.
# Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o podanych wymiarach.
# Jednostki sa umowne.
# Dane wejsciowe: Cztery liczby naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc podlogi.
# Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi.
# Przyklad:
# Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.

main() {

    echo "Podaj: cene plytki, dlugosc boku plytki i wymiary podlogi: "
    read cena
    read bokPlytki
    read szerokoscPodlogi
    read dlugoscPodlogi

    szerokoscKonieczna=$(($szerokoscPodlogi + $bokPlytki - $szerokoscPodlogi % $bokPlytki))
    dlugoscKonieczna=$(($dlugoscPodlogi + $bokPlytki - $dlugoscPodlogi % $bokPlytki))

    polePlytki=$(($bokPlytki*$bokPlytki))
    polePodlogi=$(($szerokoscKonieczna*$dlugoscKonieczna))

    calkowityKoszt=$(($cena * $polePodlogi / $polePlytki))

    echo "Dla plytki o dlugosci boku $bokPlytki  i ceny $cena calkowity koszt wylozenia podlogi o wymiarach $szerokoscPodlogi x $dlugoscPodlogi wynosi $calkowityKoszt"

}

main "$@"

