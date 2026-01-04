# ZAD-08 — Wypisz pionowo słowa ze zdania
#
# **Poziom:** ★☆☆
# **Tagi:** `split`, `string`
#
# ### Treść
#
# Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.
#
# ### Wejście
#
# * 1. linia: zdanie
#
# ### Wyjście
#
# * wiele linii: słowa w kolejności występowania
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
# Ala
# ma
# kota
# ```
source ../assert.sh

# Funkcja wypisujaca slowa pionowo (kazde slowo w nowej linii)
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

main() {
    local zdanie="We think in generalities, but we live in details."
    wypisz_slowa "$zdanie"
}

main "$@"
