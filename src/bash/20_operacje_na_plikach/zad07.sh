# Tytul: Skopiuj pliki.
# Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Skopiuj wszystkie pliki PNG z pierwszego folderu do drugiego folderu.
# Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
# Dane wyjsciowe: Brak.

source ../assert.sh

wstaw_na_poczatek_pliku() {
    local plik="$1"
    local wiersz="$2"

    local tresc_pliku=$(cat "$plik")
    local tresc_pliku=$(cat "$plik")

    echo "$wiersz" > "$plik"
    echo "$wiersz" > "$plik"

    echo "$tresc_pliku" >> "$plik"
    echo "$tresc_pliku" >> "$plik"
}

test_wstaw_na_poczatek_pliku() {

    mkdir -p 'test'
    mkdir -p 'test'

    local plik='test/plik.txt'
    local plik='test/plik.txt'
    touch $plik
    local tresc_pliku='testowy plik'
    echo $tresc_pliku > $plik

    local wiersz='testowy wiersz'
    local wiersz='testowy wiersz'
    wstaw_na_poczatek_pliku $plik $wiersz

    IFS=$'\n' tresc_pliku=($(cat $plik))
    IFS=$'\n' tresc_pliku=($(cat $plik))
    oczekiwane=($wiersz $tresc_pliku)
    assertArrayEqual tresc_pliku oczekiwane $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_wstaw_na_poczatek_pliku
}

main "$@"

