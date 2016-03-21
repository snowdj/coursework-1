

#ifndef STUDENT_INFO_HPP
#define STUDENT_INFO_HPP 1


#include <iostream>
#include <string>
#include <stdexcept>

#include "Core.hpp"
#include "Ptr.hpp"


class Student_info 
{
public:
  //constructors
  Student_info()  {}
  Student_info(std::istream& is) 
  {
    read(is);
  }

  // operations
  std::string name() const
  {
    if (cp)
      return cp -> name();
    else
      throw std::runtime_error("uninitialized student");
  }
  
  std::istream& read(std::istream&);

  double grade() const
  {
    if (cp)
      return cp -> grade();
    else
      throw std::runtime_error("uninitialized student");
  }

  static bool compare(const Student_info& s1, const Student_info& s2)
  {
    return s1.name() < s2.name();
  }

private:
  Ptr<Core> cp;

};



std::istream& Student_info::read(std::istream& is)
{
  char ch;
  is >> ch;
  
  if (ch == 'U')
    cp = new Core(is);
  else
    cp = new Grad(is);

  return is;
  
}





#endif
