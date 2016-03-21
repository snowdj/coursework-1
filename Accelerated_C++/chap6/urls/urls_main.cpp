#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

#include "urls.h"

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::find_if;
using std::getline;


int main()
{
  string s;
  while (getline(cin,s))
    {
      vector<string> v = find_urls(s);
      for (vector<string>::const_iterator i = v.begin(); i!=v.end(); ++i)
        cout << *i << endl;
    }
  return 0;
  
}
