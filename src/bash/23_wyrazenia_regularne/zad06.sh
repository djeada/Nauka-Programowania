# ZAD-06 — Wiersze kończące się określonym napisem
#
# **Poziom:** ★☆☆
# **Tagi:** `regex`, `string`, `linijki`
#
# ### Treść
#
# Otrzymujesz dwa napisy:
#
# 1. tekst wielowierszowy,
# 2. słowo lub fragment.
#
# Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).
#
# ### Wejście
#
# Dwie części:
#
# 1. Tekst (wiele wierszy)
# 2. W osobnej linii: `koncowka`
#
# *(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*
#
# ### Wyjście
#
# Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Folgujmy paniom nie sobie, ma rada;
# Milujmy wiernie nie jest w nich przysada.
# Godności trzeba nie za nic tu cnota,
# Miłości pragną nie pragną tu złota.
# da
# ```
#
# **Wyjście:**
#
# ```
# Folgujmy paniom nie sobie, ma rada;
# Milujmy wiernie nie jest w nich przysada.
# ```
source ../assert.sh

# Znajduje wiersze kończące się podanym napisem.
# Złożoność czasowa: O(n*m), gdzie n to liczba wierszy, m to długość wiersza
# Złożoność pamięciowa: O(n)
wiersze_konczace_sie_napisem() {
    local tekst=$1
    local koniec=$2

    for wiersz in $tekst; do
        if [[ $wiersz == *$koniec ]]; then
            echo $wiersz
        fi
    done

    echo "$tekst" | grep -E ".*$koniec"
}

test_wiersze_konczace_sie_napisem() {
    local tekst="Folgujmy paniom nie sobie, ma rada;
    Milujmy wiernie nie jest w nich przysada.
    Godnosci trzeba nie za nic tu cnota,
    Milosci pragna nie pragna tu zlota."
    local koniec="da"
    local wynik=($(wiersze_konczace_sie_napisem "$tekst" "$koniec"))
    local oczekiwane=('Folgujmy paniom nie sobie, ma rada;' 'Milujmy wiernie nie jest w nich przysada.')

    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_wiersze_konczace_sie_napisem
}

main "$@"
