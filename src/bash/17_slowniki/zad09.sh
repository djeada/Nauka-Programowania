# ZAD-09 — Znaki występujące co najmniej dwa razy
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.
# 
# ### Wejście
# 
# * 1 linia: napis
# 
# ### Wyjście
# 
# * 1 linia: wynikowy napis
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# aaabbbccc
# ```
# 
# **Wyjście:**
# 
# ```
# abc
# ```

# Uzycie:
#   bash zad09.sh                     - uruchamia testy
#   bash zad09.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca napis zlozony z (unikalnych) znakow napisu $1, ktore wystepuja co
# najmniej 2 razy - w kolejnosci pierwszego wystapienia. Wystapienia liczymy
# w tablicy asocjacyjnej, a kolejnosc pierwszych wystapien w tablicy indeksowanej.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(k), k - liczba roznych znakow
znaki_powtorzone() {
    local napis=$1 znak wynik="" i
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

    for znak in "${kolejnosc[@]}"; do
        if ((${licznik[$znak]} >= 2)); then
            wynik+=$znak
        fi
    done

    echo "$wynik"
}

program() {
    local napis
    IFS= read -r napis
    znaki_powtorzone "$napis"
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

test_znaki_powtorzone() {
    assertEqual "$(znaki_powtorzone "abcab")" "ab" $LINENO
    assertEqual "$(znaki_powtorzone "baab")" "ba" $LINENO
    # Wielkosc liter ma znaczenie
    assertEqual "$(znaki_powtorzone "AaBbAa")" "Aa" $LINENO
    assertEqual "$(znaki_powtorzone "abc")" "" $LINENO
    sprawdz program "aaabbbccc" "abc" $LINENO
    sprawdz program "x1y1x" "x1" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_znaki_powtorzone
    fi
}

main "$@"
