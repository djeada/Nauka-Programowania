#!/usr/bin/env bash

main() {
	    
	#Otrzymujesz cene oraz wymiary pojedynczej plytki. Oblicz ile bedzie wynosila cena
	#za podloge o podanych wymiarach. Podloga jest prostokatem, a plytka kwadratem


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

