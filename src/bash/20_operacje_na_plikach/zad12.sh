# ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `move`, `csv`, `recursive`
#
# ### Treść
#
# Otrzymujesz ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki `.csv` z folderu źródłowego **i wszystkich jego podfolderów** do folderu docelowego.
#
# ### Wejście
#
# * 1 linia: `src_folder`
# * 2 linia: `dst_folder`
#
# ### Wyjście
#
# Brak.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Projekty
# D:\Dane\CSV
# ```
#
# **Wyjście:**
# *(brak)*
#
# ### Uwagi
#
# * Jeśli w folderze docelowym istnieje już plik o tej samej nazwie, zadanie wymaga zdefiniowania zachowania (np. zmiana nazwy / pominięcie) — jeśli sprawdzarka tego nie doprecyzowuje, przyjmij jedną spójną strategię w całym rozwiązaniu.
source ../assert.sh

przenies_pliki() {
    local -r from="$1"
    local -r to="$2"
    local -r from_files=$(find "$from" -name "*.csv")

    for file in $from_files; do
        mv "$file" "$to"
    done
}

test_przenies_pliki() {

    mkdir -p 'test1/test1'
    mkdir -p 'test1/test1'
    mkdir -p 'test2/test2'

    sciezki=('test1/test1/test1.csv' 'test1/test1/test2.csv')
    sciezki=('test1/test1/test1.csv' 'test1/test1/test2.csv')
    for plik in ${sciezki[@]}; do
        touch $plik
    done

    przenies_pliki 'test1' 'test2'
    przenies_pliki 'test1' 'test2'

    assertTrue $(if [[ -f 'test2/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertTrue $(if [[ -f 'test2/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertTrue $(if [[ -f 'test2/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO

    rm -rf 'test1' 'test2'
    rm -rf 'test1' 'test2'

}

main() {
    test_przenies_pliki
}

main "$@"
