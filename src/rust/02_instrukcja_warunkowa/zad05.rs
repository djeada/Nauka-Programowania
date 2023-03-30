/*
Dla pobranych trzech liczb, wypisz liczby w kolejnosci rosnacej.
*/

use ::std::*;

fn main() {

	println!("Podaj trzy liczby oddzielone spacjami:");
	let mut line = String::new();
	std::io::stdin().read_line(&mut line).unwrap();
	let liczby: Vec<i32> = line.trim().split(' ').map(|x| x.parse::<i32>().unwrap()).collect();

	let mut liczba_a = liczby[0];
	let mut liczba_b = liczby[1];
	let mut liczba_c = liczby[2];

	if liczba_a >= liczba_b {
		if liczba_b >= liczba_c {
			println!("{} {} {}", liczba_a, liczba_b, liczba_c);
		} else if liczba_a >= liczba_c {
			println!("{} {} {}", liczba_a, liczba_c, liczba_b);
		} else {
			println!("{} {} {}", liczba_c, liczba_a, liczba_b);
		}
	} else {
		if liczba_a >= liczba_c {
			println!("{} {} {}", liczba_b, liczba_a, liczba_c);
		} else if liczba_b >= liczba_c {
			println!("{} {} {}", liczba_b, liczba_c, liczba_a);
		} else {
			println!("{} {} {}", liczba_c, liczba_b, liczba_a);
		}
	}

}

