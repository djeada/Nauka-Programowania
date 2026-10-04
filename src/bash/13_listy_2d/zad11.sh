# ZAD-11 — Gra w statki (projekt konsolowy)
#
# **Poziom:** ★★★
# **Tagi:** `macierze`, `losowanie`, `gra`, `pętle`
#
# ### Treść
#
# Zaimplementuj grę w statki na planszy 10×10:
#
# 1. Plansza startowa: 10×10 wypełniona `.`
# 2. Losowo rozmieść statki (poziomo/pionowo), bez stykania bokami ani rogami:
#
#    * 1× długość 4
#    * 2× długość 3
#    * 3× długość 2
#    * 5× długość 1
# 3. Pętla gry:
#
#    * wypisz planszę,
#    * wczytaj `r c` (0..9),
#    * jeśli trafienie: wstaw `o`, wypisz komunikat o trafieniu,
#    * jeśli pudło: wstaw `x`, zwiększ licznik pudeł,
#    * gra kończy się, gdy:
#
#      * wszystkie pola statków trafione (wygrana), albo
#      * 10 pudeł (przegrana).
#    * po każdym ruchu wypisz zaktualizowaną planszę.
#
# ### Wejście
#
# Wielokrotnie:
#
# * `r c` (w jednej linii)
#
# ### Wyjście
#
# * plansza i komunikaty w trakcie,
# * na końcu komunikat o wygranej/przegranej.
#
# ### Uwagi praktyczne
#
# * To zadanie jest **większym projektem** — format wyjścia bywa sprawdzany „ręcznie” (nie zawsze automatycznie), więc trzymaj się spójnego stylu wypisywania planszy.

# Uwaga: rozwiazanie wedlug aktualnej tresci ZAD-11 w zbior_zadan/13_listy_2d.md
# (plansza 10×10 podana na wejsciu, strzaly "r c" numerowane od 1).
#
# Uzycie:
#   bash zad11.sh                     - uruchamia testy
#   bash zad11.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

readonly ROZMIAR=10

# Stan gry w zmiennych globalnych:
#   PLANSZA[r*10+c]  - pole (r, c) liczone od 0: '.' woda, '#' statek,
#                      'X' trafione pole statku, 'o' pudlo
#   POZOSTALE_STATKI - liczba niezatopionych statkow
declare -a PLANSZA=()
POZOSTALE_STATKI=0

# Wczytuje 10 linii planszy ze stdin.
wczytaj_plansze() {
    local r c wiersz
    PLANSZA=()
    for ((r = 0; r < ROZMIAR; r++)); do
        IFS= read -r wiersz
        for ((c = 0; c < ROZMIAR; c++)); do
            PLANSZA[r * ROZMIAR + c]=${wiersz:c:1}
        done
    done
}

# Liczy statki na planszy: kazdy statek ma dokladnie jedno pole, ktore nie ma
# pola statku ani nad soba, ani po lewej stronie.
policz_statki() {
    local r c
    POZOSTALE_STATKI=0
    for ((r = 0; r < ROZMIAR; r++)); do
        for ((c = 0; c < ROZMIAR; c++)); do
            [[ ${PLANSZA[r * ROZMIAR + c]} == "#" ]] || continue
            if ((r > 0)) && [[ ${PLANSZA[(r - 1) * ROZMIAR + c]} == "#" ]]; then
                continue
            fi
            if ((c > 0)) && [[ ${PLANSZA[r * ROZMIAR + c - 1]} == "#" ]]; then
                continue
            fi
            ((POZOSTALE_STATKI++))
        done
    done
}

# Sprawdza (kod powrotu 0), czy statek, do ktorego nalezy pole ($1, $2),
# jest zatopiony: idziemy w cztery strony po polach statku ('#' lub 'X');
# statek nie jest zatopiony, dopoki ktores z jego pol jest jeszcze '#'.
czy_zatopiony() {
    local r=$1 c=$2 kierunek dr dc rr cc pole
    for kierunek in "-1 0" "1 0" "0 -1" "0 1"; do
        read -r dr dc <<<"$kierunek"
        rr=$((r + dr))
        cc=$((c + dc))
        while ((rr >= 0 && rr < ROZMIAR && cc >= 0 && cc < ROZMIAR)); do
            pole=${PLANSZA[rr * ROZMIAR + cc]}
            if [[ $pole == "#" ]]; then
                return 1
            elif [[ $pole != "X" ]]; then
                break
            fi
            rr=$((rr + dr))
            cc=$((cc + dc))
        done
    done
    return 0
}

