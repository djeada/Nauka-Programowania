fn sort_v1(lista: &mut [i32]) {

	let srodek = lista.len() / 2;

	if srodek == 0 {
		return;
	}

	sort_v1(&mut lista[..srodek]);
	sort_v1(&mut lista[srodek..]);

	let mut ret = lista.to_vec();
	polacz(&lista[..srodek], &lista[srodek..], &mut ret[..]);
	lista.copy_from_slice(&ret);
}

fn polacz(lista_a: &[i32], lista_b: &[i32], ret: &mut [i32]) {
    let mut lewo = 0;
    let mut prawo = 0;
    let mut i = 0;

    while lewo < lista_a.len() && prawo < lista_b.len() {
        if lista_a[lewo] <= lista_b[prawo] {
            ret[i] = lista_a[lewo];
            i += 1;
            lewo += 1;
        } else {
            ret[i] = lista_b[prawo];
            i += 1;
            prawo += 1;
        }
    }

    if lewo < lista_a.len() {
        ret[i..].copy_from_slice(&lista_a[lewo..]);
    }

    if prawo < lista_b.len() {
        ret[i..].copy_from_slice(&lista_b[prawo..]);
    }
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
	test_1();
}

