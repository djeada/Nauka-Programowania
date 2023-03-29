/*

Tytuł: Rotacje napisów.

Treść: Dostajesz dwa napisy. Sprawdź, czy jeden z nich jest rotacją drugiego.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisów "malpka" i "pkamal" powinno zostać zwrócone "Prawda".

*/

function czyRotacja(napis1, napis2) {
  if (napis1.length !== napis2.length) {
    return false;
  }
  const napisPodwojony = napis1 + napis1;
  return napisPodwojony.includes(napis2);
}

function testCzyRotacja() {
  const napis1 = "malpka";
  const napis2 = "pkamal";
  const napis3 = "malpak";
  console.assert(czyRotacja(napis1, napis2) === true, "Test 1 nieudany");
  console.assert(czyRotacja(napis1, napis3) === false, "Test 2 nieudany");
}

testCzyRotacja();
