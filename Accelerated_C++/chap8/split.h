

#ifndef SPLIT_H
#define SPLIT_H 1

#include <string>
#include <algorithm>
#include <cctype>

#include "split.h"

using namespace std;


inline bool space(char c)
{
        return isspace(c);
}

inline bool not_space(char c)
{
        return !isspace(c);
}


template <class Out> 
void split(const string& str, Out os)
{
  string::const_iterator i = str.begin();
  while (i != str.end())
    {
      i = find_if(i, str.end(), not_space);
      string::const_iterator j = find_if(i, str.end(), space);
      if (i != str.end())
        *os++ = string(i,j);
      i = j;
    }
}


#endif
