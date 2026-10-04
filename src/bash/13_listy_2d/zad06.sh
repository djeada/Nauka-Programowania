# ZAD-06 — Scalanie przedziałów
#
# **Poziom:** ★★☆
# **Tagi:** `sortowanie`, `przedziały`, `algorytmy`
#
# ### Treść
#
# Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.
#
# ### Wejście
#
# * 1. linia: `n`
# * następnie `n` linii: `a_i b_i`
#
# ### Wyjście
#
# * Każdy scalony przedział w osobnej linii: `a b`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 23 67
# 23 53
# 45 88
# 77 88
# 10 22
# 11 12
# 42 45
# ```
#
# **Wyjście:**
#
# ```
# 10 22
# 23 88
# ```
#
# ### Uwagi
#
# * Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

# Uzycie:
#   bash zad06.sh                     - uruchamia testy
#   bash zad06.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Scala nachodzace na siebie przedzialy (argumenty: a1 b1 a2 b2 ...) i wypisuje
# wynikowe przedzialy rosnaco wedlug poczatku, kazdy w osobnej linii.
#
# Sortowanie: tablice indeksowane w Bashu sa rzadkie, a "${!tablica[@]}" zwraca
# indeksy rosnaco. Wystarczy wiec zapisac dla kazdego poczatku (przesunietego
# tak, aby indeks byl nieujemny) najdalszy koniec i przejsc po indeksach.
# Zlozonosc czasowa: O(n log n) (w praktyce; wstawianie do tablicy rzadkiej)
# Zlozonosc pamieciowa: O(n)
scal_przedzialy() {
    local -a poczatki=() konce=() najdalszy_koniec=()
    local przesuniecie=0 i a b indeks
    while (($# >= 2)); do
        poczatki+=("$1")
        konce+=("$2")
        shift 2
    done

    for a in "${poczatki[@]}"; do
        if ((a < -przesuniecie)); then
            przesuniecie=$((-a))
        fi
    done

    for i in "${!poczatki[@]}"; do
        indeks=$((poczatki[i] + przesuniecie))
        b=${konce[i]}
        if [[ -z ${najdalszy_koniec[indeks]:-} ]] || ((b > najdalszy_koniec[indeks])); then
            najdalszy_koniec[indeks]=$b
        fi
    done

    local biezacy_poczatek="" biezacy_koniec=""
    for indeks in "${!najdalszy_koniec[@]}"; do
        a=$((indeks - przesuniecie))
        b=${najdalszy_koniec[indeks]}
        if [[ -z $biezacy_poczatek ]]; then
            biezacy_poczatek=$a
            biezacy_koniec=$b
        elif ((a <= biezacy_koniec)); then
            # Przedzialy nachodza na siebie (lub stykaja sie koncami) - scalamy
            if ((b > biezacy_koniec)); then
                biezacy_koniec=$b
            fi
        else
            echo "$biezacy_poczatek $biezacy_koniec"
            biezacy_poczatek=$a
            biezacy_koniec=$b
        fi
    done

    if [[ -n $biezacy_poczatek ]]; then
        echo "$biezacy_poczatek $biezacy_koniec"
    fi
}

# Wczytuje n oraz n linii "a b" ze stdin i wypisuje scalone przedzialy.
program() {
    local n i a b
    local -a przedzialy=()
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r a b
        przedzialy+=("$a" "$b")
    done
    scal_przedzialy "${przedzialy[@]}"
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

test_scal_przedzialy() {
    assertEqual "$(scal_przedzialy 1 3 2 6 8 10 15 18)" $'1 6\n8 10\n15 18' $LINENO
    # Przedzialy stykajace sie koncami scalamy
    assertEqual "$(scal_przedzialy 3 5 1 3)" "1 5" $LINENO
    # Przedzial zawarty w innym
    assertEqual "$(scal_przedzialy 1 10 2 3 4 5)" "1 10" $LINENO
    # Liczby ujemne
    assertEqual "$(scal_przedzialy 4 6 -3 2 -5 -1)" $'-5 2\n4 6' $LINENO
    assertEqual "$(scal_przedzialy 7 7)" "7 7" $LINENO
}

test_program() {
    sprawdz program $'7\n23 67\n23 53\n45 88\n77 88\n10 22\n11 12\n42 45' $'10 22\n23 88' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_scal_przedzialy
        test_program
    fi
}

main "$@"
