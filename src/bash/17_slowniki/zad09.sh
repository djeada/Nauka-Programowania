# ZAD-09 — Znaki występujące co najmniej dwa razy
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`
# 
# ### Treść
# 
# Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.
# 
# ### Wejście
# 
# * 1 linia: napis
# 
# ### Wyjście
# 
# * 1 linia: wynikowy napis
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# aaabbbccc
# ```
# 
# **Wyjście:**
# 
# ```
# abc
# ```
znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="$1"
    local -A histogram=()
    for ((i = 0; i < ${#napis}; i++)); do
        ((histogram["${napis:$i:1}"]++))
    done
    for litera in ${!histogram[@]}; do
        if [[ "${histogram[$litera]}" -gt 1 ]]; then
            echo "$litera"
        fi
    done
}

test_znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="ababab"
    local wynik=($(znaki_powtarzajace_sie_wiecej_niz_raz "$napis"))
    local oczekiwane=(a b)
    assertElementsEqual wynik oczekiwane $LINENO

# Funkcja do zaimplementowania
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
funkcja_glowna() {
    # TODO: Implementacja funkcjonalnosci opisanej w docstringu
    echo "Funkcjonalnosc wymaga pelnej implementacji"
}

main() {
    funkcja_glowna
}

main "$@"
