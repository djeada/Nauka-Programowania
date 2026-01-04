# ZAD-05 — Posortuj adresy IP z pliku
#
# **Poziom:** ★☆☆
# **Tagi:** `files`, `sort`, `list`
#
# ### Treść
#
# Otrzymujesz ścieżkę do pliku tekstowego, w którym w każdej linii znajduje się jeden adres IP. Wczytaj wszystkie adresy, posortuj je **alfabetycznie** i wypisz jako listę.
#
# ### Wejście
#
# * 1 linia: `file_path`
#
# ### Wyjście
#
# * 1 linia: lista adresów IP jako napisy, np. `['10.0.0.1', ...]`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents\adresy_ip.txt
# ```
#
# **Wyjście:**
#
# ```
# ['10.0.0.1', '172.16.0.5', '192.168.1.10', '192.168.1.2']
# ```
source ../assert.sh

sortuj_adresy_ip() {
    sort -t . -g -k1,1 -k2,2 -k3,3 -k4,4 $1
}

test_sortuj_adresy_ip() {

    mkdir -p 'test'
    mkdir -p 'test'

    local plik='test/test.txt'
    local plik='test/test.txt'
    touch $plik
    echo "123.4.245.23" >$plik
    echo "104.244.253.29" >>$plik
    echo "1.198.3.93" >>$plik
    echo "32.183.93.40" >>$plik
    echo "104.30.244.2" >>$plik
    echo "104.244.4.1" >>$plik

    IFS=$'\n'
    IFS=$'\n'
    wynik=($(sortuj_adresy_ip 'test/test.txt'))

    local oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.244.4.1 104.244.253.29 123.4.245.23)
    local oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.244.4.1 104.244.253.29 123.4.245.23)
    assertArrayEqual wynik oczekiwane $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_sortuj_adresy_ip
}

main "$@"
