# ZAD-06A — Liczby mniejsze od n o sumie cyfr równej 10
# ZAD-06B — Dwucyfrowe większe od n
# ZAD-06C — Trzycyfrowe o sumie cyfr równej n
# ZAD-06D — Trzycyfrowe podzielne przez sumę cyfr liczby n
# ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

main() {
    read a

    # Funkcja pomocnicza do obliczania sumy cyfr
    suma_cyfr() {
        local num=$1
        local suma=0
        while [ $num -gt 0 ]; do
            suma=$(($suma + $num % 10))
            num=$(($num / 10))
        done
        echo $suma
    }

    # Funkcja sprawdzająca czy wszystkie cyfry są parzyste
    wszystkie_parzyste() {
        local num=$1
        if [ $num -eq 0 ]; then
            return 1  # Pomijamy 0
        fi
        while [ $num -gt 0 ]; do
            local cyfra=$(($num % 10))
            if [[ $(($cyfra % 2)) -ne 0 ]]; then
                return 1
            fi
            num=$(($num / 10))
        done
        return 0
    }

    # ZAD-06A: Liczby mniejsze od n o sumie cyfr równej 10
    for ((i = 0; i < $a; i++)); do
        if [[ $(suma_cyfr $i) -eq 10 ]]; then
            echo $i
        fi
    done

    # ZAD-06B: Dwucyfrowe większe od n
    for ((i = 10; i < 100; i++)); do
        if [[ $i -gt $a ]]; then
            echo $i
        fi
    done

    # ZAD-06C: Trzycyfrowe o sumie cyfr równej n
    for ((i = 100; i < 1000; i++)); do
        if [[ $(suma_cyfr $i) -eq $a ]]; then
            echo $i
        fi
    done

    # ZAD-06D: Trzycyfrowe podzielne przez sumę cyfr liczby n
    suma_n=$(suma_cyfr $a)
    if [[ $suma_n -gt 0 ]]; then
        for ((i = 100; i < 1000; i++)); do
            if [[ $(($i % $suma_n)) -eq 0 ]]; then
                echo $i
            fi
        done
    fi

    # ZAD-06E: Mniejsze od n złożone wyłącznie z parzystych cyfr
    for ((i = 2; i < $a; i++)); do
        if wszystkie_parzyste $i; then
            echo $i
        fi
    done
}

main "$@"
