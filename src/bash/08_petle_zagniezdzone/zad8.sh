#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby N,
#wypisze N pierwszych liczb pierwszych.


czyPierwsza() {

    if [[ $1 -eq 2 ]] || [[ $1 -eq 3 ]]; then
        return 1
    fi
    if [[ $(($1 % 2)) -eq 0 ]] || [[ $(($1 % 3)) -eq 0 ]]; then
        return 0
    fi
    temp=5; w=2
    while [[ $((temp * temp)) -le $1 ]]; do
        if [[ $(($temp % temp)) -eq 0 ]]; then
            return 0
        fi
        temp=$((temp + w))
        w=$((6 - w))
    done
    return 1
}

liczbyPierwszeV1() {
    for (( i=2; i<$1; i++ ))
    do
        if ! czyPierwsza $i; then
            echo -n "$i "
        fi
    done
    echo ""
}

main() {

    liczbyPierwszeV1 25

}

main "$@"

