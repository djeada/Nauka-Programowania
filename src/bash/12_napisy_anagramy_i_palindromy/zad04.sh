# ZAD-04 — Palindromy w zdaniu
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `tokenizacja`, `palindrom`
#
# ### Treść
#
# Wczytaj zdanie i wypisz wszystkie słowa, które są palindromami.
# Ignoruj wielkość liter przy sprawdzaniu.
#
# ### Wejście
#
# * 1. linia: zdanie (może zawierać spacje i znaki interpunkcyjne)
#
# ### Wyjście
#
# Każdy znaleziony palindrom w osobnej linii, w kolejności występowania w zdaniu.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Tata zabrał kajak na wycieczkę i uderzył się w oko
# ```
#
# **Wyjście:**
#
# ```
# Tata
# kajak
# i
# w
# oko
# ```
#
# ### Uwagi o formatowaniu
#
# * Traktuj „słowo” jako ciąg liter/cyfr po usunięciu interpunkcji z brzegów (np. `kara.` → `kara`).
# * Porównuj w wersji `lower()`, ale wypisz w oryginalnym brzmieniu z wejścia (tak jak w przykładzie).
source ../assert.sh

# Funkcja sprawdzajaca czy slowo jest palindromem
# Zlozonosc czasowa: O(n), gdzie n to dlugosc slowa
# Zlozonosc pamieciowa: O(n)
czy_palindrom() {
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

# Funkcja wypisujaca slowa ze zdania (po usnieciu interpunkcji)
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n)
wypisz_slowa() {
    local zdanie="$1"

    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo" | tr '[:upper:]' '[:lower:]'
        fi
    done

}

# Funkcja znajdujaca wszystkie palindromy w zdaniu
# Zlozonosc czasowa: O(n * m), gdzie n to liczba slow, m to srednia dlugosc slowa
# Zlozonosc pamieciowa: O(n)
palindromy_w_zdaniu() {
    local zdanie="$1"
    local slowa=$(wypisz_slowa "$zdanie")
    for slowo in $slowa; do
        if [ "$(czy_palindrom "$slowo")" == "true" ]; then
            echo "$slowo"
        fi
    done
}

test_palindromy_w_zdaniu() {
    local wynik=($(palindromy_w_zdaniu "Tata zbaral kajak na wycieczke i uderzyl sie w oko."))
    local oczekiwane=(kajak i w oko)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_palindromy_w_zdaniu
}

main "$@"
