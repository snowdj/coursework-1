

#include <vector>
#include <iterator>
#include <algorithm>

#include "Student_info.h"
#include "grade.h"

using std::vector;
using std::remove_if;
using std::remove_copy_if;
using std::back_inserter;

vector<Student_info> extract_fails(vector<Student_info>& students)
{
  vector<Student_info> fail;
  remove_copy_if(students.begin(), students.end(), back_inserter(fail), pgrade);
  students.erase(remove_if(students.begin(), students.end(), fgrade), students.end());
  return fail;
  
}
