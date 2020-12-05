#!/usr/bin/env bash

#Dla pobranej liczby, sprawdz czy jest palindromem.

main() {
	
	echo "Podaj liczbe: "    
	read a

	pom=$a
	odwrocona=0

	while [ $pom -gt 0 ] 
	do
		cyfra=$(($pom % 10))
		
		odwrocona=$(($odwrocona*10 + $cyfra))
		pom=$(($pom / 10 )) 
	done
	
	if [[ $odwrocona -eq $a ]]; then
		echo "podana liczba jest palindromem"
	else
		echo "podana liczba nie jest palindromem"
	fi
}

main "$@"

