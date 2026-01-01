# ZAD-09 — Usuwanie plików większych niż 10 kB

source ../assert.sh

# Funkcja usuwająca pliki wieksze niz 10kB
# Zlozonosc czasowa: O(n), gdzie n to liczba plikow
# Zlozonosc pamieciowa: O(1)
usun_pliki_wieksze_niz_10k() {
    local katalog=$1
    
    for plik in "$katalog"/*; do
        if [ -f "$plik" ]; then
            local rozmiar=$(stat -f%z "$plik" 2>/dev/null || stat -c%s "$plik" 2>/dev/null)
            if [ "$rozmiar" -gt 10240 ]; then
                rm "$plik"
            fi
        fi
    done
}

test_usun_pliki_wieksze_niz() {
    mkdir -p 'test'
    
    # Tworzenie plikow testowych
    echo "maly plik" > 'test/maly.txt'
    
    usun_pliki_wieksze_niz_10k 'test'
    
    # Sprawdzenie czy male pliki zostaly
    assertTrue $(if [[ -f 'test/maly.txt' ]]; then echo "true"; else echo "false"; fi) $LINENO
    
    rm -rf 'test'
}

main() {
    test_usun_pliki_wieksze_niz
}

main "$@"
