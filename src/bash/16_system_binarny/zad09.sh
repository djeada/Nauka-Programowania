# ZAD-09A — Wielkie → małe (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `string`
#
# ### Treść
#
# Wczytaj napis. Zamień wszystkie wielkie litery alfabetu łacińskiego (`A–Z`) na małe, używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.
#
# ### Wejście
#
# * 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)
#
# ### Wyjście
#
# Jedna linia: napis po zamianie.
#
# ### Ograniczenia
#
# * napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)
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
# ### Uwagi
#
# * Kody wielkiej i małej litery różnią się tylko bitem o wartości 32 (`0b100000`): `ord("A")` to `65`, a `ord("a")` to `97`. Ustawienie tego bitu: `ord(znak) | 32`.
# * Zmieniaj tylko litery `A–Z` — np. `@` i `[` sąsiadują w tablicy ASCII z literami, ale mają pozostać bez zmian.
# * Odwrotną zamianę (małe → wielkie) daje wyzerowanie tego bitu: `ord(znak) & ~32`.
#
# ZAD-09B — Numer litery w alfabecie (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `maski`
#
# ### Treść
#
# Wczytaj słowo złożone z liter alfabetu łacińskiego. Dla każdej litery wyznacz jej numer w alfabecie — `a` i `A` mają numer `1`, `b` i `B` numer `2`, …, `z` i `Z` numer `26` — używając operacji bitowej na kodzie ASCII zamiast porównań i odejmowania.
#
# ### Wejście
#
# * 1. linia: słowo
#
# ### Wyjście
#
# Jedna linia: numery kolejnych liter słowa oddzielone pojedynczymi spacjami.
#
# ### Ograniczenia
#
# * słowo ma od 1 do 100 znaków i składa się wyłącznie z liter `a–z` i `A–Z`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# Bit
# ```
#
# **Wyjście:**
#
# ```
# 2 9 20
# ```
#
# ### Uwagi
#
# * Zapisz kody binarnie: `ord("A")` to $65 = 1000001_2$, a `ord("a")` to $97 = 1100001_2$. Pięć najniższych bitów kodu każdej litery to właśnie jej numer w alfabecie — i to niezależnie od wielkości litery.
# * Pięć najniższych bitów wydobędziesz **maską** $31 = 11111_2$: `ord(znak) & 31`. Operacja `&` z maską zeruje wszystkie bity poza tymi, które w masce są jedynkami.
#
# ZAD-09C — Odwróć wielkość liter (bitowo)
#
# **Poziom:** ★★☆
# **Tagi:** `ASCII`, `bitwise`, `toggle case`
#
# ### Treść
#
# Wczytaj napis. Zamień wielkość każdej litery alfabetu łacińskiego na przeciwną (mała ↔ wielka), używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.
#
# ### Wejście
#
# * 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)
#
# ### Wyjście
#
# Jedna linia: napis po zmianie.
#
# ### Ograniczenia
#
# * napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)
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
#
# ### Uwagi
#
# * Odwrócenie bitu o wartości 32: `ord(znak) ^ 32`. Stosuj je tylko do liter `a–z` i `A–Z`.

# Uzycie:
#   bash zad09.sh                         - uruchamia testy
#   bash zad09.sh --stdin A|B|C < dane.txt - rozwiazuje podpunkt A, B albo C

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

# Numer litery w alfabecie: piec najnizszych bitow kodu ASCII (maska 0b11111)
numery_liter() {
    local slowo=$1 wynik="" kod i
    for ((i = 0; i < ${#slowo}; i++)); do
        printf -v kod '%d' "'${slowo:i:1}"
        ((i > 0)) && wynik+=" "
        wynik+=$((kod & 31))
    done
    echo "$wynik"
}

program_a() {
    local napis
    IFS= read -r napis
    na_male "$napis"
}

program_b() {
    local slowo
    IFS= read -r slowo
    numery_liter "$slowo"
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

test_numery_liter() {
    sprawdz program_b "Bit" "2 9 20" $LINENO
    sprawdz program_b "zZaA" "26 26 1 1" $LINENO
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
            B) program_b ;;
            C) program_c ;;
            *)
                echo "Uzycie: bash zad09.sh --stdin A|B|C < dane.txt" >&2
                return 2
                ;;
        esac
    else
        test_na_male
        test_numery_liter
        test_odwroc_wielkosc
    fi
}

main "$@"
