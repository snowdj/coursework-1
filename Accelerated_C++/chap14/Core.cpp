

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stdexcept>

#include "Core.hpp"
#include "median.hpp"

using namespace std;


string Core::name() const 
{
  return n;
}

istream& Core::read_common(istream& is)
{
  is >> n >> midterm >> final;
  return is;
}

istream& Core::read_hw(istream& is, vector<double>& hw)
{
  if (is)
    {
      // clear content
      hw.clear();
      
      //read homework grades
      double x;
      while (cin >> x)
	hw.push_back(x);
      
      // clear stream for next student record
      is.clear();
    }
  return is;
}

istream& Core::read(istream& is)
{
  read_common(is);
  read_hw(is, homework);
  return is;
}

istream& Grad::read(istream& is)
{
read_common(is);
is >> thesis;
read_hw(is, homework);
return is;
}

double grade(double midterm, double final, double homework)
{
return 0.2 * midterm + 0.4 * final + 0.4 * homework;
}


double grade(double midterm, double final, vector<double> hw)
{
if (hw.size() == 0)
  throw domain_error("student has done no homework");
return grade(midterm, final, median(hw));
}

double Core::grade() const
{
return ::grade(midterm, final, homework);
}

double Grad::grade() const
{
return min(Core::grade(), thesis);
}



