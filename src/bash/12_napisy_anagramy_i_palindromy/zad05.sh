# ZAD-05 — Anagramy słowa w zdaniu
#
# **Poziom:** ★★☆
# **Tagi:** `anagram`, `string`, `zliczanie`
#
# ### Treść
#
# Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).
#
# ### Wejście
#
# * 1. linia: zdanie
# * 2. linia: słowo-klucz `k`
#
# ### Wyjście
#
# Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Sroga kara.
# arak
# ```
#
# **Wyjście:**
#
# ```
# kara
# ```
#
# ### Uwagi
#
# * Tak jak wyżej: usuń interpunkcję z brzegów słów.
# * Porównuj np. posortowane litery w `lower()`.
source ../assert.sh

# Funkcja sortujaca znaki w napisie alfabetycznie
# Zlozonosc czasowa: O(n log n)
# Zlozonosc pamieciowa: O(n)
sortuj_napis() {
    local napis=$1
    echo "$napis" | tr -d ' ' | tr -d '\n' | tr -d '\t' | tr -d '\r' | grep -o . | sort | tr -d "\n"
}

# Funkcja sprawdzajaca czy dwa napisy sa anagramami
# Zlozonosc czasowa: O(n log n)
# Zlozonosc pamieciowa: O(n)
czy_anagramy() {
    local napis_a="$1"
    local napis_b="$2"

    # Sprawdzenie dlugosci
    if [ ${#napis_a} -ne ${#napis_b} ]; then
        echo false
        return
    fi

    # Porownanie posortowanych napisow
    local napis_a_sorted=$(sortuj_napis "$napis_a")
    local napis_b_sorted=$(sortuj_napis "$napis_b")

    if [ "$napis_a_sorted" == "$napis_b_sorted" ]; then
        echo true
    else
        echo false
    fi
}

# Funkcja wypisujaca slowa ze zdania
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
wypisz_slowa() {
    local zdanie="$1"

    # Usuniecie znakow interpunkcyjnych
    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo" | tr '[:upper:]' '[:lower:]'
        fi
    done

}

# Funkcja znajdujaca wszystkie anagramy slowa w zdaniu
# Zlozonosc czasowa: O(n * m log m), gdzie n to liczba slow, m to srednia dlugosc slowa
# Zlozonosc pamieciowa: O(n)
anagramy_w_zdaniu() {
    local zdanie="$1"
    local slowo="$2"
    local slowa=$(wypisz_slowa "$zdanie")

    for inne_slowo in $slowa; do
        if [ "$(czy_anagramy "$slowo" "$inne_slowo")" == "true" ]; then
            echo "$inne_slowo"
        fi
    done
}

test_anagramy_w_zdaniu() {
    local zdanie="Za jego nikczemne uczynki, spotkala go wysoce sroga kara."
    local slowo="arak"
    local wynik=($(anagramy_w_zdaniu "$zdanie" "$slowo"))
    local oczekiwane=(kara)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_anagramy_w_zdaniu
}

main "$@"
