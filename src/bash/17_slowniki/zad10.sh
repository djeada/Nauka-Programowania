# ZAD-10 — Znalezienie anagramów w tekście (grupy)
# 
# **Poziom:** ★★☆
# **Tagi:** `dict`, `anagramy`, `string`
# 
# ### Treść
# 
# Wczytaj tekst. Znajdź grupy słów będących anagramami (ignoruj wielkość liter, słowa to tylko litery).
# Wypisz wynik jako listę list, np. `[['absurd', 'brudas'], ...]`.
# Do grup wypisuj tylko te klucze, które mają co najmniej 2 słowa.
# 
# ### Wejście
# 
# * 1 linia: tekst
# 
# ### Wyjście
# 
# * Lista list słów
# 
# ### Przykład
# 
# Wejście jak w treści zadania → wyjście:
# 
# ```
# [["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
# ```

# Uzycie:
#   bash zad10.sh                     - uruchamia testy
#   bash zad10.sh --stdin < dane.txt  - rozwiazuje zadanie dla danych ze stdin

# shellcheck shell=bash source=../assert.sh
source "$(dirname "${BASH_SOURCE[0]}")/../assert.sh"

# Zapisuje w zmiennej o nazwie $1 litery slowa $2 posortowane rosnaco
# (sortowanie przez wstawianie - slowa sa krotkie).
# Zlozonosc czasowa: O(d^2), d - dlugosc slowa
# Zlozonosc pamieciowa: O(d)
posortuj_litery() {
    local -n _posortowane=$1
    local slowo=$2 litera i j
    local -a litery=()
    for ((i = 0; i < ${#slowo}; i++)); do
        litera=${slowo:i:1}
        j=${#litery[@]}
        while ((j > 0)) && [[ ${litery[j - 1]} > $litera ]]; do
            litery[j]=${litery[j - 1]}
            ((j--))
        done
        litery[j]=$litera
    done
    printf -v _posortowane '%s' "${litery[@]}"
}

# Wypisuje grupy anagramow z tekstu $1 - kazda grupa (co najmniej 2 rozne
# slowa) w osobnej linii, albo "Brak anagramów".
# Slownik: posortowane litery slowa -> slowa z tymi literami. Kolejnosc kluczy
# (pierwszych wystapien grup) trzymamy w osobnej tablicy indeksowanej.
# Zlozonosc czasowa: O(n * d^2)
# Zlozonosc pamieciowa: O(n)
znajdz_anagramy() {
    local tekst=${1,,} slowo klucz znaleziono=0
    local -a slowa kolejnosc_grup=()
    local -A grupy=() widziane=()
    tekst=${tekst//[^[:alpha:]]/ }
    read -ra slowa <<<"$tekst"

    for slowo in "${slowa[@]}"; do
        # Powtorzone slowo liczy sie raz
        if [[ -n ${widziane[$slowo]+x} ]]; then
            continue
        fi
        widziane[$slowo]=1
        posortuj_litery klucz "$slowo"
        if [[ -z ${grupy[$klucz]+x} ]]; then
            kolejnosc_grup+=("$klucz")
            grupy[$klucz]=$slowo
        else
            grupy[$klucz]+=" $slowo"
        fi
    done

    for klucz in "${kolejnosc_grup[@]}"; do
        if [[ ${grupy[$klucz]} == *" "* ]]; then
            echo "${grupy[$klucz]}"
            znaleziono=1
        fi
    done
    if ((!znaleziono)); then
        echo "Brak anagramów"
    fi
}

program() {
    local tekst
    IFS= read -r tekst
    znajdz_anagramy "$tekst"
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

test_posortuj_litery() {
    local wynik
    posortuj_litery wynik "brudas"
    assertEqual "$wynik" "abdrsu" $LINENO
    posortuj_litery wynik "a"
    assertEqual "$wynik" "a" $LINENO
}

test_znajdz_anagramy() {
    assertEqual "$(znajdz_anagramy "Ala ma kota")" "Brak anagramów" $LINENO
    assertEqual "$(znajdz_anagramy "kot kot KOT")" "Brak anagramów" $LINENO
    assertEqual "$(znajdz_anagramy "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. \
Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz.")" \
        $'absurd brudas\ntyran narty\nbandzior zbrodnia\nburza arbuz\ngaleria alergia' $LINENO
    assertEqual "$(znajdz_anagramy "kto tok kot; ok")" "kto tok kot" $LINENO
    sprawdz program "Tyran Brudas kupił narty. To absurd! Arbuz i burza." \
        $'tyran narty\nbrudas absurd\narbuz burza' $LINENO
}

main() {
    if [[ ${1:-} == --stdin ]]; then
        program
    else
        test_posortuj_litery
        test_znajdz_anagramy
    fi
}

main "$@"
