# ZAD-06 — Statystyki pliku tekstowego
#
# **Poziom:** ★★☆
# **Tagi:** `files`, `stats`, `dict`, `regex`
#
# ### Treść
#
# Otrzymujesz ścieżkę do pliku tekstowego. Oblicz:
#
# a) liczbę wierszy,
# b) łączną liczbę słów (słowa = ciągi liter),
# c) średnią długość wiersza (w znakach),
# d) średnią liczbę słów na wiersz,
# e) częstość występowania słów (słownik).
#
# ### Wejście
#
# * 1 linia: `file_path`
#
# ### Wyjście
#
# 5 elementów w tej kolejności:
#
# 1. liczba wierszy
# 2. liczba słów
# 3. średnia długość wiersza
# 4. średnia liczba słów na wiersz
# 5. słownik częstości słów
#
# Każdy element wypisz w osobnej linii.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# C:\Users\Username\Documents\tekst.txt
# ```
#
# **Wyjście:**
#
# ```
# 4
# 12
# 17.75
# 3.0
# {'ala': 2, 'ma': 2, 'kota': 1, 'kot': 1, 'na': 1, 'imię': 1, 'filemon': 1, 'filemona': 1, 'lubi': 2, 'mleko': 1}
# ```
#
# ### Uwagi o formatowaniu
#
# * Jeżeli ujednolicisz wielkość liter — w słowniku używaj małych liter (jak w przykładzie).
# * Interpunkcję traktuj jako separator (usuń ją przy wyznaczaniu słów).
source ../assert.sh

# Funkcja wczytujaca plik
# Zlozonosc czasowa: O(n), gdzie n to liczba wierszy
# Zlozonosc pamieciowa: O(n)
wczytaj_plik() {
    local plik="$1"
    local lista=()
    while read -r wiersz; do
        lista+=("$wiersz")
    done <"$plik"
    printf '%s\n' "${lista[@]}"
}

# Funkcja liczaca wiersze
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(1)
liczba_wierszy() {
    local plik="$1"
    wc -l <"$plik"
}

# Funkcja rozdzielająca zdanie na slowa
# Zlozonosc czasowa: O(n), gdzie n to liczba znakow
# Zlozonosc pamieciowa: O(m), gdzie m to liczba slow
podziel_zdanie_na_slowa() {
    local zdanie="$1"
    local lista=()

    # Usuniecie interpunkcji i normalizacja
    zdanie=$(echo "$zdanie" | sed -r 's/[''".,:;!?\\@\<\>\/]+/ /g' | tr -s ' ')
    zdanie=$(echo "$zdanie" | sed -r 's/[-]+//g')
    lista_slow=($zdanie)

    for slowo in "${lista_slow[@]}"; do
        # Sprawdzenie czy slowo zawiera tylko znaki alfanumeryczne i nie jest liczba
        if [[ "$slowo" =~ ^[[:alnum:]]+$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            lista+=("$slowo")
        fi
    done

    printf '%s\n' "${lista[@]}"
}

# Funkcja liczaca slowa w pliku
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(n*m)
liczba_slow() {
    local plik="$1"
    tresc=($(wczytaj_plik "$plik"))
    local licznik=0
    for wiersz in "${tresc[@]}"; do
        slowa=($(podziel_zdanie_na_slowa "$wiersz"))
        licznik=$((licznik + ${#slowa[@]}))
    done
    echo "$licznik"
}

# Funkcja obliczajaca srednia dlugosc wiersza
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(1)
srednia_dlugosc_wiersza() {
    local plik="$1"
    local suma_dlugosci_wierszy=$(awk '{print length}' "$plik" | awk '{s+=$1} END {print s}')
    echo "scale=2; $suma_dlugosci_wierszy / $(liczba_wierszy "$plik")" | bc
}

# Funkcja obliczajaca srednia liczbe slow na wiersz
# Zlozonosc czasowa: O(n*m)
# Zlozonosc pamieciowa: O(1)
srednia_liczba_slow_na_wiersz() {
    local plik="$1"
    echo "scale=2; $(liczba_slow "$plik") / $(liczba_wierszy "$plik")" | bc
}

# Funkcja liczaca czestotliwosc slow
# Zlozonosc czasowa: O(n*m log m)
# Zlozonosc pamieciowa: O(m)
czestosc_slow() {
    local plik="$1"
    tresc=($(wczytaj_plik "$plik"))
    local histogram=()

    for wiersz in "${tresc[@]}"; do
        slowa=($(podziel_zdanie_na_slowa "$wiersz"))
        histogram+=(${slowa[@]})
    done

    for slowo in "${histogram[@]}"; do
        echo "$slowo" | awk '{print tolower($0)}'
    done | sort | uniq -c | awk '{print $2, $1}'
}

test_statystyki() {
    mkdir -p 'test'

    local plik='test/test.txt'
    touch "$plik"

    echo -e 'Hej \nThis is an example of a simple ASCII text file stored on a Web server. Note that it has a file\nextension of \".txt\".\n\nAlthough such files may contains some basic layout formatting, such as paragraphs, there is no\nsupport for the text to have attributes, such as bolding.\n\nText files can contain Hypertext Mark-up codes but these will not be interpreted by the \nbrowser. For example, if the following characters <strong>hello</strong> were typed into an\n"html" file then the word "hello" would be shown in bold.' >'test/test.txt'

    assertEqual "$(liczba_wierszy "$plik")" "10" $LINENO
    assertEqual "$(liczba_slow "$plik")" "92" $LINENO
}

main() {
    test_statystyki
}

main "$@"
