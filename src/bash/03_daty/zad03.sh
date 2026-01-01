# ZAD-03 — Rok przestępny
#
# **Poziom:** ★☆☆
# **Tagi:** `modulo`, `if`, `kalendarz`
#
# ### Treść
#
# Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.
#
# Wypisz:
#
# * `Rok jest przestępny.`
# * `Rok nie jest przestępny.`
#
# ### Wejście
#
# * 1 linia: `y` (liczba całkowita, `y ≥ 0`)
#
# ### Wyjście
#
# Jedna linia — odpowiedni komunikat.
#
# ### Definicja
#
# Rok jest przestępny, gdy:
#
# * jest podzielny przez 400 **lub**
# * jest podzielny przez 4 i **nie** jest podzielny przez 100.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2100
# ```
#
# **Wyjście:**
#
# ```
# Rok nie jest przestępny.
# ```

main() {

    echo "Podaj rok:"
    read rok

    if [[ $(($rok % 4)) -eq 0 ]]; then
        if [[ $(($rok % 100)) -eq 0 ]]; then
            if [[ $(($rok % 400)) -eq 0 ]]; then
                echo "rok jest przestepny"
            else
                echo "rok nie jest przestepny"
            fi
        else
            echo "rok jest przestepny"
        fi
    else
        echo "rok nie jest przestepny"
    fi
}

main "$@"
