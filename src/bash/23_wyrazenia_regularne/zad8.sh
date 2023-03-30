# Tytul: Podmien napisy z listy A na napisy z listy B.
# Tresc: Dostajesz napis oraz dwie listy napisow. Zastap napisy z pierwszej listy w pierwszym napisie odpowiadajacymi im napisami z drugiej listy.
# Dane wejsciowe: Napis oraz dwie listy napisow.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla podanych danych:
# > 'Every mile was tilted at seven or.
# Wished her entire esteem mr oh by.
# He prevents requests by if in pleased.
# Picture too and concerned was comforting.
# Ten difficult resembled eagerness nor.
# Same park bore on be.
# Warmth his law design says he is a person.
# Pronunciation suspected in belonging conveying ye repulsive.
# oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinien zostac zwrocony napis:
# > Every mile was tilted at seven and.
# Wished her entire esteem mr oh by.
# She prevents requests by if in pleased.
# Picture too and concerned was comforting.
# Ten difficult resembled eagerness nor.
# Same park bore on and off.
# Warmth his law design says she is a person.
# Pronunciation suspected in belonging conveying ye repulsive.

source ../assert.sh

cyfry_bedace_czescia_slow() {
    local zdanie="$1"
    local cyfry=()

    for slowo in $zdanie; do
        if [[ $slowo =~ [a-zA-Z]+ ]]; then
            cyfry+=($(echo $slowo | sed -r 's/[a-zA-Z|]+//g'))
        fi
    done

    echo ${cyfry[@]}
}

test_cyfry_bedace_czescia_slow() {
    local zdanie="jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go"
    local wynik=($(cyfry_bedace_czescia_slow "$zdanie"))
    local oczekiwane=(29 37 3891 3)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_cyfry_bedace_czescia_slow
}

main "$@"

