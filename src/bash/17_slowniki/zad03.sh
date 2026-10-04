# ZAD-03 — Biblioteka: baza wypożyczeń
#
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `list`, `pętle`, `string`
#
# ### Treść
#
# Utrzymuj słownik: `imię -> lista wypożyczonych książek`.
# Obsługuj komendy (każda w osobnej linii) aż do `koniec`:
#
# * `dodaj [imię] [tytuł]`
# * `zwróć [imię] [tytuł]`
# * `lista [imię]`
#
# Po `lista [imię]` wypisz:
#
# * jeśli lista niepusta: `Książki wypożyczone przez [imię]: t1, t2, ...`
# * jeśli brak książek (lub brak czytelnika): `Książki wypożyczone przez [imię]: brak`
#
# ### Wejście
#
# Wiele linii z komendami, koniec po słowie `koniec`.
#
# ### Wyjście
#
# Tylko po komendach `lista ...`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# dodaj Jan Hobbit
# dodaj Anna "Duma i uprzedzenie"
# dodaj Jan "Władca Pierścieni"
# lista Jan
# zwróć Jan Hobbit
# lista Jan
# lista Anna
# koniec
# ```
#
# **Wyjście:**
#
# ```
# Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
# Książki wypożyczone przez Jan: Władca Pierścieni
# Książki wypożyczone przez Anna: Duma i uprzedzenie
# ```

# Uzycie:
#   bash zad03.sh                     - uruchamia testy
#   bash zad03.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace tablice
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Baza to tablica asocjacyjna: imie -> lista tytulow. Bash nie ma list
# zagniezdzonych w tablicach, wiec liste tytulow trzymamy jako napis, w ktorym
# tytuly sa oddzielone znakiem nowej linii (tytul jest jedna linia wejscia).

# Dopisuje tytul $3 na koniec listy czytelnika $2 w bazie o nazwie $1.
dodaj_ksiazke() {
    local -n _baza=$1
    if [[ -n ${_baza[$2]:-} ]]; then
        _baza[$2]+=$'\n'"$3"
    else
        _baza[$2]=$3
    fi
}

# Usuwa pierwsze wystapienie tytulu $3 z listy czytelnika $2 (jesli jest).
zwroc_ksiazke() {
    local -n _baza=$1
    local tytul usunieto=0 wynik=""
    local -a tytuly
    if [[ -z ${_baza[$2]:-} ]]; then
        return
    fi
    mapfile -t tytuly <<<"${_baza[$2]}"
    for tytul in "${tytuly[@]}"; do
        if ((!usunieto)) && [[ $tytul == "$3" ]]; then
            usunieto=1
            continue
        fi
        wynik+=$tytul$'\n'
    done
    _baza[$2]=${wynik%$'\n'}
}

# Wypisuje linie z ksiazkami czytelnika $2 (albo "brak").
wypisz_liste() {
    local -n _baza=$1
    local -a tytuly
    local lista
    if [[ -z ${_baza[$2]:-} ]]; then
        echo "Książki wypożyczone przez $2: brak"
        return
    fi
    mapfile -t tytuly <<<"${_baza[$2]}"
    printf -v lista '%s, ' "${tytuly[@]}"
    echo "Książki wypożyczone przez $2: ${lista%, }"
}

# Wczytuje komendy az do "koniec". Linie dzielimy na najwyzej 3 czesci:
# read przypisuje ostatniej zmiennej (tytul) cala reszte linii.
program() {
    local komenda imie tytul
    # shellcheck disable=SC2034 # uzywana przez nameref w funkcjach bazy
    local -A baza=()
    while read -r komenda imie tytul; do
        case $komenda in
            koniec) break ;;
            dodaj) dodaj_ksiazke baza "$imie" "$tytul" ;;
            zwróć) zwroc_ksiazke baza "$imie" "$tytul" ;;
            lista) wypisz_liste baza "$imie" ;;
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

test_program() {
    sprawdz program "dodaj Jan Hobbit
dodaj Anna Duma i uprzedzenie
dodaj Jan Władca Pierścieni
lista Jan
zwróć Jan Hobbit
lista Jan
lista Anna
koniec" "Książki wypożyczone przez Jan: Hobbit, Władca Pierścieni
Książki wypożyczone przez Jan: Władca Pierścieni
Książki wypożyczone przez Anna: Duma i uprzedzenie" $LINENO
    # Kilka egzemplarzy - "zwróć" usuwa tylko jeden; nieznany czytelnik i
    # zwrot niewypozyczonej ksiazki niczego nie psuja
    sprawdz program "dodaj Ola Lalka
dodaj Ola Potop
dodaj Ola Lalka
zwróć Ola Lalka
zwróć Ola Quo vadis
lista Ola
lista Ewa
zwróć Ewa Potop
zwróć Ola Potop
zwróć Ola Lalka
lista Ola
koniec
lista Ola" "Książki wypożyczone przez Ola: Potop, Lalka
Książki wypożyczone przez Ewa: brak
Książki wypożyczone przez Ola: brak" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_program
    fi
}

main "$@"
