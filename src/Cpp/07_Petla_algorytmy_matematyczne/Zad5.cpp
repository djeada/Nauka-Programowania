#include <cassert>

/*
Napisz funkcję, która dla otrzymanych dwóch liczb zwróci
ich największy wspólny dzielnik.
*/

int nwdV1(int a, int b) {

  if (b == 0)
    return a;

  return nwdV1(b, a % b);
}

int nwdV2(int a, int b) {

  int c;

  while (b != a % b) {
    c = b;
    b = a % b;
    a = c;

    if (b == 0)
      break;
  }

  return a;
}

void testNwd1() {
  assert(nwdV1(12, 15) == 3);
  assert(nwdV1(15, 12) == 3);
  assert(nwdV1(15, 0) == 15);
  assert(nwdV1(0, 15) == 15);
}

void testNwd2() {
  assert(nwdV2(12, 15) == 3);
  assert(nwdV2(15, 12) == 3);
  assert(nwdV2(15, 0) == 15);
  assert(nwdV2(0, 15) == 15);
}

int main() {

  testNwd1();
  testNwd2();

  return 0;
}
