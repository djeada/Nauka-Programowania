# ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)
#
# **Poziom:** ★★☆
# **Tagi:** `sumowanie`, `tablice`, `przestępny`
#
# ### Treść
#
# Wczytaj datę `d, m, y` i oblicz numer dnia w roku, tzn. ile dni minęło od 1 stycznia do tej daty **włącznie**.
#
# ### Wejście
#
# 3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`
#
# ### Wyjście
#
# Jedna liczba całkowita: numer dnia w roku.
#
# ### Ograniczenia / gwarancje
#
# * Podana data jest poprawna (nie musisz jej sprawdzać), **albo** możesz jawnie napisać: „jeśli data jest niepoprawna, zachowanie nieokreślone”.
#
#   * (Najczyściej: dać gwarancję poprawności.)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 14
# 2
# 1482
# ```
#
# **Wyjście:**
#
# ```
# 45
# ```
main() {
    read d
    read m
    read y

    # Tablica dni w miesiącach (dla roku nieprzestępnego)
    dni_w_miesiacach=(0 31 28 31 30 31 30 31 31 30 31 30 31)

    # Sprawdź czy rok przestępny
    if [[ $(($y % 400)) -eq 0 ]] || ([[ $(($y % 4)) -eq 0 ]] && [[ $(($y % 100)) -ne 0 ]]); then
        dni_w_miesiacach[2]=29
    fi

    # Oblicz dzień roku
    dzien_roku=$d
    for ((i = 1; i < m; i++)); do
        dzien_roku=$(($dzien_roku + ${dni_w_miesiacach[$i]}))
    done

    echo $dzien_roku
}

main "$@"
