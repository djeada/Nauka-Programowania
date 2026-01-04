# ZAD-05 — Największy wspólny dzielnik (NWD)
# 
# **Poziom:** ★☆☆
# **Tagi:** `Euklides`, `modulo`, `pętle`
# 
# ### Treść
# 
# Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.
# 
# ### Wejście
# 
# Dwa argumenty funkcji:
# 
# * `a` (liczba naturalna, `a > 0`)
# * `b` (liczba naturalna, `b > 0`)
# 
# ### Wyjście
# 
# Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(nwd(60, 45))
# ```
# 
# **Wyjście:**
# 
# ```
# 15
# ```
source ../assert.sh

nwdV1() {

    a=$1
    b=$2

    if (( $a % $b == 0)); then
        echo $b
    else
        nwdV1 $b $(( $a % $b ))
    fi
}

nwdV2() {

    a=$1
    b=$2

    while [ $b -ne $(($a % $b)) ]; do
        c=$b
        b=$(($a % $b))
        a=$c

        if (( $b == 0 )); then
            break;
        fi
    done

    echo $a
}

test1() {
    test1() {
        a=14
        b=21
        wynik=7
        assert "$wynik -eq $(nwdV1 $a $b)" $LINENO
    }

    test2() {
        a=14
        b=21
        wynik=7
        assert "$wynik -eq $(nwdV2 $a $b)" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

