# ZAD-05 — Klasa Macierz
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `macierze`, `operacje`
#
# ### Treść
#
# Zaprojektuj klasę **Macierz**:
#
# 1. Konstruktor przyjmuje listę list (domyślnie pusta).
# 2. Operacje: dodawanie, odejmowanie, mnożenie.
# 3. Metoda wypisująca macierz (wierszami).
# 4. Porównania `==` i `!=`.
#
# (Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)
#
# Program tworzy:
#
# * A = [[1, 3], [4, 2]]
# * B = [[5, 0], [1, 3]]
#
# Wypisuje A, B, a potem A+B, A-B, A*B.
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
# Macierz A:
# [1, 3]
# [4, 2]
#
# Macierz B:
# [5, 0]
# [1, 3]
#
# Suma macierzy:
# [6, 3]
# [5, 5]
#
# Różnica macierzy A - B:
# [-4, 3]
# [3, -1]
#
# Iloczyn macierzy A * B:
# [8, 9]
# [22, 12]
# ```

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self) - pola obiektu odczytuje przez nameref (local -n).
# Macierz trzyma wymiary w polach "wiersze" i "kolumny", a element (i, j)
# pod kluczem "i,j". Operatory tworza NOWA macierz o nazwie podanej w $1,
# np. Macierz_dodaj c a b (c = a + b); przy niezgodnych wymiarach zwracaja kod 1
# (odpowiednik None).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji (stad np. nazwy macierz_suma).

