# ZAD-03A — Mnożenie przy pomocy dodawania
# 
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `dodawanie`, `mnożenie`
# 
# ### Treść
# 
# Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko dodawania** i pętli.
# 
# ### Wejście
# 
# Dwa argumenty funkcji:
# 
# * `a` (liczba naturalna, `a ≥ 0`)
# * `b` (liczba naturalna, `b ≥ 0`)
# 
# ### Wyjście
# 
# Funkcja zwraca jedną liczbę naturalną — `a * b`.
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(iloczyn(3, 2))
# ```
# 
# **Wyjście:**
# 
# ```
# 6
# ```
# 
# ZAD-03B — Dzielenie całkowite przy pomocy odejmowania
# 
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `odejmowanie`, `dzielenie`
# 
# ### Treść
# 
# Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko odejmowania** i pętli.
# 
# ### Wejście
# 
# Dwa argumenty funkcji:
# 
# * `a` (liczba naturalna, `a ≥ 0`)
# * `b` (liczba naturalna)
# 
# ### Ograniczenia / gwarancje
# 
# * `b > 0`
# 
# ### Wyjście
# 
# Funkcja zwraca jedną liczbę naturalną — `a // b`.
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(iloraz(3, 2))
# ```
# 
# **Wyjście:**
# 
# ```
# 1
# ```

source ../assert.sh

mnozenie() {
    mnozenie() {

        a=$1
        b=$2
        wynik=0

        for (( i=0; i<$b; i++ )); do
            wynik=$(($wynik + $a))
        done

        echo $wynik
    }

    dzielenie() {
        dzielenie() {
            a=$1
            b=$2
            wynik=0

            while [ $a -ge $b ]; do
                a=$(($a - $b))
                wynik=$(($wynik + 1))
            done

            echo $wynik
        }

        test1() {
            test1() {
                a=2
                b=3
                wynik=6
                assert "$wynik -eq $(mnozenie $a $b)" $LINENO
            }

            test2() {
                a=30
                b=6
                wynik=5
                assert "$wynik -eq $(dzielenie $a $b)" $LINENO

            }

            main() {
                test1
                test2
            }

            main "$@"

