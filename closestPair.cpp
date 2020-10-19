#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;

struct Point {
  float x, y;
};
int c,d;
float closest(Point points[],int index, int n, float distance){
    if(index == n)
        return distance;
    for(int i = index+1; i < n; i++) 
        if(sqrt(pow(points[index].x - points[i].x,2) + pow(points[index].y - points[i+1].y,2)) < distance){
            distance = sqrt(pow(points[index].x - points[i].x,2) + pow(points[index].y - points[i].y,2)* 1.0);
            c = index;
            d = i;
        }
    return closest(points,index+1, n, distance);    
}

int main()
{
    float x,y;
    float distance = 100000;
    while(true){
        int n;
        cin >> n;
        if(n == 0)
            return 0;
        Point points[n];
        Point points2[n];
        vector<int> index;
        for(int i = 0; i < n; i++) {
            cin >> x>>y;
            points[i].x = x;
            points[i].y = y;
            points2[i].x = x;
            points2[i].y = y;
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n-i; j++) {
                if (points[j-1].x > points[j].x) {
                    Point temp = points[j-1];
                    points[j-1] = points[j];
                    points[j] = temp;
                }
            }
        }
        if(n > 2) {
            distance = closest(points, 0, (int)n/2,distance);
            distance = closest(points, (int)n/2, n,distance);

            for (int i = 0; i < n; i++) {
                for (int j = 1; j < n-i; j++) {
                    if (points2[j-1].y > points2[j].y) {
                        Point temp = points2[j-1];
                        points2[j-1] = points2[j];
                        points2[j] = temp;
                    }
                }
            }
            
            for(int i = 0; i < n; i++) {
                if(i == (int)n/2)
                    continue;
                if(sqrt(pow(points[i].x - points[(int)n/2].x,2) + pow(points[i].y - points[(int)n/2].y,2)) < 2*distance)
                    index.push_back(i);
            }
            Point s[index.size()];
            for(int i = 0; i <index.size(); i++) {
                s[i] = points[index.at(i)];
            }
            distance = closest(s, 0, index.size(), distance);
        }
        else
            closest(points, 0, n, distance);
        cout << fixed << setprecision(2);
        cout << points[c].x << ' ' << points[c].y << ' ' << points[d].x << ' ' << points[d].y << endl;
    }
    return 0;
}
