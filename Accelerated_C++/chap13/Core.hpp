

#ifndef CORE_HPP
#define CORE_HPP 1


#include <iostream>
#include <vector>
#include <string>



class Core
{
friend class Student_info;

public:
  // constructors
  Core(): midterm(0), final(0) { }
  Core(std::istream& is) 
  {
    read(is);
  }

  // interface
  std::string name() const;
  virtual std::istream& read(std::istream&);
  virtual double grade() const;
  
  // destructor
  virtual ~Core()
  { 
  }

protected:
  // attributes
  double midterm, final;
  std::vector<double> homework;

  // utilities
  std::istream& read_common(std::istream&);

  std::istream& read_hw(std::istream&, std::vector<double>&);

  virtual Core* clone() const
  {
    return new Core(*this);
  }

private:
  std::string n;
};



class Grad: public Core
{
public:
  // constructors
  Grad(): thesis(0) { }
  Grad(std::istream& is) 
  {
    read(is);
  }

  //interface
  std::istream& read(std::istream&);
  double grade() const;

private:
  double thesis;

  Grad* clone() const 
  {
    return new Grad(*this);
  }

};

double grade(double, double, double);

double grade(double, double, std::vector<double>&);






#endif
