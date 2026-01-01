# ZAD-05 — Diament
main() {
    read n
    # Górna połowa (wraz ze środkiem)
    for ((i=0; i<n; i++)); do
        # Spacje na początku
        for ((j=0; j<n-i-1; j++)); do
            echo -n " "
        done
        # Gwiazdki i spacje wewnętrzne
        for ((j=0; j<2*i+1; j++)); do
            if [[ $j -eq 0 || $j -eq $((2*i)) ]]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done
    # Dolna połowa
    for ((i=n-2; i>=0; i--)); do
        for ((j=0; j<n-i-1; j++)); do
            echo -n " "
        done
        for ((j=0; j<2*i+1; j++)); do
            if [[ $j -eq 0 || $j -eq $((2*i)) ]]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done
}
main "$@"
