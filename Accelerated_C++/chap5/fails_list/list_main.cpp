

#include <list>
#include <string>
#include <algorithm>

#include "grade.h"
#include "Student_info.h"
#include "extract_fails.h"

using std::max;
using std::cin;
using std::cout;
using std::endl;
using std::list;
using std::string;


int main()
{
  list<Student_info> students;
  Student_info s;
  string::size_type maxlen;
  while (read(cin,s))
    {
      maxlen = max(maxlen, s.name.size());
      students.push_back(s);
    }

  students.sort(compare);

  list<Student_info> students_failed = extract_fails(students);

  list<Student_info>::iterator i;
  
  for (i=students_failed.begin(); i != students_failed.end(); ++i)
    cout << i->name << " " << grade(*i) << endl;
  
  return 0;
  
}
