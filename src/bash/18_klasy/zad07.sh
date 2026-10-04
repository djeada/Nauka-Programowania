# ZAD-07 — Zliczanie instancji klasy
#
# **Poziom:** ★☆☆
# **Tagi:** `class`, `static`
#
# ### Treść
#
# Zaprojektuj klasę **MojaKlasa**, która zlicza ile instancji utworzono:
#
# * prywatne pole statyczne licznik,
# * konstruktor zwiększa licznik,
# * metoda statyczna zwraca licznik.
#
# Program tworzy np. 3 obiekty i wypisuje liczbę instancji.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Jedna linia.
#
# ### Przykład
#
# **Wyjście:**
#
# ```
# Liczba utworzonych instancji: 3
# ```

# Uzycie:
#   bash zad07.sh                     - uruchamia testy
#   bash zad07.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self). Atrybut klasy (wspolny dla wszystkich obiektow) to zmienna globalna
# Klasa_atrybut; podkreslenie na poczatku oznacza pole "prywatne".
_MojaKlasa_licznik=0

# Konstruktor: zwieksza licznik klasy i zapisuje numer obiektu w polu "numer".
MojaKlasa_new() {
    declare -gA "$1"
    local -n _obiekt=$1
    ((_MojaKlasa_licznik++))
    _obiekt=([numer]=$_MojaKlasa_licznik)
}

# Zwraca numer obiektu.
MojaKlasa_numer() {
    local -n _obiekt=$1
    echo "${_obiekt[numer]}"
}

# Metoda statyczna: liczba dotychczas utworzonych obiektow.
MojaKlasa_liczba_instancji() {
    echo "$_MojaKlasa_licznik"
}

# Wykonuje n polecen "nowy" / "ile".
program() {
    local n i polecenie
    read -r n
    for ((i = 1; i <= n; i++)); do
        read -r polecenie
        case $polecenie in
            nowy)
                MojaKlasa_new "obiekt_$i"
                echo "Utworzono obiekt nr $(MojaKlasa_numer "obiekt_$i")."
                ;;
            ile)
                echo "Liczba utworzonych instancji: $(MojaKlasa_liczba_instancji)"
                ;;
        esac
    done
}

# Uruchamia funkcje $1 z wejsciem $2 i porownuje jej wyjscie (dokladnie, wraz
# z koncowym znakiem nowej linii) z $3. ${x@Q} wymusza porownanie napisow.
sprawdz() {
    local funkcja=$1 wejscie=$2 oczekiwane=$3 linia=$4 wynik
    wynik=$("$funkcja" <<<"$wejscie"; printf x)
    wynik=${wynik%x}
    if [[ -n $oczekiwane ]]; then
        oczekiwane+=$'\n'
    fi
    assertEqual "${wynik@Q}" "${oczekiwane@Q}" "$linia"
}

# Program dziala w podpowloce, wiec startuje z licznikiem rownym biezacemu -
# dlatego ten test uruchamiamy przed testami tworzacymi obiekty.
test_program() {
    sprawdz program $'5\nnowy\nnowy\nile\nnowy\nile' "Utworzono obiekt nr 1.
Utworzono obiekt nr 2.
Liczba utworzonych instancji: 2
Utworzono obiekt nr 3.
Liczba utworzonych instancji: 3" $LINENO
    sprawdz program $'1\nile' "Liczba utworzonych instancji: 0" $LINENO
}

test_licznik() {
    local przed
    przed=$(MojaKlasa_liczba_instancji)
    MojaKlasa_new pierwszy
    MojaKlasa_new drugi
    assertEqual "$(MojaKlasa_liczba_instancji)" $((przed + 2)) $LINENO
    assertEqual "$(MojaKlasa_numer pierwszy)" $((przed + 1)) $LINENO
    assertEqual "$(MojaKlasa_numer drugi)" $((przed + 2)) $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_program
        test_licznik
    fi
}

main "$@"
