fn sort_v1(lista: &mut [i32]) {
	szybkie(lista, 0, lista.len() - 1);
}

fn szybkie(lista: &mut [i32], dol: usize, gora: usize) 
{ 
    if dol < gora { 
	let piwot = podziel(lista, dol, gora);
	szybkie(lista, dol, piwot - 1);
	szybkie(lista, piwot, gora); 
    } 
} 

fn podziel (lista: &mut [i32], dol: usize, gora: usize) -> usize {  
	let indeks = (dol + gora) / 2;
	let piwot = lista[indeks];
	let mut i = dol;
	let mut j = gora;
	while i <= j {
		while lista[i] < piwot {
			i += 1;
		}
		while j > 0 && lista[j] > piwot {
			j -= 1;
		}

		if i <= j{
			lista.swap(i, j);
			i += 1;
			if j == 0 {
				break;
			}
			j -= 1;
		}
	}
	return i; 
} 

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
	test_1();
}
