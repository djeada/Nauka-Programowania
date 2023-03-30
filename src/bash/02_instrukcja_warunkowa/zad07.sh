# Tytul: Dowody praw logicznych.
# Tresc: Pokaz za pomoca operacji logicznych nastepujace prawa:
# a) Prawo wylaczonego srodka.
# b) Prawo niesprzecznosci.
# c) Przemiennosc koniunkcji.
# d) Przemiennosc alternatywy.
# e) Pierwsze prawo de Morgana.
# f) Drugie prawo de Morgana.
# Dane wejsciowe: Brak.
# Dane wyjsciowe: Komunikat.
# a) Prawo wylaczonego srodka:
# - Dla p majacego wartosc logiczna: `False` wyrazenie p v ~p ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` wyrazenie p v ~p ma wartosc logiczna: `True`.
# b) Zasada niesprzecznosci:
# - Dla p majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.
# c) Przemiennosc koniunkcji:
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
# d) Przemiennosc alternatywy:
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
# e) Pierwsze prawo de Morgana:
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
# f) Drugie prawo de Morgana:
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
# - Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.

main() {

    echo "Prawo wylacznego srodka"
    echo "Prawo wylacznego srodka"
    p=false
    echo "dla p majacego wartosc logiczna $p wyrazenie p v ~p ma wartosc logiczna $(($p || !$p))"
    p=true
    echo "dla p majacego wartosc logiczna $p wyrazenie p v ~p ma wartosc logiczna $(($p || !$p))"

    echo -e "\nZasada niesprzecznosci"
    echo -e "\nZasada niesprzecznosci"
    p=false
    echo "dla p majacego wartosc logiczna $p wyrazenie ~(p Ʌ ~p) ma wartosc logiczna $((!($p && !$p)))"
    p=true
    echo "dla p majacego wartosc logiczna $p wyrazenie ~(p Ʌ ~p) ma wartosc logiczna $((!($p && !$p)))"

    echo -e "\nPrzemiennosc koniunkcji"
    echo -e "\nPrzemiennosc koniunkcji"
    p=false
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p Ʌ q) <=> (q Ʌ p) ma wartosc logiczna $((($p && $q) == ($q && $p)))"
    p=true
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p Ʌ q) <=> (q Ʌ p) ma wartosc logiczna $((($p && $q) == ($q && $p)))"
    p=false
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p Ʌ q) <=> (q Ʌ p) ma wartosc logiczna $((($p && $q) == ($q && $p)))"
    p=true
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p Ʌ q) <=> (q Ʌ p) ma wartosc logiczna $((($p && $q) == ($q && $p)))"

    echo -e "\nPrzemiennosc alternatywy"
    echo -e "\nPrzemiennosc alternatywy"
    p=false
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p v q) <=> (q v p) ma wartosc logiczna $((($p || $q) == ($q || $p)))"
    p=true
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p v q) <=> (q v p) ma wartosc logiczna $((($p || $q) == ($q || $p)))"
    p=false
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p v q) <=> (q v p) ma wartosc logiczna $((($p || $q) == ($q || $p)))"
    p=true
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie (p v q) <=> (q v p) ma wartosc logiczna $((($p || $q) == ($q || $p)))"

    echo -e "\nPierwsze prawo de Morgana"
    echo -e "\nPierwsze prawo de Morgana"
    p=false
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p Ʌ q) <=> (~p v ~q) ma wartosc logiczna $((!($p && $q) == (!$p || !$q)))"
    p=true
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p Ʌ q) <=> (~p v ~q) ma wartosc logiczna $((!($p && $q) == (!$p || !$q)))"
    p=false
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p Ʌ q) <=> (~p v ~q) ma wartosc logiczna $((!($p && $q) == (!$p || !$q)))"
    p=true
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p Ʌ q) <=> (~p v ~q) ma wartosc logiczna $((!($p && $q) == (!$p || !$q)))"

    echo -e "\nDrugie prawo de Morgana"
    echo -e "\nDrugie prawo de Morgana"
    p=false
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p v q) <=> (~p Ʌ ~q) ma wartosc logiczna $((!($p || $q) == (!$p && !$q)))"
    p=true
    q=false
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p v q) <=> (~p Ʌ ~q) ma wartosc logiczna $((!($p || $q) == (!$p && !$q)))"
    p=false
    q=true
    echo "dla p majacego wartosc logiczna $p oraz q majacego wartosc logiczna $q wyrazenie ~(p v q) <=> (~p Ʌ ~q) ma wartosc logiczna $((!($p || $q) == (!$p && !$q)))"
    p=true
    q=true
}

main "$@"

