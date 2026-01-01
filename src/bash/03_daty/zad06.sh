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

    echo "Podaj dzien, miesiac i rok: "
    read dzien
    read miesiac
    read rok

    if [[ $rok -ge 1 ]]; then
        if [ $miesiac -eq 1 ] || [ $miesiac -eq 3 ] || [ $miesiac -eq 5 ] || [ $miesiac -eq 7 ] || [ $miesiac -eq 8 ] || [ $miesiac -eq 10 ] || [ $miesiac -eq 12 ]; then
            if [ $dzien -ge 1 ] && [ $dzien -le 31 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        elif [ $miesiac -eq 4 ] || [ $miesiac -eq 6 ] || [ $miesiac -eq 9 ] || [ $miesiac -eq 11 ]; then
            if [ $dzien -ge 1 ] && [ $dzien -le 30 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        elif [ $miesiac -eq 2 ]; then
            if [[ $(($rok % 4)) -eq 0 ]]; then
                if [[ $(($rok % 100)) -eq 0 ]]; then
                    if [ $(($rok % 400)) -eq 0 ] && [ $dzien -ge 1 ] && [ $dzien -le 29 ]; then
                        echo "Podana data jest poprawna"
                    elif [ $dzien -ge 1 ] && [ $dzien -le 28 ]; then
                        echo "Podana data jest poprawna"
                    else
                        echo "Podano niepoprawna date"
                    fi
                elif [ $dzien -ge 1 ] && [ $dzien -le 29 ]; then
                    echo "Podana data jest poprawna"
                else
                    echo "Podano niepoprawna date"
                fi
            elif [ $dzien -ge 1 ] && [ $dzien -le 28 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        else
            echo "Podano niepoprawna date"
        fi
    fi
}

main "$@"
