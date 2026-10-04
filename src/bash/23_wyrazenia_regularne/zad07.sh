# ZAD-07 — Podziel tekst względem znaków interpunkcyjnych
#
# **Poziom:** ★☆☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz napis (jedno lub kilka zdań). Podziel tekst na fragmenty w miejscach występowania znaków interpunkcyjnych (np. `, . ! ? ; :`). Usuń spacje na początku i końcu każdego fragmentu.
#
# ### Wejście
#
# Jedna linia:
#
# * `tekst`
#
# ### Wyjście
#
# Każdy fragment w osobnej linii.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Ani nie poszedł do kina, ani nie wybrał się do teatru.
# ```
#
# **Wyjście:**
#
# ```
# Ani nie poszedł do kina
# ani nie wybrał się do teatru
# ```
source ../assert.sh

# Dzieli zdanie na fragmenty w miejscach znaków interpunkcyjnych i usuwa
# spacje z początku i końca każdego fragmentu (puste fragmenty są pomijane).
# Złożoność czasowa: O(n), gdzie n to liczba znaków w zdaniu
# Złożoność pamięciowa: O(n)
podziel_na_slowa() {
    local zdanie="$1"
    echo "$zdanie" | tr '[:punct:]' '\n' | awk 'NF {$1=$1; print}'
}

test_podziel_na_slowa() {
    local zdanie="hej, pan slimak! tak to ja. chodzcie to zaspiewam wam."
    local wynik
    mapfile -t wynik < <(podziel_na_slowa "$zdanie")
    local oczekiwane=("hej" "pan slimak" "tak to ja" "chodzcie to zaspiewam wam")
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_podziel_na_slowa
}

main "$@"
