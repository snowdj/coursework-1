
#include <iostream>

#include "Student_info.hpp"


Student_info::Student_info(const Student_info&s): cp(0)  //copy constructor
{
  if (s.cp)
    cp = s.cp -> clone();
} 

Student_info& Student_info::operator=(const Student_info& s) //assignment operator
{
  if (&s != this)
    {
      delete cp;
      if (s.cp)
	cp = s.cp -> clone();
      else
	cp = 0;
    }
  return *this;
}


std::istream& Student_info::read(std::istream& is)
{
  delete cp; // have to delete previous object as we don't know if the new one is Core or Grad.
  
  char ch;
  is >> ch;
  
  if (ch == 'U')
    cp = new Core(is);
  else
    cp = new Grad(is);
  
  return is;
}


