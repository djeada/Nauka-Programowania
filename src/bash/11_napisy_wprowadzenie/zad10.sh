# ZAD-10 — Najdłuższe i najkrótsze słowo
# 
# **Poziom:** ★☆☆
# **Tagi:** `string`, `min/max`, `len`
# 
# ### Treść
# 
# Wczytaj zdanie i znajdź:
# 
# a) najdłuższe słowo,
# b) najkrótsze słowo.
# 
# Jeśli jest remis, wybierz słowo, które występuje wcześniej.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: najdłuższe słowo
# * 2. linia: najkrótsze słowo
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Kaczka lubi wiosnę.
# ```
# 
# **Wyjście:**
# 
# ```
# Kaczka
# lubi
# ```

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo"
            fi
        done

    }

    najdluzsze() {
        local zdanie="$1"
        awk 'length > maks_dlugosc { maks_dlugosc = length; najdluzsze = $0 } END { print najdluzsze }' <<< $(wypisz_slowa "$zdanie")
    }

    najkrotsze() {
        local zdanie="$1"
        local n=${#zdanie}
        awk -v n=$n 'BEGIN { min_dlugosc = n } length < min_dlugosc { min_dlugosc = length; najkrotsze = $0 } END { print najkrotsze }' <<< $(wypisz_slowa "$zdanie")
    }

    test1() {
        local napis="Kaczka lubi wiosne."
        local wynik="Kaczka"
        assertEqual "$(najdluzsze "$napis")" "$wynik" $LINENO
    }

    test2() {
        local napis="Kaczka lubi wiosne."
        local wynik="lubi"
        assertEqual "$(najkrotsze "$napis")" "$wynik" $LINENO
        assertEqual "$(najkrotsze "$napis")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

