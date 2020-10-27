#!/usr/bin/env bash

#Dla pobranej liczby, powinna zostac wyswietlona suma wszystkich liczb naturalnych mniejszych od pobranej liczby.

main() {
    
	echo "Podaj liczbe:"
  	read a
	suma=0

	for (( i=0; i<$a; i++ ))
		do 
			echo $i
			suma=$(($suma + $i))
		done

	echo "Suma liczb naturalnych mniejszych od pobranej liczby wynosi $suma"
}

main "$@"

