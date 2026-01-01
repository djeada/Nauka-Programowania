# ZAD-03 — Rysowanie kształtów znakami
#
# **Poziom:** ★☆☆
# **Tagi:** `print`, `formatowanie`, `pętle`, `string`
#
# ### Treść
#
# Wypisz na wyjście trzy kształty:
#
# 1. **Kwadrat 2×2** z liter `x`
# 2. **Trójkąt liczbowy** z 3 linii: w linii `i` wypisz `i` razy cyfrę `i` (dla i=1..3)
# 3. **Romb z jedynek** o maksymalnej szerokości 5 znaków
#
# Każdy kształt ma być oddzielony **jedną pustą linią**.
#
# ### Wejście
#
# Brak.
#
# ### Wyjście
#
# Dokładnie:
#
# * 2 linie kwadratu,
# * pusta linia,
# * 3 linie trójkąta,
# * pusta linia,
# * 5 linii rombu.
#
# ### Przykład (oczekiwane wyjście)
#
# ```
# xx
# xx
#
# 1
# 22
# 333
#
#   1
#  111
# 11111
#  111
#   1
# ```
#
# ### Uwagi o formatowaniu
#
# * W rombie spacje na początku linii są istotne.
# * Nie dodawaj dodatkowych pustych linii na początku; jedna na końcu jest zwykle akceptowalna, ale trzymaj się przykładu.

main() {

    echo "xx"
    echo "xx"
    echo "xx"

    echo "1"
    echo "1"
    echo "22"
    echo "333"

    echo "  1"
    echo "  1"
    echo " 111"
    echo "11111"
    echo " 111"
    echo "  1"

}

main "$@"
