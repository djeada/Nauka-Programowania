# ZAD-07 — Wszystkie trójkąty
main() {
    read n
    for ((size=1; size<=n; size++)); do
        for ((i=1; i<=size; i++)); do
            for ((j=0; j<i; j++)); do
                echo -n "*"
            done
            echo ""
        done
    done
}
main "$@"
