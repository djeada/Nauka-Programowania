# ZAD-01 — Podmiana słowa w zdaniu
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `replace`, `substring`
#
# ### Treść
#
# Masz trzy napisy:
#
# 1. Zdanie (tekst do modyfikacji),
# 2. Słowo A (podnapis do znalezienia),
# 3. Słowo B (podnapis zastępujący).
#
# Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.
#
# > Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.
#
# ### Wejście
#
# * 1 linia: zdanie `S`
# * 2 linia: napis `A`
# * 3 linia: napis `B`
#
# ### Wyjście
#
# * 1 linia: zdanie po zamianie
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Lezy jezy na wiezy
# zy
# rzy
# ```
#
# **Wyjście:**
#
# ```
# Lerzy jerzy na wierzy
# ```

source ../assert.sh

# Zamienia wszystkie wystąpienia podnapisu A na B w zdaniu.
# Złożoność czasowa: O(n*m), gdzie n to długość zdania, m to długość A
# Złożoność pamięciowa: O(n)
podmien_slowo() {
    local zdanie="$1"
    local slowo_a="$2"
    local slowo_b="$3"
    
    echo "${zdanie//$slowo_a/$slowo_b}"
}

test_podmien_slowo() {
    local wynik=$(podmien_slowo "Lezy jezy na wiezy" "zy" "rzy")
    assertEqual "$wynik" "Lerzy jerzy na wierzy" $LINENO
}

main() {
    test_podmien_slowo
}

main "$@"
