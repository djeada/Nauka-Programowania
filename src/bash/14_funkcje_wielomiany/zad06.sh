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
main() {
}

main "$@"
