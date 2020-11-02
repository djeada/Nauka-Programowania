#!/usr/bin/env bash

#Dla pobranej liczby, wyswietl liczbe Pi podniesiona do potegi rownej pobranej liczbie. Wynik powinien byc zaokraglony do dwoch miejsc po przecinku.

main() {
    	
	echo "Podaj liczbe:"
  	read x
	pi=$(echo "scale=2; 4*a(1)" | bc -l)
	potega=$pi

	for (( i=1; i<=$x; i++ )); do
		potega=$(echo "scale=2; $potega * $pi" | bc)
	done

	echo "liczbe Pi podniesiona do potegi rownej pobranej liczbie, wynosi $potega"

	
}

main "$@"

