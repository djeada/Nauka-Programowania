/*
ZAD-10 — Podmień napisy z listy A na napisy z listy B

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `zamiana`

### Treść

Otrzymujesz:

* tekst,
* listę A (napisy do znalezienia),
* listę B (napisy do podmiany), tej samej długości co A.

Zastąp w tekście wszystkie wystąpienia słów z listy A odpowiadającymi im słowami z listy B (ten sam indeks). Zamieniaj tylko **całe słowa**, nie fragmenty innych słów.

### Wejście

1. Tekst (jedna lub wiele linii)
2. Liczba naturalna `n` — długość list
3. `n` wierszy: elementy listy A
4. `n` wierszy: elementy listy B

### Wyjście

Zmodyfikowany tekst.

### Przykład

*(jak w treści — z listami A/B)*

*/

function podmien_napisy(napis, lista_a, lista_b) {
  return napis.replace(
    new RegExp(lista_a.join("|"), "g"),
    function (znaleziony) {
      return lista_b[lista_a.indexOf(znaleziony)];
    }
  );
}

function test_podmien_napisy() {
  const napis = `Every mile was tilted at seven or.
Wished her entire esteem mr oh by.
He prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on be.
Warmth his law design says he is a person.
Pronunciation suspected in belonging conveying ye repulsive.`;

  const lista_a = ["or", "be", "he"];
  const lista_b = ["and", "off", "she"];

  const wynik = `Every mile was tilted at seven and.
Wished her entire esteem mr oh by.
She prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on and off.
Warmth his law design says she is a person.
Pronunciation suspected in belonging conveying ye repulsive.`;

  console.assert(podmien_napisy(napis, lista_a, lista_b) === wynik);
}

test_podmien_napisy();

