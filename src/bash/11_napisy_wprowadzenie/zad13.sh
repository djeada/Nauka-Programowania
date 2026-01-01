# ZAD-13 — Znaki na indeksach będących liczbami pierwszymi
# 
# **Poziom:** ★☆☆
# **Tagi:** `liczby pierwsze`, `indeksy`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.
# 
# ### Wejście
# 
# * 1. linia: napis
# 
# ### Wyjście
# 
# * 1. linia: lista znaków, np. `['o', 'ń']`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Słoń
# ```
# 
# **Wyjście:**
# 
# ```
# ['o', 'ń']
# ```
# 
# ### Uwagi
# 
# * Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

source ../assert.sh

srednia_dlugosc() {

    local zdanie="$1"
    local licznik=0
    local calkowita_dlugosc=0

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                local licznik=$((licznik + 1))
                local calkowita_dlugosc=$(( calkowita_dlugosc + ${#slowo} ))
            fi
        done

        echo $(bc -l <<< "scale=0; $calkowita_dlugosc/$licznik")
    }

    test1() {
        local zdanie="Ile to   ma :  slow w swoim zdaniu na   koniec?"
        local wynik=3
        assertEqual "$(srednia_dlugosc "$zdanie")" "$wynik" $LINENO
    }

    test2() {
        local zdanie="Kaczka lubi wiosne."
        local wynik=5
        assertEqual "$(srednia_dlugosc "$zdanie")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

