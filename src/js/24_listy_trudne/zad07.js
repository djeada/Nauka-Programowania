/*

Tytul: Woda

Tresc: Otrzymujesz liste wysokosci slupkow. Wszystkie slupki maja jednakowa szerokosc, rowna jednej jednostce wysokosci, i ustawione sa obok siebie. Wysokosc rowna 0 oznacza brak slupka. Oblicz ile jednostek wody maksymalnie mozemy umiescic miedzy slupkami.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla wejsciowej listy [3, 0, 1, 0, 2], powinna zostac zwrocona liczba: 5.

Oto ilustracja dla powyzszego przykladu:

```
   o           
   o      o    
o  o   o  o  o 
```

Mozemy umiescic 5 jednostek wody pomiedzy slupkami.

*/

const woda = (lista) => {
  let max = lista[0];
  let maxIndex = 0;
  let sum = 0;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] > max) {
      max = lista[i];
      maxIndex = i;
    }
  }
  let temp = lista[0];
  for (let i = 1; i < maxIndex; i++) {
    if (lista[i] > temp) {
      temp = lista[i];
    } else {
      sum += temp - lista[i];
    }
  }
  temp = lista[lista.length - 1];
  for (let i = lista.length - 2; i > maxIndex; i--) {
    if (lista[i] > temp) {
      temp = lista[i];
    } else {
      sum += temp - lista[i];
    }
  }
  return sum;
};

// Testy
const lista1 = [3, 0, 1, 0, 2];
const wynik1 = 5;

const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = 0;

const lista3 = [9, 8, 7, 6, 5, 4, 3, 2, 1];
const wynik3 = 0;

console.assert(woda(lista1) === wynik1, "Test 1 nieudany");
console.assert(woda(lista2) === wynik2, "Test 2 nieudany");
console.assert(woda(lista3) === wynik3, "Test 3 nieudany");

