#!/usr/bin/env bash

#Napisz funkcje realizujaca zaokraglanie ilorazu 
#bez użycia '/' i '%'.

podziel() {
	a=$1
	b=$2
	znak=1
	
	if [[ $b -eq 0 ]]; then
		echo "Error!"
		return
	fi
	
	if [[ $a -eq 0 ]]; then
		return 0
	fi

	if [[ $a -lt $b ]]; then
		znak=-1
		a=$(($a*-1))
	fi
	
	if [[ $b -lt 0 ]]; then
		znak=$(($znak*-1))
		b=$(($b*-1))
	fi
	
	if [[ $znak -eq 1 ]]; then
		licznik=0 
		while [[ $a -ge $b ]]; do
			a=$(($a - $b))
			licznik=$(($licznik + 1))
		done
	else
		licznik=1 
		while [[ $a -gt $b ]]; do
			a=$(($a - $b))
			licznik=$(($licznik + 1))
		done
	fi
	
	wynik=$(($licznik*$znak))
	
	return $wynik
}

main() {
    echo "Podaj dwie liczby: "
	read a
	read b

	podziel $a $b
	wynik=$?
    echo "iloraz pierwszej przez druga: $wynik"

}

main "$@"

