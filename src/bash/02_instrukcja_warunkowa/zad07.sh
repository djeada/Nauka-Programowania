# ZAD-07 — Prawa logiki (p i q)
#
# **Poziom:** ★★☆
# **Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

main() {
    # Funkcje pomocnicze do konwersji bool
    to_str() {
        if [ "$1" -eq 1 ]; then echo "True"; else echo "False"; fi
    }

    # Prawo wyłączonego środka: p OR (NOT p)
    echo "Prawo wyłączonego środka:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( $p || !$p ))
            R=1  # zawsze prawda
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done

    echo ""
    # Prawo niesprzeczności: NOT (p AND (NOT p))
    echo "Prawo niesprzeczności:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( !($p && !$p) ))
            R=1  # zawsze prawda
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done

    echo ""
    # Przemienność koniunkcji: p AND q = q AND p
    echo "Przemienność koniunkcji:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( $p && $q ))
            R=$(( $q && $p ))
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done

    echo ""
    # Przemienność alternatywy: p OR q = q OR p
    echo "Przemienność alternatywy:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( $p || $q ))
            R=$(( $q || $p ))
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done

    echo ""
    # Pierwsze prawo de Morgana: NOT (p AND q) = (NOT p) OR (NOT q)
    echo "Pierwsze prawo de Morgana:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( !($p && $q) ))
            R=$(( !$p || !$q ))
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done

    echo ""
    # Drugie prawo de Morgana: NOT (p OR q) = (NOT p) AND (NOT q)
    echo "Drugie prawo de Morgana:"
    for p in 0 1; do
        for q in 0 1; do
            L=$(( !($p || $q) ))
            R=$(( !$p && !$q ))
            EQ=$(( $L == $R ))
            echo "p=$(to_str $p) q=$(to_str $q) L=$(to_str $L) R=$(to_str $R) EQ=$(to_str $EQ)"
        done
    done
}

main "$@"
