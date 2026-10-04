# ZAD-01 — Słownik: liczby i ich kwadraty
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `pętla`
#
# ### Treść
#
# Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.
#
# ### Wejście
#
# * 1 linia: `n` (n ≥ 1)
#
# ### Wyjście
#
# * Słownik w postaci: `{1: 1, 2: 4, ...}`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# ```
#
# **Wyjście:**
#
# ```
# {1: 1, 2: 4, 3: 9, 4: 16}
# ```

# Uzycie:
#   bash zad01.sh                     - uruchamia testy
#   bash zad01.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

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

# Tworzy i wypisuje slownik {i: i^2} dla i od 1 do n-1.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
slownik_kwadratow() {
    local n=$1 i
    local -A kwadraty=()
    local -a klucze=()
    for ((i = 1; i < n; i++)); do
        # shellcheck disable=SC2034 # odczytywana przez nameref w wypisz_slownik
        kwadraty[$i]=$((i * i))
        klucze+=("$i")
    done
    wypisz_slownik kwadraty klucze
}

program() {
    local n
    read -r n
    slownik_kwadratow "$n"
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

test_slownik_kwadratow() {
    assertEqual "$(slownik_kwadratow 1)" "{}" $LINENO
    assertEqual "$(slownik_kwadratow 2)" "{1: 1}" $LINENO
    assertEqual "$(slownik_kwadratow 12)" \
        "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121}" $LINENO
    sprawdz program "5" "{1: 1, 2: 4, 3: 9, 4: 16}" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_slownik_kwadratow
    fi
}

main "$@"
