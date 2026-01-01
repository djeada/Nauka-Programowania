# ZAD-09 — Rozdziel informacje o pracowniku
#
# **Poziom:** ★☆☆
# **Tagi:** `split`, `formatowanie`
#
# ### Treść
#
# Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:
#
# 1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki
#
# Wypisz każdą informację w osobnej linii z etykietą.
#
# ### Wejście
#
# * 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`
#
# ### Wyjście
#
# Pięć linii w formacie:
#
# * `Imię: ...`
# * `Nazwisko: ...`
# * `Miejsce urodzenia: ...`
# * `Zawód: ...`
# * `Zarobki: ...`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Jan; Kowalski; Warszawa; Programista; 1000;
# ```
#
# **Wyjście:**
#
# ```
# Imię: Jan
# Nazwisko: Kowalski
# Miejsce urodzenia: Warszawa
# Zawód: Programista
# Zarobki: 1000
# ```
#
# ### Uwagi
#
# * Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
# * Ostatni średnik może powodować pusty element na końcu — zignoruj go.

wypisz_dane() {
    IFS='; ' read -ra wynik <<<"$1"
    echo "Imie: ${wynik[0]}"
    echo "Nazwisko: ${wynik[1]}"
    echo "Miejsce urodzenia: ${wynik[2]}"
    echo "Zawod: ${wynik[3]}"
    echo "Zarobki: ${wynik[4]}"
}

main() {
    local napis="Jan; Kowalski; Warszawa; Programista; 1000"
    wypisz_dane "$napis"
}

main "$@"
