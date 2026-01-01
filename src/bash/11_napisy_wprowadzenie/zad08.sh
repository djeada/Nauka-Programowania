# ZAD-08 — Wypisz pionowo słowa ze zdania
# 
# **Poziom:** ★☆☆
# **Tagi:** `split`, `string`
# 
# ### Treść
# 
# Wczytaj zdanie, podziel na słowa i wypisz każde słowo w osobnej linii. Interpunkcja nie jest słowem.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * wiele linii: słowa w kolejności występowania
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Ala ma kota
# ```
# 
# **Wyjście:**
# 
# ```
# Ala
# ma
# kota
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

    main() {
        local zdanie="We think in generalities, but we live in details."
        wypisz_slowa "$zdanie"
    }

    main "$@"

