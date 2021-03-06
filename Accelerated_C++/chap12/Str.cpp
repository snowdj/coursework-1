


#include <cctype>
#include <iostream>
#include <iterator>

#include "Str.h"


using std::istream;
using std::istream_iterator;
using std::ostream;



ostream& operator<<(ostream& os, const Str& s)
{
  for (Str::size_type i = 0; i != s.size(); ++i)
    os << s[i];
  
  return os;
}


istream& operator>>(istream& is, Str& s)
{
  s.data.clear();
  
  char c;
  while (is.get(c) && isspace(c))
    ;
  
  if (is)
    {
      do
	s.data.push_back(c);
      while (is.get(c) && !isspace(c));
      
      if (is)
	is.unget(c);
    }
  return is;
}


Str operator+(const Str& s, const Str& t)
{
  Str r = s;
  r += s;
  return r;
}

istream& getline(istream& is, Str& s)
{
  s.data.clear();
  
  char c;
  while (is.get(c) && isspace(c))
    ;
  
  if (is)
    {
      do
	s.data.push_back(c);
      while (is.get(c) && c != "\n");
      if (is)
	is.unget();
      
    }

  return is;
	
}
