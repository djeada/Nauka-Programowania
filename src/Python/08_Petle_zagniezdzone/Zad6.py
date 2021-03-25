"""
Wypisz za pomoca petli, litere Z zbudowana z literek 'x'.

Przyklad dla wysokosci 5:
*****
   * 
  *  
 *   
*****
"""

# Wersja 1
def wypiszZV1(wysokosc):
    for j in range(wysokosc):
        for i in range(wysokosc):
            if j == 0 or j == wysokosc - 1:
                print("*", end="")
            elif i == wysokosc - j - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


for i in range(1, 6):
    wypiszZV1(i)
