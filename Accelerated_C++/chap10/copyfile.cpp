
#include <fstream>
#include <string>

using std::ifstream;
using std::ofstream;
using std::getline;
using std::endl;
using std::string;



int main(int argc, char** argv)
{
  ifstream source_file(argv[1]);
  ofstream dest_file(argv[2]);
  

  string s;
  while (getline(source_file, s))
    dest_file << s << endl;
  
  return 0;
  
}
