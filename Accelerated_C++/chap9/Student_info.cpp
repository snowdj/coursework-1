#include <iostream>
#include <vector>


#include "Student_info.h"
#include "grade.h"

using namespace std;


Student_info::Student_info(): midterm(0), final(0) {};

Student_info::Student_info(istream& is) 
{
  read(is);
}


istream& read_hw(istream& is, vector<double>& hw)
{
  if (is)
    {
      hw.clear();
      double x;
      while (is >> x)
        hw.push_back(x);
      is.clear();
    }
  return is;
}


istream& Student_info::read(istream& is)
{
  is >> n >> midterm >> final;
  read_hw(is, homework);
  return is;
}


double Student_info::grade() const
{
  return ::grade(midterm, final, homework);
}


bool compare(const Student_info& x, const Student_info& y)
{
  return x.name() < y.name();
}
