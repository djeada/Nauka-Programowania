# ZAD-02 — Sortowanie słów w zdaniu
#
# **Poziom:** ★★☆
# **Tagi:** `sort`, `string`, `split`
#
# ### Treść
#
# Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.
#
# ### Wejście
#
# * 1 linia: napis `zdanie`
#
# ### Wyjście
#
# * 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Lemur wygina śmiało ciało
# ```
#
# **Wyjście:**
#
# ```
# ['Lemur', 'ciało', 'wygina', 'śmiało']
# ```
#
# ### Uwagi o formatowaniu
#
# * Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
# * Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

source ../assert.sh

# Sortuje słowa w zdaniu alfabetycznie, usuwając znaki interpunkcyjne.
# Złożoność czasowa: O(n log n), gdzie n to liczba słów
# Złożoność pamięciowa: O(n)
sortuj_slowa_w_zdaniu() {
    local zdanie="$1"
    zdanie="${zdanie//[,.:;?!]/}"
    echo "$zdanie" | tr " " "\n" | sort -V | tr "\n" " "
}

test_sortuj_slowa_w_zdaniu() {
    local wynik=($(sortuj_slowa_w_zdaniu "Lemur wygina smialo cialo"))
    local oczekiwane=(Lemur cialo smialo wygina)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_sortuj_slowa_w_zdaniu
}

main "$@"
