/*
ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu linii.
* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.

*/
function main() {
  const n = parseInt(prompt("Podaj liczbe:"));
  
  // Helper function to check if a number is prime
  function isPrime(num) {
    if (num < 2) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i * i <= num; i += 2) {
      if (num % i === 0) return false;
    }
    return true;
  }
  
  const primes = [];
  let candidate = 2;
  
  while (primes.length < n) {
    if (isPrime(candidate)) {
      primes.push(candidate);
    }
    candidate++;
  }
  
  console.log(primes.join(" "));
}

main();
