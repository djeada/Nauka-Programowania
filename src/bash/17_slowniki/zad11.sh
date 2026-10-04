# ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach
# 
# **Poziom:** ★☆☆
# **Tagi:** `sort`, `dict`
# 
# ### Treść
# 
# Wczytaj `n` par `klucz wartość`.
# a) Wypisz listę par posortowaną rosnąco po kluczach.
# b) Wypisz listę par posortowaną rosnąco po wartościach.
# 
# ### Wejście
# 
# * 1 linia: `n`
# * następnie `n` linii: `klucz wartość`
# 
# ### Wyjście
# 
# * 1 linia: lista par dla a)
# * 2 linia: lista par dla b)
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 4
# c 3
# x 5
# a -2
# b 4
# ```
# 
# **Wyjście:**
# 
# ```
# [('a', -2), ('b', 4), ('c', 3), ('x', 5)]
# [('a', -2), ('c', 3), ('b', 4), ('x', 5)]
# ```

# Uzycie:
#   bash zad11.sh                     - uruchamia testy
#   bash zad11.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Slownik trzymamy w tablicy asocjacyjnej "slownik" (klucz -> wartosc), a do
# sortowania uzywamy tablicy jego kluczy. Funkcje porownujace odczytuja
# "slownik" funkcji wywolujacej (w Bashu zmienne local maja zasieg dynamiczny).

# Sortuje stabilnie (przez wstawianie) tablice o nazwie $1. $2 to funkcja
# porownujaca: kod powrotu 0, gdy jej pierwszy argument ma byc przed drugim.
# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(1)
sortuj() {
    local -n _tablica=$1
    local mniejszy=$2 i j biezacy
    for ((i = 1; i < ${#_tablica[@]}; i++)); do
        biezacy=${_tablica[i]}
        j=$((i - 1))
        while ((j >= 0)) && "$mniejszy" "$biezacy" "${_tablica[j]}"; do
            _tablica[j + 1]=${_tablica[j]}
            ((j--))
        done
        _tablica[j + 1]=$biezacy
    done
}

# Porzadek wedlug kluczy (porownanie napisow).
klucz_mniejszy() {
    [[ $1 < $2 ]]
}

# Porzadek wedlug wartosci, a przy rownych wartosciach - wedlug kluczy.
wartosc_potem_klucz() {
    local wartosc_a=${slownik[$1]} wartosc_b=${slownik[$2]}
    if ((wartosc_a != wartosc_b)); then
        ((wartosc_a < wartosc_b))
    else
        [[ $1 < $2 ]]
    fi
}

# Wypisuje pary klucz:wartosc dla kluczy z tablicy o nazwie $1.
wypisz_pary() {
    local -n _klucze=$1
    local klucz
    local -a pary=()
    for klucz in "${_klucze[@]}"; do
        pary+=("$klucz:${slownik[$klucz]}")
    done
    echo "${pary[*]}"
}

# Wczytuje n par "klucz wartosc" i wypisuje je posortowane wedlug kluczy,
# a w drugiej linii - wedlug wartosci (przy remisie wedlug kluczy).
program() {
    local n i klucz wartosc
    local -A slownik=()
    local -a po_kluczach=() po_wartosciach
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r klucz wartosc
        if [[ -z ${slownik[$klucz]+x} ]]; then
            po_kluczach+=("$klucz")
        fi
        slownik[$klucz]=$wartosc
    done
    # shellcheck disable=SC2034 # uzywana przez nameref w sortuj i wypisz_pary
    po_wartosciach=("${po_kluczach[@]}")

    sortuj po_kluczach klucz_mniejszy
    sortuj po_wartosciach wartosc_potem_klucz
    wypisz_pary po_kluczach
    wypisz_pary po_wartosciach
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

test_sortuj() {
    local -a liczby=(5 -1 3 3 0)
    liczba_mniejsza() { (($1 < $2)); }
    sortuj liczby liczba_mniejsza
    assertEqual "${liczby[*]}" "-1 0 3 3 5" $LINENO
}

test_program() {
    sprawdz program $'4\nc 3\nx 5\na -2\nb 4' $'a:-2 b:4 c:3 x:5\na:-2 c:3 b:4 x:5' $LINENO
    # "ab" jest przed "b"; rowne wartosci porzadkujemy wedlug kluczy
    sprawdz program $'4\nb 1\nab 1\nzz 0\na 7' $'a:7 ab:1 b:1 zz:0\nzz:0 ab:1 b:1 a:7' $LINENO
    sprawdz program $'1\nk -5' $'k:-5\nk:-5' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_sortuj
        test_program
    fi
}

main "$@"
