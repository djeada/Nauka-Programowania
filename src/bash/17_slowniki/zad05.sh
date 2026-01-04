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
najlepszy_pracownik() {
    local transakcje=($1)
    local -A lista_pracownikow=()

    for transakcja in ${transakcje[@]}; do
        local pracownik="$(echo $transakcja | cut -d' ' -f1) $(echo $transakcja | cut -d' ' -f2)"
        local zysk="$(echo $transakcja | cut -d' ' -f3)"

        if [[ -z ${lista_pracownikow[$pracownik]} ]]; then
            lista_pracownikow[$pracownik]=$zysk
        else

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
