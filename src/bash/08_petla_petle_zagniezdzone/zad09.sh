# ZAD-09 — Liczby pierwsze
main() {
    read n
    count=0
    num=2
    while [[ $count -lt $n ]]; do
        is_prime=1
        if [[ $num -gt 2 ]]; then
            for ((i=2; i*i<=num; i++)); do
                if [[ $((num % i)) -eq 0 ]]; then
                    is_prime=0
                    break
                fi
            done
        fi
        if [[ $is_prime -eq 1 ]]; then
            if [[ $count -eq 0 ]]; then
                echo -n "$num"
            else
                echo -n " $num"
            fi
            count=$((count + 1))
        fi
        num=$((num + 1))
    done
    echo ""
}
main "$@"
