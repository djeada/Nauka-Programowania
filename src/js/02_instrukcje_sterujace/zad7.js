/*
Tytuł: Dowody praw logicznych.

Treść: Pokaż za pomocą operacji logicznych następujące prawa:

a) Prawo wyłączonego środka.

b) Prawo niesprzeczności.

c) Przemienność koniunkcji.

d) Przemienność alternatywy.

e) Pierwsze prawo de Morgana.

f) Drugie prawo de Morgana.

Dane wejściowe: Brak.

Dane wyjściowe: Komunikat.

a) Prawo wyłączonego środka:
- Dla p mającego wartość logiczną: `False` wyrażenie p v ~p ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` wyrażenie p v ~p ma wartość logiczną: `True`.

b) Zasada niesprzeczności:
- Dla p mającego wartość logiczną: `False` wyrażenie ~(p Ʌ ~p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` wyrażenie ~(p Ʌ ~p) ma wartość logiczną: `True`.

c) Przemienność koniunkcji:
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie (p Ʌ q) < = > (q Ʌ p) ma wartość logiczną: `True`.

d) Przemienność alternatywy:
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie (p v q) < = > (q v p) ma wartość logiczną: `True`.

e) Pierwsze prawo de Morgana:
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `True` wyrażenie ~(p Ʌ q) < = > (~p v ~q) ma wartość logiczną: `True`.

f) Drugie prawo de Morgana:
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `False` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczną: `False` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `False` oraz q mającego wartość logiczną: `True` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
- Dla p mającego wartość logiczną: `True` oraz q mającego wartość logiczna: `True` wyrażenie ~(p v q) < = > (~p Ʌ ~q) ma wartość logiczną: `True`.
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
console.info("wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ", ((p && q) == (q && p)));
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ", ((p && q) == (q && p)));
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ", ((p && q) == (q && p)));
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ", ((p && q) == (q && p)));
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna ", ((p && q) == (q && p)));

console.info("Przemiennosc alternatywy");
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ", ((p || q) == (q || p)));
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ", ((p || q) == (q || p)));
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ", ((p || q) == (q || p)));
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie (p v q) < = > (q v p) ma wartosc logiczna ", ((p || q) == (q || p)));

console.info("Pierwsze prawo de Morgana");
p = false;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ", ((!(p && q)) == (!p || !q)));
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ", ((!(p && q)) == (!p || !q)));
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna ", ((!(p && q)) == (!p || !q)));
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);

console.info("Drugie prawo de Morgana");
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ", ((!(p || q)) == (!p && !q)));
p = true;
q = false;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ", ((!(p || q)) == (!p && !q)));
p = false;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ", ((!(p || q)) == (!p && !q)));
p = true;
q = true;
console.info("dla p majacego wartosc logiczna ", p);
console.info("oraz q majacego wartosc logiczna ", q);
console.info("wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna ", ((!(p || q)) == (!p && !q)));