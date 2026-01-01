# ZAD-06 — Klepsydra
main() {
    read n
    # Górna część
    for ((i=0; i<n; i++)); do
        for ((j=0; j<i; j++)); do
            echo -n " "
        done
        for ((j=0; j<n-i; j++)); do
            echo -n "*"
        done
        echo ""
    done
    # Dolna część
    for ((i=n-2; i>=0; i--)); do
        for ((j=0; j<i; j++)); do
            echo -n " "
        done
        for ((j=0; j<n-i; j++)); do
            echo -n "*"
        done
        echo ""
    done
}
main "$@"
