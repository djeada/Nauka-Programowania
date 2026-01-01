# ZAD-01A — Dziesiętny → binarny
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersja`, `binarne`, `pętle`
#
# ### Treść
#
# Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.
#
# ZAD-01B — Binarny → dziesiętny
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersja`, `string`, `binarne`
#
# ### Treść
#
# Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

# Funkcja konwertujaca z dziesietnego na binarny
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(log n)
dziesietny_na_binarny() {
    local n=$1
    
    if [ $n -eq 0 ]; then
        echo "0"
        return
    fi
    
    local wynik=""
    while [ $n -gt 0 ]; do
        wynik="$((n % 2))$wynik"
        n=$((n / 2))
    done
    
    echo "$wynik"
}

# Funkcja konwertujaca z binarnego na dziesietny
# Zlozonosc czasowa: O(n), gdzie n to dlugosc ciagu binarnego
# Zlozonosc pamieciowa: O(1)
binarny_na_dziesietny() {
    local binarny=$1
    local wynik=0
    local dlugosc=${#binarny}
    
    for ((i = 0; i < dlugosc; i++)); do
        local cyfra=${binarny:$i:1}
        wynik=$((wynik * 2 + cyfra))
    done
    
    echo $wynik
}

main() {
    echo "3 -> $(dziesietny_na_binarny 3)"
    echo "101 -> $(binarny_na_dziesietny 101)"
}

main "$@"
