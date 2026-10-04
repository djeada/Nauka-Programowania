# ZAD-06 — Klasa LiczbaZespolona
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `operacje`, `math`
#
# ### Treść
#
# Zaprojektuj klasę **LiczbaZespolona**:
#
# * konstruktor `(re=0, im=0)`,
# * dodawanie, odejmowanie, mnożenie, dzielenie,
# * porównania,
# * moduł,
# * wypisywanie w formacie `a + bi` lub `a - bi` (z zachowaniem znaku).
#
# Program tworzy:
#
# * A = 9 + 12i
# * B = -3 - 3i
#
# Wypisuje A, B oraz: sumę, różnicę A-B, iloczyn i iloraz A/B.
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
# Liczba A: 9 + 12i
# Liczba B: -3 - 3i
#
# Suma: 6 + 9i
# Różnica A - B: 12 + 15i
# Iloczyn: 27 + 63i
# Iloraz A / B: -3.5 + 0.5i
# ```

# Uzycie:
#   bash zad06.sh                     - uruchamia testy
#   bash zad06.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self) - pola obiektu odczytuje przez nameref (local -n). Operatory tworza
# NOWY obiekt o nazwie podanej w $1, np. LiczbaZespolona_dodaj c a b.
#
# Czesci liczby zespolonej moga byc rzeczywiste (np. po dzieleniu), a Bash
# liczy tylko na liczbach calkowitych - dzialania wykonuje wiec awk
# (LC_ALL=C wymusza kropke dziesietna; "+ 0" zamienia -0 na 0).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji (stad np. nazwy liczba_suma).

# Konstruktor: LiczbaZespolona_new obiekt [re=0] [im=0]
LiczbaZespolona_new() {
    declare -gA "$1"
    local -n _liczba=$1
    _liczba=([re]="${2:-0}" [im]="${3:-0}")
}

# Tworzy obiekt $1 z wyniku dzialania na liczbach $2 = a + bi i $3 = c + di;
# $4 to instrukcje awk ustawiajace re i im.
_LiczbaZespolona_dzialanie() {
    local wynik=$1 wzor=$4 re im
    local -n _x=$2 _y=$3
    read -r re im < <(LC_ALL=C awk -v a="${_x[re]}" -v b="${_x[im]}" -v c="${_y[re]}" -v d="${_y[im]}" \
        "BEGIN { $wzor; printf \"%.17g %.17g\\n\", re + 0, im + 0 }")
    LiczbaZespolona_new "$wynik" "$re" "$im"
}

# Odpowiedniki __add__, __sub__, __mul__
LiczbaZespolona_dodaj() {
    _LiczbaZespolona_dzialanie "$1" "$2" "$3" 're = a + c; im = b + d'
}
LiczbaZespolona_odejmij() {
    _LiczbaZespolona_dzialanie "$1" "$2" "$3" 're = a - c; im = b - d'
}
LiczbaZespolona_pomnoz() {
    _LiczbaZespolona_dzialanie "$1" "$2" "$3" 're = a * c - b * d; im = a * d + b * c'
}

# Odpowiednik __truediv__; przy dzielniku 0 + 0i zwraca kod 1.
LiczbaZespolona_podziel() {
    LiczbaZespolona_new _zero 0 0
    if LiczbaZespolona_rowne "$3" _zero; then
        return 1
    fi
    _LiczbaZespolona_dzialanie "$1" "$2" "$3" \
        'm = c * c + d * d; re = (a * c + b * d) / m; im = (b * c - a * d) / m'
}

# Odpowiednik __eq__: kod powrotu 0, gdy czesci rzeczywiste i urojone sa rowne.
LiczbaZespolona_rowne() {
    local -n _x=$1 _y=$2
    LC_ALL=C awk -v a="${_x[re]}" -v b="${_x[im]}" -v c="${_y[re]}" -v d="${_y[im]}" \
        'BEGIN { exit !(a == c && b == d) }'
}

