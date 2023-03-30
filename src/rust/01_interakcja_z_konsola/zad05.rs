/*
Wyznacz wartosc funkcji w punkcie:

a) Otrzymujesz wspolrzedna x. Wyznacz wartosc funkcji y = 3x + 10 w zadanym
punkcie. 
b) Pobierz wspolczynniki a, b oraz punkt x. Wyznacz wartosc funkcji y =
ax + b w zadanym punkcie. 
c) Otrzymujesz wspolrzedna x. Wyznacz wartosc funkcji
y = x3 + 22 - 20 w zadanym punkcie. 
d) Pobierz wspolczynniki a, b, c, d, m, n
oraz punkt x. Wyznacz wartosc funkcji y = a*xm + b*xn + c - a w zadanym punkcie.
e) Otrzymujesz wspolrzedna x. Wyznacz wartosc funkcji y = sin3x*cos2x + ex2 +
log(x3+2x2-x-3) w zadanym punkcie.
*/

use ::std::*;

fn main() {
	
	// Podpunkt a)
	println!("Podaj wspolrzedna x: ");
	let mut x = String::new();
	std::io::stdin().read_line(&mut x).expect("Blad odczytu");
	let x: f64 = x.trim().parse().expect("Blad parsowania");
	println!("Wartosc funkcji y=3x+10 w punkcie {} wynosi: {}", x, 3*x+10);

	// Podpunkt b)
	println!("Podaj wspolczynnik a: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: f64 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik b: ");
	let mut b = String::new();
	std::io::stdin().read_line(&mut b).expect("Blad odczytu");
	let b: f64 = b.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolrzedna x: ");
	let mut x = String::new();
	std::io::stdin().read_line(&mut x).expect("Blad odczytu");
	let x: f64 = x.trim().parse().expect("Blad parsowania");
	println!("Wartosc funkcji y={}x+{} w punkcie {} wynosi: {}", a, b, x, a*x+b);

	// Podpunkt c)
	println!("Podaj wspolrzedna x: ");
	let mut x = String::new();
	std::io::stdin().read_line(&mut x).expect("Blad odczytu");
	let x: f64 = x.trim().parse().expect("Blad parsowania");
	println!("Wartosc funkcji y=x3+22-20 w punkcie {} wynosi: {}", x, x*x*x+22-20);

	// Podpunkt d)
	println!("Podaj wspolczynnik a: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: f64 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik b: ");
	let mut b = String::new();
	std::io::stdin().read_line(&mut b).expect("Blad odczytu");
	let b: f64 = b.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik c: ");
	let mut c = String::new();
	std::io::stdin().read_line(&mut c).expect("Blad odczytu");
	let c: f64 = c.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik d: ");
	let mut d = String::new();
	std::io::stdin().read_line(&mut d).expect("Blad odczytu");
	let d: f64 = d.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik m: ");
	let mut m = String::new();
	std::io::stdin().read_line(&mut m).expect("Blad odczytu");
	let m: f64 = m.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolczynnik n: ");
	let mut n = String::new();
	std::io::stdin().read_line(&mut n).expect("Blad odczytu");
	let n: f64 = n.trim().parse().expect("Blad parsowania");
	println!("Podaj wspolrzedna x: ");
	let mut x = String::new();
	std::io::stdin().read_line(&mut x).expect("Blad odczytu");
	let x: f64 = x.trim().parse().expect("Blad parsowania");
	println!("Wartosc funkcji y={}x{}+{}x{}+{} w punkcie {} wynosi: {}", a, m, b, n, c, x, a*x*m+b*x*n+c);

	// Podpunkt e)
	println!("Podaj wspolrzedna x: ");
	let mut x = String::new();
	std::io::stdin().read_line(&mut x).expect("Blad odczytu");
	let x: f64 = x.trim().parse().expect("Blad parsowania");
	println!("Wartosc funkcji y=sin3x*cos2x+e^2+log(x3+2x2-x-3) w punkcie {} wynosi: {}", x, (x*x*x).sin()*(x*x).cos()+x.exp()+x.ln());

}

