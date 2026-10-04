# ZAD-08 — Najczęstsza litera w zdaniu
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
# Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.
# 
# ### Wejście
# 
# * 1 linia: zdanie
# 
# ### Wyjście
# 
# * 1 znak
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# lezy jerzy na wiezy
# ```
# 
# **Wyjście:**
# 
# ```
# e
# ```

# Uzycie:
#   bash zad08.sh                     - uruchamia testy
#   bash zad08.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca (mala) litere wystepujaca najczesciej w zdaniu $1, bez rozrozniania
# wielkosci liter i z pominieciem znakow niebedacych literami. Przy remisie
# wygrywa litera, ktora pojawia sie w zdaniu jako pierwsza - przechodzimy po
# literach w kolejnosci pierwszego wystapienia i zamieniamy tylko na wieksza liczbe.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(k), k - liczba roznych liter
najczestsza_litera() {
    local zdanie=${1,,} znak litera najlepsza="" i
    local -A licznik=()
    local -a kolejnosc=()

    for ((i = 0; i < ${#zdanie}; i++)); do
        znak=${zdanie:i:1}
        if [[ $znak != [[:alpha:]] ]]; then
            continue
        fi
        if [[ -z ${licznik[$znak]+x} ]]; then
            kolejnosc+=("$znak")
            licznik[$znak]=0
        fi
        licznik[$znak]=$((${licznik[$znak]} + 1))
    done

    for litera in "${kolejnosc[@]}"; do
        if [[ -z $najlepsza ]] || ((${licznik[$litera]} > ${licznik[$najlepsza]})); then
            najlepsza=$litera
        fi
    done

    echo "$najlepsza"
}

program() {
    local zdanie
    IFS= read -r zdanie
    najczestsza_litera "$zdanie"
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

test_najczestsza_litera() {
    assertEqual "$(najczestsza_litera "Ala ma Asa")" "a" $LINENO
    assertEqual "$(najczestsza_litera "baab")" "b" $LINENO
    assertEqual "$(najczestsza_litera "Hello, World!!! 777")" "l" $LINENO
    assertEqual "$(najczestsza_litera "X")" "x" $LINENO
    sprawdz program "lezy jerzy na wiezy" "e" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_najczestsza_litera
    fi
}

main "$@"
