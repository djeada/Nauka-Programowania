# Tytul: Rok przestepny.
# Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie sprawdzal, czy dany rok jest przestepny.
# Podpowiedz: Rok przestepny jest podzielny przez 4, ale nie jest podzielny przez 100, chyba ze jest podzielny przez 400.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat o tym, czy rok jest przestepny, czy tez nie.
# Przyklad:
# Dla pobranej liczby 2100, program powinien wypisac informacje, ze rok nie jest przestepny.

main() {

    echo "Podaj rok:"
    read rok

    if [[ $(($rok % 4)) -eq 0 ]]; then
        if [[ $(($rok % 100)) -eq 0 ]]; then
            if [[ $(($rok % 400)) -eq 0 ]]; then
                echo "rok jest przestepny"
            else
                echo "rok nie jest przestepny"
            fi
        else
            echo "rok jest przestepny"
        fi
    else
        echo "rok nie jest przestepny"
    fi
}

main "$@"

