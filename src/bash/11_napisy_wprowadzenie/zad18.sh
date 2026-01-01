# ZAD-18 — Odwróć słowa w zdaniu
# 
# **Poziom:** ★★☆
# **Tagi:** `split`, `string`, `pętle`
# 
# ### Treść
# 
# Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: zdanie z odwróconymi słowami
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Ala ma kota
# ```
# 
# **Wyjście:**
# 
# ```
# alA am atok
# ```

source ../assert.sh

# Funkcja odwracajaca slowa w zdaniu
# Zlozonosc czasowa: O(n), gdzie n to liczba znakow w zdaniu
# Zlozonosc pamieciowa: O(n) dla tablicy slow
odwroc_slowa() {
    local zdanie="$1"
    
    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')
    
    read -ra lista_slow <<<"$zdanie"
    
    local wynik=""
    
    # Iteracja przez wszystkie slowa
    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            local wynik="$wynik$(echo "$slowo" | rev) "
        fi
    done
    
    # Usuniecie koncowej spacji
    if [ ${#wynik} -gt 0 ]; then
        echo "${wynik::-1}"
    else
        echo ""
    fi
}

test1() {
    local napis="Cameron Diaz"
    local wynik="noremaC zaiD"
    assertEqual "$(odwroc_slowa "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="Ala ma kota"
    local wynik="alA am atok"
    assertEqual "$(odwroc_slowa "$napis")" "$wynik" $LINENO
}

test3() {
    local napis=""
    local wynik=""
    assertEqual "$(odwroc_slowa "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

