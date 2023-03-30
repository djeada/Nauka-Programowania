/*

Tytul: Rotacje napisow.

Tresc: Dostajesz dwa napisy. Sprawdz, czy jeden z nich jest rotacja drugiego.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla napisow "malpka" i "pkamal" powinno zostac zwrocone "Prawda".

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

