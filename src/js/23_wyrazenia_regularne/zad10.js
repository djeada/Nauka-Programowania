/*

Tytuł: Podmień napisy z listy A na napisy z listy B.

Treść: Dostajesz napis oraz dwie listy napisów. Zastąp napisy z pierwszej listy w pierwszym napisie odpowiadającymi im napisami z drugiej listy.

Dane wejściowe: Napis oraz dwie listy napisów.

Dane wyjściowe: Napis.

Przykład:

Dla podanych danych:

> 'Every mile was tilted at seven or.
  Wished her entire esteem mr oh by.
  He prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on be.
  Warmth his law design says he is a person.
  Pronunciation suspected in belonging conveying ye repulsive.

oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinien zostać zwrócony napis:

> Every mile was tilted at seven and.
  Wished her entire esteem mr oh by.
  She prevents requests by if in pleased.
  Picture too and concerned was comforting.
  Ten difficult resembled eagerness nor.
  Same park bore on and off.
  Warmth his law design says she is a person.
  Pronunciation suspected in belonging conveying ye repulsive.

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
