# ZAD-01 — Klasa Koło
#
# **Poziom:** ★★☆
# **Tagi:** `class`, `metody`, `float`, `math`
#
# ### Treść
#
# Zaprojektuj klasę **Koło**:
#
# 1. Konstruktor przyjmuje promień `r` (domyślnie 1).
# 2. Metoda licząca **obwód**: ( 2\pi r )
# 3. Metoda licząca **pole**: ( \pi r^2 )
# 4. Metoda wypisująca informacje: promień, obwód i pole.
#
# Program ma utworzyć koło o promieniu wczytanym z wejścia (np. 3) i wypisać informacje.
#
# ### Wejście
#
# * 1 linia: `r` (liczba rzeczywista)
#
# ### Wyjście
#
# Trzy linie jak w przykładzie (obwód i pole do 4 miejsc po przecinku).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ```
#
# **Wyjście:**
#
# ```
# Koło o promieniu: 3
# Obwód koła: 18.8496
# Pole koła: 28.2743
# ```

# Uzycie:
#   bash zad01.sh                     - uruchamia testy
#   bash zad01.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# (jej nazwa sluzy za referencje do obiektu), a metoda to funkcja
# Klasa_metoda, ktorej pierwszym argumentem jest nazwa obiektu (odpowiednik
# self) - pola obiektu odczytuje przez nameref (local -n). Metody zwracajace
# wartosc wypisuja ja na stdout.
#
# Bash liczy tylko na liczbach calkowitych, wiec pi i mnozenie liczb
# rzeczywistych liczy awk (LC_ALL=C wymusza kropke jako separator dziesietny).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.

# Konstruktor: Kolo_new obiekt [r=1]
Kolo_new() {
    declare -gA "$1"
    local -n _kolo=$1
    _kolo=([r]="${2:-1}")
}

# Zwraca obwod kola: 2 * pi * r
Kolo_obwod() {
    local -n _kolo=$1
    LC_ALL=C awk -v r="${_kolo[r]}" 'BEGIN { printf "%.17g\n", 2 * atan2(0, -1) * r }'
}

# Zwraca pole kola: pi * r^2
Kolo_pole() {
    local -n _kolo=$1
    LC_ALL=C awk -v r="${_kolo[r]}" 'BEGIN { printf "%.17g\n", atan2(0, -1) * r * r }'
}

# Wypisuje promien, obwod i pole z dokladnoscia do 2 miejsc po przecinku.
Kolo_wypisz() {
    local -n _kolo=$1
    LC_ALL=C printf 'Koło o promieniu: %.2f\n' "${_kolo[r]}"
    LC_ALL=C printf 'Obwód koła: %.2f\n' "$(Kolo_obwod "$1")"
    LC_ALL=C printf 'Pole koła: %.2f\n' "$(Kolo_pole "$1")"
}

# Wczytuje promien, tworzy kolo i wypisuje informacje o nim.
program() {
    local r
    read -r r
    Kolo_new kolo "$r"
    Kolo_wypisz kolo
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

test_kolo() {
    # Konstruktor z domyslnym promieniem 1
    Kolo_new jednostkowe
    assertEqual "$(Kolo_wypisz jednostkowe)" \
        $'Koło o promieniu: 1.00\nObwód koła: 6.28\nPole koła: 3.14' $LINENO
    sprawdz program "3" $'Koło o promieniu: 3.00\nObwód koła: 18.85\nPole koła: 28.27' $LINENO
    sprawdz program "2.5" $'Koło o promieniu: 2.50\nObwód koła: 15.71\nPole koła: 19.63' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_kolo
    fi
}

main "$@"
