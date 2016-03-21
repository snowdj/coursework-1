

#ifndef PTR_HPP
#define PTR_HPP 1

#include <cstddef>
#include <stdexcept>


template <class T> class Ptr
{
public:
  //constructors
  Ptr(): p(0), refptr(new size_t(1)) { }
  Ptr(T* t): p(t), refptr(new size_t(1)) { }
  Ptr(const Ptr& h): p(h.p), refptr(h.refptr)   //copy constructor
  {
    ++*refptr;
  }
  Ptr& operator=(const Ptr&); // assignment operator
  ~Ptr(); //destructor

  // pointer-like operators
  T& operator*() const;
  T* operator->() const;
  operator bool() const 
  {
    return p;
  }

  // make a new copy when needed
  void make_unique()
  {
    if (*refptr != 1)
      {
	--*refptr;
	refptr = new size_t(1);
	p = p ? clone(p) : 0;
      }
  }

private:
  T* p;
  std::size_t* refptr;
};




template <class T> 
T* clone(const T* tp)
{
  return tp -> clone();
}

template <class T> 
T& Ptr<T>::operator*() const
{
  if (p)
    return *p;
  throw
    std::runtime_error("unbound Ptr");
}

template <class T>
T* Ptr<T>::operator->() const
{
  if (p)
    return p;
  throw
    std::runtime_error("unbound Ptr");
}

template <class T>
Ptr<T>& Ptr<T>::operator=(const Ptr& rhs)
{
  ++*rhs.refptr;
  if (--*refptr == 0)
    {
      delete refptr;
      delete p;
    }

  refptr = rhs.refptr;
  p = rhs.p;
  return *this;
  
}

template <class T>
Ptr<T>::~Ptr()
{
  if (--*refptr == 0)
    {
      delete refptr;
      delete p;
    }
}



#endif
