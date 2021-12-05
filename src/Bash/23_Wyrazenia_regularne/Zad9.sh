#!/usr/bin/env bash

# Otrzymujesz dwa napisy. Pierwszy napis reprezentuje tekst, a drugi zakazane slowo. 
# Jesli w danym wierszu tekstu wystepuje zakazane slowo, to usun czesc wiersza 
# od wystapienia zakazanego slowa do konca. Zwroc zmodyfikowany tekst.

usun_zakazane_slowo() {
    local tekst="$1"
    local zakazane_slowo="$2"

    for wiersz in $tekst; do
        if [[ $wiersz =~ $zakazane_slowo ]]; then
            local pozycja_zakazanego_slowa=$(echo $wiersz | grep -b -o $zakazane_slowo)   
            pozycja_zakazanego_slowa=${pozycja_zakazanego_slowa%%:*}
            wiersz=${wiersz:0:$pozycja_zakazanego_slowa}
            echo $wiersz
        fi
    done
}

test_usun_zakazane_slowo() {
    local tekst="Turned it up should no valley cousin he.\n 
Speaking numerous ask did horrible packages set.\n
Ashamed herself has distant can studied mrs.\n
Led therefore its middleton perpetual fulfilled provision frankness.\n
Small he drawn after among every three no.\n
All having but you edward genius though remark one.\n
Rooms oh fully taken by worse do.\n
Points afraid but may end law lasted.\n
Was out laughter raptures returned outweigh.\n
Luckily cheered colonel me do we attacks on highest enabled.\n
Tried law yet style child.\n
Bore of true of no be deal.\n
Frequently sufficient in be unaffected.\n
The furnished she concluded depending procuring concealed.\n
"
    local zakazane_slowo="a"
    local wynik=($(usun_zakazane_slowo "$tekst" "$zakazane_slowo"))
    local oczekiwane=('Turned it up should no v' 'Spe' 'Ash' 'Led therefore its middleton perpetu' 'Sm' 'All h' 'Rooms oh fully t' 'Points ' 'W' 'Luckily cheered colonel me do we ' 'Tried l' 'Bore of true of no be de' 'Frequently sufficient in be un' 'The furnished she concluded depending procuring conce')
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_usun_zakazane_slowo
}

main "$@"

