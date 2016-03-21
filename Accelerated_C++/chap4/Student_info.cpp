

// source file for Student_info-related functions

#include "Student_info.h"

using std::istream;
using std::vector;

bool compare(const Student_info& x, const Student_info& y)
{
  return x.name < y.name;
}

istream& read_hw(istream& in, vector<double>& hw)
{
  if (in)
    {
      // get rid of prevous contents
      hw.clear();

      // read homework grades
      double x;
      while (in >> x)
        hw.push_back(x);
      
      //clear the stream so that input will work for the next student
      in.clear();
    }
  return in;
}

istream& read(istream& is, Student_info& s)
{
  //read and store students' names and midterm and final exam grades
  is >> s.name >> s.midterm >> s.final;
  read_hw(is, s.homework);
  return is;
}
