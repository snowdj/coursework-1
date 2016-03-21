

#include <vector>
#include <algorithm>

#include "Student_info.h"
#include "grade.h"

using std::vector;
using std::stable_partition;

vector<Student_info> extract_fails(vector<Student_info>& students)
{
  vector<Student_info>::iterator iter = stable_partition(students.begin(), students.end(), pgrade);

  vector<Student_info> fail(iter, students.end());
  
  students.erase(iter, students.end());
  
  return fail;
  
}
