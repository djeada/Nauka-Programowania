# ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `suma cyfr`, `warunki`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz suma cyfr liczby `x` wynosi `10`. Każdą liczbę wypisz w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Liczby spełniające warunek, każda w nowej linii.
# Jeśli brak — brak wyjścia.
#
# ZAD-06B — Dwucyfrowe większe od n
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `przedziały`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby **dwucyfrowe** większe od `n` (czyli z zakresu 10–99), każdą w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Liczby dwucyfrowe `x` takie, że `x > n`, każda w nowej linii.
# Jeśli brak — brak wyjścia.
#
# ### Przykład (dla n = 95)
#
# **Wejście:**
#
# ```
# 95
# ```
#
# **Wyjście:**
#
# ```
# 96
# 97
# 98
# 99
# ```
#
# ZAD-06C — Trzycyfrowe o sumie cyfr równej n
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `suma cyfr`, `warunki`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby trzycyfrowe `x` (100–999), których suma cyfr jest równa `n`. Każdą liczbę wypisz w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Liczby trzycyfrowe spełniające warunek, każda w nowej linii.
# Jeśli brak — brak wyjścia.
#
# ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `dzielenie`, `suma cyfr`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Oblicz sumę cyfr liczby `n` i oznacz ją jako `s`. Następnie wypisz wszystkie liczby trzycyfrowe `x` (100–999), które są podzielne przez `s`. Każdą liczbę wypisz w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Ograniczenia / gwarancje
#
# * Suma cyfr `n` jest większa od zera (czyli `n ≠ 0`), aby dzielenie było poprawne.
#
# ### Wyjście
#
# Liczby trzycyfrowe podzielne przez `s`, każda w nowej linii.
#
# ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `warunki`, `cyfry`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Wypisz wszystkie liczby naturalne `x` takie, że `0 ≤ x < n` oraz każda cyfra w zapisie dziesiętnym `x` jest parzysta. Każdą liczbę wypisz w osobnej linii.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Liczby spełniające warunek, każda w nowej linii.
# Jeśli brak — brak wyjścia.
#
# ### Przykład (dla n = 95)
#
# **Wejście:**
#
# ```
# 95
# ```
#
# **Wyjście:**
#
# ```
# 2
# 4
# 6
# 8
# 22
# 24
# 26
# 28
# 42
# 44
# 46
# 48
# 62
# 64
# 66
# 68
# 82
# 84
# 86
# 88
# ```
#
# ### Uwagi o formatowaniu
#
# * W tym zadaniu `0` też składa się wyłącznie z parzystych cyfr. Jeśli chcesz je uwzględniać, dopisz to jako regułę w treści (tu: pomijamy `0`, bo w przykładzie go nie ma).
main() {
    read a

    # Funkcja pomocnicza do obliczania sumy cyfr
    suma_cyfr() {
        local num=$1
        local suma=0
        while [ $num -gt 0 ]; do
            suma=$(($suma + $num % 10))
            num=$(($num / 10))
        done
        echo $suma
    }

    # Funkcja sprawdzająca czy wszystkie cyfry są parzyste
    wszystkie_parzyste() {
        local num=$1
        if [ $num -eq 0 ]; then
            return 1 # Pomijamy 0
        fi
        while [ $num -gt 0 ]; do
            local cyfra=$(($num % 10))
            if [[ $(($cyfra % 2)) -ne 0 ]]; then
                return 1
            fi
            num=$(($num / 10))
        done
        return 0
    }

    # ZAD-06A: Liczby mniejsze od n o sumie cyfr równej 10
    for ((i = 0; i < $a; i++)); do
        if [[ $(suma_cyfr $i) -eq 10 ]]; then
            echo $i
        fi
    done

    # ZAD-06B: Dwucyfrowe większe od n
    for ((i = 10; i < 100; i++)); do
        if [[ $i -gt $a ]]; then
            echo $i
        fi
    done

    # ZAD-06C: Trzycyfrowe o sumie cyfr równej n
    for ((i = 100; i < 1000; i++)); do
        if [[ $(suma_cyfr $i) -eq $a ]]; then
            echo $i
        fi
    done

    # ZAD-06D: Trzycyfrowe podzielne przez sumę cyfr liczby n
    suma_n=$(suma_cyfr $a)
    if [[ $suma_n -gt 0 ]]; then
        for ((i = 100; i < 1000; i++)); do
            if [[ $(($i % $suma_n)) -eq 0 ]]; then
                echo $i
            fi
        done
    fi

    # ZAD-06E: Mniejsze od n złożone wyłącznie z parzystych cyfr
    for ((i = 2; i < $a; i++)); do
        if wszystkie_parzyste $i; then
            echo $i
        fi
    done
}

main "$@"
