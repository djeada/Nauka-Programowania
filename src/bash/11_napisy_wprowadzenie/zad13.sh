# ZAD-13 — Znaki na indeksach będących liczbami pierwszymi
# 
# **Poziom:** ★☆☆
# **Tagi:** `liczby pierwsze`, `indeksy`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.
# 
# ### Wejście
# 
# * 1. linia: napis
# 
# ### Wyjście
# 
# * 1. linia: lista znaków, np. `['o', 'ń']`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Słoń
# ```
# 
# **Wyjście:**
# 
# ```
# ['o', 'ń']
# ```
# 
# ### Uwagi
# 
# * Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

source ../assert.sh

# Funkcja pomocnicza sprawdzajaca czy liczba jest pierwsza
# Zlozonosc czasowa: O(sqrt(n))
# Zlozonosc pamieciowa: O(1)
czy_pierwsza() {
    local n=$1
    
    if [ $n -lt 2 ]; then
        return 1
    fi
    
    if [ $n -eq 2 ]; then
        return 0
    fi
    
    local j
    for ((j = 2; j * j <= n; j++)); do
        if [ $((n % j)) -eq 0 ]; then
            return 1
        fi
    done
    
    return 0
}

# Funkcja wypisujaca znaki na indeksach bedacych liczbami pierwszymi
# Zlozonosc czasowa: O(n * sqrt(n)), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(n) dla listy wynikowej
znaki_na_indeksach_pierwszych() {
    local napis="$1"
    local n=${#napis}
    local wynik="["
    local pierwszy=1
    
    # Iteracja przez wszystkie indeksy
    local i
    for ((i = 0; i < n; i++)); do
        # Sprawdzenie czy indeks jest liczba pierwsza
        if czy_pierwsza $i; then
            if [ $pierwszy -eq 1 ]; then
                wynik="${wynik}'${napis:$i:1}'"
                pierwszy=0
            else
                wynik="${wynik}, '${napis:$i:1}'"
            fi
        fi
    done
    
    wynik="${wynik}]"
    echo "$wynik"
}

test1() {
    local napis="Slon"
    local wynik="['o', 'n']"
    assertEqual "$(znaki_na_indeksach_pierwszych "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="abcdefghijk"
    local wynik="['c', 'd', 'f', 'h']"
    assertEqual "$(znaki_na_indeksach_pierwszych "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

