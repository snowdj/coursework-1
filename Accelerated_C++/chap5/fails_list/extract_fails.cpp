

#include <list>
#include "Student_info.h"
#include "grade.h"
#include "extract_fails.h"

std::list<Student_info> extract_fails(std::list<Student_info>& students)
{
  std::list<Student_info> students_failed;
  std::list<Student_info>::iterator iter = students.begin();
  
  while(iter != students.end())
    {
      if (fgrade(*iter))
                 {
                   students_failed.push_back(*iter);
                   iter = students.erase(iter);
                 }
      else
        ++iter;
    }
  return students_failed;
}
