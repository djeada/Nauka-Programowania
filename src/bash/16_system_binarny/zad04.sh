# ZAD-04A — Liczba zer w zapisie binarnym
#
# **Poziom:** ★☆☆
# **Tagi:** `binarne`, `zliczanie`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.
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
# 0
# ```
#
# ### Uwagi
#
# * Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.
#
# ZAD-04B — Liczba jedynek w zapisie binarnym
#
# **Poziom:** ★☆☆
# **Tagi:** `popcount`, `binarne`
#
# ### Treść
#
# Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.
#
# ### Wejście
#
# * 1. linia: `n`
#
# ### Wyjście
#
# Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.
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
# 2
# ```

# Uzycie:
#   bash zad04.sh                       - uruchamia testy
#   bash zad04.sh --stdin A < dane.txt  - podpunkt A (B - podpunkt B)

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# ZAD-04A: liczba zer w zapisie binarnym n (bez zer wiodacych; dla 0 - 1).
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(1)
liczba_zer() {
    local n=$1 zera=0
    if ((n == 0)); then
        echo 1
        return
    fi
    while ((n > 0)); do
        if (((n & 1) == 0)); then
            ((zera++))
        fi
        ((n >>= 1))
    done
    echo "$zera"
}

# ZAD-04B: liczba jedynek w zapisie binarnym n.
# Zlozonosc czasowa: O(log n)
# Zlozonosc pamieciowa: O(1)
liczba_jedynek() {
    local n=$1 jedynki=0
    while ((n > 0)); do
        ((jedynki += n & 1))
        ((n >>= 1))
    done
    echo "$jedynki"
}

program_a() {
    local n
    read -r n
    liczba_zer "$n"
}

program_b() {
    local n
    read -r n
    liczba_jedynek "$n"
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

test_liczba_zer() {
    assertEqual "$(liczba_zer 0)" 1 $LINENO
    assertEqual "$(liczba_zer 1)" 0 $LINENO
    assertEqual "$(liczba_zer 8)" 3 $LINENO
    assertEqual "$(liczba_zer 10)" 2 $LINENO
    assertEqual "$(liczba_zer 1000000000)" 17 $LINENO
    sprawdz program_a "3" "0" $LINENO
}

test_liczba_jedynek() {
    assertEqual "$(liczba_jedynek 0)" 0 $LINENO
    assertEqual "$(liczba_jedynek 255)" 8 $LINENO
    assertEqual "$(liczba_jedynek 1000000000)" 13 $LINENO
    sprawdz program_b "3" "2" $LINENO
}

main() {
    local podpunkt=${2:-}
    if [[ ${1:-} == --stdin ]]; then
        case ${podpunkt^^} in
            A) program_a ;;
            B) program_b ;;
            *)
                echo "Uzycie: bash zad04.sh --stdin A|B < dane.txt" >&2
                return 2
                ;;
        esac
    else
        test_liczba_zer
        test_liczba_jedynek
    fi
}

main "$@"
