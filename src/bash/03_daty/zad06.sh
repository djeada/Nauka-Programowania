# ZAD-06 — Sprawdzanie poprawności daty
#
# **Poziom:** ★★☆
# **Tagi:** `walidacja`, `przestępny`, `if`
#
# ### Treść
#
# Wczytaj `d, m, y` i sprawdź, czy jest to poprawna data w kalendarzu gregoriańskim.
#
# Wypisz:
#
# * `Data jest poprawna.`
# * `Data jest niepoprawna.`
#
# ### Wejście
#
# 3 liczby całkowite (w osobnych liniach):
#
# 1. `d` — dzień
# 2. `m` — miesiąc
# 3. `y` — rok
#
# ### Wyjście
#
# Jedna linia — komunikat.
#
# ### Ograniczenia / gwarancje
#
# * `y ≥ 0` (lub `y ≥ 1`, jeśli tak chcesz przyjąć — ważne, by było spójnie w całym zbiorze)
#
# ### Reguły walidacji
#
# 1. `m` musi być w zakresie 1–12
# 2. Ustal liczbę dni w miesiącu:
#
#    * 31: 1,3,5,7,8,10,12
#    * 30: 4,6,9,11
#    * luty: 28 lub 29 (zależnie od przestępności roku)
# 3. `d` musi być w zakresie 1–dni_w_miesiącu
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 31
# 4
# 2021
# ```
#
# **Wyjście:**
#
# ```
# Data jest niepoprawna.
# ```
main() {
    read dzien
    read miesiac
    read rok

    # Sprawdź poprawność miesiąca
    if [[ $miesiac -lt 1 ]] || [[ $miesiac -gt 12 ]]; then
        echo "Data jest niepoprawna."
        return
    fi

    # Określ liczbę dni w miesiącu
    if [[ $miesiac -eq 1 ]] || [[ $miesiac -eq 3 ]] || [[ $miesiac -eq 5 ]] || [[ $miesiac -eq 7 ]] || [[ $miesiac -eq 8 ]] || [[ $miesiac -eq 10 ]] || [[ $miesiac -eq 12 ]]; then
        maxDni=31
    elif [[ $miesiac -eq 4 ]] || [[ $miesiac -eq 6 ]] || [[ $miesiac -eq 9 ]] || [[ $miesiac -eq 11 ]]; then
        maxDni=30
    else # luty
        # Sprawdź czy rok przestępny
        if [[ $(($rok % 400)) -eq 0 ]] || ([[ $(($rok % 4)) -eq 0 ]] && [[ $(($rok % 100)) -ne 0 ]]); then
            maxDni=29
        else
            maxDni=28
        fi
    fi

    # Sprawdź poprawność dnia
    if [[ $dzien -ge 1 ]] && [[ $dzien -le $maxDni ]]; then
        echo "Data jest poprawna."
    else
        echo "Data jest niepoprawna."
    fi
}

main "$@"
