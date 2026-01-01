# ZAD-11 — Gra w statki (projekt konsolowy)
#
# **Poziom:** ★★★
# **Tagi:** `macierze`, `losowanie`, `gra`, `pętle`
#
# ### Treść
#
# Zaimplementuj grę w statki na planszy 10×10:
#
# 1. Plansza startowa: 10×10 wypełniona `.`
# 2. Losowo rozmieść statki (poziomo/pionowo), bez stykania bokami ani rogami:
#
#    * 1× długość 4
#    * 2× długość 3
#    * 3× długość 2
#    * 5× długość 1
# 3. Pętla gry:
#
#    * wypisz planszę,
#    * wczytaj `r c` (0..9),
#    * jeśli trafienie: wstaw `o`, wypisz komunikat o trafieniu,
#    * jeśli pudło: wstaw `x`, zwiększ licznik pudeł,
#    * gra kończy się, gdy:
#
#      * wszystkie pola statków trafione (wygrana), albo
#      * 10 pudeł (przegrana).
#    * po każdym ruchu wypisz zaktualizowaną planszę.
#
# ### Wejście

# Funkcja do zaimplementowania
# Zlozonosc czasowa: O(n^2)
# Zlozonosc pamieciowa: O(n^2)
funkcja_glowna() {
    # TODO: Implementacja funkcjonalnosci opisanej w docstringu
    echo "Funkcjonalnosc wymaga pelnej implementacji"
}

main() {
    funkcja_glowna
}

main "$@"
