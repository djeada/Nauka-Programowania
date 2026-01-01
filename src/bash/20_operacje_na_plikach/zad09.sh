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

usun_pliki_wieksze_niz_10k() {
    local folder=$1
    find $folder -type f -size +10k-exec rm -f {} \;
}

test_usun_pliki_wieksze_niz() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    sciezki=('test/test1/test1.txt' 'test/test1/test2.txt' 'test/test2/test1.txt' 'test/test2/test2.txt')
    sciezki=('test/test1/test1.txt' 'test/test1/test2.txt' 'test/test2/test1.txt' 'test/test2/test2.txt')
    for plik in ${sciezki[@]}; do
        touch $plik
        for i in {1..10000}; do
            echo 'test' >> $plik
        done
    done

    usun_pliki_wieksze_niz_10k 'test'
    usun_pliki_wieksze_niz_10k 'test'

    for plik in ${sciezki[@]}; do
        for plik in ${sciezki[@]}; do
            assertTrue $(if [[ -f $plik ]]; then echo "true"; else echo "false"; fi) $LINENO
        done

        rm -rf 'test'
        rm -rf 'test'

    }

    main() {
        test_usun_pliki_wieksze_niz
    }

    main "$@"

