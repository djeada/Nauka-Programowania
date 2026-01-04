# ZAD-06 — Czy średnia elementów znajduje się w liście?
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `średnia`, `wyszukiwanie`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.
#
# Wypisz:
#
# * `Tak` — jeśli średnia występuje w liście,
# * `Nie` — w przeciwnym razie.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
# * kolejne `N` linii: liczby całkowite
#
# ### Wyjście
#
# Jedno słowo: `Tak` lub `Nie`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 6
# 2
# 1
# 4
# 27
# ```
#
# **Wyjście:**
#
# ```
# Nie
# ```
#
# ### Uwagi
#
# * Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb całkowitych.
source ../assert.sh

srednia() {
    local suma=$(
        IFS=+
        echo "$((${lista[*]}))"
    )
    local n=${#lista[@]}
    echo $((suma / n))
}

czy_srednia_w_liscie() {

    local srednia_wartosc=$(srednia)
    for elem in "${lista[@]}"; do
        if [ $elem -eq $srednia_wartosc ]; then
            echo true
            return
        fi
    done

    echo false
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    assertFalse "$(czy_srednia_w_liscie)" $LINENO
}

test2() {
    local lista=(1 2 3)
    assertTrue "$(czy_srednia_w_liscie)" $LINENO
}

main() {
    test1
    test2
}

main "$@"
