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
    read a

    pom=$a
    odwrocona=0

    # Przypadek specjalny: n = 0 jest palindromem
    if [[ $a -eq 0 ]]; then
        echo "Liczba jest palindromem."
        return
    fi

    # Odwróć liczbę
    while [ $pom -gt 0 ]; do
        cyfra=$(($pom % 10))
        odwrocona=$(($odwrocona * 10 + $cyfra))
        pom=$(($pom / 10))
    done

    # Sprawdź czy jest palindromem
    if [[ $odwrocona -eq $a ]]; then
        echo "Liczba jest palindromem."
    else
        echo "Liczba nie jest palindromem."
    fi
}

main "$@"
