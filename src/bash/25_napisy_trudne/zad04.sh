# ZAD-04 — Wszystkie wystąpienia podnapisu
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `substring`, `find`
#
# ### Treść
#
# Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`, od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.
#
# Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się na pozycjach `0`, `1` i `2`.
#
# ### Wejście
#
# * 1. linia: napis `S`
# * 2. linia: wzorzec `W`
#
# ### Wyjście
#
# Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone pojedynczymi spacjami.
# Jeśli `W` nie występuje w `S`, wypisz `Brak`.
#
# ### Ograniczenia
#
# * `1 ≤ |S| ≤ 1000`
# * `1 ≤ |W| ≤ 100`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# abrakadabra
# abra
# ```
#
# **Wyjście:**
#
# ```
# 0 7
# ```
#
# ### Uwagi
#
# * Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do `len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak sprawdzałeś przedrostek w zadaniu ZAD-03.
# * W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.
export LC_ALL=C.UTF-8

wystapienia() {
    # Indeksy wszystkich (takze nachodzacych) wystapien wzorca w napisie.
    local napis=$1 wzorzec=$2 i wynik=""
    local m=${#wzorzec}
    for ((i = 0; i + m <= ${#napis}; i++)); do
        if [[ "${napis:i:m}" == "$wzorzec" ]]; then
            wynik+="${wynik:+ }$i"
        fi
    done
    echo "${wynik:-Brak}"
}

main() {
    local napis wzorzec
    IFS= read -r napis
    IFS= read -r wzorzec
    wystapienia "$napis" "$wzorzec"
}

main "$@"
