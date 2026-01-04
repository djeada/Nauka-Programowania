# ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)
# 
# **Poziom:** ★☆☆
# **Tagi:** `nww`, `nwd`, `arytmetyka`
# 
# ### Treść
# 
# Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb `a` i `b`.
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
# Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.
# 
# ### Przykład
# 
# **Wywołanie funkcji:**
# 
# ```python
# print(nww(7, 9))
# ```
# 
# **Wyjście:**
# 
# ```
# 63
# ```
# 
# ### Ograniczenia / gwarancje
# 
# * Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.
source ../assert.sh

nwd() {

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

nww() {
    echo $(($a * $b / $(nwd $a $b)))
}

test1() {
    test1() {
        a=14
        b=21
        wynik=42
        assert "$wynik -eq $(nww $a $b)" $LINENO
    }

    main() {
        test1

    }

    main "$@"

