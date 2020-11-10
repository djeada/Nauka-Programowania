#!/usr/bin/env bash

#Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie 
#nazwy i hasla oraz zwracac otrzymane dane.

inicjalizacjaDanych() {
	echo "podaj nazwe oraz haslo do zapamietania"
	read nazwaTemp
	read hasloTemp
	eval "$1=$nazwaTemp $2=$hasloTemp"
}

#Druga powinna otrzymywac dane od pierwszej i ponownie prosic o
#podanie nazwy oraz hasla, dopoki dane nie beda identyczne z tymi
#podanymi za pierwszym razem.

czyDanePoprawne() {
	
	staraNazwa=$1
	stareHaslo=$2
	
	nowaNazwa=""
	noweHaslo=""


	while [[ $nowaNazwa != $staraNazwa ]] || [[ $noweHaslo != $stareHaslo ]]
	do
		echo "Aby zalogowac sie do systemu: podaj nazwe oraz haslo"
		read nowaNazwa
		read noweHaslo
	done

	echo "Logowanie do systemu przebieglo pomyslnie"
}

main() {
  	nazwa=""
	haslo=""
	inicjalizacjaDanych nazwa haslo
	czyDanePoprawne $nazwa $haslo
}

main "$@"

