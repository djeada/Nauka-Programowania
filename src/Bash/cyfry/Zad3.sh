#!/usr/bin/env bash

#Dla pobranej od uzytkownika liczby, zwroc liczbe cyfr pobranje liczby.

main() {
	
	echo "Podaj liczbe: "    
	read a

	suma=0


	while [ $a -gt 0 ] 
	do
		suma=$(($suma + $a % 10))
		a=$(( $a / 10 )) 
	done

	echo "Suma cyfr podanej liczby wynosi $suma."
}

main "$@"

