# ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat
#
# **Poziom:** ★★☆
# **Tagi:** `dziedziczenie`, `polimorfizm`, `math`
#
# ### Treść
#
# Zaprojektuj hierarchię klas:
#
# * **Kształt** — klasa bazowa (ogólna) dla kształtów.
# * **Koło** — dziedziczy po `Kształt`.
# * **Kwadrat** — dziedziczy po `Kształt`.
#
# Każda klasa ma mieć:
#
# * metodę obliczającą **pole**,
# * metodę wypisującą informacje o obiekcie: typ, parametry i pole.
#
# Program:
#
# * wczytuje promień `r` koła oraz bok `a` kwadratu,
# * tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
# * wypisuje informacje o obu.
#
# **Uwaga do formatowania:**
# *Pole koła wypisz do 4 miejsc po przecinku.*
# *Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*
#
# ### Wejście
#
# * 1 linia: `r` (liczba rzeczywista)
# * 2 linia: `a` (liczba rzeczywista)
#
# ### Wyjście
#
# Blok informacji o kole, pusta linia, blok informacji o kwadracie.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 4
# ```
#
# **Wyjście:**
#
# ```
# Kształt: Koło
# Promień: 5
# Pole powierzchni: 78.5398
#
# Kształt: Kwadrat
# Długość boku: 4
# Pole powierzchni: 16
# ```

# Uzycie:
#   bash zad02.sh                     - uruchamia testy
#   bash zad02.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

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
#
# Pola powierzchni sa liczbami rzeczywistymi, wiec liczy je awk (LC_ALL=C
# wymusza kropke jako separator dziesietny).
declare -rA RODZICE=([Kolo]=Ksztalt [Kwadrat]=Ksztalt)

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

# ---- Klasa Ksztalt ----
# Metody "abstrakcyjne" (odpowiednik NotImplementedError) - musza je nadpisac
# klasy potomne.
_metoda_abstrakcyjna() {
    echo "Metoda abstrakcyjna $1 - klasa potomna musi ja nadpisac" >&2
    return 1
}
Ksztalt_nazwa() { _metoda_abstrakcyjna nazwa; }
Ksztalt_parametr() { _metoda_abstrakcyjna parametr; }
Ksztalt_pole() { _metoda_abstrakcyjna pole; }

# Napisana tylko raz - korzysta z metod nadpisanych w klasach potomnych.
Ksztalt_wypisz() {
    echo "Kształt: $(wywolaj "$1" nazwa)"
    wywolaj "$1" parametr
    LC_ALL=C printf 'Pole powierzchni: %.2f\n' "$(wywolaj "$1" pole)"
}

# ---- Klasa Kolo (Ksztalt) ----
Kolo_init() {
    local -n _ten=$1
    _ten+=([r]="$2")
}
Kolo_nazwa() {
    echo "Koło"
}
Kolo_parametr() {
    local -n _ten=$1
    LC_ALL=C printf 'Promień: %.2f\n' "${_ten[r]}"
}
Kolo_pole() {
    local -n _ten=$1
    LC_ALL=C awk -v r="${_ten[r]}" 'BEGIN { printf "%.17g\n", atan2(0, -1) * r * r }'
}

# ---- Klasa Kwadrat (Ksztalt) ----
Kwadrat_init() {
    local -n _ten=$1
    _ten+=([a]="$2")
}
Kwadrat_nazwa() {
    echo "Kwadrat"
}
Kwadrat_parametr() {
    local -n _ten=$1
    LC_ALL=C printf 'Długość boku: %.2f\n' "${_ten[a]}"
}
Kwadrat_pole() {
    local -n _ten=$1
    LC_ALL=C awk -v a="${_ten[a]}" 'BEGIN { printf "%.17g\n", a * a }'
}

# Wczytuje liste ksztaltow, wypisuje informacje o kazdym i sume pol.
program() {
    local n i rodzaj wartosc ksztalt
    local -a ksztalty=() pola=()
    read -r n
    for ((i = 1; i <= n; i++)); do
        read -r rodzaj wartosc
        if [[ $rodzaj == kolo ]]; then
            nowy Kolo "ksztalt_$i" "$wartosc"
        else
            nowy Kwadrat "ksztalt_$i" "$wartosc"
        fi
        ksztalty+=("ksztalt_$i")
    done
    for ksztalt in "${ksztalty[@]}"; do
        wywolaj "$ksztalt" wypisz
        echo
        pola+=("$(wywolaj "$ksztalt" pole)")
    done
    printf '%s\n' "${pola[@]}" | LC_ALL=C awk '{ suma += $1 } END { printf "Suma pól: %.2f\n", suma }'
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

test_ksztalty() {
    # Metoda wypisz jest tylko w klasie Ksztalt
    znajdz_metode Kwadrat wypisz
    assertEqual "$REPLY" "Ksztalt_wypisz" $LINENO
    nowy Ksztalt ogolny
    wywolaj ogolny pole 2>/dev/null
    assertEqual $? 1 $LINENO
    nowy Kwadrat kwadrat 2.5
    assertEqual "$(wywolaj kwadrat wypisz)" $'Kształt: Kwadrat\nDługość boku: 2.50\nPole powierzchni: 6.25' $LINENO
}

test_program() {
    sprawdz program $'2\nkolo 5\nkwadrat 4' "Kształt: Koło
Promień: 5.00
Pole powierzchni: 78.54

Kształt: Kwadrat
Długość boku: 4.00
Pole powierzchni: 16.00

Suma pól: 94.54" $LINENO
    sprawdz program $'3\nkwadrat 1\nkolo 1\nkwadrat 0.5' "Kształt: Kwadrat
Długość boku: 1.00
Pole powierzchni: 1.00

Kształt: Koło
Promień: 1.00
Pole powierzchni: 3.14

Kształt: Kwadrat
Długość boku: 0.50
Pole powierzchni: 0.25

Suma pól: 4.39" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_ksztalty
        test_program
    fi
}

main "$@"
