# ZAD-06 — Histogram znaków w słowie
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.
# 
# ### Wejście
# 
# * 1 linia: napis
# 
# ### Wyjście
# 
# * Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# klasa
# ```
# 
# **Wyjście:**
# 
# ```
# {'k': 1, 'l': 1, 'a': 2, 's': 1}
# ```

# Uzycie:
#   bash zad06.sh                     - uruchamia testy
#   bash zad06.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

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

# Wypisuje slownik: znak -> liczba wystapien w napisie $1 (znaki w kolejnosci
# pierwszego wystapienia; liczy sie kazdy znak, takze spacja i cyfry).
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(k), k - liczba roznych znakow
histogram_znakow() {
    local napis=$1 znak i
    local -A licznik=()
    local -a kolejnosc=()
    for ((i = 0; i < ${#napis}; i++)); do
        znak=${napis:i:1}
        if [[ -z ${licznik[$znak]+x} ]]; then
            kolejnosc+=("$znak")
            licznik[$znak]=0
        fi
        licznik[$znak]=$((${licznik[$znak]} + 1))
    done
    wypisz_slownik licznik kolejnosc napisy
}

program() {
    local napis
    IFS= read -r napis
    histogram_znakow "$napis"
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

test_histogram_znakow() {
    assertEqual "$(histogram_znakow "aA a")" "{'a': 2, 'A': 1, ' ': 1}" $LINENO
    assertEqual "$(histogram_znakow "1*@*1")" "{'1': 2, '*': 2, '@': 1}" $LINENO
    sprawdz program "klasa" "{'k': 1, 'l': 1, 'a': 2, 's': 1}" $LINENO
    sprawdz program "ala ma kota" "{'a': 4, 'l': 1, ' ': 2, 'm': 1, 'k': 1, 'o': 1, 't': 1}" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_histogram_znakow
    fi
}

main "$@"
