# ZAD-07 — Powtarzające się podnapisy
#
# **Poziom:** ★★★
# **Tagi:** `string`, `substrings`, `count`
#
# ### Treść
#
# Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.
#
# ### Wejście
#
# * 1 linia: napis `S`
#
# ### Wyjście
#
# * 1 linia: lista napisów — wszystkie powtarzające się podnapisy
#
# ### Przykład
#
# **Wejście:**
#
# ```
# pythonpython
# ```
#
# **Wyjście:**
#
# ```
# ['python']
# ```
#
# ### Uwagi
#
# * Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

source ../assert.sh

# Znajduje wszystkie powtarzające się podnapisy.
# Złożoność czasowa: O(n^3), gdzie n to długość napisu
# Złożoność pamięciowa: O(n^2)
powtarzajace_podnapisy() {
    local napis="$1"
    local n=${#napis}
    declare -A widziane
    declare -A powtorzone
    
    # Generuj wszystkie podnapisy
    for ((i=0; i<n; i++)); do
        for ((j=i+1; j<=n; j++)); do
            local podnapis="${napis:$i:$((j-i))}"
            if [ -n "$podnapis" ]; then
                if [ "${widziane[$podnapis]}" = "1" ]; then
                    powtorzone[$podnapis]=1
                else
                    widziane[$podnapis]=1
                fi
            fi
        done
    done
    
    # Wypisz unikalne powtarzające się podnapisy
    echo "${!powtorzone[@]}"
}

test_powtarzajace_podnapisy() {
    local wynik=($(powtarzajace_podnapisy "pythonpython"))
    # Powinno zawierać przynajmniej "python"
    [[ " ${wynik[*]} " =~ " python " ]] || exit 1
}

main() {
    test_powtarzajace_podnapisy
}

main "$@"