# Odczytuje z linii $1 wspolrzedne strzalu (1..10) i zapisuje je - jako
# indeksy od 0 - w zmiennych o nazwach $2 i $3. Kod 1, gdy linia nie jest
# para liczb calkowitych z zakresu 1..10.
odczytaj_strzal() {
    local -n _wiersz=$2 _kolumna=$3
    local wzorzec='^[[:space:]]*\+?([0-9]+)[[:space:]]+\+?([0-9]+)[[:space:]]*$'
    local tekst_r tekst_c
    if [[ ! $1 =~ $wzorzec ]]; then
        return 1
    fi
    # Usuwamy zera wiodace (inaczej np. "08" byloby liczba osemkowa), a zbyt
    # dlugie liczby od razu odrzucamy (nie zmieszcza sie w zakresie 1..10)
    tekst_r=${BASH_REMATCH[1]}
    tekst_r=${tekst_r#"${tekst_r%%[!0]*}"}
    tekst_c=${BASH_REMATCH[2]}
    tekst_c=${tekst_c#"${tekst_c%%[!0]*}"}
    if ((${#tekst_r} > 2 || ${#tekst_c} > 2)) ||
        ((${tekst_r:-0} < 1 || tekst_r > ROZMIAR || ${tekst_c:-0} < 1 || tekst_c > ROZMIAR)); then
        return 1
    fi
    _wiersz=$((tekst_r - 1))
    _kolumna=$((tekst_c - 1))
}

# Rozstrzyga strzal w pole ($1, $2) (indeksy od 0) i wypisuje wynik.
strzel() {
    local r=$1 c=$2
    case ${PLANSZA[r * ROZMIAR + c]} in
        X | o)
            echo "Pole już ostrzelane"
            ;;
        "#")
            PLANSZA[r * ROZMIAR + c]="X"
            if czy_zatopiony "$r" "$c"; then
                ((POZOSTALE_STATKI--))
                echo "Trafiony, zatopiony"
            else
                echo "Trafiony"
            fi
            ;;
        *)
            PLANSZA[r * ROZMIAR + c]="o"
            echo "Pudło"
            ;;
    esac
}

# Wczytuje plansze i rozstrzyga kolejne strzaly az do wygranej albo konca danych.
program() {
    local linia wiersz kolumna liczba_strzalow=0
    wczytaj_plansze
    policz_statki
    while IFS= read -r linia || [[ -n $linia ]]; do
        ((liczba_strzalow++))
        if ! odczytaj_strzal "$linia" wiersz kolumna; then
            echo "Niepoprawny strzał"
            continue
        fi
        strzel "$wiersz" "$kolumna"
        if ((POZOSTALE_STATKI == 0)); then
            echo "Wygrana po $liczba_strzalow strzałach"
            return
        fi
    done
    echo "Pozostało statków: $POZOSTALE_STATKI"
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

readonly PLANSZA_PRZYKLAD="#.........
#.........
..........
....###...
..........
..........
.........#
..........
.##.......
.........."

test_odczytaj_strzal() {
    local wiersz kolumna linia
    odczytaj_strzal "10 10" wiersz kolumna
    assertEqual "$wiersz $kolumna" "9 9" $LINENO
    odczytaj_strzal "  08   1 " wiersz kolumna
    assertEqual "$wiersz $kolumna" "7 0" $LINENO
    odczytaj_strzal "0003 +10" wiersz kolumna
    assertEqual "$wiersz $kolumna" "2 9" $LINENO
    for linia in "" "1" "1 1 1" "0 5" "00 5" "11 3" "-1 3" "a b" "1.5 2" "1 99999999999999999999"; do
        odczytaj_strzal "$linia" wiersz kolumna
        assertEqual $? 1 $LINENO
    done
}

test_policz_statki() {
    wczytaj_plansze <<<"$PLANSZA_PRZYKLAD"
    policz_statki
    assertEqual "$POZOSTALE_STATKI" 4 $LINENO
}

test_program() {
    sprawdz program "$PLANSZA_PRZYKLAD
1 1
5 5
2 1
1 1
11 3
7 10" "Trafiony
Pudło
Trafiony, zatopiony
Pole już ostrzelane
Niepoprawny strzał
Trafiony, zatopiony
Pozostało statków: 2" $LINENO
    # Brak strzalow
    sprawdz program "$PLANSZA_PRZYKLAD" "Pozostało statków: 4" $LINENO
    # Wygrana: linie po ostatnim strzale sa pomijane, a licza sie wszystkie
    # wczytane linie ze strzalami (takze niepoprawne i powtorzone)
    sprawdz program "##........
..........
..........
..........
..........
..........
..........
..........
..........
.........#
1 2
1 2
zle
10 10
1 1
5 5" "Trafiony
Pole już ostrzelane
Niepoprawny strzał
Trafiony, zatopiony
Trafiony, zatopiony
Wygrana po 5 strzałach" $LINENO
    # Statek pionowy trafiony najpierw w srodku
    sprawdz program "..........
..#.......
..#.......
..#.......
..........
..........
..........
..........
..........
..........
3 3
2 3
4 3" "Trafiony
Trafiony
Trafiony, zatopiony
Wygrana po 3 strzałach" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_odczytaj_strzal
        test_policz_statki
        test_program
    fi
}

main "$@"
