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
