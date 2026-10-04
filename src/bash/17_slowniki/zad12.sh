# ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)
# 
# **Poziom:** ★★☆
# **Tagi:** `dict`, `porównanie`, `list`
# 
# ### Treść
# 
# Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
# Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.
# 
# ### Wejście
# 
# * Najpierw:
# 
#   * 1 linia: `n`
#   * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
# * Potem:
# 
#   * 1 linia: `m`
#   * następnie `m` linii: `klucz v1 v2 v3 ...`
# 
# ### Wyjście
# 
# * `Prawda` lub `Fałsz`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 2
# a 1 2 3
# b 4 5
# 2
# a 3 2 1
# b 5 4
# ```
# 
# **Wyjście:**
# 
# ```
# Prawda
# ```

# Uzycie:
#   bash zad12.sh                     - uruchamia testy
#   bash zad12.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zapisuje w zmiennej o nazwie $1 liczby z napisu $2 posortowane rosnaco
# (sortowanie przez wstawianie). Posortowana lista to postac "kanoniczna"
# wielozbioru: dwie listy maja te same liczby tyle samo razy dokladnie wtedy,
# gdy po posortowaniu sa rowne.
# Zlozonosc czasowa: O(k^2), k - dlugosc listy
# Zlozonosc pamieciowa: O(k)
posortuj_liczby() {
    local -n _posortowane=$1
    local -a liczby
    local i j biezaca
    read -ra liczby <<<"$2"
    for ((i = 1; i < ${#liczby[@]}; i++)); do
        biezaca=${liczby[i]}
        for ((j = i - 1; j >= 0 && liczby[j] > biezaca; j--)); do
            liczby[j + 1]=${liczby[j]}
        done
        liczby[j + 1]=$biezaca
    done
    _posortowane="${liczby[*]}"
}

# Wczytuje ze stdin slownik (n, potem n linii "klucz v1 v2 ...") do tablicy
# asocjacyjnej o nazwie $1: klucz -> posortowana lista liczb.
wczytaj_slownik() {
    local -n _slownik=$1
    local n i klucz wartosci posortowane
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r klucz wartosci
        posortuj_liczby posortowane "$wartosci"
        _slownik[$klucz]=$posortowane
    done
}

# Wczytuje dwa slowniki ze stdin i wypisuje "Prawda", gdy maja te same klucze
# i pod kazdym kluczem ten sam wielozbior liczb, w przeciwnym razie "Fałsz".
# Zlozonosc czasowa: O(n * k^2)
# Zlozonosc pamieciowa: O(n * k)
program() {
    local -A pierwszy=() drugi=()
    local klucz
    wczytaj_slownik pierwszy
    wczytaj_slownik drugi

    if ((${#pierwszy[@]} != ${#drugi[@]})); then
        echo "Fałsz"
        return
    fi
    for klucz in "${!pierwszy[@]}"; do
        if [[ -z ${drugi[$klucz]+x} || ${drugi[$klucz]} != "${pierwszy[$klucz]}" ]]; then
            echo "Fałsz"
            return
        fi
    done
    echo "Prawda"
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

test_posortuj_liczby() {
    local wynik
    posortuj_liczby wynik "3 -2 10 -2 0"
    assertEqual "$wynik" "-2 -2 0 3 10" $LINENO
}

test_program() {
    sprawdz program $'2\na 1 2 3\nb 4 5\n2\na 3 2 1\nb 5 4' "Prawda" $LINENO
    sprawdz program $'1\na 1 2\n1\na 2 1 1' "Fałsz" $LINENO
    # Kolejnosc kluczy na wejsciu nie ma znaczenia
    sprawdz program $'2\nx -1 7\ny 0\n2\ny 0\nx 7 -1' "Prawda" $LINENO
    sprawdz program $'1\na 1\n1\nb 1' "Fałsz" $LINENO
    sprawdz program $'1\na 1\n2\na 1\nb 1' "Fałsz" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_posortuj_liczby
        test_program
    fi
}

main "$@"
