# ZAD-04 — Tabliczka mnożenia
main() {
    read n
    for ((i=1; i<=n; i++)); do
        for ((j=1; j<=n; j++)); do
            if [[ $j -eq 1 ]]; then
                echo -n "$((i*j))"
            else
                echo -n " $((i*j))"
            fi
        done
        echo ""
    done
}
main "$@"
