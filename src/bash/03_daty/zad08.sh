# ZAD-08 — Dzień tygodnia dla daty (Zeller)

main() {
    read d
    read m
    read y

    # Algorytm Zellera - dla stycznia i lutego traktuj jako miesiące 13 i 14 poprzedniego roku
    if [[ $m -le 2 ]]; then
        m=$(($m + 12))
        y=$(($y - 1))
    fi

    K=$(($y % 100))
    J=$(($y / 100))
    
    # Wzór Zellera
    h=$(( ($d + (13*($m+1))/5 + $K + $K/4 + $J/4 + 5*$J) % 7 ))

    # Mapowanie wyniku na dzień tygodnia
    case $h in
        0) echo "Sobota" ;;
        1) echo "Niedziela" ;;
        2) echo "Poniedziałek" ;;
        3) echo "Wtorek" ;;
        4) echo "Środa" ;;
        5) echo "Czwartek" ;;
        6) echo "Piątek" ;;
    esac
}

main "$@"
