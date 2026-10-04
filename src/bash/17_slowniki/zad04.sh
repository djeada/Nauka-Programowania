# ZAD-04 — Usuń pary ze słownika na podstawie wartości
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `filtrowanie`
#
# ### Treść
#
# Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.
#
# ### Wejście
#
# * 1 linia: `n`
# * następnie `n` linii: `klucz wartość`
# * ostatnia linia: `k`
#
# ### Wyjście
#
# * Słownik po usunięciu par
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4
# aaa 5
# abc 1
# xxx 5
# cba 3
# 5
# ```
#
# **Wyjście:**
#
# ```
# {'abc': 1, 'cba': 3}
# ```

# Uzycie:
#   bash zad04.sh                     - uruchamia testy
#   bash zad04.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Slownik to tablica asocjacyjna (bash 4+). Nie pamieta ona kolejnosci
# dodawania kluczy, wiec kolejnosc trzymamy w osobnej tablicy indeksowanej.

# Wypisuje slownik tak jak print() w Pythonie: {klucz: wartosc, ...}.
# $1 - nazwa tablicy asocjacyjnej, $2 - nazwa tablicy z kluczami w kolejnosci
# dodawania, $3 - "napisy", gdy klucze sa napisami (wypisywane w apostrofach).
wypisz_slownik() {
    local -n _slownik=$1 _klucze=$2
    local apostrof="" klucz wynik=""
    if [[ ${3:-} == napisy ]]; then
        apostrof="'"
    fi
    for klucz in "${_klucze[@]}"; do
        wynik+=", $apostrof$klucz$apostrof: ${_slownik[$klucz]}"
    done
    echo "{${wynik:2}}"
}

# Usuwa ze slownika $1 (z kolejnoscia kluczy w tablicy $2) wszystkie pary
# o wartosci $3. Po kopii kluczy przechodzimy, a usuwamy z oryginalu.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
usun_wartosc() {
    local -n _slownik=$1 _klucze=$2
    local k=$3 klucz
    local -a pozostale=()
    for klucz in "${_klucze[@]}"; do
        if ((${_slownik[$klucz]} == k)); then
            unset '_slownik[$klucz]'
        else
            pozostale+=("$klucz")
        fi
    done
    _klucze=("${pozostale[@]}")
}

# Wczytuje n par "klucz wartosc" i liczbe k, wypisuje slownik bez par o wartosci k.
program() {
    local n i klucz wartosc k
    local -A slownik=()
    local -a klucze=()
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r klucz wartosc
        klucze+=("$klucz")
        slownik[$klucz]=$wartosc
    done
    read -r k
    usun_wartosc slownik klucze "$k"
    wypisz_slownik slownik klucze napisy
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

test_usun_wartosc() {
    local -A slownik=([a]=1 [b]=2 [c]=3 [d]=1)
    local -a klucze=(a b c d)
    usun_wartosc slownik klucze 1
    assertEqual "${klucze[*]}" "b c" $LINENO
    assertEqual "${#slownik[@]}" 2 $LINENO
}

test_program() {
    sprawdz program $'4\naaa 5\nabc 1\nxxx 5\ncba 3\n5' "{'abc': 1, 'cba': 3}" $LINENO
    sprawdz program $'2\nx -1\ny -1\n-1' "{}" $LINENO
    sprawdz program $'1\nx 0\n7' "{'x': 0}" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_usun_wartosc
        test_program
    fi
}

main "$@"
