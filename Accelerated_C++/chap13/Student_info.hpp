
/*  handle class for Core{} and Grad{} */

#ifndef STUDENT_INFO_HPP
#define STUDENT_INFO_HPP 1

#include <iostream>
#include <string>
#include <stdexcept>

#include "Core.hpp"

class Student_info 
{
public:
  //constructors
  Student_info(): cp(0) { };
  Student_info(std::istream& is): cp(0) 
  {
    read(is);
  }

  // rule of three
  Student_info(const Student_info&); //copy constructor
  Student_info& operator=(const Student_info&); //assignment operator
  ~Student_info() //destructor
  {
    delete cp;
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
      throw std::runtime_error("unintialized student");
  }

  static bool compare(const Student_info& s1, const Student_info& s2)
  {
    return s1.name() < s2.name();
  }

private:
  Core* cp;
};



#endif
