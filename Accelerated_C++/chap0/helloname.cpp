// ask for a person's name, and greet the person
#include <iostream>
#include <string>

int main()
{
    // ask for the person's name
    std::cout << "Please enter your first name: ";

    // read the name
    std::string name;         // define name
    std::cin >> name;         // read into

    // write a greeting
    std::cout << "Hello, " << name << "!" << std::endl;
    const std::string s1 = "abc";
    const std::string s2 = "cde";
    const std::string s3 = s1+" is a word.";
    
    std::cout << s3 << std::endl;

    //test i++ and ++i
    int i=0;int j;
    
    while (i!=10)
      {
	//	std::cout<< i << std::endl;
	//j = i++;
	j = ++i;
	std::cout<< j << std::endl;
	
      }	

    return 0;
}
