/*

Tytuł: Woda

Treść: Otrzymujesz listę wysokości słupków. Wszystkie słupki mają jednakową szerokość, równą jednej jednostce wysokości, i ustawione są obok siebie. Wysokość równa 0 oznacza brak słupka. Oblicz ile jednostek wody maksymalnie możemy umieścić między słupkami.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla wejściowej listy [3, 0, 1, 0, 2], powinna zostać zwrócona liczba: 5.

Oto ilustracja dla powyższego przykładu:

```
   o           
   o      o    
o  o   o  o  o 
```

Możemy umieścić 5 jednostek wody pomiędzy słupkami.

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
