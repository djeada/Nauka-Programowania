/*
Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.
*/

use ::std::*;

fn main() {

	println!("Podaj dwie liczby oddzielone spacjami.");
	let mut wiersz = String::new();
	std::io::stdin().read_line(&mut wiersz).unwrap();
	let liczby: Vec<i32> = wiersz.trim().split(' ').map(|x| x.parse::<i32>().unwrap()).collect();

	if liczby[0] > liczby[1] {
		println!("{} {}", liczby[0], liczby[1]);
	} else {
		println!("{} {}", liczby[1], liczby[0]);
	}
	
}
