# ZAD-04 — Obliczanie silni liczby
# 
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `silnia`, `mnożenie`
# 
# ### Treść
# 
# Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
# Przyjmij, że `0! = 1`.
# 
# ### Wejście
# 
# Jeden argument funkcji:
# 
# * `n` (liczba naturalna, `n ≥ 0`)
# 
# ### Wyjście
# 
# Funkcja zwraca jedną liczbę naturalną — `n!`.
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(silnia(3))
# ```
# 
# **Wyjście:**
# 
# ```
# 6
# ```
source ../assert.sh

silnia() {

    a=$1
    wynik=1

    while [ $a -gt 0 ]; do
        wynik=$(($wynik * $a))
        a=$(($a - 1))
    done

    echo $wynik
}

test1() {
    test1() {
        a=0
        wynik=1
        assert "$wynik -eq $(silnia $a $b)" $LINENO
    }

    test2() {
        a=4
        wynik=24
        assert "$wynik -eq $(silnia $a $b)" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

