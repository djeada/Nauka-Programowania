# ZAD-15 — Słowa jako lista
# 
# **Poziom:** ★☆☆
# **Tagi:** `split`, `list`
# 
# ### Treść
# 
# Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: lista słów (jak w przykładzie)
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
# ["Ala", "ma", "kota"]
# ```

source ../assert.sh

# Funkcja wypisujaca slowa jako liste w formacie JSON
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n) dla tablicy slow
wypisz_slowa_jako_liste() {
    local zdanie="$1"
    
    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')
    
    read -ra lista_slow <<<"$zdanie"
    
    local wynik="["
    local pierwszy=1
    
    # Iteracja przez wszystkie slowa
    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [ $pierwszy -eq 1 ]; then
                wynik="${wynik}\"${slowo}\""
                pierwszy=0
            else
                wynik="${wynik}, \"${slowo}\""
            fi
        fi
    done
    
    wynik="${wynik}]"
    echo "$wynik"
}

test1() {
    local napis="Ala ma kota"
    local wynik='["Ala", "ma", "kota"]'
    assertEqual "$(wypisz_slowa_jako_liste "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="We think in generalities, but we live in details"
    local wynik='["We", "think", "in", "generalities", "but", "we", "live", "in", "details"]'
    assertEqual "$(wypisz_slowa_jako_liste "$napis")" "$wynik" $LINENO
}

test3() {
    local napis=""
    local wynik="[]"
    assertEqual "$(wypisz_slowa_jako_liste "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

