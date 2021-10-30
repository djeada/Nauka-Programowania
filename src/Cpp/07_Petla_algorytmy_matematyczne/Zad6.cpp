#include <cassert>

/*
Napisz funkcję, która dla otrzymanych dwóch liczb 
zwróci ich najmniejszą wspólną wielokrotność.
*/

int nwd(int a, int b) {

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

int nww(int a, int b) { return a * b / nwd(a, b); }

void testNww(){
  assert(nww(12, 15) == 60);
  assert(nww(12, 16) == 48);
  assert(nww(12, 18) == 36);
}

int main() {

  testNww();
  
  return 0;
}
