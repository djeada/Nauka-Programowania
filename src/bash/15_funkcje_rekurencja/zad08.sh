# ZAD-08 — Wieża Hanoi
# 
# **Poziom:** ★★☆
# **Tagi:** `rekurencja`, `Hanoi`
# 
# ### Treść
# 
# Na słupku `A` leży `N` krążków o różnych średnicach: na dole największy, a każdy kolejny jest mniejszy od poprzedniego. Słupki `B` i `C` są puste. Należy przenieść wszystkie krążki na słupek `B`, korzystając ze słupka `C` jako pomocniczego. Obowiązują zasady:
# 
# * w jednym ruchu przenosimy dokładnie jeden krążek — górny krążek z jednego słupka na inny,
# * nie wolno położyć większego krążka na mniejszym.
# 
# Napisz rekurencyjną funkcję `hanoi(n, skad, dokad, pomocniczy)`, która wypisuje ruchy przenoszące `n` krążków ze słupka `skad` na słupek `dokad`. Program wczytuje `N` i wypisuje **najkrótszą** sekwencję ruchów (ma ona $2^N - 1$ ruchów i jest wyznaczona jednoznacznie).
# 
# ### Wejście
# 
# Jedna liczba naturalna `N`.
# 
# ### Wyjście
# 
# $2^N - 1$ linii — kolejne ruchy w formacie `X -> Y`, gdzie `X` to słupek, z którego zdejmujemy krążek, a `Y` to słupek, na który go kładziemy.
# 
# ### Ograniczenia
# 
# * `1 ≤ N ≤ 10`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 3
# ```
# 
# **Wyjście:**
# 
# ```
# A -> B
# A -> C
# B -> C
# A -> B
# C -> A
# C -> B
# A -> B
# ```
# 
# ### Uwagi
# 
# * Aby przenieść `n` krążków ze słupka `skad` na `dokad`: przenieś `n-1` górnych krążków na słupek `pomocniczy`, przenieś największy krążek na `dokad`, a na koniec przenieś `n-1` krążków ze słupka `pomocniczy` na `dokad`. Przypadek bazowy: jeden krążek (albo zero krążków — wtedy nic nie robimy).
# 
# ### Kod startowy
# 
# ```python
# def hanoi(n, skad, dokad, pomocniczy):
#     pass
# 
# 
# n = int(input())
# hanoi(n, "A", "B", "C")
# ```
source ../assert.sh

hanoi() {
    # Wypisuje ruchy "X -> Y" przenoszące n krążków ze słupka skad na słupek dokad.
    # Złożoność czasowa: O(2^n), złożoność pamięciowa: O(n) - przez stos rekurencji
    local n=$1
    local skad=$2
    local dokad=$3
    local pomocniczy=$4

    if ((n == 0)); then
        return
    fi

    hanoi $((n - 1)) "$skad" "$pomocniczy" "$dokad"
    echo "$skad -> $dokad"
    hanoi $((n - 1)) "$pomocniczy" "$dokad" "$skad"
}

main() {
    assertEqual "$(hanoi 1 A B C)" "A -> B" $LINENO
    assertEqual "$(hanoi 2 A B C)" $'A -> C\nA -> B\nC -> B' $LINENO
    assertEqual "$(hanoi 3 A B C)" $'A -> B\nA -> C\nB -> C\nA -> B\nC -> A\nC -> B\nA -> B' $LINENO
    assertEqual "$(hanoi 10 A B C | wc -l)" 1023 $LINENO
}

main "$@"