# Konstruktor: Macierz_new obiekt [wiersz ...], gdzie wiersz to napis z liczbami
# oddzielonymi spacjami, np. Macierz_new a "1 3" "4 2". Bez wierszy - macierz pusta.
Macierz_new() {
    local obiekt=$1 wiersz i=0 j
    shift
    local -a liczby
    declare -gA "$obiekt"
    local -n _macierz=$obiekt
    _macierz=([wiersze]=$# [kolumny]=0)
    for wiersz in "$@"; do
        read -ra liczby <<<"$wiersz"
        if ((i > 0 && ${#liczby[@]} != _macierz[kolumny])); then
            echo "Macierz_new: wiersze roznej dlugosci" >&2
            return 1
        fi
        _macierz[kolumny]=${#liczby[@]}
        for j in "${!liczby[@]}"; do
            _macierz[$i,$j]=${liczby[j]}
        done
        ((i++))
    done
    return 0
}

# Odpowiednik __str__: wiersze w osobnych liniach, elementy oddzielone spacja.
Macierz_str() {
    local -n _macierz=$1
    local i j
    local -a wiersz
    for ((i = 0; i < _macierz[wiersze]; i++)); do
        wiersz=()
        for ((j = 0; j < _macierz[kolumny]; j++)); do
            wiersz+=("${_macierz[$i,$j]}")
        done
        echo "${wiersz[*]}"
    done
}

# Tworzy macierz $1 = $2 + $4 * $3 ($4 = 1 - suma, $4 = -1 - roznica).
# Wymaga rownych wymiarow.
_Macierz_dodaj_lub_odejmij() {
    local wynik=$1 znak=$4 i j
    local -n _a=$2 _b=$3
    local -a wiersze=() wiersz
    if ((_a[wiersze] != _b[wiersze] || _a[kolumny] != _b[kolumny])); then
        return 1
    fi
    for ((i = 0; i < _a[wiersze]; i++)); do
        wiersz=()
        for ((j = 0; j < _a[kolumny]; j++)); do
            wiersz+=("$((${_a[$i,$j]} + znak * ${_b[$i,$j]}))")
        done
        wiersze+=("${wiersz[*]}")
    done
    Macierz_new "$wynik" "${wiersze[@]}"
}

# Odpowiednik __add__ i __sub__
Macierz_dodaj() { _Macierz_dodaj_lub_odejmij "$1" "$2" "$3" 1; }
Macierz_odejmij() { _Macierz_dodaj_lub_odejmij "$1" "$2" "$3" -1; }

# Odpowiednik __mul__: $1 = $2 * $3, c[i][j] = suma po k z a[i][k] * b[k][j].
# Wymaga, by liczba kolumn $2 byla rowna liczbie wierszy $3.
# Zlozonosc czasowa: O(n*m*q)
Macierz_pomnoz() {
    local wynik=$1 i j k suma
    local -n _a=$2 _b=$3
    local -a wiersze=() wiersz
    if ((_a[kolumny] != _b[wiersze])); then
        return 1
    fi
    for ((i = 0; i < _a[wiersze]; i++)); do
        wiersz=()
        for ((j = 0; j < _b[kolumny]; j++)); do
            suma=0
            for ((k = 0; k < _a[kolumny]; k++)); do
                ((suma += ${_a[$i,$k]} * ${_b[$k,$j]}))
            done
            wiersz+=("$suma")
        done
        wiersze+=("${wiersz[*]}")
    done
    Macierz_new "$wynik" "${wiersze[@]}"
}

# Odpowiednik __eq__: te same wymiary i te same elementy.
Macierz_rowne() {
    local -n _a=$1 _b=$2
    local i j
    if ((_a[wiersze] != _b[wiersze] || _a[kolumny] != _b[kolumny])); then
        return 1
    fi
    for ((i = 0; i < _a[wiersze]; i++)); do
        for ((j = 0; j < _a[kolumny]; j++)); do
            ((${_a[$i,$j]} == ${_b[$i,$j]})) || return 1
        done
    done
    return 0
}

# Wczytuje ze stdin "n m" i n wierszy, tworzy z nich macierz o nazwie $1.
wczytaj_macierz() {
    local n i
    local -a wiersze=()
    read -r n _
    for ((i = 0; i < n; i++)); do
        IFS= read -r 'wiersze[i]'
    done
    Macierz_new "$1" "${wiersze[@]}"
}

# Wypisuje naglowek $1, macierz o nazwie $2 (albo "Niezgodne wymiary.", gdy $2
# jest puste) i pusta linie.
wypisz_blok() {
    echo "$1"
    if [[ -n $2 ]]; then
        Macierz_str "$2"
    else
        echo "Niezgodne wymiary."
    fi
    echo
}

program() {
    # Nazwy obiektow z wynikami (puste, gdy dzialania nie da sie wykonac)
    local suma=macierz_suma roznica=macierz_roznica iloczyn=macierz_iloczyn
    wczytaj_macierz macierz_a
    wczytaj_macierz macierz_b
    Macierz_dodaj macierz_suma macierz_a macierz_b || suma=""
    Macierz_odejmij macierz_roznica macierz_a macierz_b || roznica=""
    Macierz_pomnoz macierz_iloczyn macierz_a macierz_b || iloczyn=""

    wypisz_blok "Macierz A:" macierz_a
    wypisz_blok "Macierz B:" macierz_b
    wypisz_blok "Suma macierzy:" "$suma"
    wypisz_blok "Różnica macierzy A - B:" "$roznica"
    wypisz_blok "Iloczyn macierzy A * B:" "$iloczyn"
    if Macierz_rowne macierz_a macierz_b; then
        echo "Macierze A i B są równe."
    else
        echo "Macierze A i B są różne."
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

test_macierz() {
    Macierz_new a "1 2 3" "4 5 6"
    Macierz_new b "7 8" "9 10" "11 12"
    Macierz_pomnoz c a b
    assertEqual "$(Macierz_str c)" $'58 64\n139 154' $LINENO
    Macierz_dodaj d a b
    assertEqual $? 1 $LINENO
    Macierz_new e "1 2 3" "4 5 6"
    Macierz_rowne a e
    assertEqual $? 0 $LINENO
    Macierz_rowne a b
    assertEqual $? 1 $LINENO
    Macierz_new pusta
    assertEqual "$(Macierz_str pusta)" "" $LINENO
}

test_program() {
    sprawdz program $'2 2\n1 3\n4 2\n2 2\n5 0\n1 3' "Macierz A:
1 3
4 2

Macierz B:
5 0
1 3

Suma macierzy:
6 3
5 5

Różnica macierzy A - B:
-4 3
3 -1

Iloczyn macierzy A * B:
8 9
22 6

Macierze A i B są różne." $LINENO
    sprawdz program $'1 2\n1 2\n1 2\n3 4' "Macierz A:
1 2

Macierz B:
3 4

Suma macierzy:
4 6

Różnica macierzy A - B:
-2 -2

Iloczyn macierzy A * B:
Niezgodne wymiary.

Macierze A i B są różne." $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_macierz
        test_program
    fi
}

main "$@"
