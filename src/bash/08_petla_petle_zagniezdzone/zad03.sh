# ZAD-03 — Trójkąt malejący
main() {
    read n
    for ((i=n; i>=1; i--)); do
        for ((j=0; j<i; j++)); do
            echo -n "*"
        done
        echo ""
    done
}
main "$@"
