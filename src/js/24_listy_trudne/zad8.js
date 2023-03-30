/*

Tytuł: Sznurek.

Treść: Masz do sprzedania sznurek o długości n, a także listę cen dla sznurków o długościach od 1 do n. Ceny mogą być różne dla różnych długości. Znajdź maksymalny zysk, który można osiągnąć poprzez sprzedaż danego sznurka.

Dane wejściowe: Lista n liczb całkowitych reprezentujących ceny dla sznurków o długościach od 1 do n, oraz liczba naturalna n reprezentująca długość sznurka, który chcesz sprzedać.

Dane wyjściowe: Największa możliwa wartość, jaką można uzyskać ze sprzedaży danego sznurka.

Przykład:

Dla listy cen: [1, 5, 8, 9, 10, 17, 17, 20] oraz długości sznurka 4, powinna zostać zwrócona liczba 10.

*/

const sznurek = (lista, n) => {
  let max = 0;
  for (let i = 0; i < n; i++) {
    let suma = 0;
    for (let j = 0; j < n - i; j++) {
      suma += lista[j];
    }
    if (suma > max) {
      max = suma;
    }
  }
  return max;
};

// Testy
const lista1 = [1, 5, 8, 9, 10, 17, 17, 20];
const wynik1 = 10;
const lista2 = [3, 5, 8, 9, 10, 17, 17, 20];
const wynik2 = 22;

console.assert(sznurek(lista1, 4) === wynik1, "Test 1 nieudany");
console.assert(sznurek(lista2, 8) === wynik2, "Test 2 nieudany");
