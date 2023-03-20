/*

Tytuł: Naiwny test pierwszości

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej sprawdzi, czy jest ona liczbą pierwszą.

Dane wejściowe: liczba naturalna

Dane wyjściowe: wartość logiczna

Przykład:

Dla otrzymanej liczby 7, funkcja powinna zwrócić wartość logiczną prawda. Dla otrzymanej liczby 2, funkcja powinna zwrócić wartość logiczną prawda.
*/

// Funkcja zwracająca wartość logiczną, czy liczba jest pierwsza
function czyPierwsza(liczba) {
    if (liczba < 2) {
        return false;
    }
    for (var i = 2; i < liczba; i++) {
        if (liczba % i == 0) {
            return false;
        }
    }
    return true;
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testCzyPierwsza() {
    assert(czyPierwsza(2) == true);
    assert(czyPierwsza(3) == true);
    assert(czyPierwsza(4) == false);
    assert(czyPierwsza(7) == true);
    assert(czyPierwsza(9) == false);
    assert(czyPierwsza(11) == true);
    assert(czyPierwsza(13) == true);
    assert(czyPierwsza(14) == false);
    assert(czyPierwsza(16) == false);
    assert(czyPierwsza(19) == true);
}

// Funkcja uruchamiająca testy
function main() {
    testCzyPierwsza();
}

// Uruchomienie testów
main();