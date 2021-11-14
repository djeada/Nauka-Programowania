/*
Pokaz za pomoca operacji logicznych:

a) Prawo wylaczonego srodka.
b) Prawo niesprzecznosci.
c) Przemiennosc koniunkcji.
d) Przemiennosc alternatywy.
e) Pierwsze prawo de Morgana.
f) Drugie prawo de Morgana.
*/

use ::std::*;

fn main() {

	// Podpunkt a)
	println!("Prawo wylaczonego srodka.");
	let mut p = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Wyrazenie p v ~p ma wartosc logiczna {}", p || !p);
	let mut p = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Wyrazenie p v ~p ma wartosc logiczna {}", p || !p);

	// Podpunkt b)
	println!("Prawo niesprzecznosci.");
	let mut p = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Wyrazenie ~(p Ʌ ~p) ma wartosc logiczna {}", !(p && !p));
	let mut p = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Wyrazenie ~(p Ʌ ~p) ma wartosc logiczna {}", !(p && !p));

	// Podpunkt c)
	println!("Przemiennosc koniunkcji.");
	let mut p = true;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna {}", (p && q) == (q && p));
	let mut p = false;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna {}", (p && q) == (q && p));
	let mut p = true;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna {}", (p && q) == (q && p));
	let mut p = false;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna {}", (p && q) == (q && p));

	// Podpunkt d)
	println!("Przemiennosc alternatywy.");
	let mut p = true;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p v q) < = > (q v p) ma wartosc logiczna {}", (p || q) == (q || p));
	let mut p = false;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p v q) < = > (q v p) ma wartosc logiczna {}", (p || q) == (q || p));
	let mut p = true;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p v q) < = > (q v p) ma wartosc logiczna {}", (p || q) == (q || p));
	let mut p = false;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie (p v q) < = > (q v p) ma wartosc logiczna {}", (p || q) == (q || p));

	// Podpunkt e)
	println!("Pierwsze prawo de Morgana.");
	let mut p = true;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna {}", !(p && q) == (!p || !q));
	let mut p = false;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna {}", !(p && q) == (!p || !q));
	let mut p = true;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna {}", !(p && q) == (!p || !q));
	let mut p = false;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna {}", !(p && q) == (!p || !q));

	// Podpunkt f)
	println!("Pierwsze prawo de Morgana.");
	let mut p = true;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna {}", !(p || q) == (!p && !q));
	let mut p = false;
	let mut q = true;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna {}", !(p || q) == (!p && !q));
	let mut p = true;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna {}", !(p || q) == (!p && !q));
	let mut p = false;
	let mut q = false;
	println!("Dla p majacego wartosc logiczna {}", p);
	println!("Dla q majacego wartosc logiczna {}", q);
	println!("Wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna {}", !(p || q) == (!p && !q));

}
