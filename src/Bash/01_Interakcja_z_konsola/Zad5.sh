#!/usr/bin/env bash

main() {
	    
	#Otrzymujesz wspolrzedna x. Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.	

    echo "Podaj wspolrzedna x: "
    read x

    echo "Wartosc funkcji y = 3x + 10 w punkcie $x: wynosi  $((3*$x + 10))"		    
	#Pobierz wspolczynniki a, b oraz punkt x. Wyznacz wartosc funkcji y = ax + b w zadanym punkcie.	

    echo "Podaj wspolczynniki a, b oraz wspolrzedna x: "
    read a
	read b
	read x

    echo "Wartosc funkcji y = $a x + $b w punkcie $x: wynosi  $(($a*$x + $b))"

	#Otrzymujesz wspolrzedna x. Wyznacz wartosc funkcji y = x^3 + 2*(x^2) - 20 w zadanym punkcie.	

    echo "Podaj wspolrzedna x: "
    read x

    echo "Wartosc funkcji y = x^3 + 2x^2 - 20 w punkcie $x: wynosi  $(($x**3 + 2*($x**2)-20))"
	    
	#Pobierz wspolczynniki a, b, c, d, m, n oraz wspolrzedna x. Wyznacz wartosc funkcji y = a*x^m + b*x^n + c - a w zadanym punkcie.	

    echo "Podaj wspolczynniki a, b, c, d, m, n oraz wspolrzedna x: "
    read a
	read b
	read c
	read d
	read m
	read n

    echo "Wartosc funkcji  y = $a*x^$m + $b*x^$n + $c - $a w punkcie $x: wynosi  $(( $a*($x**$m) + $b*($x**$n) + $c - $a ))"

}

main "$@"

