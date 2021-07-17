#!/usr/bin/env bash

#Napisz funkcje, ktora zamieni wartosci miejscami.

swapV1() {

    eval "$1=${!2} $2=${!1}"
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    swapV1 a b

    echo "Liczby zamienione miejscami: $a $b"

}

main "$@"

