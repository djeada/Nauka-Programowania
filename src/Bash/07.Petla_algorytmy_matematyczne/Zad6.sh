#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
#ich najmniejsza wspolna wielokrotnosc.

nwd() {
	
	a=$1
	b=$2
	
	while [ $b -ne $(($a % $b)) ]; do
        		c=$b
        		b=$(($a % $b))
		a=$c
		
		if (( $b == 0 )); then
        			break;
    		fi
    	done

	echo $a
}

nww() {
	echo $(($a * $b / $(nwd $a $b)))
}

#Testy
test1() {
	a=14
	b=21
	wynik=42
	assert "$wynik -eq $(nww $a $b)" $LINENO
}

main() {
	test1

}

main "$@"

