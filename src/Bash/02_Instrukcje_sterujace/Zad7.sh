#!/usr/bin/env bash

#Dowody praw logicznych

main() {
    
    #Prawo wylacznego srodka
    echo "Prawo wylacznego srodka"
    p=false
    echo "dla p majacego wartosc logiczna $p wyrazenie p v ~p ma wartosc logiczna $(($p || !$p))"
    p=true
    echo "dla p majacego wartosc logiczna $p wyrazenie p v ~p ma wartosc logiczna $(($p || !$p))"

    #Zasada niesprzecznosci
    echo -e "\nZasada niesprzecznosci"
    p=false
    echo "dla p majacego wartosc logiczna $p wyrazenie ~(p Ʌ ~p) ma wartosc logiczna $((!($p && !$p)))"
    p=true
    echo "dla p majacego wartosc logiczna $p wyrazenie ~(p Ʌ ~p) ma wartosc logiczna $((!($p && !$p)))"

    #Przemiennosc koniunkcji
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

    #Przemiennosc alternatywy
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

    #Pierwsze prawo de Morgana
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

    #Drugie prawo de Morgana
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

