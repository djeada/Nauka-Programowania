# ZAD-02A — Suma dwóch liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `arytmetyka`
#
# ### Treść
#
# Napisz funkcję `suma(a, b)`, która zwraca sumę dwóch liczb całkowitych.
#
# ### Wejście
#
# Dwa argumenty funkcji:
#
# * `a` (liczba całkowita)
# * `b` (liczba całkowita)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `a + b`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(suma(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 8
# ```
#
# ZAD-02B — Różnica: b − a
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `arytmetyka`
#
# ### Treść
#
# Napisz funkcję `roznica(a, b)`, która zwraca różnicę: `b - a`.
#
# ### Wejście
#
# Dwa argumenty funkcji: `a`, `b` (liczby całkowite)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `b - a`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(roznica(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
#
# ZAD-02C — Iloczyn dwóch liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `arytmetyka`
#
# ### Treść
#
# Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn `a * b`.
#
# ### Wejście
#
# Dwa argumenty funkcji: `a`, `b` (liczby całkowite)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `a * b`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(iloczyn(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 15
# ```
#
# ZAD-02D — Iloraz całkowity: a // b
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `dzielenie`, `//`
#
# ### Treść
#
# Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.
#
# ### Wejście
#
# Dwa argumenty funkcji: `a`, `b` (liczby całkowite)
#
# ### Ograniczenia / gwarancje
#
# * `b ≠ 0`
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `a // b`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(iloraz(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 0
# ```
#
# ZAD-02E — Reszta z dzielenia: a % b
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `modulo`, `%`
#
# ### Treść
#
# Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.
#
# ### Wejście
#
# Dwa argumenty funkcji: `a`, `b` (liczby całkowite)
#
# ### Ograniczenia / gwarancje
#
# * `b ≠ 0`
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `a % b`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(reszta(3, 5))
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```

suma() {
    return $(($1 + $2))
}

roznica() {
    return $(($2 - $1))
}

iloczyn() {
    return $(($1 * $2))
}

reszta() {
    return $(($2 % $1))
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    suma $a $b
    wynik=$?
    echo "suma liczb to $wynik"

    roznica $a $b
    wynik=$?
    echo "iloczyn liczb to $wynik"

    iloczyn $a $b
    wynik=$?
    echo "suma liczb to $wynik"

    reszta $a $b
    wynik=$?
    echo "reszte z dzielenia pierwszej przez druga to $wynik"
}

main "$@"
