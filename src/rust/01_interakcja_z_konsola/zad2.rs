/*
Dla pobranych od uzytkownika liczb, wypisz najpierw pierwsza, a nastepnie druga
liczbe.
*/

use ::std::*;

fn main() {

	println!("Podaj dwie liczby oddzielone spacjami.");
	let mut wiersz = String::new();
	std::io::stdin().read_line(&mut wiersz).unwrap();
	let liczby: Vec<i32> = wiersz.trim().split(' ').map(|x| x.parse::<i32>().unwrap()).collect();
	println!("{} {}", liczby[0], liczby[1]);
	
}
