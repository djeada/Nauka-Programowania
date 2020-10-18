#!/bin/bash

main() {
    #Napisz program, ktory wczyta liczbe i wypisze ja jesli jest wieksza od 5. 

    echo "Podaj liczbe"
	read x

	if [[ $x -gt 5 ]]; then
	    echo $x
	fi
}

main "$@"
