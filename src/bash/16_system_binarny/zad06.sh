# ZAD-06 — Konwersja między dowolnymi systemami (2..36)
#
# **Poziom:** ★★☆
# **Tagi:** `konwersja`, `base`, `string`
#
# ### Treść
#
# Wczytaj:
#
# 1. liczbę `X` zapisaną w systemie o podstawie `p`
# 2. podstawę `p` (2..36)
# 3. podstawę docelową `q` (2..36)
#
# i wypisz reprezentację `X` w systemie o podstawie `q`.
#
# ### Wejście
#
# Trzy linie:
#
# 1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
# 2. `p` (2..36)
# 3. `q` (2..36)
#
# ### Wyjście
#
# Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4301
# 10
# 4
# ```
#
# **Wyjście:**
#
# ```
# 1003031
# ```
#
# ### Uwagi o formacie
#
# * `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
# * Dla wartości 10..35 stosuj `A..Z`.

# Uzycie:
#   bash zad06.sh                     - uruchamia testy
#   bash zad06.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

readonly CYFRY=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Zamienia zapis X ($1) z systemu o podstawie p ($2) na system o podstawie q ($3).
# X moze miec do 20 cyfr (36^20 nie miesci sie w 64 bitach), wiec nie zamieniamy
# go na jedna liczbe: trzymamy liste cyfr w systemie p i wielokrotnie dzielimy ja
# "pisemnie" przez q. Kolejne reszty to cyfry wyniku (od najmlodszej).
# Zlozonosc czasowa: O(d^2), gdzie d to liczba cyfr
# Zlozonosc pamieciowa: O(d)
zmien_system() {
    local x=${1^^} p=$2 q=$3
    local -a cyfry=() iloraz
    local i znak przed_znakiem wartosc reszta biezaca cyfra wynik=""

    for ((i = 0; i < ${#x}; i++)); do
        znak=${x:i:1}
        przed_znakiem=${CYFRY%%"$znak"*}
        wartosc=${#przed_znakiem}
        if ((wartosc >= p)); then
            echo "Niepoprawna cyfra '$znak' w systemie o podstawie $p" >&2
            return 1
        fi
        cyfry+=("$wartosc")
    done

    while ((${#cyfry[@]} > 0)); do
        reszta=0
        iloraz=()
        for cyfra in "${cyfry[@]}"; do
            biezaca=$((reszta * p + cyfra))
            # Pomijamy zera wiodace ilorazu
            if ((${#iloraz[@]} > 0 || biezaca >= q)); then
                iloraz+=("$((biezaca / q))")
            fi
            reszta=$((biezaca % q))
        done
        wynik=${CYFRY:reszta:1}$wynik
        cyfry=("${iloraz[@]}")
    done

    echo "${wynik:-0}"
}

# Wczytuje X, p i q (kazde w osobnej linii) i wypisuje X w systemie q.
program() {
    local x p q
    read -r x
    read -r p
    read -r q
    zmien_system "$x" "$p" "$q"
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

test_zmien_system() {
    sprawdz program $'4301\n10\n4' "1003031" $LINENO
    sprawdz program $'1003031\n4\n10' "4301" $LINENO
    sprawdz program $'FF\n16\n2' "11111111" $LINENO
    sprawdz program $'ZZ\n36\n10' "1295" $LINENO
    sprawdz program $'0\n2\n36' "0" $LINENO
    sprawdz program $'000\n10\n2' "0" $LINENO
    sprawdz program $'0007\n8\n2' "111" $LINENO
    sprawdz program $'35\n10\n36' "Z" $LINENO
    # Liczby wieksze niz 64 bity
    sprawdz program $'18446744073709551616\n10\n16' "10000000000000000" $LINENO
    sprawdz program $'ZZZZZZZZZZZZZZZZZZZZ\n36\n10' "13367494538843734067838845976575" $LINENO
    # Niepoprawna cyfra
    zmien_system "19" 8 10 2>/dev/null
    assertEqual $? 1 $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_zmien_system
    fi
}

main "$@"
