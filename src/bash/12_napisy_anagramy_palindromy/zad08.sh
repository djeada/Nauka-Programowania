# Tytul: Wyjatkowe palindromy.
# Tresc: Napisz program, ktory znajdzie wszystkie wyjatkowe palindromy, jakie mozna utworzyc ze znakow w slowie (bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.
# Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:
# 1. Wszystkie znaki sa identyczne, np. "xxx".
# 2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. "ccdcc".
# Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: "xxxx", powinna zostac zwrocona lista: ["x", "xx", "xxx", "xxxx"].

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
        local srodek=$(( ${#slowo} / 2 ))
        sprawdzane="${slowo:0:$srodek}${slowo:$((srodek+1)):$(( ${#slowo} - $srodek - 1 ))}"
    fi

    # Sprawdz czy wszystkie znaki sa identyczne
    local pierwszy="${sprawdzane:0:1}"
    for (( i=1; i<${#sprawdzane}; i++ )); do
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
wyjatkowe_palindromy(){
    local slowo="$1"

    if [ ${#slowo} -eq 1 ]; then
        echo "$slowo"
        return
    fi

    local wynik=()
    
    # Sprawdz wszystkie podnapisy
    for (( i=0; i<${#slowo}; i++ )); do
        for (( j=1; j<=${#slowo}-i; j++ )); do
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

test_wyjatkowe_palindromy(){
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
