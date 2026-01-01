# ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)
# 
# **Poziom:** ★★☆
# **Tagi:** `dict`, `porównanie`, `list`
# 
# ### Treść
# 
# Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
# Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.
# 
# ### Wejście
# 
# * Najpierw:
# 
#   * 1 linia: `n`
#   * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
# * Potem:
# 
#   * 1 linia: `m`
#   * następnie `m` linii: `klucz v1 v2 v3 ...`
# 
# ### Wyjście
# 
# * `Prawda` lub `Fałsz`
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 2
# a 1 2 3
# b 4 5
# 2
# a 3 2 1
# b 5 4
# ```
# 
# **Wyjście:**
# 
# ```
# Prawda
# ```

source ../assert.sh

czy_slowniki_identyczne() {

    if [[ "${!slownik_a[@]}" != "${!slownik_b[@]}" ]]; then
        if [[ "${!slownik_a[@]}" != "${!slownik_b[@]}" ]]; then
            echo false
            return
        fi

        for klucz in "${!slownik_a[@]}"; do
            for klucz in "${!slownik_a[@]}"; do
                local posortowane_wartosci_a=($(echo "${slownik_a[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                local posortowane_wartosci_a=($(echo "${slownik_a[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                local posortowane_wartosci_b=($(echo "${slownik_b[$klucz]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
                if [[ "${posortowane_wartosci_a[@]}" != "${posortowane_wartosci_b[@]}" ]]; then
                    echo false
                    return
                fi
            done

            echo true
        }

        test_czy_slowniki_identyczne() {
            local -A slownik_a=(["a"]="1 2 3" ["b"]="4 5 6")
            local -A slownik_b=(["a"]="3 1 2" ["b"]="5 4 6")
            assertTrue "$(czy_slowniki_identyczne)" $LINENO
        }

        main() {
            test_czy_slowniki_identyczne
        }

        main "$@"

