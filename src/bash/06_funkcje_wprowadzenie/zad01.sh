# ZAD-01A — Zwracanie stałej wartości: liczba 3
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `return`, `int`
#
# ### Treść
#
# Napisz funkcję (bez argumentów), która zwraca liczbę całkowitą `3`.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Funkcja ma zwrócić:
#
# * `3`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# wynik = zwroc_liczbe()
# print(wynik)
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```
#
# ZAD-01B — Zwracanie stałej wartości: napis „Tak”
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `return`, `string`
#
# ### Treść
#
# Napisz funkcję (bez argumentów), która zwraca napis `Tak`.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Funkcja ma zwrócić:
#
# * `Tak`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# wynik = zwroc_napis()
# print(wynik)
# ```
#
# **Wyjście:**
#
# ```
# Tak
# ```
#
# ZAD-01C — Zwracanie stałej wartości: True
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `return`, `bool`
#
# ### Treść
#
# Napisz funkcję (bez argumentów), która zwraca wartość logiczną `True`.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Funkcja ma zwrócić:
#
# * `True`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# wynik = zwroc_prawda()
# print(wynik)
# ```
#
# **Wyjście:**
#
# ```
# True
# ```

funkcja1() {
    return 3
}

funkcja2() {
    echo "Tak"
}

funkcja3() {
    echo true
}

main() {
    funkcja1
    wynik=$?
    echo $wynik

    wynik=$(funkcja2)
    echo $wynik

    wynik=$(funkcja3)
    echo $wynik
}

main "$@"
