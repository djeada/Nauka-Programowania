# ZAD-11 — Zamień miejscami treści dwóch plików
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `swap`, `read/write`
#
# ### Treść
#
# Otrzymujesz ścieżki do dwóch plików. Zamień ich treści miejscami:
#
# * plik A ma mieć dawną treść pliku B,
# * plik B ma mieć dawną treść pliku A.
#
# ### Wejście
#
# * 1 linia: `file_A`
# * 2 linia: `file_B`
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
# C:\Users\Username\Documents\plik1.txt
# C:\Users\Username\Documents\plik2.txt
# ```
#
# **Wyjście:**
# *(brak)*

source ../assert.sh

podmien_tresci() {
    local plik_1="$1"
    local plik_2="$2"
    local tmp="$(mktemp)"
    cat "$plik_1" >"$tmp"
    cat "$plik_2" >"$plik_1"
    cat "$tmp" >"$plik_2"
    rm "$tmp"
}

test_podmien_tresci() {

    mkdir -p 'test'
    mkdir -p 'test'

    echo 'test1' >'test/plik_1'
    echo 'test1' >'test/plik_1'
    echo 'test2' >'test/plik_2'

    podmien_tresci 'test/plik_1' 'test/plik_2'
    podmien_tresci 'test/plik_1' 'test/plik_2'

    assertEqual $(cat 'test/plik_1') 'test2' $LINENO
    assertEqual $(cat 'test/plik_1') 'test2' $LINENO
    assertEqual $(cat 'test/plik_2') 'test1' $LINENO

    rm -rf 'test'
    rm -rf 'test'

}

main() {
    test_podmien_tresci
}

main "$@"
