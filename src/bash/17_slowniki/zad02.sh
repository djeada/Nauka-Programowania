# ZAD-02 — Słownik z dwóch list (klucze i wartości)
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `listy`
#
# ### Treść
#
# Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
# Jeśli długości są różne, wypisz pusty słownik `{}`.
#
# ### Wejście
#
# * 1 linia: `n`
# * 2 linia: `m`
# * następnie `n` liczb (pierwsza lista)
# * następnie `m` liczb (druga lista)
#
# ### Wyjście
#
# * Słownik albo `{}`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 3
# 3 5 8
# 1 2 -1
# ```
#
# **Wyjście:**
#
# ```
# {3: 1, 5: 2, 8: -1}
# ```

# Uzycie:
#   bash zad02.sh                     - uruchamia testy
#   bash zad02.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

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

# Tworzy slownik z list kluczy ($1) i wartosci ($2) podanych jako napisy z
# liczbami oddzielonymi spacjami. Przy roznych dlugosciach list slownik jest
# pusty. Powtorzony klucz dostaje ostatnia wartosc, ale zostaje na miejscu
# pierwszego wystapienia (jak kolejne przypisania slownik[klucz] = wartosc).
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
slownik_z_list() {
    local -a klucze_wejscie wartosci kolejnosc=()
    local -A slownik=()
    local i klucz
    read -ra klucze_wejscie <<<"$1"
    read -ra wartosci <<<"$2"

    if ((${#klucze_wejscie[@]} == ${#wartosci[@]})); then
        for i in "${!klucze_wejscie[@]}"; do
            klucz=${klucze_wejscie[i]}
            if [[ -z ${slownik[$klucz]+x} ]]; then
                kolejnosc+=("$klucz")
            fi
            slownik[$klucz]=${wartosci[i]}
        done
    fi

    wypisz_slownik slownik kolejnosc
}

# Wczytuje n, m oraz linie z kluczami i z wartosciami, wypisuje slownik.
program() {
    local klucze wartosci
    read -r _
    read -r _
    read -r klucze
    read -r wartosci
    slownik_z_list "$klucze" "$wartosci"
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

test_slownik_z_list() {
    assertEqual "$(slownik_z_list "1 2 3" "4 5")" "{}" $LINENO
    assertEqual "$(slownik_z_list "1 2 1" "5 6 7")" "{1: 7, 2: 6}" $LINENO
    assertEqual "$(slownik_z_list "-4" "0")" "{-4: 0}" $LINENO
    sprawdz program $'3\n3\n3 5 8\n1 2 -1' "{3: 1, 5: 2, 8: -1}" $LINENO
    sprawdz program $'2\n1\n1 2\n3' "{}" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_slownik_z_list
    fi
}

main "$@"
