# ZAD-09A — Wielkie → małe (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `string`
#
# ### Treść
#
# Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# Jedna linia: napis po konwersji.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Test
# ```
#
# **Wyjście:**
#
# ```
# test
# ```
#
# ZAD-09B — Małe → wielkie (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `string`
#
# ### Treść
#
# Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# Jedna linia: napis po konwersji.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Test
# ```
#
# **Wyjście:**
#
# ```
# TEST
# ```
#
# ZAD-09C — Odwróć wielkość liter (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `toggle case`
#
# ### Treść
#
# Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.
#
# ### Wejście
#
# * 1. linia: napis
#
# ### Wyjście
#
# Jedna linia: napis po zmianie.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Test
# ```
#
# **Wyjście:**
#
# ```
# tEST
# ```

# Uzycie:
#   bash zad09.sh                       - uruchamia testy
#   bash zad09.sh --stdin A < dane.txt  - podpunkt A (C - podpunkt C)

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Kody ASCII wielkiej i malej litery roznia sie tylko bitem o wartosci 32.
readonly BIT_WIELKOSCI=32

# Przeksztalca litery napisu $2 operacja bitowa $1 na kodach ASCII:
#   male   - A-Z: kod | 32
#   odwroc - A-Z i a-z: kod ^ 32
# Pozostale znaki zostaja bez zmian.
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
przeksztalc_litery() {
    local operacja=$1 napis=$2 wynik="" znak kod nowy_kod hex i
    for ((i = 0; i < ${#napis}; i++)); do
        znak=${napis:i:1}
        printf -v kod '%d' "'$znak"
        nowy_kod=$kod
        case $operacja in
            male)
                if ((kod >= 65 && kod <= 90)); then
                    ((nowy_kod |= BIT_WIELKOSCI))
                fi
                ;;
            odwroc)
                if ((kod >= 65 && kod <= 90 || kod >= 97 && kod <= 122)); then
                    ((nowy_kod ^= BIT_WIELKOSCI))
                fi
                ;;
        esac
        if ((nowy_kod != kod)); then
            # Kod ASCII -> znak: printf '%b' rozumie sekwencje \xHH
            printf -v hex '%x' "$nowy_kod"
            printf -v znak '%b' "\\x$hex"
        fi
        wynik+=$znak
    done
    echo "$wynik"
}

# ZAD-09A
na_male() {
    przeksztalc_litery male "$1"
}

# ZAD-09C
odwroc_wielkosc() {
    przeksztalc_litery odwroc "$1"
}

program_a() {
    local napis
    IFS= read -r napis
    na_male "$napis"
}

program_c() {
    local napis
    IFS= read -r napis
    odwroc_wielkosc "$napis"
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

test_na_male() {
    sprawdz program_a "Test" "test" $LINENO
    sprawdz program_a "Ala ma 2 KOTY!" "ala ma 2 koty!" $LINENO
    # Znaki sasiadujace z literami w tablicy ASCII zostaja bez zmian
    sprawdz program_a "@[\`{AZ" "@[\`{az" $LINENO
}

test_odwroc_wielkosc() {
    sprawdz program_c "Test" "tEST" $LINENO
    sprawdz program_c "  Ala ma 2 Koty!  " "  aLA MA 2 kOTY!  " $LINENO
    sprawdz program_c "@[\`{aZ" "@[\`{Az" $LINENO
}

main() {
    local podpunkt=${2:-}
    if [[ ${1:-} == --stdin ]]; then
        case ${podpunkt^^} in
            A) program_a ;;
            C) program_c ;;
            *)
                echo "Uzycie: bash zad09.sh --stdin A|C < dane.txt" >&2
                return 2
                ;;
        esac
    else
        test_na_male
        test_odwroc_wielkosc
    fi
}

main "$@"
