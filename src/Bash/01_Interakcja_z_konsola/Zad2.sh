#!/usr/bin/env bash

#Wypisz na konsole najpierw druga potem pierwsza pobrana dana.
   
main() {
    echo "Wpisz dwie liczby."
	read a
	read b
	echo "Liczby w odwrotnej kolejnosci to: "
	echo "${b}"
	echo "${a}"
}

main "$@"
