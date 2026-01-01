# ZAD-10 — Podmień napisy z listy A na napisy z listy B
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`, `zamiana`
#
# ### Treść
#
# Otrzymujesz:
#
# * tekst,
# * listę A (napisy do znalezienia),
# * listę B (napisy do podmiany), tej samej długości co A.
#
# Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.
#
# ### Wejście
#
# 1. Tekst (jedna lub wiele linii)
# 2. Liczba naturalna `n` — długość list
# 3. `n` wierszy: elementy listy A
# 4. `n` wierszy: elementy listy B
#
# ### Wyjście
#
# Zmodyfikowany tekst.
#
# ### Przykład
#
# *(jak w treści — z listami A/B)*

source ../assert.sh

podmien_napisy() {
    local tekst="$1"

    for i in "${!lista_a[@]}"; do
        tekst="${tekst//${lista_a[$i]}/${lista_b[$i]}}"
    done

    echo "$tekst"
}

test_podmien_napisy() {
    local tekst='Whole every miles as tiled at seven or.
    Wished he entire esteem mr oh by.
    He prevent request by if in pleased.
    Picture too and concern has was comfort.
    Ten difficult resembled eagerness nor.
    Same park bore on be.
    Warmth his law design say are person.
    Pronounce suspected in belonging conveying ye repulsive.'
    local lista_a=(or be he)
    local lista_b=(and off she)
    local wynik="$(podmien_napisy "$tekst")"
    local oczekiwane='Whole every miles as tiled at seven and.
    Wished she entire esteem mr oh by.
    He prevent request by if in pleased.
    Picture too and concern has was comfort.
    Ten difficult resembled eagerness nor.
    Same park bore on off.
    Warmth his law design say are person.
    Pronounce suspected in belonging conveying ye repulsive.'
    assertEqual "$wynik" "$oczekiwane"
}

main() {
    test_podmien_napisy
}

main "$@"
