# ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)
#
# **Poziom:** ★★★
# **Tagi:** `substring`, `palindrom`, `unikalność`
#
# ### Treść
#
# Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków, spełniające warunek „wyjątkowości”:
#
# 1. wszystkie znaki są identyczne (np. `aaa`), **albo**
# 2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).
#
# Pojedynczy znak też jest wyjątkowym palindromem.
#
# ### Wejście
#
# * 1. linia: słowo (litery)
#
# ### Wyjście
#
# Każdy unikalny wyjątkowy palindrom w osobnej linii.
# Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki (po jednej linii na znak).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# xxyxx
# ```
#
# **Wyjście:**
#
# ```
# x
# xx
# xxx
# xxyxx
# y
# yxy
# ```
#
# ### Uwagi o formatowaniu
#
# * Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach wypisz raz).
# * Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście (łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.
source ../assert.sh

# Funkcja sprawdzajaca czy slowo jest wyjatkowym palindromem
# Zlozonosc czasowa: O(n), gdzie n to dlugosc slowa
# Zlozonosc pamieciowa: O(n)
wyjatkowy_palindrom() {
    local slowo="$1"

    # Pojedynczy znak jest wyjatkowym palindromem
    if [ ${#slowo} -eq 1 ]; then
        echo true
        return
    fi

    # Jesli dlugosc nieparzysta, usun srodkowy znak
    local sprawdzane="$slowo"
    if [ $((${#slowo} % 2)) -eq 1 ]; then
        local srodek=$((${#slowo} / 2))
        sprawdzane="${slowo:0:$srodek}${slowo:$((srodek + 1)):$((${#slowo} - $srodek - 1))}"
    fi

    # Sprawdz czy wszystkie znaki sa identyczne
    local pierwszy="${sprawdzane:0:1}"
    for ((i = 1; i < ${#sprawdzane}; i++)); do
        if [ "$pierwszy" != "${sprawdzane:$i:1}" ]; then
            echo false
            return
        fi
    done

    echo true
}

# Funkcja znajdujaca wszystkie wyjatkowe palindromy w slowie
# Zlozonosc czasowa: O(n^3), gdzie n to dlugosc slowa
# Zlozonosc pamieciowa: O(n^2)
wyjatkowe_palindromy() {
    local slowo="$1"

    if [ ${#slowo} -eq 1 ]; then
        echo "$slowo"
        return
    fi

    local wynik=()

    # Sprawdz wszystkie podnapisy
    for ((i = 0; i < ${#slowo}; i++)); do
        for ((j = 1; j <= ${#slowo} - i; j++)); do
            local podnapis="${slowo:$i:$j}"
            if [ "$(wyjatkowy_palindrom "$podnapis")" == "true" ]; then
                # Dodaj tylko jesli jeszcze nie ma w wyniku
                if ! [[ " ${wynik[@]} " =~ " $podnapis " ]]; then
                    wynik+=("$podnapis")
                fi
            fi
        done
    done

    echo "${wynik[@]}"
}

test_wyjatkowe_palindromy() {
    local wynik=($(wyjatkowe_palindromy "abc"))
    local oczekiwane=(a b c)
    assertArrayEqual wynik oczekiwane $LINENO

    local wynik=($(wyjatkowe_palindromy "xxxx"))
    local oczekiwane=(x xx xxx xxxx)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_wyjatkowe_palindromy
}

main "$@"
