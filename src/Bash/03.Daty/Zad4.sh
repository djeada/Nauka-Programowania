#!/usr/bin/env bash

#Dla pobranej liczby, wypisz dzien tygodnia odpowiadajcy tej liczbie.

main() {
    
    echo "Podaj numer dnia tygodnia:"
		read dzien
	
    if [[ dzien -eq 1 ]]; then
		echo "pierwszym dniem tygodnia jest poniedzialek"
	
	elif [[ dzien -eq 2 ]]; then
		echo "drugim dniem tygodnia jest wtorek"
         
	elif [[ dzien -eq 3 ]]; then
		echo "trzecim dniem tygodnia jest sroda"
    
	elif [[ dzien -eq 4 ]]; then
		echo "czwartym dniem tygodnia jest czwartek"
     
	elif [[ dzien -eq 5 ]]; then
		echo "piatym dniem tygodnia jest piatek"
        
	elif [[ dzien -eq 6 ]]; then
		echo "szostym dniem tygodnia jest sobota"
    
	elif [[ dzien -eq 7 ]]; then
		echo "siodmym dniem tygodnia jest niedziela"      

	else  
		echo "podano niepoprawna liczbe"
  fi
}

main "$@"

