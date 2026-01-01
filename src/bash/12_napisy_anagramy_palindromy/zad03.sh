# Tytul: Sprawdzenie, czy dwa slowa sa anagramami.
# Tresc: Napisz program, ktory dla podanych dwoch napisow sprawdzi, czy sa anagramami. Dwa napisy sa anagramami, jesli jeden z nich mozna zbudowac poprzez przestawienie znakow w drugim.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Wartosc logiczna.
# Przyklad:
# Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostac zwrocona wartosc logiczna: Prawda.

source ../assert.sh

# Funkcja sortujaca znaki w napisie alfabetycznie
# Zlozonosc czasowa: O(n log n), gdzie n to liczba znakow
# Zlozonosc pamieciowa: O(n)
sortuj_napis() {
    local napis=$1
    echo "$napis" | tr -d ' ' | tr -d '\n' | tr -d '\t' | tr -d '\r' | grep -o . | sort | tr -d "\n"
}

# Funkcja sprawdzajaca czy dwa napisy sa anagramami
# Zlozonosc czasowa: O(n log n), gdzie n to dlugosc napisow
# Zlozonosc pamieciowa: O(n)
czy_anagramy() {
    local napis_a="$1"
    local napis_b="$2"

    # Sprawdzenie dlugosci
    if [ ${#napis_a} -ne ${#napis_b} ]; then
        echo false
        return
    fi

    # Porownanie posortowanych napisow
    local napis_a_sorted=$(sortuj_napis "$napis_a")
    local napis_b_sorted=$(sortuj_napis "$napis_b")

    if [ "$napis_a_sorted" == "$napis_b_sorted" ]; then
        echo true
    else
        echo false
    fi
}

test_czy_anagramy() {

    assertTrue $(czy_anagramy "kajak" "kajak") $LINENO
    assertFalse $(czy_anagramy "kajak" "kjakk") $LINENO
    assertFalse $(czy_anagramy "adam" "mada") $LINENO

}

main() {
    test_czy_anagramy
}

main "$@"
