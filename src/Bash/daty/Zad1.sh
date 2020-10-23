#!/usr/bin/env bash

#Czy liczba jest numerem tygodnia/miesiąca?

main() {
    
    echo "Podaj liczbe:"
    read a

	if [[ $a -ge 1 ]] && [[ $a -le 7 ]]; then
		echo "Liczba jest poprawnym numerem tygodnia"

	else
		echo "Liczba nie jest poprawnym numerem tygodnia"
	fi

	if [[ $a -ge 1 ]] && [[ $a -le 12 ]]; then
		echo "Liczba jest poprawnym numerem miesiaca"
	else
		echo "Liczba nie jest poprawnym numerem miesiaca"
	fi
}

main "$@"

