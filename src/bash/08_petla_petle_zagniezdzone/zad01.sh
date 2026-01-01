# ZAD-01 — Kwadrat
main() {
    read n
    for ((i=0; i<n; i++)); do
        for ((j=0; j<n; j++)); do
            echo -n "*"
        done
        echo ""
    done
}
main "$@"
