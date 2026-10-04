# ZAD-02 — Klasa Punkt
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `static`, `porównania`, `math`
#
# ### Treść
#
# Zaprojektuj klasę **Punkt**:
#
# 1. Konstruktor `(x=0, y=0)`.
# 2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
# 3. Metoda wypisująca współrzędne.
# 4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).
#
# Program tworzy:
#
# * A = (5, 5)
# * B = (-3, -3)
#
# Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Jak w przykładzie.
#
# ### Przykład
#
# **Wyjście:**
#
# ```
# Punkt A: (5, 5)
# Punkt B: (-3, -3)
# Odległość między punktami A i B: 11.3137
# ```

# Uzycie:
#   bash zad02.sh                     - uruchamia testy
#   bash zad02.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self) - pola obiektu odczytuje przez nameref (local -n). Metoda "statyczna"
# to funkcja Klasa_metoda, ktora nie dostaje self. Metody zwracajace wartosc
# wypisuja ja na stdout, a porownania zwracaja kod powrotu (0 = prawda).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.

# Konstruktor: Punkt_new obiekt [x=0] [y=0]
Punkt_new() {
    declare -gA "$1"
    local -n _punkt=$1
    _punkt=([x]="${2:-0}" [y]="${3:-0}")
}

# Metoda statyczna: odleglosc miedzy punktami $1 i $2. Pierwiastek wymaga
# liczb rzeczywistych, wiec liczy go awk (LC_ALL=C - kropka dziesietna).
Punkt_odleglosc() {
    local -n _p1=$1 _p2=$2
    local dx=$((_p1[x] - _p2[x])) dy=$((_p1[y] - _p2[y]))
    LC_ALL=C awk -v kwadrat=$((dx * dx + dy * dy)) 'BEGIN { printf "%.17g\n", sqrt(kwadrat) }'
}

# Odpowiednik __str__: "(x, y)"
Punkt_str() {
    local -n _punkt=$1
    echo "(${_punkt[x]}, ${_punkt[y]})"
}

# Odpowiednik __eq__: kod powrotu 0, gdy obie wspolrzedne sa rowne.
Punkt_rowne() {
    local -n _p1=$1 _p2=$2
    ((_p1[x] == _p2[x] && _p1[y] == _p2[y]))
}

# Wczytuje dwa punkty i wypisuje je, ich odleglosc oraz informacje o rownosci.
program() {
    local x y
    read -r x y
    Punkt_new punkt_a "$x" "$y"
    read -r x y
    Punkt_new punkt_b "$x" "$y"

    echo "Punkt A: $(Punkt_str punkt_a)"
    echo "Punkt B: $(Punkt_str punkt_b)"
    LC_ALL=C printf 'Odległość między punktami A i B: %.2f\n' "$(Punkt_odleglosc punkt_a punkt_b)"
    if Punkt_rowne punkt_a punkt_b; then
        echo "Punkty są równe."
    else
        echo "Punkty są różne."
    fi
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

test_punkt() {
    Punkt_new poczatek
    Punkt_new p 3 4
    assertEqual "$(Punkt_str poczatek)" "(0, 0)" $LINENO
    assertEqual "$(Punkt_odleglosc poczatek p)" 5 $LINENO
    Punkt_rowne poczatek p
    assertEqual $? 1 $LINENO
    Punkt_new q 3 4
    Punkt_rowne p q
    assertEqual $? 0 $LINENO
}

test_program() {
    sprawdz program $'5 5\n-3 -3' $'Punkt A: (5, 5)\nPunkt B: (-3, -3)
Odległość między punktami A i B: 11.31\nPunkty są różne.' $LINENO
    sprawdz program $'-1 2\n-1 2' $'Punkt A: (-1, 2)\nPunkt B: (-1, 2)
Odległość między punktami A i B: 0.00\nPunkty są równe.' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_punkt
        test_program
    fi
}

main "$@"
