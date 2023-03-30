fn sort_v1(lista: &mut [i32]) {

	for i in 0..lista.len() {
		for j in (i + 1)..lista.len() {
			if lista[i] > lista[j] {
				lista.swap(i, j);
			}
		}
	}
}

fn sort_v2(lista: &mut [i32]) {
    let mut nowa_dl: usize;
    let mut dl = lista.len();
    loop {
        nowa_dl = 0;
        for i in 1..dl {
            if lista[i - 1] > lista[i] {
                lista.swap(i - 1, i);
                nowa_dl = i;
            }
        }
        if nowa_dl == 0 {
            break;
        }
        dl = nowa_dl;
    }
}

fn test_1() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v1(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn test_2() {
    let mut lista = vec![4, 2, 5, 3, 1];
    sort_v2(&mut lista);
    assert_eq!(lista, &[1, 2, 3, 4, 5]);
}

fn main() {
	test_1();
	test_2();
}

