# ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `recursive`, `txt`, `csv`
#
# ### Treść
#
# Otrzymujesz ścieżkę do folderu. Wykonaj:
#
# a) dopisz swoje inicjały na końcu każdego pliku `.txt` w folderze i podfolderach,
# b) usuń **środkowy wiersz** z każdego pliku `.csv` w folderze i podfolderach
# (jeśli liczba wierszy jest parzysta — usuń **dolny z dwóch środkowych**).
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
# C:\Users\Username\Documents\Projekt
# ```
#
# **Wyjście:**
# *(brak)*

source ../assert.sh

dodaj_inicjaly_do_plikow_w_folderze() {
    local folder=$1
    local inicjaly=$2
    local pliki=$(find $folder -type f -name "*.txt")
    for plik in $pliki; do
        sed -i "s/^/$inicjaly /" $plik
    done
}

usun_srodkowy_wiersz_z_plikow_w_folderze() {
    local folder=$1
    local pliki=$(find $folder -type f -name "*.csv")
    for plik in $pliki; do
        sed -i '1d' $plik
    done
}

test_dodaj_inicjaly_do_plikow_w_folderze() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    local sciezki=('test/test1/plik1.txt' 'test/test1/plik2.txt' 'test/test2/plik3.txt' 'test/test2/plik4.txt')
    local sciezki=('test/test1/plik1.txt' 'test/test1/plik2.txt' 'test/test2/plik3.txt' 'test/test2/plik4.txt')
    local tresc='testowy tekst'

    for plik in ${sciezki[@]}; do
        echo $tresc >$plik
    done

    local inicjaly='A.D.'
    local inicjaly='A.D.'
    local dodaj_inicjaly_do_plikow_w_folderze 'test' $inicjaly

    IFS=$'\n'
    IFS=$'\n'
    local oczekiwane=('A.D.' 'testowy tekst')
    for plik in ${sciezki[@]}; do
        tresc_pliku=($(cat $plik))
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done
    unset IFS

    rm -rf 'test'
    rm -rf 'test'
}

test_usun_srodkowy_wiersz_z_plikow_w_folderze() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    local sciezki=('test/test1/plik1.csv' 'test/test1/plik2.csv' 'test/test2/plik3.csv' 'test/test2/plik4.csv')
    local sciezki=('test/test1/plik1.csv' 'test/test1/plik2.csv' 'test/test2/plik3.csv' 'test/test2/plik4.csv')
    local tresc='test1; test2;\ntest3; test4;\ntest5; test6;'

    for plik in ${sciezki[@]}; do
        echo $tresc >$plik
    done

    local usun_srodkowy_wiersz_z_plikow_w_folderze 'test'
    local usun_srodkowy_wiersz_z_plikow_w_folderze 'test'

    IFS=$'\n'
    IFS=$'\n'
    local oczekiwane=('test1; test2;\ntest5; test6;')
    for plik in ${sciezki[@]}; do
        tresc_pliku=($(cat $plik))
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_dodaj_inicjaly_do_plikow_w_folderze
    test_usun_srodkowy_wiersz_z_plikow_w_folderze
}

main "$@"
