# ZAD-05 — Sortowanie trzech liczb
# 
# **Poziom:** ★★☆
# **Tagi:** `sort`, `warunki`, `porządkowanie`
# 
# ### Treść
# 
# Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.
# 
# ### Wejście
# 
# * 1 linia: `a` (całkowita, `a ≥ 0`)
# * 2 linia: `b` (całkowita, `b ≥ 0`)
# * 3 linia: `c` (całkowita, `c ≥ 0`)
# 
# ### Wyjście
# 
# Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 2
# 1
# 4
# ```
# 
# **Wyjście:**
# 
# ```
# 1 2 4
# ```
# 
# ### Uwagi
# 
# * Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

main() {

    echo "Podaj trzy liczby:"
    read a
    read b
    read c

    if [[ $a -ls $b && $a -ls $c ]]; then
        if [[ $b -ls $c ]]; then
            echo $a
            echo $b
            echo $c
        else
            echo $a
            echo $c
            echo $b
        fi

    elif [[ $b -ls $a && $b -ls $c ]]; then
        if [[ $a -ls $c ]]; then
            echo $b
            echo $a
            echo $c
        else
            echo $b
            echo $c
            echo $a
        fi
    else
        if [[ $a -ls $b ]]; then
            echo $c
            echo $a
            echo $b
        else
            echo $c
            echo $b
            echo $a
        fi
    fi
}

main "$@"

