# ZAD-10 — Znalezienie anagramów w tekście (grupy)
# 
# **Poziom:** ★★☆
# **Tagi:** `dict`, `anagramy`, `string`
# 
# ### Treść
# 
# Wczytaj tekst. Znajdź grupy słów będących anagramami (ignoruj wielkość liter, słowa to tylko litery).
# Wypisz wynik jako listę list, np. `[['absurd', 'brudas'], ...]`.
# Do grup wypisuj tylko te klucze, które mają co najmniej 2 słowa.
# 
# ### Wejście
# 
# * 1 linia: tekst
# 
# ### Wyjście
# 
# * Lista list słów
# 
# ### Przykład
# 
# Wejście jak w treści zadania → wyjście:
# 
# ```
# [["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
# ```

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo" | tr '[:upper:]' '[:lower:]'
            fi
        done

    }

    sortuj_napis() {
        local napis=$1
        local napis=$1

# Funkcja do zaimplementowania
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
funkcja_glowna() {
    # TODO: Implementacja funkcjonalnosci opisanej w docstringu
    echo "Funkcjonalnosc wymaga pelnej implementacji"
}

main() {
    funkcja_glowna
}

main "$@"
