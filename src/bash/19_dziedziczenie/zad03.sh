# ZAD-03 — Polimorfizm: Zwierz, Pies i Kot
#
# **Poziom:** ★★☆
# **Tagi:** `dziedziczenie`, `polimorfizm`, `override`
#
# ### Treść
#
# Zaprojektuj klasy:
#
# * **Zwierz** — metoda `odglos()` zwraca/drukuje ogólny dźwięk.
# * **Pies** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
# * **Kot** — dziedziczy po `Zwierz` i nadpisuje `odglos()`.
#
# Program testowy:
#
# * tworzy obiekty: `Zwierz`, `Pies`, `Kot`,
# * umieszcza je w jednej kolekcji,
# * iteruje i dla każdego wypisuje linię w formacie:
#   `NazwaKlasy wydaje odgłos: ...`
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Trzy linie, po jednej dla każdego obiektu.
#
# ### Przykład
#
# **Wyjście:**
#
# ```
# Zwierz wydaje odgłos: ...
# Pies wydaje odgłos: Hau!
# Kot wydaje odgłos: Miau!
# ```

# Uzycie:
#   bash zad03.sh                     - uruchamia testy
#   bash zad03.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# z polem "klasa", a metoda to funkcja Klasa_metoda, ktorej pierwszym
# argumentem jest nazwa obiektu (odpowiednik self). Metody zwracajace
# wartosc wypisuja ja na stdout.
# Dziedziczenie: tablica RODZICE mapuje klase na jej klase bazowa. Funkcja
# `wywolaj` szuka metody najpierw w klasie obiektu, a potem w klasach
# bazowych - to daje nadpisywanie metod i polimorfizm.
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.
declare -rA RODZICE=([Pies]=Zwierz [Kot]=Zwierz)

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

Zwierz_odglos() {
    echo "..."
}

# Dzieki wywolaj "$1" odglos uruchamia sie wersja odglos() wlasciwa dla
# klasy obiektu (polimorfizm), choc przedstaw_sie jest zdefiniowane tylko tu.
Zwierz_przedstaw_sie() {
    local -n _ten=$1
    echo "${_ten[klasa]} ${_ten[imie]} wydaje odgłos: $(wywolaj "$1" odglos)"
}

# ---- Klasy Pies i Kot (Zwierz) - nadpisuja tylko odglos ----
Pies_odglos() {
    echo "Hau!"
}

Kot_odglos() {
    echo "Miau!"
}

# Wczytuje liste zwierzat i dla kazdego wywoluje przedstaw_sie.
program() {
    local n i rodzaj imie zwierze
    local -a zwierzeta=()
    read -r n
    for ((i = 1; i <= n; i++)); do
        read -r rodzaj imie
        case $rodzaj in
            pies) nowy Pies "zwierze_$i" "$imie" ;;
            kot) nowy Kot "zwierze_$i" "$imie" ;;
            *) nowy Zwierz "zwierze_$i" "$imie" ;;
        esac
        zwierzeta+=("zwierze_$i")
    done
    for zwierze in "${zwierzeta[@]}"; do
        wywolaj "$zwierze" przedstaw_sie
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

test_polimorfizm() {
    # Pies nie definiuje przedstaw_sie - dziedziczy je po Zwierz
    znajdz_metode Pies przedstaw_sie
    assertEqual "$REPLY" "Zwierz_przedstaw_sie" $LINENO
    znajdz_metode Kot odglos
    assertEqual "$REPLY" "Kot_odglos" $LINENO
    nowy Pies azor Azor
    assertEqual "$(wywolaj azor odglos)" "Hau!" $LINENO
}

test_program() {
    sprawdz program $'3\nzwierz Gucio\npies Burek\nkot Mruczek' "Zwierz Gucio wydaje odgłos: ...
Pies Burek wydaje odgłos: Hau!
Kot Mruczek wydaje odgłos: Miau!" $LINENO
    sprawdz program $'2\nkot Filemon\nkot Bonifacy' "Kot Filemon wydaje odgłos: Miau!
Kot Bonifacy wydaje odgłos: Miau!" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_polimorfizm
        test_program
    fi
}

main "$@"
