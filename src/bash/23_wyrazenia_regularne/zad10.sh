# Tytul: Sprawdz poprawnosc hasla.
# Tresc: Masz napis reprezentujacy haslo. Sprawdz, czy haslo spelnia nastepujace warunki:
# 1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
# 2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
# 3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
# 4. Haslo musi zawierac przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
# 5. Minimalna dlugosc hasla to 8 znakow.
# 6. Maksymalna dlugosc hasla to 20 znakow.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Wartosc logiczna.
# Przyklad:
# Dla napisu: “abc1234”, powinna zostac zwrocona wartosc logiczna: Falsz.

source ../assert.sh

podmien_napisy() {
    local tekst="$1"

    for i in "${!lista_a[@]}"; do
        tekst="${tekst//${lista_a[$i]}/${lista_b[$i]}}"
    done

    echo "$tekst"
}

test_podmien_napisy() {
    local tekst='Whole every miles as tiled at seven or.
    Wished he entire esteem mr oh by.
    He prevent request by if in pleased.
    Picture too and concern has was comfort.
    Ten difficult resembled eagerness nor.
    Same park bore on be.
    Warmth his law design say are person.
    Pronounce suspected in belonging conveying ye repulsive.'
    local lista_a=(or be he)
    local lista_b=(and off she)
    local wynik="$(podmien_napisy "$tekst")"
    local oczekiwane='Whole every miles as tiled at seven and.
    Wished she entire esteem mr oh by.
    He prevent request by if in pleased.
    Picture too and concern has was comfort.
    Ten difficult resembled eagerness nor.
    Same park bore on off.
    Warmth his law design say are person.
    Pronounce suspected in belonging conveying ye repulsive.'
    assertEqual "$wynik" "$oczekiwane"
}

main() {
    test_podmien_napisy
}

main "$@"

