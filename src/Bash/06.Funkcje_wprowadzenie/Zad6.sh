#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

sumaCyfr() {

	a=$1
    suma=0
	
	while [ $a -gt 0 ] 
	do
		suma=$(($suma + $a % 10))
		a=$(( $a / 10 )) 
	done
	
	return $suma
}

main() {
    echo "Podaj liczbe: "
	read a

	sumaCyfr $a
	wynik=$?

	echo "Suma cyfr twojej liczby: $wynik"

}

main "$@"

