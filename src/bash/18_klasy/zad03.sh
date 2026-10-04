# ZAD-03 — Pole nałożenia się dwóch prostokątów
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `static`, `geometria`
#
# ### Treść
#
# Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:
#
# * lewy dolny `(x1, y1)`
# * prawy górny `(x2, y2)`
#   Boki równoległe do osi.
#
# Klasa ma mieć:
#
# 1. Konstruktor `(x1, y1, x2, y2)`
# 2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
# 3. Metodę wypisującą informacje o prostokącie.
#
# Program tworzy:
#
# * A: (3, 4) i (9, 6)
# * B: (2, 2) i (7, 5)
#
# Wypisuje oba i pole części wspólnej.
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
# Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
# Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
# Pole części wspólnej: 6
# ```

# Uzycie:
#   bash zad03.sh                     - uruchamia testy
#   bash zad03.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self) - pola obiektu odczytuje przez nameref (local -n). Metoda "statyczna"
# to funkcja Klasa_metoda, ktora nie dostaje self. Metody zwracajace wartosc
# wypisuja ja na stdout.
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.

# Konstruktor: Prostokat_new obiekt x1 y1 x2 y2 (lewy dolny i prawy gorny wierzcholek)
Prostokat_new() {
    declare -gA "$1"
    local -n _prostokat=$1
    _prostokat=([x1]="$2" [y1]="$3" [x2]="$4" [y2]="$5")
}

# Odpowiednik __str__
Prostokat_str() {
    local -n _prostokat=$1
    echo "lewy dolny (${_prostokat[x1]}, ${_prostokat[y1]}), prawy górny (${_prostokat[x2]}, ${_prostokat[y2]})"
}

# Metoda statyczna: pole czesci wspolnej prostokatow $1 i $2. Lewa krawedz
# czesci wspolnej to wieksza z lewych krawedzi, prawa - mniejsza z prawych
# (analogicznie w pionie). Brak nalozenia lub styk krawedzia daje 0.
# Zlozonosc czasowa: O(1)
Prostokat_pole_wspolne() {
    local -n _a=$1 _b=$2
    local lewa=$((_a[x1] > _b[x1] ? _a[x1] : _b[x1]))
    local prawa=$((_a[x2] < _b[x2] ? _a[x2] : _b[x2]))
    local dolna=$((_a[y1] > _b[y1] ? _a[y1] : _b[y1]))
    local gorna=$((_a[y2] < _b[y2] ? _a[y2] : _b[y2]))
    if ((prawa <= lewa || gorna <= dolna)); then
        echo 0
    else
        echo $(((prawa - lewa) * (gorna - dolna)))
    fi
}

# Wczytuje dwa prostokaty i wypisuje je oraz pole ich czesci wspolnej.
program() {
    local x1 y1 x2 y2
    read -r x1 y1 x2 y2
    Prostokat_new prostokat_a "$x1" "$y1" "$x2" "$y2"
    read -r x1 y1 x2 y2
    Prostokat_new prostokat_b "$x1" "$y1" "$x2" "$y2"

    echo "Prostokąt A: $(Prostokat_str prostokat_a)"
    echo "Prostokąt B: $(Prostokat_str prostokat_b)"
    echo "Pole części wspólnej: $(Prostokat_pole_wspolne prostokat_a prostokat_b)"
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

test_pole_wspolne() {
    Prostokat_new duzy 0 0 10 10
    Prostokat_new w_srodku 2 3 4 8
    Prostokat_new obok 10 0 12 5
    Prostokat_new na_ukos 10 10 11 11
    Prostokat_new daleko -20 -20 -15 -15
    Prostokat_new zachodzacy -5 -5 2 3
    assertEqual "$(Prostokat_pole_wspolne duzy w_srodku)" 10 $LINENO
    assertEqual "$(Prostokat_pole_wspolne w_srodku duzy)" 10 $LINENO
    # Styk bokiem lub wierzcholkiem to pole 0
    assertEqual "$(Prostokat_pole_wspolne duzy obok)" 0 $LINENO
    assertEqual "$(Prostokat_pole_wspolne duzy na_ukos)" 0 $LINENO
    assertEqual "$(Prostokat_pole_wspolne duzy daleko)" 0 $LINENO
    assertEqual "$(Prostokat_pole_wspolne duzy zachodzacy)" 6 $LINENO
    assertEqual "$(Prostokat_pole_wspolne duzy duzy)" 100 $LINENO
}

test_program() {
    sprawdz program $'3 4 9 6\n2 2 7 5' "Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 4" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_pole_wspolne
        test_program
    fi
}

main "$@"
