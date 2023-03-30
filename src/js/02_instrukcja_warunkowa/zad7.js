/*
Tytul: Dowody praw logicznych.

Tresc: Pokaz za pomoca operacji logicznych nastepujace prawa:

a) Prawo wylaczonego srodka.

b) Prawo niesprzecznosci.

c) Przemiennosc koniunkcji.

d) Przemiennosc alternatywy.

e) Pierwsze prawo de Morgana.

f) Drugie prawo de Morgana.

Dane wejsciowe: Brak.

Dane wyjsciowe: Komunikat.

a) Prawo wylaczonego srodka:
- Dla p majacego wartosc logiczna: `False` wyrazenie p v ~p ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` wyrazenie p v ~p ma wartosc logiczna: `True`.

b) Zasada niesprzecznosci:
- Dla p majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.

c) Przemiennosc koniunkcji:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.

d) Przemiennosc alternatywy:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.

e) Pierwsze prawo de Morgana:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.

f) Drugie prawo de Morgana:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
*/

console.info("Prawo wylacznego srodka");
var p = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info(" wyrazenie p v ~p ma wartosc logiczna ", p || !p);
p = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("wyrazenie p v ~p ma wartosc logiczna", p || !p);
p = false;

console.info("Zasada niesprzecznosci");
console.info("dla p majacego wartosc logiczna ", p);
console.info("wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ", !(p && !p));
p = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ", !(p && !p));
p = false;
var q = false;

console.info("Przemiennosc koniunkcji");
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
  (p && q) == (q && p)
);
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
  (p && q) == (q && p)
);
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
  (p && q) == (q && p)
);
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
  (p && q) == (q && p)
);
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ",
  (p && q) == (q && p)
);

console.info("Przemiennosc alternatywy");
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
  (p || q) == (q || p)
);
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
  (p || q) == (q || p)
);
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
  (p || q) == (q || p)
);
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ",
  (p || q) == (q || p)
);

console.info("Pierwsze prawo de Morgana");
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
  !(p && q) == (!p || !q)
);
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
  !(p && q) == (!p || !q)
);
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ",
  !(p && q) == (!p || !q)
);
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);

console.info("Drugie prawo de Morgana");
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
  !(p || q) == (!p && !q)
);
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
  !(p || q) == (!p && !q)
);
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
  !(p || q) == (!p && !q)
);
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info(
  "wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ",
  !(p || q) == (!p && !q)
);

