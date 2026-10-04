# ZAD-01 — Wywołanie metody klasy bazowej w klasie potomnej
#
# **Poziom:** ★☆☆
# **Tagi:** `dziedziczenie`, `override`, `super`
#
# ### Treść
#
# Zaprojektuj dwie klasy:
#
# 1. **Bazowa** — posiada metodę `przedstaw_sie()`, która wypisuje komunikat o klasie bazowej.
# 2. **Potomna** — dziedziczy po **Bazowej** i **nadpisuje** metodę `przedstaw_sie()`, ale w swojej implementacji:
#
#    * najpierw **wywołuje** wersję metody z klasy bazowej,
#    * potem dopisuje własny komunikat.
#
# Program testowy:
#
# * tworzy obiekt klasy potomnej,
# * wywołuje metodę `przedstaw_sie()`.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Dwie linie, pokazujące najpierw komunikat klasy bazowej, a potem potomnej.
#
# ### Przykład
#
# **Wyjście:**
#
# ```
# Jestem klasą bazową.
# A ja jestem klasą potomną.
# ```

# Uzycie:
#   bash zad01.sh                     - uruchamia testy
#   bash zad01.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# z polem "klasa", a metoda to funkcja Klasa_metoda, ktorej pierwszym
# argumentem jest nazwa obiektu (odpowiednik self).
# Dziedziczenie: tablica RODZICE mapuje klase na jej klase bazowa. Funkcja
# `wywolaj` szuka metody najpierw w klasie obiektu, a potem w klasach
# bazowych - to daje nadpisywanie metod i polimorfizm. Funkcja `super`
# zaczyna szukanie od klasy bazowej (odpowiednik super()).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.
declare -rA RODZICE=([Potomna]=Bazowa)

# Szuka metody $2 w klasie $1 i (rekurencyjnie) w jej klasach bazowych.
# Nazwe znalezionej funkcji zapisuje w REPLY; kod 1, gdy metody nie ma.
znajdz_metode() {
    local klasa=$1 metoda=$2 rodzic
    local -a rodzice
    if declare -F "${klasa}_${metoda}" >/dev/null; then
        REPLY=${klasa}_${metoda}
        return 0
    fi
    read -ra rodzice <<<"${RODZICE[$klasa]:-}"
    for rodzic in "${rodzice[@]}"; do
        if znajdz_metode "$rodzic" "$metoda"; then
            return 0
        fi
    done
    return 1
}

# Tworzy obiekt $2 klasy $1 i wywoluje jego konstruktor (metode init - takze
# odziedziczona) z pozostalymi argumentami.
nowy() {
    local klasa=$1 obiekt=$2
    shift 2
    declare -gA "$obiekt"
    local -n _nowy=$obiekt
    _nowy=([klasa]="$klasa")
    if znajdz_metode "$klasa" init; then
        "$REPLY" "$obiekt" "$@"
    fi
}

# Wywoluje metode $2 obiektu $1 (wersje wlasciwa dla klasy obiektu).
wywolaj() {
    local obiekt=$1 metoda=$2
    local -n _obiekt=$obiekt
    shift 2
    if ! znajdz_metode "${_obiekt[klasa]}" "$metoda"; then
        echo "Brak metody $metoda w klasie ${_obiekt[klasa]}" >&2
        return 1
    fi
    "$REPLY" "$obiekt" "$@"
}

# Odpowiednik super().metoda(): wywoluje metode $3 obiektu $2, szukajac jej
# od klasy bazowej klasy $1.
super() {
    local klasa=$1 obiekt=$2 metoda=$3
    shift 3
    if ! znajdz_metode "${RODZICE[$klasa]:-}" "$metoda"; then
        echo "Brak metody $metoda w klasie bazowej klasy $klasa" >&2
        return 1
    fi
    "$REPLY" "$obiekt" "$@"
}

# ---- Klasa Bazowa ----
Bazowa_init() {
    local -n _ten=$1
    _ten+=([nazwa]="$2")
}

Bazowa_przedstaw_sie() {
    local -n _ten=$1
    echo "Jestem klasą bazową. Nazywam się ${_ten[nazwa]}."
}

# ---- Klasa Potomna (Bazowa) - konstruktor dziedziczy, przedstaw_sie nadpisuje ----
Potomna_przedstaw_sie() {
    super Potomna "$1" przedstaw_sie
    echo "A ja jestem klasą potomną."
}

# Wczytuje opisy obiektow, tworzy je i dla kazdego wywoluje przedstaw_sie.
program() {
    local n i rodzaj nazwa obiekt
    local -a obiekty=()
    read -r n
    for ((i = 1; i <= n; i++)); do
        read -r rodzaj nazwa
        if [[ $rodzaj == bazowa ]]; then
            nowy Bazowa "obiekt_$i" "$nazwa"
        else
            nowy Potomna "obiekt_$i" "$nazwa"
        fi
        obiekty+=("obiekt_$i")
    done
    for obiekt in "${obiekty[@]}"; do
        wywolaj "$obiekt" przedstaw_sie
    done
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

test_dziedziczenie() {
    # Potomna nie ma wlasnego konstruktora - dziedziczy go po Bazowej
    znajdz_metode Potomna init
    assertEqual "$REPLY" "Bazowa_init" $LINENO
    znajdz_metode Potomna przedstaw_sie
    assertEqual "$REPLY" "Potomna_przedstaw_sie" $LINENO
    znajdz_metode Potomna lec
    assertEqual $? 1 $LINENO

    nowy Potomna ola Ola
    assertEqual "$(wywolaj ola przedstaw_sie)" \
        $'Jestem klasą bazową. Nazywam się Ola.\nA ja jestem klasą potomną.' $LINENO
}

test_program() {
    sprawdz program $'3\nbazowa Ala\npotomna Ola\nbazowa Jan' "Jestem klasą bazową. Nazywam się Ala.
Jestem klasą bazową. Nazywam się Ola.
A ja jestem klasą potomną.
Jestem klasą bazową. Nazywam się Jan." $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_dziedziczenie
        test_program
    fi
}

main "$@"
