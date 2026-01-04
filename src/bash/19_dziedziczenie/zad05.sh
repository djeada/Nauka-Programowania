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
funkcja_glowna() {
    # TODO: Implementacja funkcjonalnosci opisanej w docstringu
    # Bash nie ma natywnego wsparcia dla dziedziczenia klas
    # Mozna symulowac przez zagniezdzone funkcje lub композycję
    echo "Funkcjonalnosc wymaga pelnej implementacji"
}

main() {
    funkcja_glowna
}

main "$@"
