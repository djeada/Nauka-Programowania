#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego. Oblicz:
# a) Liczbę wierszy pliku.
# b) Liczbę słów w pliku. Słowa oddzielone są spacjami i mogą składać 
# się wyłącznie ze znaków będących literami.
# c) Średnią długość wiersza.
# d) Średnią liczbę słów na wiersz.
# e) Częstość występowania każdego ze słów w pliku.

wczytaj_plik() {
    local plik="$1"
    local lista=()
    while read -r wiersz; do
        lista+=("$wiersz")
    done < "$plik"
    echo "${lista[@]}"
}

liczba_wierszy() {
    echo "${#lista[@]}"
}

podziel_zdanie_na_slowa() {
    zdanie="$1"
    echo "$zdanie" | tr -s ' ' '\n'
}

na_male() {
    for (( i=0; i<${#slowa[@]}; i++ ));
    do
        slowa[$i]=$( echo "${slowa[$i]}" | awk '{print tolower($0)}')
    done 
}

liczba_slow() {
    local licznik=0
    for wiersz in "${lista[@]}"; do
        IFS='~' 
        read -r -a slowa <<<=($(podziel_zdanie_na_slowa "$wiersz"))
        IFS=' '
        licznik=$((licznik+${#slowa[@]}))
    done
    echo "$licznik"
}

srednia_dlugosc_wiersza() {
    local suma=0
    for wiersz in "${lista[@]}"; do
        suma=$((suma+${#wiersz}))
    done
    echo "scale=2; $suma / ${#lista[@]}" | bc
}

srednia_liczba_slow_na_wiersz() {
    local suma=0
    for wiersz in "${lista[@]}"; do
        IFS='~' 
        read -r -a slowa <<<=($(podziel_zdanie_na_slowa "$wiersz"))
        IFS=' '
        suma=$((suma+${#slowa[@]}))
    done
    echo "scale=2; $suma / ${#lista[@]}" | bc
}

czestosc_slow() {
    local slowa=()
    for wiersz in "${lista[@]}"; do
        IFS='~' 
        read -r -a slowa <<<=($(podziel_zdanie_na_slowa "$wiersz"))
        IFS=' '
        for slowo in "${slowa[@]}"; do
            if [[ ! " ${slowa[@]} " =~ " $slowo " ]]; then
                slowa+=("$slowo")
            fi
        done
    done
    for slowo in "${slowa[@]}"; do
        echo "$slowo"
    done | sort | uniq -c | sort -nr    
}

test_statystyki() {

    # stworz folder testowy
    mkdir -p 'test'

    # stworz plik testowy
    touch 'test/test.txt'

    # wypelnij plik testowy
    echo -e 'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of \".txt\".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.' > 'test/test.txt'

    # wczytaj plik testowy
    wczytaj_plik 'test/test.txt'

    # sprawdz liczbe wierszy
    assertEquals "$(liczba_wierszy)" "4"

    # sprawdz liczbe slow
    assertEquals "$(liczba_slow)" "42"

    # sprawdz srednia dlugosc wiersza
    assertEquals "$(srednia_dlugosc_wiersza)" "42.00"

    # sprawdz srednia liczbe slow na wiersz
    assertEquals "$(srednia_liczba_slow_na_wiersz)" "7.00"

    # sprawdz czestosc slow
    assertEquals "$(czestosc_slow)" 'hello 1 this 1 is 1 an 1 example 1 of 1 a 1 simple 1 ascii 1 text 1 file 1 stored 1 on 1 a 1 web 1 server 1 note 1 that 1 it 1 has 1 a 1 file 1 extension 1 of 1 \".txt\" 1 although 1 such 1 files 1 may 1 contain 1 some 1 basic 1 layout 1 formatting 1 such 1 as 1 paragraphs 1 there 1 is 1 no 1 support 1 for 1 the 1 text 1 to 1 have 1 attributes 1 such 1 as 1 bolding 1 text 1 files 1 can 1 contain 1 Hypertext 1 Mark-up 1 codes 1 but 1 these 1 will 1 not 1 be 1 interpreted 1 by 1 the 1 browser 1 for 1 example 1 if 1 the 1 following 1 characters 1 <strong>hello</strong> 1 were 1 typed 1 into 1 an 1 \""html\" 1 file 1 then 1 the 1 word 1 \"hello\" 1 would 1 be 1 shown 1 in 1 bold 1'

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_statystyki
}

main "$@"