# ZAD-07 — Dzień roku (liczba dni od 1 stycznia, włącznie)

main() {
    read d
    read m
    read y

    # Tablica dni w miesiącach (dla roku nieprzestępnego)
    dni_w_miesiacach=(0 31 28 31 30 31 30 31 31 30 31 30 31)
    
    # Sprawdź czy rok przestępny
    if [[ $(($y % 400)) -eq 0 ]] || ( [[ $(($y % 4)) -eq 0 ]] && [[ $(($y % 100)) -ne 0 ]] ); then
        dni_w_miesiacach[2]=29
    fi

    # Oblicz dzień roku
    dzien_roku=$d
    for ((i=1; i<m; i++)); do
        dzien_roku=$(($dzien_roku + ${dni_w_miesiacach[$i]}))
    done

    echo $dzien_roku
}

main "$@"
