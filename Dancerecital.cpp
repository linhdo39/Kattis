#include <iostream>
#include <string>

using namespace std;
int count = 0;

int quickchange(string dancer1,string dancer2){
  int quick = 0;
  for(char character:dancer1)
      if (dancer2.find(character) !=string::npos)
        quick +=1;
  return quick;
}

void alignment(string dancer[], int index, int r, int quick) { 
  if (index == r - 1) {
    count = min(quick,count);
    return;
  }
  else {
    int a = 0;
    a = quickchange(dancer[index],dancer[index+1]);
    for (int i = index; i < r; i++){ 
      swap(dancer[index], dancer[i]);
      alignment(dancer, index+1, r,quick+ a); 
      swap(dancer[index], dancer[i]);
      }
  }
}

int main() {
  count = 100000;
  int r;
  cin >> r;
  string dancer [r];
  int quick = 0;
  for(int i = 0; i < r; i++){
    string str;
    cin >> str;
    dancer[i] = str;
  }
  
  alignment(dancer,0,r,quick);
  cout << count;
return 0;
}
