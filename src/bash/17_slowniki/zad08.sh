# ZAD-08 — Najczęstsza litera w zdaniu
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
# Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.
# 
# ### Wejście
# 
# * 1 linia: zdanie
# 
# ### Wyjście
# 
# * 1 znak
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# lezy jerzy na wiezy
# ```
# 
# **Wyjście:**
# 
# ```
# e
# ```
source ../assert.sh

najczesciej_wystepujaca_litera() {
    local zdanie="$1"

    local zdanie=$(echo "$zdanie" | tr -d ' .,:;!?\n')
    local zdanie=$(echo "$zdanie" | tr -d ' .,:;!?\n')

    local -A histogram=()
    local -A histogram=()
    for (( i=0; i<${#zdanie}; i++ )); do
        ((histogram["${zdanie:$i:1}"]++))
    done

    local maks=0
    local maks=0
    for litera in ${!histogram[@]}; do

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
