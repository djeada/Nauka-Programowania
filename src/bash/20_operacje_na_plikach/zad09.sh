# ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `delete`, `size`, `recursive`
#
# ### Treść
#
# Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240 bajtów** w tym folderze i jego podfolderach.
#
# ### Wejście
#
# * 1 linia: `folder_path`
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
# C:\Users\Username\Documents\DoUsunięcia
# ```
#
# **Wyjście:**
# *(brak)*
source ../assert.sh

# Funkcja usuwająca pliki wieksze niz 10kB
# Zlozonosc czasowa: O(n), gdzie n to liczba plikow
# Zlozonosc pamieciowa: O(1)
usun_pliki_wieksze_niz_10k() {
    local katalog=$1

    for plik in "$katalog"/*; do
        if [ -f "$plik" ]; then
            local rozmiar=$(stat -f%z "$plik" 2>/dev/null || stat -c%s "$plik" 2>/dev/null)
            if [ "$rozmiar" -gt 10240 ]; then
                rm "$plik"
            fi
        fi
    done
}

test_usun_pliki_wieksze_niz() {
    mkdir -p 'test'

    # Tworzenie plikow testowych
    echo "maly plik" >'test/maly.txt'

    usun_pliki_wieksze_niz_10k 'test'

    # Sprawdzenie czy male pliki zostaly
    assertTrue $(if [[ -f 'test/maly.txt' ]]; then echo "true"; else echo "false"; fi) $LINENO

    rm -rf 'test'
}

main() {
    test_usun_pliki_wieksze_niz
}

main "$@"
