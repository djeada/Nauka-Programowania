# ZAD-02 — Trójkąt prostokątny (rosnący)
#
# **Poziom:** ★☆☆
# **Tagi:** `pętle`, `print`, `string`
#
# ### Treść
#
# Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt o wysokości `n`, gdzie w wierszu `i` jest `i` gwiazdek (`i = 1..n`).
#
# ### Wejście
#
# * 1. linia: `n` (`n ≥ 1`)
#
# ### Wyjście
#
# `n` linii:
#
# * 1. linia: `*`
# * 2. linia: `**`
# * …
# * `n`-ta linia: `n` gwiazdek
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# ```
#
# **Wyjście:**
#
# ```
# *
# **
# ***
# ```
main() {
    read n
    for ((i = 1; i <= n; i++)); do
        for ((j = 0; j < i; j++)); do
            echo -n "*"
        done
        echo ""
    done
}
main "$@"
