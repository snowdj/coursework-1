

#ifndef PIC_HPP
#define PIC_HPP 1

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include "Ptr.hpp"


class Picture; //forward declaration

class Pic_base
{
  friend std::ostream& operator<<(std::ostream&, const Picture&);
  friend class Frame_Pic;
  friend class HCat_Pic;
  friend class VCat_Pic;
  friend class String_Pic;

public:
  virtual ~Pic_base() {}

  //abstract base class. no constructor
private:
  typedef std::vector<std::string>::size_type ht_sz;
  typedef std::string::size_type wd_sz;
  
  // pure virtual functions
  virtual wd_sz width() const = 0;
  virtual ht_sz height() const = 0;
  virtual void display(std::ostream&, ht_sz, bool) const = 0;

protected:
  static void pad(std::ostream& os, wd_sz, wd_sz);

};

class String_Pic: public Pic_base 
{
  friend class Picture;

private:
  // attribute (data)
  std::vector<std::string> data;

  //constructor
  String_Pic(const std::vector<std::string>& v): data(v) {}

  // redefine all virtual functions from abstract base class
  ht_sz height() const 
  {
    return data.size();
  }
  
  wd_sz width() const;
  
  void display(std::ostream&, ht_sz, bool) const;
};


class VCat_Pic: public Pic_base
{
  friend Picture vcat(const Picture&, const Picture&);

private:
  // attributes
  Ptr<Pic_base> top, bottom;
  
  //constructor
  VCat_Pic(const Ptr<Pic_base>& t, const Ptr<Pic_base>& b): top(t), bottom(b) {}

  // redefine all virtual functions from abstract base class
  wd_sz width() const
  {
    return std::max(top -> width(), bottom -> width());
  }

  ht_sz height() const
  {
    return top -> height() + bottom -> height();
  }

  void display(std::ostream&, ht_sz, bool) const;
};


class HCat_Pic: public Pic_base 
{
  friend Picture hcat(const Picture&, const Picture&);

private:
  //attributes
  Ptr<Pic_base> left, right;
  //constructor
  HCat_Pic(const Ptr<Pic_base>& l, const Ptr<Pic_base>& r): left(l), right(r) {}

  // redefine all virtual functions from abstract base class
  wd_sz width() const
  {
    return left -> width() + right -> width();
  }

  ht_sz height() const
  {
    return std::max(left -> height(), right -> height());
  }

  void display(std::ostream&, ht_sz, bool) const;
};


class Frame_Pic: public Pic_base
{
  friend Picture frame(const Picture&);

private:
  //attribute
  Ptr<Pic_base> p;
  //constructor
  Frame_Pic(const Ptr<Pic_base>& pic): p(pic) {}

  // redefine all virtual functions from abstract base class
  wd_sz width() const 
  {
    return p -> width() + 4;
  }
  
  ht_sz height() const
  {
    return p -> height() + 4;
  }
  
  void display(std::ostream&, ht_sz, bool) const;
};
  

class Picture 
{
  friend std::ostream& operator<<(std::ostream&, const Picture&);
  friend Picture frame(const Picture&);
  friend Picture hcat(const Picture&, const Picture&);
  friend Picture vcat(const Picture&, const Picture&);
  
public:
  // constructor from a string vector
  Picture(const std::vector<std::string>& = std::vector<std::string>());

private:
  // attribute:
  Ptr<Pic_base> p;
  // constructor from a pointer to Pic_base derived class
  Picture(Pic_base* ptr): p(ptr) {}
};


// operation functions on Picture 
Picture frame(const Picture&);
Picture hcat(const Picture&, const Picture&);
Picture vcat(const Picture&, const Picture&);
std::ostream& operator<<(std::ostream&, const Picture&);





#endif






