# ZAD-03A — Dodawanie bitowe
#
# **Poziom:** ★☆☆
# **Tagi:** `bitwise`, `XOR`, `AND`
#
# ### Treść
#
# Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie operatorów bitowych (i przesunięć).
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba naturalna: `a + b`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 3
# ```
#
# **Wyjście:**
#
# ```
# 5
# ```
#
# ZAD-03B — Odejmowanie bitowe
#
# **Poziom:** ★☆☆
# **Tagi:** `bitwise`, `pożyczki`, `XOR`
#
# ### Treść
#
# Wczytaj `a` i `b`. Oblicz `a - b` używając wyłącznie operatorów bitowych.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba naturalna: `a - b`.
#
# ### Ograniczenia / gwarancje
#
# * Zakładamy, że `a ≥ b` (wynik jest naturalny).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 5
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```
#
# ZAD-03C — Mnożenie bitowe
#
# **Poziom:** ★☆☆
# **Tagi:** `bitwise`, `shift`, `pętle`
#
# ### Treść
#
# Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np. metoda „shift-and-add”).
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# Jedna liczba naturalna: `a * b`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 4
# 4
# ```
#
# **Wyjście:**
#
# ```
# 16
# ```
#
# ZAD-03D — Dzielenie całkowite bitowe
#
# **Poziom:** ★☆☆
# **Tagi:** `bitwise`, `dzielenie`, `shift`
#
# ### Treść
#
# Wczytaj `a` i `b`. Oblicz `a // b` używając wyłącznie operatorów bitowych.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Ograniczenia / gwarancje
#
# * `b > 0`
#
# ### Wyjście
#
# Jedna liczba naturalna: `a // b`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 9
# 3
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```

# Uzycie:
#   bash zad03.sh                       - uruchamia testy
#   bash zad03.sh --stdin A < dane.txt  - podpunkt A (B, C, D - pozostale podpunkty)

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# W obliczeniach wyniku uzywamy tylko operatorow bitowych (&, |, ^, ~, <<, >>)
# i porownan - bez +, -, *, /, %.
#
# Funkcje pomocnicze zmieniaja zmienna, ktorej nazwe dostaja w $1 (nameref),
# dzieki czemu petle mnozenia i dzielenia nie tworza podpowlok.

# Dodaje bitowo $2 do zmiennej o nazwie $1:
# a ^ b to suma bez przeniesien, (a & b) << 1 to przeniesienia.
# Zlozonosc czasowa: O(log(a+b))
_dodaj_do() {
    local -n _suma=$1
    local skladnik=$2 przeniesienie
    while ((skladnik != 0)); do
        przeniesienie=$(((_suma & skladnik) << 1))
        _suma=$((_suma ^ skladnik))
        skladnik=$przeniesienie
    done
}

# Odejmuje bitowo $2 od zmiennej o nazwie $1 (zakladamy wynik >= 0):
# a ^ b to roznica bez pozyczek, (~a & b) << 1 to pozyczki.
# Zlozonosc czasowa: O(log a)
_odejmij_od() {
    local -n _roznica=$1
    local odjemnik=$2 pozyczka
    while ((odjemnik != 0)); do
        pozyczka=$(((~_roznica & odjemnik) << 1))
        _roznica=$((_roznica ^ odjemnik))
        odjemnik=$pozyczka
    done
}

# ZAD-03A: a + b
dodaj_bitowo() {
    local wynik=$1
    _dodaj_do wynik "$2"
    echo "$wynik"
}

# ZAD-03B: a - b (a >= b)
odejmij_bitowo() {
    local wynik=$1
    _odejmij_od wynik "$2"
    echo "$wynik"
}

# ZAD-03C: a * b metoda "przesun i dodaj": dla kazdego ustawionego bitu k
# liczby b dodajemy a << k.
# Zlozonosc czasowa: O(log b * log(a*b))
pomnoz_bitowo() {
    local a=$1 b=$2 wynik=0
    while ((b != 0)); do
        if ((b & 1)); then
            _dodaj_do wynik "$a"
        fi
        ((a <<= 1))
        ((b >>= 1))
    done
    echo "$wynik"
}

# ZAD-03D: a // b (b > 0) jak dzielenie pisemne: znajdujemy najwieksze b << k
# nie wieksze od a, potem dla kolejnych k (malejaco) odejmujemy b << k od a,
# jesli sie miesci, i ustawiamy bit k ilorazu.
# Zlozonosc czasowa: O(log a * log a)
podziel_bitowo() {
    local reszta=$1 dzielnik=$2 iloraz=0 bit=1
    if ((reszta < dzielnik)); then
        echo 0
        return
    fi
    while (((dzielnik << 1) <= reszta)); do
        ((dzielnik <<= 1))
        ((bit <<= 1))
    done
    while ((bit != 0)); do
        if ((reszta >= dzielnik)); then
            _odejmij_od reszta "$dzielnik"
            ((iloraz |= bit))
        fi
        ((dzielnik >>= 1))
        ((bit >>= 1))
    done
    echo "$iloraz"
}

# Wczytuje a i b (kazda w osobnej linii) i wypisuje wynik funkcji $1.
_wczytaj_i_policz() {
    local a b
    read -r a
    read -r b
    "$1" "$a" "$b"
}

program_a() { _wczytaj_i_policz dodaj_bitowo; }
program_b() { _wczytaj_i_policz odejmij_bitowo; }
program_c() { _wczytaj_i_policz pomnoz_bitowo; }
program_d() { _wczytaj_i_policz podziel_bitowo; }

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

test_dodaj_bitowo() {
    assertEqual "$(dodaj_bitowo 0 0)" 0 $LINENO
    assertEqual "$(dodaj_bitowo 7 1)" 8 $LINENO
    assertEqual "$(dodaj_bitowo 1000000000 1000000000)" 2000000000 $LINENO
    sprawdz program_a $'2\n3' "5" $LINENO
}

test_odejmij_bitowo() {
    assertEqual "$(odejmij_bitowo 5 5)" 0 $LINENO
    assertEqual "$(odejmij_bitowo 1000 1)" 999 $LINENO
    assertEqual "$(odejmij_bitowo 1000000000 0)" 1000000000 $LINENO
    sprawdz program_b $'7\n5' "2" $LINENO
}

test_pomnoz_bitowo() {
    assertEqual "$(pomnoz_bitowo 0 5)" 0 $LINENO
    assertEqual "$(pomnoz_bitowo 123 456)" 56088 $LINENO
    assertEqual "$(pomnoz_bitowo 1000000 1000000)" 1000000000000 $LINENO
    sprawdz program_c $'4\n4' "16" $LINENO
}

test_podziel_bitowo() {
    assertEqual "$(podziel_bitowo 0 5)" 0 $LINENO
    assertEqual "$(podziel_bitowo 7 2)" 3 $LINENO
    assertEqual "$(podziel_bitowo 100 7)" 14 $LINENO
    assertEqual "$(podziel_bitowo 1 1)" 1 $LINENO
    assertEqual "$(podziel_bitowo 1000000000 3)" 333333333 $LINENO
    assertEqual "$(podziel_bitowo 999999999 1000000000)" 0 $LINENO
    sprawdz program_d $'9\n3' "3" $LINENO
}

main() {
    local podpunkt=${2:-}
    if [[ ${1:-} == --stdin ]]; then
        case ${podpunkt^^} in
            A) program_a ;;
            B) program_b ;;
            C) program_c ;;
            D) program_d ;;
            *)
                echo "Uzycie: bash zad03.sh --stdin A|B|C|D < dane.txt" >&2
                return 2
                ;;
        esac
    else
        test_dodaj_bitowo
        test_odejmij_bitowo
        test_pomnoz_bitowo
        test_podziel_bitowo
    fi
}

main "$@"
