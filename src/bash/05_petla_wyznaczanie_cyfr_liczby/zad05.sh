# ZAD-05 — Sprawdzanie, czy liczba jest palindromem
#
# **Poziom:** ★★☆
# **Tagi:** `string`, `pętle`, `odwracanie`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:
#
# * `Liczba jest palindromem.`
# * `Liczba nie jest palindromem.`
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Jeden komunikat tekstowy (dokładnie jeden z powyższych).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 13231
# ```
#
# **Wyjście:**
#
# ```
# Liczba jest palindromem.
# ```
#
# ### Uwagi o formatowaniu
#
# * `0` jest palindromem.

main() {

    echo "Podaj liczbe: "
    read a

    pom=$a
    odwrocona=0

    while [ $pom -gt 0 ]; do
        cyfra=$(($pom % 10))

        odwrocona=$(($odwrocona * 10 + $cyfra))
        pom=$(($pom / 10))
    done

    if [[ $odwrocona -eq $a ]]; then
        echo "podana liczba jest palindromem"
    else
        echo "podana liczba nie jest palindromem"
    fi
}

main "$@"
