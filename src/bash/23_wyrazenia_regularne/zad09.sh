# ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`
#
# ### Treść
#
# Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.
#
# ### Wejście
#
# Dwie części:
#
# 1. Tekst (może mieć wiele wierszy)
# 2. W osobnej linii: `klucz`
#
# ### Wyjście
#
# Zmodyfikowany tekst.
#
# ### Przykład
#
# *(jak w treści zadania — długi tekst)*
source ../assert.sh

# Usuwa z każdego wiersza tekstu część od pierwszego wystąpienia zakazanego
# słowa do końca wiersza (wiersze bez zakazanego słowa pozostają bez zmian).
# Białe znaki na początku wierszy są pomijane.
# Złożoność czasowa: O(n*m), gdzie n to liczba wierszy, m to długość wiersza
# Złożoność pamięciowa: O(n)
usun_zakazane_slowo() {
    local tekst="$1"
    local zakazane_slowo="$2"
    local wiersz

    while IFS= read -r wiersz; do
        wiersz="${wiersz#"${wiersz%%[![:space:]]*}"}"
        if [[ -z $wiersz ]]; then
            continue
        fi
        echo "${wiersz%%"$zakazane_slowo"*}"
    done <<<"$tekst"
}

test_usun_zakazane_slowo() {
    local tekst="Turned it up should no valley cousin he.
    Speaking numerous ask did horrible packages set.
    Ashamed herself has distant can studied mrs.
    Led therefore its middleton perpetual fulfilled provision frankness.
    Small he drawn after among every three no.
    All having but you edward genius though remark one.
    Rooms oh fully taken by worse do.
    Points afraid but may end law lasted.
    Was out laughter raptures returned outweigh.
    Luckily cheered colonel me do we attacks on highest enabled.
        Tried law yet style child.
        Bore of true of no be deal.
        Frequently sufficient in be unaffected.
        The furnished she concluded depending procuring concealed.
        "
    local zakazane_slowo="a"
    local wynik
    mapfile -t wynik < <(usun_zakazane_slowo "$tekst" "$zakazane_slowo")
    local oczekiwane=('Turned it up should no v' 'Spe' 'Ash' 'Led therefore its middleton perpetu' 'Sm' 'All h' 'Rooms oh fully t' 'Points ' 'W' 'Luckily cheered colonel me do we ' 'Tried l' 'Bore of true of no be de' 'Frequently sufficient in be un' 'The furnished she concluded depending procuring conce')
    assertArrayEqual wynik oczekiwane $LINENO
}

test_brak_zakazanego_slowa() {
    local wynik
    mapfile -t wynik < <(usun_zakazane_slowo "Ala ma kota" "pies")
    local oczekiwane=('Ala ma kota')
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_usun_zakazane_slowo
    test_brak_zakazanego_slowa
}

main "$@"
