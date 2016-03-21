

/* Determine if a string is a palindrome or not. */

#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::equal;
using std::string;
using std::transform;


bool is_palindrome(const string& s)
{
  return equal(s.begin(), s.end(), s.rbegin());
}

int main()
{
  string s;
  while (cin >> s)
    {
      if (is_palindrome(s))
        cout << s << " is a palindrome." << endl;
      else
        cout << s << " is not a plindrome." <<endl;
      
    }
  return 0;
  
}
