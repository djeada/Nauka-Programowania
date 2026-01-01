# ZAD-03 — Z ilu słów składa się zdanie?
# 
# **Poziom:** ★☆☆
# **Tagi:** `string`, `split`
# 
# ### Treść
# 
# Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: liczba słów
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# gram na pianinie.
# ```
# 
# **Wyjście:**
# 
# ```
# 3
# ```
# 
# ### Uwagi o formatowaniu
# 
# * Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

source ../assert.sh

# Funkcja liczaca slowa w zdaniu
# Zlozonosc czasowa: O(n), gdzie n to liczba slow
# Zlozonosc pamieciowa: O(n) dla tablicy slow
liczba_slow_v1() {

    local zdanie="$1"
    local licznik=0

    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    # Iteracja przez wszystkie slowa
    # Zlozonosc czasowa: O(n), gdzie n to liczba slow
    # Zlozonosc pamieciowa: O(n) dla tablicy slow
    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            local licznik=$((licznik + 1))
        fi
    done

    echo "$licznik"
}

test1() {
    local zdanie="Ile to   ma :  slow w swoim zdaniu na   koniec?"
    local wynik=9
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

test2() {
    local zdanie="to sa cztery slowa"
    local wynik=4
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

test3() {
    local zdanie="31    331 .,,,.,.,brak slow!!!    "
    local wynik=2
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

