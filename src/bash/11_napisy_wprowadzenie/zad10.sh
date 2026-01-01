# ZAD-10 — Najdłuższe i najkrótsze słowo
# 
# **Poziom:** ★☆☆
# **Tagi:** `string`, `min/max`, `len`
# 
# ### Treść
# 
# Wczytaj zdanie i znajdź:
# 
# a) najdłuższe słowo,
# b) najkrótsze słowo.
# 
# Jeśli jest remis, wybierz słowo, które występuje wcześniej.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: najdłuższe słowo
# * 2. linia: najkrótsze słowo
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Kaczka lubi wiosnę.
# ```
# 
# **Wyjście:**
# 
# ```
# Kaczka
# lubi
# ```

source ../assert.sh

# Funkcja pomocnicza wypisujaca slowa ze zdania
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n) dla tablicy slow
wypisz_slowa() {

    local zdanie="$1"

    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    # Iteracja przez wszystkie slowa
    # Zlozonosc czasowa: O(n), gdzie n to liczba slow
    # Zlozonosc pamieciowa: O(n) dla tablicy slow
    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo"
        fi
    done

}

# Funkcja znajdujaca najdluzsze slowo w zdaniu
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n) dla wyniku wypisz_slowa
najdluzsze() {
    local zdanie="$1"
    awk 'length > maks_dlugosc { maks_dlugosc = length; najdluzsze = $0 } END { print najdluzsze }' <<< $(wypisz_slowa "$zdanie")
}

# Funkcja znajdujaca najkrotsze slowo w zdaniu
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n) dla wyniku wypisz_slowa
najkrotsze() {
    local zdanie="$1"
    local n=${#zdanie}
    awk -v n=$n 'BEGIN { min_dlugosc = n } length < min_dlugosc { min_dlugosc = length; najkrotsze = $0 } END { print najkrotsze }' <<< $(wypisz_slowa "$zdanie")
}

test1() {
    local napis="Kaczka lubi wiosne."
    local wynik="Kaczka"
    assertEqual "$(najdluzsze "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="Kaczka lubi wiosne."
    local wynik="lubi"
    assertEqual "$(najkrotsze "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

