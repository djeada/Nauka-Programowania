# ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`, `tekst`
# 
# ### Treść
# 
# Wczytaj tekst. Policz częstość występowania słów (tylko litery), ignorując wielkość liter. Wypisz słownik: słowo (małe litery) → liczba wystąpień.
# 
# ### Wejście
# 
# * 1 linia: tekst
# 
# ### Wyjście
# 
# * Słownik
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Ala ma kota. Ala lubi koty.
# ```
# 
# **Wyjście:**
# 
# ```
# {'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
# ```

# Uzycie:
#   bash zad07.sh                     - uruchamia testy
#   bash zad07.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

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

# Wypisuje slownik: slowo (malymi literami) -> liczba wystapien w tekscie $1.
# Slowo to ciag liter ([[:alpha:]] - przy locale UTF-8 takze polskich);
# kazdy inny znak zamieniamy na spacje, a potem dzielimy tekst po spacjach.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
histogram_slow() {
    local tekst=${1,,} slowo
    local -a slowa kolejnosc=()
    local -A licznik=()
    tekst=${tekst//[^[:alpha:]]/ }
    read -ra slowa <<<"$tekst"
    for slowo in "${slowa[@]}"; do
        if [[ -z ${licznik[$slowo]+x} ]]; then
            kolejnosc+=("$slowo")
            licznik[$slowo]=0
        fi
        licznik[$slowo]=$((${licznik[$slowo]} + 1))
    done
    wypisz_slownik licznik kolejnosc napisy
}

program() {
    local tekst
    IFS= read -r tekst
    histogram_slow "$tekst"
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

test_histogram_slow() {
    local polska_litera="ż"
    assertEqual "$(histogram_slow "Kot, KOT i kot!")" "{'kot': 3, 'i': 1}" $LINENO
    assertEqual "$(histogram_slow "a1b2a")" "{'a': 2, 'b': 1}" $LINENO
    assertEqual "$(histogram_slow "123 ... !")" "{}" $LINENO
    # Polskie litery wymagaja locale UTF-8 (wtedy "ż" to jeden znak)
    if ((${#polska_litera} == 1)); then
        assertEqual "$(histogram_slow "Żółw i ŻÓŁW.")" "{'żółw': 2, 'i': 1}" $LINENO
    fi
    sprawdz program "Ala ma kota. Ala lubi koty." "{'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_histogram_slow
    fi
}

main "$@"
