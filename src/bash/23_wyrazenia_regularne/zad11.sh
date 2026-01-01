# ZAD-11 — Nazwa pliku bez rozszerzenia
#
# **Poziom:** ★★☆
# **Tagi:** `regex`, `string`, `ścieżki`
#
# ### Treść
#
# Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku (bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą nazwę bez rozszerzenia.
#
# Ścieżka może zawierać separator `\` lub `/`.
#
# ### Wejście
#
# Jedna linia:
#
# * `sciezka`
#
# ### Wyjście
#
# Jedna linia:
#
# * `nazwa_pliku_bez_rozszerzenia`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\my-long\path_directory\file.html
# ```
#
# **Wyjście:**
#
# ```
# file
# ```

source ../assert.sh

# Wyciąga nazwę pliku ze ścieżki (bez rozszerzenia i ścieżki).
# Złożoność czasowa: O(n), gdzie n to długość ścieżki
# Złożoność pamięciowa: O(n)
nazwa_pliku() {
    local sciezka="$1"
    sciezka="${sciezka//\\//}"
    sciezka="${sciezka%/}"
    sciezka="${sciezka#/}"
    sciezka="${sciezka##*/}"

    while [[ "$sciezka" = *.* ]]; do
        sciezka="${sciezka%.*}"
    done

    echo "$sciezka"
}

test_nazwa_pliku() {
    assertEqual $(nazwa_pliku 'C:\\Windows\\explorer.exe') "explorer" $LINENO
    assertEqual $(nazwa_pliku '/home/user/var/log/syslog') "syslog" $LINENO
    assertEqual $(nazwa_pliku 'test.jpg.png.mp3.mp5.html.txt') "test" $LINENO
    assertEqual $(nazwa_pliku 'test') "test" $LINENO
}

main() {
    test_nazwa_pliku
}

main "$@"
