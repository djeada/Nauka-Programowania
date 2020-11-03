#!/usr/bin/env bash

#Napisz funkcje ktora zwroci

#a) liczbe 3

funkcja1() {
	return 3
}

#b) napis "Tak"

funkcja2() {
	echo "Tak"
}

#c) wartosc logiczna prawda

funkcja3() {
	echo true
}

main() {
    funkcja1
  	wynik=$?
    echo $wynik

	wynik=$(funkcja2)
	echo $wynik

	wynik=$(funkcja3)
	echo $wynik
}

main "$@"

