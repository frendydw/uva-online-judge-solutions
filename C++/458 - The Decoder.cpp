#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <utility>
#include <set>
#include <math.h>
using namespace std;

int main()
{
     char ch;
     int d;
     while((ch=getc(stdin))!=EOF)
     {
            d=ch;
            if(d==10)
           {
                  printf("\n");
                  continue;
            }
            printf("%c",d-7);
      }
      return 0;
 }
