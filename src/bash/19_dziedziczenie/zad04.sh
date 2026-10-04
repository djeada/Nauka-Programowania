# ZAD-04 — Dziedziczenie wielopoziomowe: Człowiek → Student → StudentFizyki
#
# **Poziom:** ★★☆
# **Tagi:** `dziedziczenie`, `konstruktory`, `super`
#
# ### Treść
#
# Zaprojektuj hierarchię klas:
#
# 1. **Człowiek** — pola:
#
#    * imię
#    * nazwisko
#    * miejsce urodzenia
#    * zawód
#
# 2. **Student** (dziedziczy po `Człowiek`) — dodatkowo:
#
#    * numer albumu
#    * kierunek studiów
#
# 3. **StudentFizyki** (dziedziczy po `Student`) — dodatkowo:
#
#    * średnia z laboratoriów
#    * średnia z wykładów
#
# Program:
#
# * wczytuje dane dla trzech obiektów (Człowiek, Student, StudentFizyki),
# * tworzy obiekty,
# * wypisuje je w formacie jak w przykładzie.
#
# **Uwaga do wejścia:** wszystko w osobnych liniach, w podanej kolejności.
#
# ### Wejście
#
# **Dane dla Człowiek:**
#
# 1. imię
# 2. nazwisko
# 3. miejsce urodzenia
# 4. zawód
#
# **Dane dla Student:**
# 5. imię
# 6. nazwisko
# 7. miejsce urodzenia
# 8. zawód
# 9. numer albumu (int)
# 10. kierunek studiów
#
# **Dane dla StudentFizyki:**
# 11. imię
# 12. nazwisko
# 13. miejsce urodzenia
# 14. zawód
# 15. numer albumu (int)
# 16. kierunek studiów
# 17. średnia z laboratoriów (float)
# 18. średnia z wykładów (float)
#
# ### Wyjście
#
# Trzy bloki jak w przykładzie, oddzielone pustą linią.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Jan
# Kowalski
# Kraków
# Inżynier
# Anna
# Nowak
# Warszawa
# Student
# 12345
# Informatyka
# Piotr
# Wiśniewski
# Gdańsk
# Student
# 54321
# Fizyka
# 4.5
# 4.0
# ```
#
# **Wyjście:**
#
# ```
# Człowiek:
# Imię: Jan
# Nazwisko: Kowalski
# Miejsce urodzenia: Kraków
# Zawód: Inżynier
#
# Student:
# Imię: Anna
# Nazwisko: Nowak
# Miejsce urodzenia: Warszawa
# Zawód: Student
# Numer albumu: 12345
# Kierunek studiów: Informatyka
#
# Student Fizyki:
# Imię: Piotr
# Nazwisko: Wiśniewski
# Miejsce urodzenia: Gdańsk
# Zawód: Student
# Numer albumu: 54321
# Kierunek studiów: Fizyka
# Średnia z laboratoriów: 4.5
# Średnia z wykładów: 4.0
# ```

# Uzycie:
#   bash zad04.sh                     - uruchamia testy
#   bash zad04.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# SC2178: shellcheck bledne zglasza namerefy (local -n) wskazujace obiekty
# shellcheck shell=bash source=../assert.sh disable=SC2178
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Bash nie ma klas, wiec je emulujemy: obiekt to globalna tablica asocjacyjna
# z polem "klasa", a metoda to funkcja Klasa_metoda, ktorej pierwszym
# argumentem jest nazwa obiektu (odpowiednik self). Metody zwracajace
# wartosc wypisuja ja na stdout (opis() wypisuje kolejne linie).
# Dziedziczenie: tablica RODZICE mapuje klase na jej klase bazowa. Funkcja
# `wywolaj` szuka metody najpierw w klasie obiektu, a potem w klasach
# bazowych - to daje nadpisywanie metod i polimorfizm. Funkcja `super`
# zaczyna szukanie od klasy bazowej (odpowiednik super()).
# Atrybut klasy "naglowek" emulujemy metoda naglowek nadpisywana w potomnych.
# Uwaga: przez dynamiczny zasieg zmiennych w Bashu nazwa obiektu nie moze
# byc nazwa zmiennej lokalnej ktorejs z funkcji.
declare -rA RODZICE=([Student]=Czlowiek [StudentFizyki]=Student)

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

# ---- Klasa Czlowiek ----
# init obiekt imie nazwisko miejsce_urodzenia zawod
Czlowiek_init() {
    local -n _ten=$1
    _ten+=(
        [imie]="$2"
        [nazwisko]="$3"
        [miejsce_urodzenia]="$4"
        [zawod]="$5"
    )
}

Czlowiek_naglowek() {
    echo "Człowiek"
}

