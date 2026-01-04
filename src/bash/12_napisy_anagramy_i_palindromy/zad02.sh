# ZAD-02 — Wszystkie permutacje słowa
#
# **Poziom:** ★★☆
# **Tagi:** `rekurencja`, `permutacje`, `backtracking`
#
# ### Treść
#
# Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.
#
# ### Wejście
#
# * 1. linia: słowo (litery nie powtarzają się)
#
# ### Wyjście
#
# Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# abc
# ```
#
# **Wyjście:**
#
# ```
# abc
# acb
# bac
# bca
# cab
# cba
# ```
#
# ### Uwagi o formatowaniu
#
# * Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.
source ../assert.sh

# Funkcja generujaca wszystkie permutacje napisu (rekurencyjnie)
# Zlozonosc czasowa: O(n!), gdzie n to dlugosc napisu
# Zlozonosc pamieciowa: O(n!)
permutacje() {
    local napis=$1

    # Przypadek bazowy: slowo jednoznakowe
    if [ ${#napis} -eq 1 ]; then
        echo "$napis"
        return
    fi

    local permutacje=()

    # Dla kazdego znaku generuj permutacje pozostalych znakow
    for ((i = 0; i < ${#napis}; i++)); do
        for permutacja in $(permutacje ${napis:0:$i}${napis:$((i + 1)):${#napis}}); do
            local permutacja="${napis:$i:1}$permutacja"
            if [[ ! " ${permutacje[@]} " =~ " $permutacja " ]] && [ ${#permutacja} -eq ${#napis} ]; then
                permutacje+=("$permutacja")
            fi
        done
    done

    echo "${permutacje[@]}"
}

test_permutacje() {
    local wynik=($(permutacje "abc"))
    local oczekiwane=(abc acb bac bca cab cba)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_permutacje
}

main "$@"
