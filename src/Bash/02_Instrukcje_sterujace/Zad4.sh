#!/bin/bash

main() {
    #Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

    echo "Podaj dwie liczby:"
	read x
	read y

	if [[ $x -gt $y ]]; then
	    echo $x
	    echo $y
	else
	  echo $y
	  echo $x
	fi
}

main "$@"
