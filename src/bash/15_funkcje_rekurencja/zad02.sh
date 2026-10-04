# ZAD-02 — Suma liczb naturalnych mniejszych od N
# 
# **Poziom:** ★☆☆
# **Tagi:** `rekurencja`, `suma`
# 
# ### Treść
# 
# Napisz rekurencyjną funkcję `suma_mniejszych(n)`, która zwraca sumę wszystkich liczb naturalnych mniejszych od $n$, czyli $0 + 1 + 2 + \dots + (n-1)$.
# 
# Program wczytuje $N$ i wypisuje wynik funkcji.
# 
# ### Wejście
# 
# Jedna liczba naturalna `N`.
# 
# ### Wyjście
# 
# Jedna liczba naturalna — suma liczb naturalnych mniejszych od `N`. Dla `N = 0` nie ma takich liczb, więc suma wynosi `0`.
# 
# ### Ograniczenia
# 
# * `0 ≤ N ≤ 100`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 10
# ```
# 
# **Wyjście:**
# 
# ```
# 45
# ```
# 
# $0 + 1 + 2 + \dots + 9 = 45$ (liczba `10` nie jest mniejsza od `10`).
# 
# ### Uwagi
# 
# * Suma liczb mniejszych od $n$ to $(n-1)$ plus suma liczb mniejszych od $n-1$.
# 
# ### Kod startowy
# 
# ```python
# def suma_mniejszych(n):
#     pass
# 
# 
# n = int(input())
# print(suma_mniejszych(n))
# ```
source ../assert.sh

suma_mniejszych() {
    # Wypisuje sumę 0 + 1 + ... + (n - 1).
    # Złożoność czasowa: O(n), złożoność pamięciowa: O(n) - przez stos rekurencji
    local n=$1

    if ((n <= 1)); then
        echo 0
        return
    fi

    echo $((n - 1 + $(suma_mniejszych $((n - 1)))))
}

main() {
    assertEqual "$(suma_mniejszych 0)" 0 $LINENO
    assertEqual "$(suma_mniejszych 1)" 0 $LINENO
    assertEqual "$(suma_mniejszych 10)" 45 $LINENO
    assertEqual "$(suma_mniejszych 100)" 4950 $LINENO
}

main "$@"
