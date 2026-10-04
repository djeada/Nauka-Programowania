# ZAD-04 — Klasy Wektor2D i Wektor3D
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `operatory`, `math`
#
# ### Treść
#
# Zaprojektuj klasy **Wektor2D** i **Wektor3D**:
#
# Wspólne:
#
# * konstruktor z domyślnymi współrzędnymi 0,
# * dodawanie, odejmowanie,
# * iloczyn skalarny,
# * porównania `==` i `!=`,
# * moduł (długość),
# * metoda wypisująca wektor.
#
# Dodatkowo dla **Wektor3D**:
#
# * iloczyn wektorowy.
#
# Program tworzy:
#
# * A = (-3, -3, -3)
# * B = (5, 5, 5)
#
# Wypisuje A, B oraz:
#
# * A + B
# * A - B
# * A · B
# * A × B
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
# Wektor A: (-3, -3, -3)
# Wektor B: (5, 5, 5)
# Suma wektorów: (2, 2, 2)
# Różnica wektorów A - B: (-8, -8, -8)
# Iloczyn skalarny: -45
# Iloczyn wektorowy: (0, 0, 0)
# ```

# Uzycie:
#   bash zad04.sh                     - uruchamia testy
#   bash zad04.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu; pole "klasa" zapamietuje klase),
# a metoda to funkcja Klasa_metoda, ktorej pierwszym argumentem jest nazwa
# obiektu (odpowiednik self) - pola obiektu odczytuje przez nameref (local -n).
# Operatory (+, -, iloczyn wektorowy) tworza NOWY obiekt o nazwie podanej
# w pierwszym argumencie, np. Wektor3D_dodaj c a b  (c = a + b).
#
# Wektor2D i Wektor3D roznia sie tylko liczba wspolrzednych, wiec ich metody
# korzystaja ze wspolnych funkcji _Wektor_*, ktore czytaja nazwy wspolrzednych
# klasy z tablicy WSPOLRZEDNE.
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji (stad np. nazwy wektor_suma).
declare -grA WSPOLRZEDNE=([Wektor2D]="x y" [Wektor3D]="x y z")

# Tworzy obiekt $2 klasy $1 o wspolrzednych $3, $4, ... (brakujace = 0).
_Wektor_new() {
    local klasa=$1 obiekt=$2 i
    shift 2
    local -a osie wartosci=("$@")
    read -ra osie <<<"${WSPOLRZEDNE[$klasa]}"
    declare -gA "$obiekt"
    local -n _wektor=$obiekt
    _wektor=([klasa]="$klasa")
    for i in "${!osie[@]}"; do
        _wektor[${osie[i]}]=${wartosci[i]:-0}
    done
}

# Tworzy wektor $1 = $2 + $4 * $3 tej samej klasy co $2
# ($4 = 1 - suma, $4 = -1 - roznica).
_Wektor_dzialanie() {
    local wynik=$1 znak=$4 os
    local -n _a=$2 _b=$3
    local -a osie wartosci=()
    read -ra osie <<<"${WSPOLRZEDNE[${_a[klasa]}]}"
    for os in "${osie[@]}"; do
        wartosci+=("$((${_a[$os]} + znak * ${_b[$os]}))")
    done
    _Wektor_new "${_a[klasa]}" "$wynik" "${wartosci[@]}"
}

# Iloczyn skalarny: suma iloczynow odpowiadajacych sobie wspolrzednych.
_Wektor_iloczyn_skalarny() {
    local -n _a=$1 _b=$2
    local os suma=0
    local -a osie
    read -ra osie <<<"${WSPOLRZEDNE[${_a[klasa]}]}"
    for os in "${osie[@]}"; do
        ((suma += ${_a[$os]} * ${_b[$os]}))
    done
    echo "$suma"
}

# Dlugosc wektora = sqrt(iloczyn skalarny wektora z samym soba). Pierwiastek
# liczy awk (Bash ma tylko liczby calkowite; LC_ALL=C - kropka dziesietna).
_Wektor_dlugosc() {
    LC_ALL=C awk -v kwadrat="$(_Wektor_iloczyn_skalarny "$1" "$1")" \
        'BEGIN { printf "%.17g\n", sqrt(kwadrat) }'
}

# Odpowiednik __eq__: kod powrotu 0, gdy klasy i wszystkie wspolrzedne sa rowne.
_Wektor_rowne() {
    local -n _a=$1 _b=$2
    local os
    local -a osie
    [[ ${_a[klasa]} == "${_b[klasa]}" ]] || return 1
    read -ra osie <<<"${WSPOLRZEDNE[${_a[klasa]}]}"
    for os in "${osie[@]}"; do
        ((${_a[$os]} == ${_b[$os]})) || return 1
    done
    return 0
}

# Odpowiednik __str__: "(x, y)" albo "(x, y, z)"
_Wektor_str() {
    local -n _wektor=$1
    local os wynik=""
    local -a osie
    read -ra osie <<<"${WSPOLRZEDNE[${_wektor[klasa]}]}"
    for os in "${osie[@]}"; do
        wynik+=", ${_wektor[$os]}"
    done
    echo "(${wynik:2})"
}

