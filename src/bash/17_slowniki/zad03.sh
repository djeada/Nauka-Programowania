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
source ../assert.sh

dodaj_ksiazke_do_czytelnika() {
    local czytelnik=$1
    local ksiazka=$2
    baza_danych[$czytelnik]="${baza_danych[$czytelnik]} $ksiazka;"
}

zwroc_ksiazke_czytelnika() {
    local czytelnik=$1
    local ksiazka=$2

    baza_danych[$czytelnik]=${baza_danych[$czytelnik]//" $ksiazka;"/}
}

wypisz_liste_wypozyczonych_ksiazek() {
    local czytelnik=$1

    echo "Czytelnik: $czytelnik wypozyczyl nastepujace ksiazki:"
    for ksiazka in "${baza_danych[$czytelnik]}"; do
        echo "$ksiazka"
    done
}

main() {

    declare -A baza_danych
    dodaj_ksiazke_do_czytelnika "Jan Kowalski" "Opowiesci z Narnii"
    dodaj_ksiazke_do_czytelnika "Jan Kowalski" "Robinson Crusoe"
    dodaj_ksiazke_do_czytelnika "Ewa Nowak" "Opowiesci z Narnii"
    dodaj_ksiazke_do_czytelnika "Ewa Nowak" "Ogniem i mieczem"
    dodaj_ksiazke_do_czytelnika "Tymon Nowak" "Wladca Pierscieni"

    wypisz_liste_wypozyczonych_ksiazek "Jan Kowalski"
    wypisz_liste_wypozyczonych_ksiazek "Ewa Nowak"
    wypisz_liste_wypozyczonych_ksiazek "Tymon Nowak"

    zwroc_ksiazke_czytelnika "Jan Kowalski" "Opowiesci z Narnii"
    wypisz_liste_wypozyczonych_ksiazek "Jan Kowalski"

}

main "$@"
