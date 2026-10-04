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

# Dopisuje inicjały w nowym wierszu na końcu każdego pliku .txt w folderze
# (i jego podfolderach).
dodaj_inicjaly_do_plikow_w_folderze() {
    local folder=$1
    local inicjaly=$2
    local plik

    while IFS= read -r -d '' plik; do
        # jeśli plik nie kończy się znakiem nowej linii, najpierw go dopisujemy
        if [[ -s $plik && -n $(tail -c 1 "$plik") ]]; then
            echo >>"$plik"
        fi
        echo "$inicjaly" >>"$plik"
    done < <(find "$folder" -type f -name "*.txt" -print0)
}

# Usuwa środkowy wiersz (o indeksie liczba_wierszy / 2, licząc od 0) z każdego
# pliku .csv w folderze (i jego podfolderach).
usun_srodkowy_wiersz_z_plikow_w_folderze() {
    local folder=$1
    local plik
    local liczba_wierszy

    while IFS= read -r -d '' plik; do
        liczba_wierszy=$(wc -l <"$plik")
        if ((liczba_wierszy > 0)); then
            sed -i "$((liczba_wierszy / 2 + 1))d" "$plik"
        fi
    done < <(find "$folder" -type f -name "*.csv" -print0)
}

test_dodaj_inicjaly_do_plikow_w_folderze() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    local sciezki=('test/test1/plik1.txt' 'test/test1/plik2.txt' 'test/test2/plik3.txt' 'test/test2/plik4.txt')
    local tresc='testowy tekst'

    for plik in "${sciezki[@]}"; do
        echo "$tresc" >"$plik"
    done

    local inicjaly='A.D.'
    dodaj_inicjaly_do_plikow_w_folderze 'test' "$inicjaly"

    local oczekiwane=('testowy tekst' 'A.D.')
    local tresc_pliku
    for plik in "${sciezki[@]}"; do
        mapfile -t tresc_pliku <"$plik"
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done

    rm -rf 'test'
}

test_usun_srodkowy_wiersz_z_plikow_w_folderze() {

    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    local sciezki=('test/test1/plik1.csv' 'test/test1/plik2.csv' 'test/test2/plik3.csv' 'test/test2/plik4.csv')

    for plik in "${sciezki[@]}"; do
        printf 'test1; test2;\ntest3; test4;\ntest5; test6;\n' >"$plik"
    done

    usun_srodkowy_wiersz_z_plikow_w_folderze 'test'

    local oczekiwane=('test1; test2;' 'test5; test6;')
    local tresc_pliku
    for plik in "${sciezki[@]}"; do
        mapfile -t tresc_pliku <"$plik"
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done

    rm -rf 'test'
}

main() {
    # Testy tworzą i usuwają pliki — pracuj w katalogu tymczasowym, nie w repozytorium.
    local katalog_roboczy
    katalog_roboczy=$(mktemp -d)
    trap 'rm -rf "$katalog_roboczy"' EXIT
    cd "$katalog_roboczy" || exit 1
    test_dodaj_inicjaly_do_plikow_w_folderze
    test_usun_srodkowy_wiersz_z_plikow_w_folderze
}

main "$@"
