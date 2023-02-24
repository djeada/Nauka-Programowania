#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy zdanie. Zapisz w liscie cyfry 
# bedace czescia slow. Cyfry odseparowane od liter spacjami pomin.

cyfry_bedace_czescia_slow() {
    local zdanie="$1"
    local cyfry=()
    
    for slowo in $zdanie; do
        if [[ $slowo =~ [a-zA-Z]+ ]]; then
            cyfry+=($(echo $slowo | sed -r 's/[a-zA-Z|]+//g'))
        fi
    done

    echo ${cyfry[@]}
}

test_cyfry_bedace_czescia_slow() {
    local zdanie="jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go"
    local wynik=($(cyfry_bedace_czescia_slow "$zdanie"))
    local oczekiwane=(29 37 3891 3)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_cyfry_bedace_czescia_slow
}


main "$@"

