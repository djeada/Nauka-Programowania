# ZAD-03 — Potęga
# 
# **Poziom:** ★☆☆
# **Tagi:** `rekurencja`, `potęgowanie`
# 
# ### Treść
# 
# Napisz rekurencyjną funkcję `potega(a, b)`, która zwraca $a^b$, korzystając z zależności $a^0 = 1$ oraz $a^b = a \cdot a^{b-1}$ dla $b \ge 1$.
# 
# Program wczytuje $a$ i $b$, wywołuje funkcję i wypisuje wynik.
# 
# ### Wejście
# 
# * 1. linia: `a` — liczba całkowita (podstawa)
# * 2. linia: `b` — liczba naturalna (wykładnik)
# 
# ### Wyjście
# 
# Jedna liczba całkowita — wartość $a^b$. Przyjmujemy, że $0^0 = 1$.
# 
# ### Ograniczenia
# 
# * `-10 ≤ a ≤ 10`
# * `0 ≤ b ≤ 18`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 2
# 3
# ```
# 
# **Wyjście:**
# 
# ```
# 8
# ```
# 
# ### Uwagi
# 
# * Nie używaj operatora `**` ani funkcji `pow()` — potęgę ma obliczyć Twoja funkcja.
# 
# ### Kod startowy
# 
# ```python
# def potega(a, b):
#     pass
# 
# 
# a = int(input())
# b = int(input())
# print(potega(a, b))
# ```
source ../assert.sh

potega() {
    # Wypisuje a^b dla b >= 0.
    # Złożoność czasowa: O(b), złożoność pamięciowa: O(b) - przez stos rekurencji
    local a=$1
    local b=$2

    if ((b == 0)); then
        echo 1
        return
    fi

    echo $((a * $(potega "$a" $((b - 1)))))
}

main() {
    assertEqual "$(potega 2 3)" 8 $LINENO
    assertEqual "$(potega 5 0)" 1 $LINENO
    assertEqual "$(potega 0 5)" 0 $LINENO
    assertEqual "$(potega -2 5)" -32 $LINENO
}

main "$@"
