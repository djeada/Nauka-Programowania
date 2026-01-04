# ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)
#
# **Poziom:** ★☆☆
# **Tagi:** `if`, `tablice`, `walidacja`
#
# ### Treść
#
# Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
# Jeśli `m` nie jest w zakresie 1–12, wypisz:
# `Niepoprawny numer miesiąca.`
#
# ### Wejście
#
# * 1 linia: `m` (liczba całkowita, `m ≥ 0`)
#
# ### Wyjście
#
# * liczba dni (jedna linia) **albo**
# * komunikat o błędzie (jedna linia)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# ```
#
# **Wyjście:**
#
# ```
# 28
# ```
main() {
    read m

    if [[ $m -eq 1 ]] || [[ $m -eq 3 ]] || [[ $m -eq 5 ]] || [[ $m -eq 7 ]] || [[ $m -eq 8 ]] || [[ $m -eq 10 ]] || [[ $m -eq 12 ]]; then
        echo "31"
    elif [[ $m -eq 4 ]] || [[ $m -eq 6 ]] || [[ $m -eq 9 ]] || [[ $m -eq 11 ]]; then
        echo "30"
    elif [[ $m -eq 2 ]]; then
        echo "28"
    else
        echo "Niepoprawny numer miesiąca."
    fi
}

main "$@"
