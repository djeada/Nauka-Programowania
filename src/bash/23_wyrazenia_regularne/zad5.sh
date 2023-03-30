# Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.
# Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

odfiltruj_cyfry() {
    echo "$1" | grep -o '[0-9]'
}

test_odfiltruj_cyfry() {
    assertEqual $(odfiltruj_cyfry "abc123") "123"
    assertEqual $(odfiltruj_cyfry "abc") ""
    assertEqual $(odfiltruj_cyfry "123") "123"
    assertEqual $(odfiltruj_cyfry "3d4jda2") "342"
}

main() {
    test_odfiltruj_cyfry
}

main "$@"