# ---- Klasa Wektor2D ----
Wektor2D_new() { _Wektor_new Wektor2D "$1" "${2:-0}" "${3:-0}"; }
Wektor2D_dodaj() { _Wektor_dzialanie "$1" "$2" "$3" 1; }
Wektor2D_odejmij() { _Wektor_dzialanie "$1" "$2" "$3" -1; }
Wektor2D_iloczyn_skalarny() { _Wektor_iloczyn_skalarny "$1" "$2"; }
Wektor2D_dlugosc() { _Wektor_dlugosc "$1"; }
Wektor2D_rowne() { _Wektor_rowne "$1" "$2"; }
Wektor2D_str() { _Wektor_str "$1"; }

# ---- Klasa Wektor3D ----
Wektor3D_new() { _Wektor_new Wektor3D "$1" "${2:-0}" "${3:-0}" "${4:-0}"; }
Wektor3D_dodaj() { _Wektor_dzialanie "$1" "$2" "$3" 1; }
Wektor3D_odejmij() { _Wektor_dzialanie "$1" "$2" "$3" -1; }
Wektor3D_iloczyn_skalarny() { _Wektor_iloczyn_skalarny "$1" "$2"; }
Wektor3D_dlugosc() { _Wektor_dlugosc "$1"; }
Wektor3D_rowne() { _Wektor_rowne "$1" "$2"; }
Wektor3D_str() { _Wektor_str "$1"; }

# Iloczyn wektorowy (tylko 3D): $1 = $2 × $3
Wektor3D_iloczyn_wektorowy() {
    local -n _a=$2 _b=$3
    Wektor3D_new "$1" \
        $((${_a[y]} * ${_b[z]} - ${_a[z]} * ${_b[y]})) \
        $((${_a[z]} * ${_b[x]} - ${_a[x]} * ${_b[z]})) \
        $((${_a[x]} * ${_b[y]} - ${_a[y]} * ${_b[x]}))
}

# Wczytuje dwa wektory (2 liczby - Wektor2D, 3 liczby - Wektor3D) i wypisuje
# wyniki dzialan.
program() {
    local klasa
    local -a a b
    read -ra a
    read -ra b
    if ((${#a[@]} == 2)); then
        klasa=Wektor2D
    else
        klasa=Wektor3D
    fi
    "${klasa}_new" wektor_a "${a[@]}"
    "${klasa}_new" wektor_b "${b[@]}"
    "${klasa}_dodaj" wektor_suma wektor_a wektor_b
    "${klasa}_odejmij" wektor_roznica wektor_a wektor_b

    echo "Wektor A: $("${klasa}_str" wektor_a)"
    echo "Wektor B: $("${klasa}_str" wektor_b)"
    echo "Suma wektorów: $("${klasa}_str" wektor_suma)"
    echo "Różnica wektorów A - B: $("${klasa}_str" wektor_roznica)"
    echo "Iloczyn skalarny: $("${klasa}_iloczyn_skalarny" wektor_a wektor_b)"
    if [[ $klasa == Wektor3D ]]; then
        Wektor3D_iloczyn_wektorowy wektor_iloczyn wektor_a wektor_b
        echo "Iloczyn wektorowy: $(Wektor3D_str wektor_iloczyn)"
    fi
    LC_ALL=C printf 'Długość wektora A: %.2f\n' "$("${klasa}_dlugosc" wektor_a)"
    if "${klasa}_rowne" wektor_a wektor_b; then
        echo "Wektory są równe."
    else
        echo "Wektory są różne."
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

test_wektory() {
    Wektor3D_new zero
    Wektor3D_new os_x 1
    Wektor3D_new os_y 0 1
    assertEqual "$(Wektor3D_str zero)" "(0, 0, 0)" $LINENO
    Wektor3D_iloczyn_wektorowy os_z os_x os_y
    assertEqual "$(Wektor3D_str os_z)" "(0, 0, 1)" $LINENO
    assertEqual "$(Wektor3D_iloczyn_skalarny os_x os_y)" 0 $LINENO
    assertEqual "$(Wektor3D_dlugosc os_z)" 1 $LINENO

    Wektor2D_new u 1 2
    Wektor2D_new v 1 2
    Wektor2D_rowne u v
    assertEqual $? 0 $LINENO
    Wektor2D_dodaj w u v
    assertEqual "$(Wektor2D_str w)" "(2, 4)" $LINENO
    Wektor2D_rowne u w
    assertEqual $? 1 $LINENO
}

test_program() {
    sprawdz program $'-3 -3 -3\n5 5 5' "Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
Długość wektora A: 5.20
Wektory są różne." $LINENO
    sprawdz program $'3 4\n1 -2' "Wektor A: (3, 4)
Wektor B: (1, -2)
Suma wektorów: (4, 2)
Różnica wektorów A - B: (2, 6)
Iloczyn skalarny: -5
Długość wektora A: 5.00
Wektory są różne." $LINENO
    sprawdz program $'1 2 3\n1 2 3' "Wektor A: (1, 2, 3)
Wektor B: (1, 2, 3)
Suma wektorów: (2, 4, 6)
Różnica wektorów A - B: (0, 0, 0)
Iloczyn skalarny: 14
Iloczyn wektorowy: (0, 0, 0)
Długość wektora A: 3.74
Wektory są równe." $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_wektory
        test_program
    fi
}

main "$@"
