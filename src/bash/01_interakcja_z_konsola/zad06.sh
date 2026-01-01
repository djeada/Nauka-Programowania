# ZAD-06A — Kilogramy → gramy
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`
#
# ### Treść
#
# Wczytaj wartość w kilogramach `kg` i przelicz na gramy.
#
# ### Wejście
#
# * 1 linia: `kg`
#
# ### Wyjście
#
# * 1 linia: `g` jako **liczba całkowita**, gdzie:
#   `g = kg * 1000`
#
# ### Gwarancje
#
# * `kg` jest liczbą całkowitą **lub** taką, że wynik w gramach jest całkowity.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2.5
# ```
#
# **Wyjście:**
#
# ```
# 2500
# ```
#
# ZAD-06B — Cale → centymetry
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj liczbę cali `inch` i przelicz na centymetry.
#
# ### Wejście
#
# * 1 linia: `inch`
#
# ### Wyjście
#
# * 1 linia: `cm = inch * 2.54` wypisane do **2 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 10
# ```
#
# **Wyjście:**
#
# ```
# 25.40
# ```
#
# ZAD-06C — Sekundy → pełne godziny
#
# **Poziom:** ★☆☆
# **Tagi:** `dzielenie całkowite`
#
# ### Treść
#
# Wczytaj liczbę sekund `s` i wypisz liczbę **pełnych godzin**.
#
# ### Wejście
#
# * 1 linia: `s` (liczba całkowita, `s ≥ 0`)
#
# ### Wyjście
#
# * 1 linia: `s // 3600`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 8639
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
#
# ZAD-06D — Euro → złotówki (kurs stały)
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj kwotę w euro `eur` i przelicz na złotówki przy stałym kursie.
#
# ### Wejście
#
# * 1 linia: `eur`
#
# ### Wyjście
#
# * 1 linia: `pln = eur * 4.4` do **2 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ```
#
# **Wyjście:**
#
# ```
# 13.20
# ```
#
# ZAD-06E — Stopnie → radiany
#
# **Poziom:** ★☆☆
# **Tagi:** `pi`, `float`
#
# ### Treść
#
# Wczytaj kąt w stopniach `deg` i przelicz na radiany.
#
# ### Wejście
#
# * 1 linia: `deg`
#
# ### Wyjście
#
# * 1 linia: `rad = deg * π / 180` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 180
# ```
#
# **Wyjście:**
#
# ```
# 3.142
# ```
#
# ZAD-06F — Fahrenheit → Celsius i Kelviny
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`, `float`
#
# ### Treść
#
# Wczytaj temperaturę w stopniach Fahrenheita `F`. Oblicz temperaturę w Celsjuszach oraz Kelvinach.
#
# ### Wejście
#
# * 1 linia: `F`
#
# ### Wyjście
#
# Dwie linie:
#
# 1. `C = (5/9) * (F - 32)` do **3 miejsc**
# 2. `K = C + 273.15` do **3 miejsc**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 32
# ```
#
# **Wyjście:**
#
# ```
# 0.000
# 273.150
# ```

main() {
    # ZAD-06A: kg → g
    read kg
    result=$(echo "scale=0; $kg * 1000 / 1" | bc)
    echo "$result"

    # ZAD-06B: inch → cm
    read inch
    result=$(echo "scale=2; $inch * 2.54" | bc)
    printf "%.2f\n" "$result"

    # ZAD-06C: seconds → hours
    read s
    echo "$(($s / 3600))"

    # ZAD-06D: euro → pln
    read eur
    result=$(echo "scale=2; $eur * 4.4" | bc)
    printf "%.2f\n" "$result"

    # ZAD-06E: stopnie → radiany
    read deg
    # Użyj wbudowanej funkcji arctangent w bc do obliczenia pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); $deg * pi / 180" | bc -l)
    printf "%.3f\n" "$result"

    # ZAD-06F: Fahrenheit → Celsius i Kelvin
    read F
    C=$(echo "scale=10; (5.0/9.0) * ($F - 32)" | bc)
    printf "%.3f\n" "$C"
    K=$(echo "scale=10; $C + 273.15" | bc)
    printf "%.3f\n" "$K"
}

main "$@"