Czlowiek_opis() {
    local -n _ten=$1
    echo "Imię: ${_ten[imie]}"
    echo "Nazwisko: ${_ten[nazwisko]}"
    echo "Miejsce urodzenia: ${_ten[miejsce_urodzenia]}"
    echo "Zawód: ${_ten[zawod]}"
}

# Zdefiniowana tylko tu - naglowek i opis sa wybierane wedlug klasy obiektu.
Czlowiek_wypisz() {
    echo "$(wywolaj "$1" naglowek):"
    wywolaj "$1" opis
}

# ---- Klasa Student (Czlowiek) ----
# init obiekt imie nazwisko miejsce_urodzenia zawod numer_albumu kierunek
Student_init() {
    local -n _ten=$1
    super Student "$1" init "$2" "$3" "$4" "$5"
    _ten+=(
        [numer_albumu]="$6"
        [kierunek]="$7"
    )
}

Student_naglowek() {
    echo "Student"
}

Student_opis() {
    local -n _ten=$1
    super Student "$1" opis
    echo "Numer albumu: ${_ten[numer_albumu]}"
    echo "Kierunek studiów: ${_ten[kierunek]}"
}

# ---- Klasa StudentFizyki (Student) ----
# init obiekt imie nazwisko miejsce_urodzenia zawod numer_albumu kierunek
#      srednia_lab srednia_wyklad
StudentFizyki_init() {
    local -n _ten=$1
    super StudentFizyki "$1" init "$2" "$3" "$4" "$5" "$6" "$7"
    _ten+=(
        [srednia_lab]="$8"
        [srednia_wyklad]="$9"
    )
}

StudentFizyki_naglowek() {
    echo "Student Fizyki"
}

StudentFizyki_opis() {
    local -n _ten=$1
    super StudentFizyki "$1" opis
    LC_ALL=C printf 'Średnia z laboratoriów: %.2f\n' "${_ten[srednia_lab]}"
    LC_ALL=C printf 'Średnia z wykładów: %.2f\n' "${_ten[srednia_wyklad]}"
}

# Wczytuje dane osob (kazda wartosc w osobnej linii), tworzy obiekty
# odpowiednich klas i wypisuje je, oddzielajac bloki pusta linia.
program() {
    local n i rodzaj imie nazwisko miejsce zawod numer kierunek lab wyklad
    read -r n
    for ((i = 1; i <= n; i++)); do
        IFS= read -r rodzaj
        IFS= read -r imie
        IFS= read -r nazwisko
        IFS= read -r miejsce
        IFS= read -r zawod
        case $rodzaj in
            czlowiek)
                nowy Czlowiek "osoba_$i" "$imie" "$nazwisko" "$miejsce" "$zawod"
                ;;
            student)
                IFS= read -r numer
                IFS= read -r kierunek
                nowy Student "osoba_$i" "$imie" "$nazwisko" "$miejsce" "$zawod" "$numer" "$kierunek"
                ;;
            *)
                IFS= read -r numer
                IFS= read -r kierunek
                IFS= read -r lab
                IFS= read -r wyklad
                nowy StudentFizyki "osoba_$i" "$imie" "$nazwisko" "$miejsce" "$zawod" \
                    "$numer" "$kierunek" "$lab" "$wyklad"
                ;;
        esac
    done
    for ((i = 1; i <= n; i++)); do
        if ((i > 1)); then
            echo
        fi
        wywolaj "osoba_$i" wypisz
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

test_hierarchia() {
    znajdz_metode StudentFizyki wypisz
    assertEqual "$REPLY" "Czlowiek_wypisz" $LINENO
    nowy Student jan "Jan Maria" Nowak "Zielona Góra" Student 7 Matematyka
    assertEqual "$(wywolaj jan opis)" "Imię: Jan Maria
Nazwisko: Nowak
Miejsce urodzenia: Zielona Góra
Zawód: Student
Numer albumu: 7
Kierunek studiów: Matematyka" $LINENO
}

test_program() {
    sprawdz program "3
czlowiek
Jan
Kowalski
Kraków
Inżynier
student
Anna
Nowak
Warszawa
Student
12345
Informatyka
student_fizyki
Piotr
Wiśniewski
Gdańsk
Student
54321
Fizyka
4.5
4.0" "Człowiek:
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Kraków
Zawód: Inżynier

Student:
Imię: Anna
Nazwisko: Nowak
Miejsce urodzenia: Warszawa
Zawód: Student
Numer albumu: 12345
Kierunek studiów: Informatyka

Student Fizyki:
Imię: Piotr
Nazwisko: Wiśniewski
Miejsce urodzenia: Gdańsk
Zawód: Student
Numer albumu: 54321
Kierunek studiów: Fizyka
Średnia z laboratoriów: 4.50
Średnia z wykładów: 4.00" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_hierarchia
        test_program
    fi
}

main "$@"
