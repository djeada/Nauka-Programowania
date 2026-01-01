/*
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` (całkowite, każda `≥ 0`)

### Wyjście

Jedna linia: największa liczba.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

*/

use ::std::*;

fn main() {

	println!("Podaj cztery liczby oddzielone spacjami:");
	let mut wiersz = String::new();
	std::io::stdin().read_line(&mut wiersz).expect("Blad odczytu");
	let liczby: Vec<i32> = wiersz.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();

	let mut maks_1 = liczby[0] > liczby[1] ? liczby[0] : liczby[1];
	let mut maks_2 = liczby[2] > liczby[3] ? liczby[2] : liczby[3];
	let mut maks = maks_1 > maks_2 ? maks_1 : maks_2;
	
	println!("Najwieksza liczba to: {}", maks);
}

