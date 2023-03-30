# Tytul: Czy slowniki sa identyczne?
# Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one znajduja.
# Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych.
# Dane wyjsciowe: Wartosc boolowska.
# Przyklad:
# Dla otrzymanych slownikow:
# {'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}
# Powinna zostac zwrocona wartosc logiczna: Prawda.
# Dla otrzymanych slownikow:
# {'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}
# Powinna zostac zwrocona wartosc logiczna: Falsz.

znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="$1"
    local -A histogram=()
    for (( i=0; i<${#napis}; i++ )); do
        ((histogram["${napis:$i:1}"]++))
    done
    for litera in ${!histogram[@]}; do
        if [[ "${histogram[$litera]}" -gt 1 ]]; then
            echo "$litera"
        fi
    done
}

test_znaki_powtarzajace_sie_wiecej_niz_raz() {
    local napis="ababab"
    local wynik=($(znaki_powtarzajace_sie_wiecej_niz_raz "$napis"))
    local oczekiwane=(a b)
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_znaki_powtarzajace_sie_wiecej_niz_raz
}

main "$@"

