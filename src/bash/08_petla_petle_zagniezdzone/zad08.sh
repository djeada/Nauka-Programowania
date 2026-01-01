# ZAD-08 — Trójkąt Pascala
main() {
    read n
    for ((i=0; i<n; i++)); do
        c=1
        for ((j=0; j<=i; j++)); do
            if [[ $j -eq 0 ]]; then
                echo -n "$c"
            else
                echo -n " $c"
            fi
            c=$((c * (i - j) / (j + 1)))
        done
        echo ""
    done
}
main "$@"
