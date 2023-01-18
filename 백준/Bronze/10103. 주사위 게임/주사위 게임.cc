#include <iostream>
using namespace std;
 
int main() 
{
	int r;
	cin >> r;
	int a,b;
	int pointa = 100;
	int pointb = 100;
 
	for(int i = 0; i < r; i++)
	{
		cin >> a >> b;
		if(a < b)
		{
			pointa -= b;
		}
		if(a > b)
		{
			pointb -= a;
		}
	}
	cout << pointa << endl << pointb;
}