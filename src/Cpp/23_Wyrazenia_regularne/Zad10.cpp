#include <string>
#include <cassert>
#include <regex> 
#include <vector>

//Otrzymujez napis i dwie listy napisow. Podmien w pierwszym napisie, napisy z 
//pierwszej listy na odpowiadające im napisy z drugiej listy.

void podmien(std::string& napis, std::vector<std::string>& listaA, std::vector<std::string>& listaB)
{
	if (listaA.size() != listaB.size())
		return;

	auto itA = listaA.begin();
	auto itB = listaB.begin();

	while (itA != listaA.end() || itB != listaB.end()) {
		napis = std::regex_replace(napis, std::regex("\\b" + *itA + "\\b"), *itB);
		++itA;
		++itB;
	}
}

void test1() 
{
	std::string napis = "Every mile was tilted at seven or. Wished her entire esteem mr oh by. He prevents requests by if in pleased. Picture too and concerned was comforting. Ten difficult resembled eagerness nor. Same park bore on be. Warmth his law design says he is a person. Pronunciation suspected in belonging conveying ye repulsive.";

	std::vector<std::string> listaA {"or", "be", "he"};
	std::vector<std::string> listaB {"and", "off", "she"};

	std::string wynik = "Every mile was tilted at seven and. Wished her entire esteem mr oh by. He prevents requests by if in pleased. Picture too and concerned was comforting. Ten difficult resembled eagerness nor. Same park bore on off. Warmth his law design says she is a person. Pronunciation suspected in belonging conveying ye repulsive.";

	podmien(napis, listaA, listaB);

	assert(napis == wynik);	
}

int main() {

	test1();

	return 0;
}
