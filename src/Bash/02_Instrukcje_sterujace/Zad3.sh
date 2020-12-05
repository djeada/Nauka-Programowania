#!/bin/bash

main() {
    #Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

    echo "Podaj liczbe:"
	read x

	if [[ $x -gt 0 ]]; then
	    echo "libczba jest dodatnia"
	elif [[ $x -lt 0 ]]; then
	    echo "libczba jest ujemna"  
	else
		echo "libczba jest zerem"
	fi
}

main "$@"
