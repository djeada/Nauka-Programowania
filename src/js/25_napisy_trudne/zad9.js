/*

Tytul: Najdluzszy wspolny podnapis.

Tresc: Dostajesz dwa napisy. Znajdz najdluzszy wspolny podnapis tych dwoch napisow.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisow "ijkabcdl" i "xxxxabcd" powinien zostac zwrocony napis "abcd".

*/

function najdluzszyWspolnyPodnapis(napis1, napis2) {
  const m = napis1.length;
  const n = napis2.length;
  let maxLength = 0;
  let endIndex = -1;
  const dp = Array.from(
    {
      length: m + 1,
    },
    () => Array(n + 1).fill(0)
  );

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (napis1[i - 1] === napis2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
        if (dp[i][j] > maxLength) {
          maxLength = dp[i][j];
          endIndex = i - 1;
        }
      }
    }
  }

  return napis1.substring(endIndex - maxLength + 1, endIndex + 1);
}

function testNajdluzszyWspolnyPodnapis() {
  const napis1 = "ijkabcdl";
  const napis2 = "xxxxabcd";
  const wynik = "abcd";

  console.assert(
    najdluzszyWspolnyPodnapis(napis1, napis2) === wynik,
    "Test nieudany"
  );
}

testNajdluzszyWspolnyPodnapis();