# Modul: sqrt(re^2 + im^2)
LiczbaZespolona_modul() {
    local -n _liczba=$1
    LC_ALL=C awk -v a="${_liczba[re]}" -v b="${_liczba[im]}" 'BEGIN { printf "%.17g\n", sqrt(a * a + b * b) }'
}

# Odpowiednik __str__: "a + bi" albo "a - bi" (2 miejsca po przecinku).
LiczbaZespolona_str() {
    local -n _liczba=$1
    local re=${_liczba[re]} im=${_liczba[im]} znak="+"
    if [[ $im == -* ]]; then
        znak="-"
        im=${im#-}
    fi
    LC_ALL=C printf '%.2f %s %.2fi\n' "$re" "$znak" "$im"
}

# Wczytuje liczby A i B i wypisuje wyniki dzialan.
program() {
    local re im
    read -r re im
    LiczbaZespolona_new liczba_a "$re" "$im"
    read -r re im
    LiczbaZespolona_new liczba_b "$re" "$im"
    LiczbaZespolona_dodaj liczba_suma liczba_a liczba_b
    LiczbaZespolona_odejmij liczba_roznica liczba_a liczba_b
    LiczbaZespolona_pomnoz liczba_iloczyn liczba_a liczba_b

    echo "Liczba A: $(LiczbaZespolona_str liczba_a)"
    echo "Liczba B: $(LiczbaZespolona_str liczba_b)"
    echo "Suma: $(LiczbaZespolona_str liczba_suma)"
    echo "Różnica A - B: $(LiczbaZespolona_str liczba_roznica)"
    echo "Iloczyn: $(LiczbaZespolona_str liczba_iloczyn)"
    if LiczbaZespolona_podziel liczba_iloraz liczba_a liczba_b; then
        echo "Iloraz A / B: $(LiczbaZespolona_str liczba_iloraz)"
    else
        echo "Iloraz A / B: nie można dzielić przez zero"
    fi
    LC_ALL=C printf 'Moduł liczby A: %.2f\n' "$(LiczbaZespolona_modul liczba_a)"
    if LiczbaZespolona_rowne liczba_a liczba_b; then
        echo "Liczby są równe."
    else
        echo "Liczby są różne."
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

test_liczba_zespolona() {
    LiczbaZespolona_new i 0 1
    LiczbaZespolona_pomnoz minus_jeden i i
    assertEqual "$(LiczbaZespolona_str minus_jeden)" "-1.00 + 0.00i" $LINENO
    LiczbaZespolona_new zero
    LiczbaZespolona_podziel iloraz_przez_zero i zero
    assertEqual $? 1 $LINENO
    LiczbaZespolona_podziel jeden i i
    assertEqual "$(LiczbaZespolona_str jeden)" "1.00 + 0.00i" $LINENO
    LiczbaZespolona_new trzy_cztery 3 -4
    assertEqual "$(LiczbaZespolona_modul trzy_cztery)" 5 $LINENO
}

test_program() {
    sprawdz program $'9 12\n-3 -3' "Liczba A: 9.00 + 12.00i
Liczba B: -3.00 - 3.00i
Suma: 6.00 + 9.00i
Różnica A - B: 12.00 + 15.00i
Iloczyn: 9.00 - 63.00i
Iloraz A / B: -3.50 - 0.50i
Moduł liczby A: 15.00
Liczby są różne." $LINENO
    sprawdz program $'1 -1\n0 0' "Liczba A: 1.00 - 1.00i
Liczba B: 0.00 + 0.00i
Suma: 1.00 - 1.00i
Różnica A - B: 1.00 - 1.00i
Iloczyn: 0.00 + 0.00i
Iloraz A / B: nie można dzielić przez zero
Moduł liczby A: 1.41
Liczby są różne." $LINENO
    sprawdz program $'2 3\n2 3' "Liczba A: 2.00 + 3.00i
Liczba B: 2.00 + 3.00i
Suma: 4.00 + 6.00i
Różnica A - B: 0.00 + 0.00i
Iloczyn: -5.00 + 12.00i
Iloraz A / B: 1.00 + 0.00i
Moduł liczby A: 3.61
Liczby są równe." $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_liczba_zespolona
        test_program
    fi
}

main "$@"
