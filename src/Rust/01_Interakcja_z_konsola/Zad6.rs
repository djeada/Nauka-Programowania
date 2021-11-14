/*
Zamien jednostki:

a) Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.
b) Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.
c) Pobierz liczbe sekund i przelicz na godziny.
d) Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada.
e) Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.
f) Pobierz temperature w stopniach Fahrenheita i wypisz ilu stopniom Celsjusza
oraz ilu stopniom Kelwina odpowiada.
*/

use ::std::*;

fn main() {

	// Podpunkt a)
	println!("Podaj wielkosc w kilogramach: ");
	let mut wielkosc_w_kg = String::new();
	std::io::stdin().read_line(&mut wielkosc_w_kg).expect("Blad odczytu");
	let wielkosc_w_kg: f32 = wielkosc_w_kg.trim().parse().expect("Blad parsowania");
	println!("{} kg to {} gram", wielkosc_w_kg, wielkosc_w_kg * 1000.0);

	// Podpunkt b)
	println!("Podaj wielkosc w calach: ");
	let mut wielkosc_w_calach = String::new();
	std::io::stdin().read_line(&mut wielkosc_w_calach).expect("Blad odczytu");
	let wielkosc_w_calach: f32 = wielkosc_w_calach.trim().parse().expect("Blad parsowania");
	println!("{} cal to {} cm", wielkosc_w_calach, wielkosc_w_calach * 2.54);

	// Podpunkt c)
	println!("Podaj liczbe sekund: ");
	let mut liczba_sekund = String::new();
	std::io::stdin().read_line(&mut liczba_sekund).expect("Blad odczytu");
	let liczba_sekund: f32 = liczba_sekund.trim().parse().expect("Blad parsowania");
	println!("{} sekund to {} godzin", liczba_sekund, liczba_sekund / 3600.0);

	// Podpunkt d)
	println!("Podaj liczbe w euro: ");
	let mut liczba_w_euro = String::new();
	std::io::stdin().read_line(&mut liczba_w_euro).expect("Blad odczytu");
	let liczba_w_euro: f32 = liczba_w_euro.trim().parse().expect("Blad parsowania");
	println!("{} euro to {} zlotych", liczba_w_euro, liczba_w_euro * 4.2);

	// Podpunkt e)
	println!("Podaj miare kata w stopniach: ");
	let mut miare_kata_w_stopniach = String::new();
	std::io::stdin().read_line(&mut miare_kata_w_stopniach).expect("Blad odczytu");
	let miare_kata_w_stopniach: f32 = miare_kata_w_stopniach.trim().parse().expect("Blad parsowania");
	println!("{} stopni to {} radianow", miare_kata_w_stopniach, miare_kata_w_stopniach * 0.0174533);

	// Podpunkt f)
	println!("Podaj temperature w stopniach Fahrenheita: ");
	let mut temperature_w_stopniach_Fahrenheita = String::new();
	std::io::stdin().read_line(&mut temperature_w_stopniach_Fahrenheita).expect("Blad odczytu");
	let temperature_w_stopniach_Fahrenheita: f32 = temperature_w_stopniach_Fahrenheita.trim().parse().expect("Blad parsowania");
	println!("{} stopni Fahrenheita to {} stopni Celsjusza", temperature_w_stopniach_Fahrenheita, (temperature_w_stopniach_Fahrenheita - 32.0) * 5.0 / 9.0);
	println!("{} stopni Fahrenheita to {} stopni Kelwina", temperature_w_stopniach_Fahrenheita, (temperature_w_stopniach_Fahrenheita - 32.0) * 4.0 / 9.0);

}
