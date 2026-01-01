# ZAD-08 — Dzień tygodnia dla daty (Zeller)
#
# **Poziom:** ★★☆
# **Tagi:** `algorytmy`, `Zeller`, `mapowanie`, `daty`
#
# ### Treść
#
# Wczytaj datę `d, m, y` i wyznacz nazwę dnia tygodnia, używając **kongruencji Zellera** dla kalendarza gregoriańskiego.
#
# Kroki:
#
# 1. Jeśli `m <= 2`, to:
#
# * `m = m + 12`
# * `y = y - 1`
#
# 2. Oblicz:
#
# * `K = y % 100`
# * `J = y // 100`
# * `h = (d + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7`
#
# 3. Zmapuj `h` na dzień tygodnia:
#
# * 0 → `Sobota`
# * 1 → `Niedziela`
# * 2 → `Poniedziałek`
# * 3 → `Wtorek`
# * 4 → `Środa`
# * 5 → `Czwartek`
# * 6 → `Piątek`
#
# ### Wejście
#
# 3 liczby całkowite (w osobnych liniach): `d`, `m`, `y`
#
# ### Wyjście
#
# Jedna linia: nazwa dnia tygodnia (dokładnie jedna z: Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela).
#
# ### Ograniczenia / gwarancje
#
# * Data wejściowa jest poprawna (zalecane; inaczej dopisz, co robić dla błędnej).
# * Kalendarz gregoriański.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 9
# 10
# 2020
# ```
#
# **Wyjście:**
#
# ```
# Piątek
# ```

main() {

    echo "Podaj dzien:"
    read DD

    echo "Podaj miesiac:"
    read MM

    echo "Podaj rok:"
    read rok

    CC=$(($rok / 100))
    YY=$(($rok % 100))

    A=$((($CC / 4) - 2 * $CC - 1))
    B=$((5 * $YY / 4))
    C=$((26 * ($MM + 1) / 10))

    wynik=$((($A + $B + $C + $DD) % 7))

    if [[ $wynik -eq 1 ]]; then
        echo "poniedzialek"

    elif [[ $wynik -eq 2 ]]; then
        echo "wtorek"

    elif [[ $wynik -eq 3 ]]; then
        echo "sroda"

    elif [[ $wynik -eq 4 ]]; then
        echo "czwartek"

    elif [[ $wynik -eq 5 ]]; then
        echo "piatek"

    elif [[ $wynik -eq 6 ]]; then
        echo "sobota"

    elif [[ $wynik -eq 7 ]]; then
        echo "niedziela"

    else
        echo "bledne dane"

    fi
}

main "$@"
