# ZAD-05 — Dziedziczenie wielokrotne: Ptak
#
# **Poziom:** ★★☆
# **Tagi:** `multiple inheritance`, `dziedziczenie`, `metody`
#
# ### Treść
#
# Zaprojektuj klasy:
#
# * **Zwierz** — metody:
#
#   * `jedz()` → wypisuje `Ptak je.`
#   * `spij()` → wypisuje `Ptak śpi.`
#   * `wydaj_dzwiek()` → wypisuje `Ptak wydaje dźwięk.`
#
# * **ObiektLatajacy** — metody:
#
#   * `lec()` → wypisuje `Ptak leci.`
#   * `wyladuj()` → wypisuje `Ptak ląduje.`
#
# * **Ptak** — dziedziczy po `Zwierz` oraz `ObiektLatajacy`.
#
# Program testowy:
#
# * tworzy obiekt `Ptak`,
# * wywołuje metody w kolejności: `jedz`, `spij`, `wydaj_dzwiek`, `lec`, `wyladuj`.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Pięć linii jak w przykładzie.
#
# ### Przykład
#
# **Wyjście:**
#
# ```
# Ptak je.
# Ptak śpi.
# Ptak wydaje dźwięk.
# Ptak leci.
# Ptak ląduje.
# ```

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# z polem "klasa", a metoda to funkcja Klasa_metoda, ktorej pierwszym
# argumentem jest nazwa obiektu (odpowiednik self).
# Dziedziczenie: tablica RODZICE mapuje klase na liste jej klas bazowych.
# Funkcja `wywolaj` szuka metody w klasie obiektu, a potem w klasach
# bazowych - w glab i od lewej (jak MRO w Pythonie dla prostych hierarchii).
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.
declare -rA RODZICE=([Ptak]="Zwierz ObiektLatajacy")

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

# ---- Klasa Zwierz ----
Zwierz_init() {
    local -n _ten=$1
    _ten+=([imie]="$2")
}

Zwierz_jedz() {
    local -n _ten=$1
    echo "${_ten[imie]} je."
}

Zwierz_spij() {
    local -n _ten=$1
    echo "${_ten[imie]} śpi."
}

Zwierz_wydaj_dzwiek() {
    local -n _ten=$1
    echo "${_ten[imie]} wydaje dźwięk."
}

# ---- Klasa ObiektLatajacy ----
ObiektLatajacy_init() {
    local -n _ten=$1
    _ten+=(
        [imie]="$2"
        [w_powietrzu]="0"
    )
}

ObiektLatajacy_lec() {
    local -n _ten=$1
    if [[ ${_ten[w_powietrzu]} == 1 ]]; then
        echo "${_ten[imie]} już leci."
    else
        echo "${_ten[imie]} leci."
        _ten+=([w_powietrzu]="1")
    fi
}

ObiektLatajacy_wyladuj() {
    local -n _ten=$1
    if [[ ${_ten[w_powietrzu]} == 1 ]]; then
        echo "${_ten[imie]} ląduje."
        _ten+=([w_powietrzu]="0")
    else
        echo "${_ten[imie]} jest już na ziemi."
    fi
}

# ---- Klasa Ptak (Zwierz, ObiektLatajacy) ----
# Konstruktor jawnie wywoluje konstruktory obu klas bazowych; pozostale
# metody Ptak dziedziczy.
Ptak_init() {
    Zwierz_init "$1" "$2"
    ObiektLatajacy_init "$1" "$2"
}

# Wczytuje imie ptaka i wykonuje kolejne polecenia (nazwy metod).
program() {
    local imie n i polecenie
    IFS= read -r imie
    nowy Ptak ptak "$imie"
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r polecenie
        case $polecenie in
            jedz | spij | wydaj_dzwiek | lec | wyladuj)
                wywolaj ptak "$polecenie"
                ;;
            *)
                echo "Nieznane polecenie: $polecenie" >&2
                ;;
        esac
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

test_dziedziczenie_wielokrotne() {
    znajdz_metode Ptak jedz
    assertEqual "$REPLY" "Zwierz_jedz" $LINENO
    znajdz_metode Ptak lec
    assertEqual "$REPLY" "ObiektLatajacy_lec" $LINENO
    znajdz_metode Ptak plyn
    assertEqual $? 1 $LINENO
}

test_program() {
    sprawdz program $'Ptak\n5\njedz\nspij\nwydaj_dzwiek\nlec\nwyladuj' "Ptak je.
Ptak śpi.
Ptak wydaje dźwięk.
Ptak leci.
Ptak ląduje." $LINENO
    sprawdz program $'Pan Wróbel\n5\nwyladuj\nlec\nlec\nwyladuj\nwyladuj' "Pan Wróbel jest już na ziemi.
Pan Wróbel leci.
Pan Wróbel już leci.
Pan Wróbel ląduje.
Pan Wróbel jest już na ziemi." $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_dziedziczenie_wielokrotne
        test_program
    fi
}

main "$@"
