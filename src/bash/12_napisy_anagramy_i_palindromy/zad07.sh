# ZAD-07 — Minimalna liczba usunięć, aby uzyskać anagramy
#
# **Poziom:** ★★★
# **Tagi:** `anagram`, `zliczanie`, `greedy`
#
# ### Treść
#
# Wczytaj dwa słowa. Jeśli mają różne długości, wypisz `-1`.
# W przeciwnym razie oblicz minimalną liczbę znaków, które trzeba usunąć (łącznie z obu słów), aby pozostałe napisy były anagramami.
#
# ### Wejście
#
# * 1. linia: słowo `s1`
# * 2. linia: słowo `s2`
#
# ### Wyjście
#
# * jedna liczba całkowita: minimalna liczba usunięć lub `-1`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# grazyna
# razynax
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
#
# ### Uwagi
#
# * Dla tej samej długości: policz zliczenia liter i zsumuj wartości `abs(c1[lit] - c2[lit])`, a wynik wypisz jako tę sumę. (To jest łączna liczba usunięć.)
source ../assert.sh

# Funkcja liczaca minimalna ilosc znakow do usuniecia aby uzyskac anagramy
# Zlozonosc czasowa: O(n), gdzie n to dlugosc slow
# Zlozonosc pamieciowa: O(1) - tablica o stalym rozmiarze 256
liczba_znakow() {
    local slowo_a="$1"
    local slowo_b="$2"

    # Sprawdzenie czy slowa maja ta sama dlugosc
    if [ ${#slowo_a} -ne ${#slowo_b} ]; then
        echo -1
        return
    fi

    # Tablica do zliczania wystapien znakow
    local pom=()
    for ((i = 0; i < 256; i++)); do
        pom[i]=0
    done

    # Zliczanie znakow w pierwszym slowie
    for ((i = 0; i < ${#slowo_a}; i++)); do
        local litera=${slowo_a:$i:1}
        local ascii=$(printf '%d' "'$litera")
        pom[$ascii]=$((${pom[$ascii]} + 1))
    done

    # Odejmowanie znakow z drugiego slowa
    for ((i = 0; i < ${#slowo_b}; i++)); do
        local litera=${slowo_b:$i:1}
        local ascii=$(printf '%d' "'$litera")
        pom[$ascii]=$((${pom[$ascii]} - 1))
    done

    # Sumowanie bezwzglednych wartosci roznic
    local licznik=0
    for ((i = 0; i < 256; i++)); do
        if [ ${pom[$i]} -gt 0 ]; then
            licznik=$((licznik + ${pom[$i]}))
        elif [ ${pom[$i]} -lt 0 ]; then
            licznik=$((licznik - ${pom[$i]}))
        fi
    done

    echo $licznik
}

test_liczba_znakow() {
    assertEqual "$(liczba_znakow "grazyna" "razynax")" "2" $LINENO
    assertEqual "$(liczba_znakow "adam" "mada")" "0" $LINENO
    assertEqual "$(liczba_znakow "adam" "madaa")" "-1" $LINENO
}

main() {
    test_liczba_znakow
}

main "$@"
