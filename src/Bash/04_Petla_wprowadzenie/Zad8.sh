#!/usr/bin/env bash

#Na farmie mamy a glow i b nog, znajdz liczbe kur oraz owieczek.

main() {
    	
	echo "Podaj liczby a glow i b nog: "
  	read a
	read b

	for (( i=1; i<=$a; i++ )); do
		owieczki=$(($a - $i))
		
		if [[ $((2*$i + 4*$owieczki)) -eq $b ]]; then
			echo "Na farmie mamy $i kur i $owieczki owieczek"
			break
		fi


	done

}

main "$@"

