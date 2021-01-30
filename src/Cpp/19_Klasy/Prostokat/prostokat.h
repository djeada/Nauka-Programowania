class Prostokat {
	public:
		Prostokat(double lewo, double prawo, double gora, double dol); 
		double getLewo();
		double getPrawo();
		double getGora();
		double getDol();
		double poleCzesciWspolnej(Prostokat& innyProstokat); 

	private:
		double lewo, prawo, gora, dol;
};
