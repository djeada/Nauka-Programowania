# ZAD-08 — Naiwny test pierwszości liczby
# 
# **Poziom:** ★★☆
# **Tagi:** `pierwszość`, `pętle`, `dzielniki`
# 
# ### Treść
# 
# Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.
# 
# ### Wejście
# 
# Jeden argument funkcji:
# 
# * `n` (liczba naturalna, `n ≥ 2`)
# 
# ### Wyjście
# 
# Funkcja zwraca wartość logiczną:
# 
# * `True` lub `False`
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(czy_pierwsza(7))
# print(czy_pierwsza(4))
# ```
# 
# **Wyjście:**
# 
# ```
# True
# False
# ```
# 
# ### Uwagi
# 
# * Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
# * Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

source ../assert.sh

czyPierwsza() {

    a=$1

    if [[ $a -lt 2 ]]; then
        echo false
        return
    fi

    if [[ $a -eq 2 ]] || [[ $a -eq 3 ]]; then
        echo true
        return
    fi

    if [[ $(($a % 2)) -eq 0 ]] || [[ $(($a % 3)) -eq 0 ]]; then
        echo false
        return
    fi

    i=3

    while [[ $((i * i)) -le $a ]]; do

        if [[ $(($a % i)) -eq 0 ]]; then
            echo false
            return
        fi

        i=$((i + 2))
    done

    echo true
    return
}

test1() {
    test1() {
        a=7
        assertTrue "$(czyPierwsza $a)" $LINENO
    }

    test2() {
        a=4
        assertFalse "$(czyPierwsza $a)" $LINENO
    }

    test3() {
        a=1
        assertTrue "$(czyPierwsza $a)" $LINENO
    }

    main() {
        test1
        test2
        test3
    }

    main "$@"

