# Tytul: Usun pliki spelniajace warunek.
# Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu. Usun wszystkie pliki o rozmiarze wiekszym niz 10 kB znajdujace sie w podanym folderze i jego podfolderach.
# Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
# Dane wyjsciowe: Brak.

source ../assert.sh

wczytaj_plik() {
    local plik="$1"
    local lista=()
    while read -r wiersz; do
        lista+=("$wiersz")
    done < "$plik"
    printf '%s\n' "${lista[@]}"
}

liczba_wierszy() {
    local plik="$1"
    wc -l < $plik
}

podziel_zdanie_na_slowa() {

    local zdanie="$1"
    local lista=()

    zdanie=$(echo "$zdanie" | sed -r 's/[''".,:;!?\\@\<\>\/]+/ /g' | tr -s ' ')
    zdanie=$(echo "$zdanie" | sed -r 's/[''".,:;!?\\@\<\>\/]+/ /g' | tr -s ' ')
    zdanie=$(echo "$zdanie" | sed -r 's/[-]+//g')
    lista_slow=($zdanie)
    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                lista+=("$slowo")
            fi
        done

        printf '%s\n' "${lista[@]}"
    }

    liczba_slow() {
        local plik="$1"
        tresc=($(wczytaj_plik $plik))
        local licznik=0
        for wiersz in "${tresc[@]}"; do
            slowa=($(podziel_zdanie_na_slowa "$wiersz"))
            licznik=$((licznik+${#slowa[@]}))
        done
        echo "$licznik"
    }

    srednia_dlugosc_wiersza() {
        local plik="$1"
        local suma_dlugosci_wierszy=$(awk '{print length}' $plik | awk '{s+=$1} END {print s}')
        echo "scale=2; $suma_dlugosci_wierszy / $(liczba_wierszy $plik)" | bc
    }

    srednia_liczba_slow_na_wiersz() {
        local plik="$1"
        echo "scale=2; $(liczba_slow $plik) / $(liczba_wierszy $plik)" | bc
    }

    czestosc_slow() {
        local plik="$1"
        tresc=($(wczytaj_plik $plik))
        local histogram=()

        for wiersz in "${tresc[@]}"; do

            slowa=($(podziel_zdanie_na_slowa "$wiersz"))
            histogram+=(${slowa[@]})
        done

        for slowo in "${histogram[@]}"; do
            echo "$slowo" | awk '{print tolower($0)}'
        done | sort | uniq -c | awk '{print $2, $1}'
    }

    test_statystyki() {

        mkdir -p 'test'
        mkdir -p 'test'

        local plik='test/test.txt'
        local plik='test/test.txt'
        touch $plik

        echo -e 'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of \".txt\".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.' > 'test/test.txt'
        echo -e 'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of \".txt\".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.' > 'test/test.txt'

        assertEqual "$(liczba_wierszy $plik)" "10" $LINENO
        assertEqual "$(liczba_wierszy $plik)" "10" $LINENO

        assertEqual "$(liczba_slow $plik)" "90" $LINENO
        assertEqual "$(liczba_slow $plik)" "90" $LINENO

        assertEqual "$(srednia_dlugosc_wiersza $plik)" "50.70" $LINENO
        assertEqual "$(srednia_dlugosc_wiersza $plik)" "50.70" $LINENO

        assertEqual "$(srednia_liczba_slow_na_wiersz $plik)" "9.00" $LINENO
        assertEqual "$(srednia_liczba_slow_na_wiersz $plik)" "9.00" $LINENO

        local histogram=$(czestosc_slow $plik)
        local oczekiwane=('bold 1' 'in 1' 'shown 1' 'word 1' 'then 1' 'html 1' 'simple 1' 'basic 1' 'contains 1' 'layout 1' 'were 1' 'may 1' 'such 3' 'file 3' 'extension 1' 'files 2' 'it 1' 'hypertext 1' 'hello 2' 'note 1' 'web 1' 'ascii 1' 'is 2' 'an 2' 'example 2' 'hej 1' 'following 1' 'this 1' 'of 2' 'txt 1' 'although 1' 'text 3' 'stored 1' 'that 1' 'by 1' 'on 1' 'formatting 1' 'support 1' 'browser 1' 'typed 1' 'a 3' 'server 1' 'would 1' 'contain 1' 'as 2' 'markup 1' 'characters 1' 'there 1' 'for 2' 'the 4' 'to 1' 'have 1' 'these 1' 'will 1' 'paragraphs 1' 'attributes 1' 'bolding 1' 'can 1' 'has 1' 'codes 1' 'if 1' 'some 1' 'no 1' 'but 1' 'not 1' 'be 2' 'interpreted 1' 'strong 2' 'into 1')
        assertSetsEqual histogram oczekiwane $LINENO

        rm -rf 'test'
        rm -rf 'test'
    }

    main() {
        test_statystyki
    }

    main "$@"

