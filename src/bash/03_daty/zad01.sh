# ZAD-01 — Numer dnia tygodnia lub miesiąca
#
# **Poziom:** ★☆☆
# **Tagi:** `if`, `zakresy`, `I/O`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz `n` **tylko wtedy**, gdy jest poprawnym numerem:
#
# * dnia tygodnia (1–7) **lub**
# * miesiąca (1–12).
#
# W praktyce oznacza to: wypisz `n` tylko wtedy, gdy `1 ≤ n ≤ 12`.
#
# ### Wejście
#
# * 1 linia: `n` (liczba całkowita, `n ≥ 0`)
#
# ### Wyjście
#
# * Jeśli `1 ≤ n ≤ 12`: wypisz `n` w osobnej linii
# * W przeciwnym razie: brak wyjścia
#
# ### Przykłady
#
# **Wejście:**
#
# ```
# 5
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```
#
# **Wejście:**
#
# ```
# 15
# ```
#
# **Wyjście:** *(brak)*

main() {

    echo "Podaj liczbe:"
    read a

    if [[ $a -ge 1 ]] && [[ $a -le 7 ]]; then
        echo "Liczba jest poprawnym numerem tygodnia"

    else
        echo "Liczba nie jest poprawnym numerem tygodnia"
    fi

    if [[ $a -ge 1 ]] && [[ $a -le 12 ]]; then
        echo "Liczba jest poprawnym numerem miesiaca"
    else
        echo "Liczba nie jest poprawnym numerem miesiaca"
    fi
}

main "$@"
