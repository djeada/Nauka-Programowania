# ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)
#
# **Poziom:** ★★☆
# **Tagi:** `funkcje`, `delta`, `pierwiastki`
#
# ### Treść
#
# Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a, b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.
#
# ### Wejście (argumenty funkcji)
#
# * `coef` — lista trzech liczb `[a, b, c]`
#
# ### Wyjście (zwracana wartość)
#
# * lista liczb zmiennoprzecinkowych:
#
#   * jeśli `Δ < 0` → pusta lista `[]`
#   * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
#   * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)
#
# ### Przykład
#
# Dla `[1, 2, 1]` funkcja zwraca:
# `[-1.0, -1.0]`
#
# ### Ograniczenia / gwarancje
#
# * Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).
#
# ### Uwagi
#
# * Licz `Δ = b^2 - 4ac`.
# * Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.

# Uzycie:
#   bash zad06.sh                     - uruchamia testy
#   bash zad06.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca rzeczywiste miejsca zerowe ax^2 + bx + c (a != 0, wspolczynniki
# calkowite) posortowane rosnaco, z dokladnoscia do 2 miejsc po przecinku.
# Pierwiastek podwojny zwraca raz; gdy delta < 0 - nie wypisuje nic.
# Delta liczymy w Bashu (liczby calkowite); pierwiastek kwadratowy i dzielenie
# wymagaja liczb zmiennoprzecinkowych, wiec liczy je awk (LC_ALL=C wymusza
# kropke jako separator dziesietny). "+ 0" zamienia -0 na 0.
# Zlozonosc czasowa: O(1)
# Zlozonosc pamieciowa: O(1)
miejsca_zerowe() {
    local a=$1 b=$2 c=$3
    local delta=$((b * b - 4 * a * c))

    if ((delta < 0)); then
        return
    fi

    LC_ALL=C awk -v a="$a" -v b="$b" -v delta="$delta" 'BEGIN {
        s = sqrt(delta)
        x1 = (-b - s) / (2 * a) + 0
        x2 = (-b + s) / (2 * a) + 0
        if (x1 > x2) { t = x1; x1 = x2; x2 = t }
        if (delta == 0)
            printf "%.2f\n", x1
        else
            printf "%.2f %.2f\n", x1, x2
    }'
}

# Wczytuje "a b c" ze stdin i wypisuje miejsca zerowe albo komunikat o ich braku.
program() {
    local a b c pierwiastki
    read -r a b c
    pierwiastki=$(miejsca_zerowe "$a" "$b" "$c")
    echo "${pierwiastki:-Brak miejsc zerowych}"
}

# Uruchamia funkcje $1 z wejsciem $2 i porownuje jej wyjscie (dokladnie, wraz
# z koncowym znakiem nowej linii) z $3. ${x@Q} wymusza porownanie napisow.
sprawdz() {
    local funkcja=$1 wejscie=$2 oczekiwane=$3 linia=$4 wynik
    wynik=$("$funkcja" <<<"$wejscie"; printf x)
    wynik=${wynik%x}
    if [[ -n $oczekiwane ]]; then
        oczekiwane+=$'\n'
    fi
    assertEqual "${wynik@Q}" "${oczekiwane@Q}" "$linia"
}

test_miejsca_zerowe() {
    assertEqual "$(miejsca_zerowe 1 -3 2)" "1.00 2.00" $LINENO
    # Dla a < 0 wzor z "+" daje mniejszy pierwiastek - wynik i tak jest posortowany
    assertEqual "$(miejsca_zerowe -1 0 4)" "-2.00 2.00" $LINENO
    assertEqual "$(miejsca_zerowe 1 1 -1)" "-1.62 0.62" $LINENO
    assertEqual "$(miejsca_zerowe 1 0 0)" "0.00" $LINENO
    assertEqual "$(miejsca_zerowe 2 0 1)" "" $LINENO
}

test_program() {
    sprawdz program "1 2 1" "-1.00" $LINENO
    sprawdz program "1 0 1" "Brak miejsc zerowych" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_miejsca_zerowe
        test_program
    fi
}

main "$@"
