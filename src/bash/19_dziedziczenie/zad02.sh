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

# Funkcja do zaimplementowania
# Zlozonosc czasowa: O(1)
# Zlozonosc pamieciowa: O(1)
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
