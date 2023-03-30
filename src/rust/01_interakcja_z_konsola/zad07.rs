/*
Oblicz pola figur i objetosci bryl:

a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz pole.
b) Pobierz dlugosci bokow prostokata i wypisz pole.
c) Pobierz dlugosci przekatnych rombu i wypisz pole.
d) Pobierz promien kuli i wypisz objetosc.
e) Pobierz promien podstawy i wysokosc stozka i wypisz objetosc.
f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz objetosc.
*/

use ::std::*;

fn main() {

	// Podpunkt a)
	println!("Podaj dlugosc podstawy trojkata: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: i32 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj wysokosc trojkata: ");
	let mut h = String::new();
	std::io::stdin().read_line(&mut h).expect("Blad odczytu");
	let h: i32 = h.trim().parse().expect("Blad parsowania");
	println!("Pole trojkata wynosi: {}", a * h / 2);

	// Podpunkt b)
  	println!("Podaj dlugosc a boku prostokata: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: i32 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj dlugosc b boku prostokata: ");
	let mut b = String::new();
	std::io::stdin().read_line(&mut b).expect("Blad odczytu");
	let b: i32 = b.trim().parse().expect("Blad parsowania");
	println!("Pole prostokata wynosi: {}", a * b);

	// Podpunkt c)
	println!("Podaj dlugosc przekatnej rombu: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: f32 = a.trim().parse().expect("Blad parsowania");
	println!("Pole rombu wynosi: {}", a * a / 2.00);

	// Podpunkt d)
	println!("Podaj promien kuli: ");
	let mut r = String::new();
	std::io::stdin().read_line(&mut r).expect("Blad odczytu");
	let r: f32 = r.trim().parse().expect("Blad parsowania");
	println!("Objetosc kuli wynosi: {}", (4.0 / 3.0) * 3.14 * (r * r * r));

	// Podpunkt e)
	println!("Podaj dlugosc podstawy stozka: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: f32 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj wysokosc stozka: ");
	let mut h = String::new();
	std::io::stdin().read_line(&mut h).expect("Blad odczytu");
	let h: f32 = h.trim().parse().expect("Blad parsowania");
	println!("Objetosc stozka wynosi: {}",  1.00 / 3.00 * 3.14 * a * a * h);

	// Podpunkt f)
	println!("Podaj dlugosc graniastoslupa: ");
	let mut a = String::new();
	std::io::stdin().read_line(&mut a).expect("Blad odczytu");
	let a: i32 = a.trim().parse().expect("Blad parsowania");
	println!("Podaj szerokosc graniastoslupa: ");
	let mut b = String::new();
	std::io::stdin().read_line(&mut b).expect("Blad odczytu");
	let b: i32 = b.trim().parse().expect("Blad parsowania");
	println!("Podaj wysokosc graniastoslupa: ");
	let mut h = String::new();
	std::io::stdin().read_line(&mut h).expect("Blad odczytu");
	let h: i32 = h.trim().parse().expect("Blad parsowania");
	println!("Objetosc graniastoslupa wynosi: {}", a * b * h );
	
}

