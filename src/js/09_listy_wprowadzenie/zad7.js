/*

Tytul: Liczba mniejsza od najwiekszej i wieksza od wszystkich pozostalych.

Tresc: Otrzymujesz liste liczb naturalnych. Znajdz najwieksza i druga co do wielkosci liczbe w liscie, a nastepnie oblicz srednia arytmetyczna tych dwoch liczb i zwroc ja jako liczbe zmiennoprzecinkowa.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Liczba zmiennoprzecinkowa oznaczajaca srednia arytmetyczna najwiekszej i drugiej co do wielkosci liczby z listy.

Przyklad:

Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostac zwrocona liczba 8.0.
    
    */

function liczbaMniejszaOdNajwiekszej(lista) {
  let max = lista[0];
  let secondMax = lista[0];
  for (let i = 1; i < lista.length; i++) {
    if (lista[i] > max) {
      secondMax = max;
      max = lista[i];
    } else if (lista[i] > secondMax) {
      secondMax = lista[i];
    }
  }
  return (max + secondMax) / 2;
}

// Testy

function testLiczbaMniejszaOdNajwiekszej() {
  console.assert(liczbaMniejszaOdNajwiekszej([9, 2, 3, 2, 1, 7]) === 8.0);
  console.assert(liczbaMniejszaOdNajwiekszej([1, 2, 3, 4, 5, 6]) === 5.5);
  console.assert(liczbaMniejszaOdNajwiekszej([6, 5, 4, 3, 2, 1]) === 3.5);
}

function main() {
  testLiczbaMniejszaOdNajwiekszej();
}

main();

