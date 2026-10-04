# ZAD-05 — Pracownik z największym sumarycznym zyskiem
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `sumowanie`
# 
# ### Treść
# 
# Wczytaj `n` wpisów: `pracownik zysk`. Zsumuj zyski per pracownik i wypisz nazwę pracownika z największą sumą.
# (Jeśli remis, wybierz tego, który pierwszy osiągnął tę maksymalną sumę podczas przetwarzania.)
# 
# ### Wejście
# 
# * 1 linia: `n`
# * następnie `n` linii: `imie_i_nazwisko zysk`
# 
# ### Wyjście
# 
# * Jedna linia: `imie_i_nazwisko`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 5
# Barnaba_Barabash 120
# Jon_Snow 100
# Kira_Summer 300
# Barnaba_Barabash 200
# Bob_Marley 110
# ```
# 
# **Wyjście:**
# 
# ```
# Barnaba_Barabash
# ```

# Uzycie:
#   bash zad05.sh                     - uruchamia testy
#   bash zad05.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zwraca pracownika z najwiekszym sumarycznym zyskiem. Argumenty to kolejne
# pary: pracownik zysk pracownik zysk ...
# Sumy trzymamy w tablicy asocjacyjnej, a kolejnosc pierwszych wystapien
# w tablicy indeksowanej - przy remisie wygrywa pracownik, ktory pojawil sie
# na wejsciu wczesniej (dlatego zamieniamy tylko przy wiekszej sumie).
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
najlepszy_pracownik() {
    local -A suma=()
    local -a kolejnosc=()
    local pracownik najlepszy="" najwieksza_suma=0

    while (($# >= 2)); do
        if [[ -z ${suma[$1]+x} ]]; then
            kolejnosc+=("$1")
            suma[$1]=0
        fi
        suma[$1]=$((${suma[$1]} + $2))
        shift 2
    done

    for pracownik in "${kolejnosc[@]}"; do
        if [[ -z $najlepszy ]] || ((${suma[$pracownik]} > najwieksza_suma)); then
            najlepszy=$pracownik
            najwieksza_suma=${suma[$pracownik]}
        fi
    done

    echo "$najlepszy"
}

# Wczytuje n oraz n linii "pracownik zysk" i wypisuje najlepszego pracownika.
program() {
    local n i pracownik zysk
    local -a wpisy=()
    read -r n
    for ((i = 0; i < n; i++)); do
        read -r pracownik zysk
        wpisy+=("$pracownik" "$zysk")
    done
    najlepszy_pracownik "${wpisy[@]}"
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

test_najlepszy_pracownik() {
    # Remis 100:100 - wygrywa ten, kto wczesniej pojawil sie na wejsciu
    assertEqual "$(najlepszy_pracownik a 100 b 50 b 50)" "a" $LINENO
    assertEqual "$(najlepszy_pracownik b 50 a 100 b 50)" "b" $LINENO
    # Straty (ujemne zyski)
    assertEqual "$(najlepszy_pracownik a -5 b -3 a 1)" "b" $LINENO
    assertEqual "$(najlepszy_pracownik Jon_Snow 10 Kira_Summer 300 Jon_Snow 291)" "Jon_Snow" $LINENO
}

test_program() {
    sprawdz program $'5\nBarnaba_Barabash 120\nJon_Snow 100\nKira_Summer 300\nBarnaba_Barabash 200\nBob_Marley 110' \
        "Barnaba_Barabash" $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_najlepszy_pracownik
        test_program
    fi
}

main "$@"
