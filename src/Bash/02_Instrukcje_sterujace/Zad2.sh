#!/bin/bash

main() {
    #Dla dwoch pobranych liczb, sprawdz czy liczby sa identyczne.

    echo "Podaj dwie liczby:"
	read x
	read y

	if [[ $x -eq $y ]]; then
	    echo "liczby sa jednakowe"
	else
	  echo "liczby sa rozne"
	fi
}

main "$@"
