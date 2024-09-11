#include <fstream>
#include <iostream>
using namespace std;

// Different OSs use different CLI commands to run Python
#ifdef _WIN32
// TODO: If your Windows machine runs Python in CLI with "python" instead of "py", update this line.
const string python = "python";
#else
// TODO: If your Mac/Linux machine runs Python in CLI with "python" instead of "python3", update this line.
const string python = "python3";
#endif

/*
 * Prompts the user for a filename.
 * Allows the user to enter nothing to use the default pic (autumn.jpg).
 * If the file has extension jpg, jpeg, jpe, or png
 * and it exists in the project folder, return it.
 * Otherwise, return the default pic filename.
 */
string get_filename();

/*
 * Prints the main menu of options:
 * (a) flip, (b) mirror, (c) invert, or (d) exit
 */
void print_menu();

/*
 * Prompts the user for one of the options from the menu.
 * Validates input: makes sure the user enters exactly one character
 * and that it is one of the four valid options.
 * If it isn't valid, keep prompting for input until a valid option
 * is entered.
 */
char get_manip_choice();

int main() {
    cout << "Welcome to the image manipulator!" << endl;
    string filename = get_filename();
    cout << "Using file " << filename << "." << endl;
    print_menu();
    char choice = get_manip_choice();
    cout << "Processing. Go to Python program when it opens. May take a few seconds." << endl;
    string command;
    switch (choice) {
        // Use command-line arguments to pass the filename and manip to the Python file
        case 'a': command = python + " ../render.py " + filename + " flip";
            break;
        case 'b': command = python + " ../render.py " + filename + " mirror";
            break;
        case 'c': command = python + " ../render.py " + filename + " invert";
            break;
    }
    system(command.c_str());
    return 0;
}

void print_menu(){
    cout << "How to manipulate your image" << endl;
    cout << "(a) flip, (b) mirror, (c) invert, or (d) exit" << endl;
}

char get_manip_choice(){
    char choice;
    cin >> choice;
    choice = tolower(choice);
    while(choice != 'a' && choice != 'b' && choice != 'c' && choice != 'd'){
        cout << "Invalid input please enter a valid input" << endl;
        print_menu();
        cin >> choice;
    }
    return choice;
}

string get_filename(){
    string filename;
    cout << "Enter the name of the image file you want to Manipulate" << endl;
    cout << "Please be sure to put the extention on the end the file name" << endl;
    cout << "Enter: ";
    cin >> filename;
    string filenamecheck = filename.substr(filename.find('.'), filename.size());
    cout << filenamecheck << endl;
    if(!(filenamecheck.compare(".jpg") == 0 || filenamecheck.compare(".jpeg") == 0 || filenamecheck.compare(".jpe") == 0 || filenamecheck.compare(".png") == 0)){
        filename = "autumn.jpg";
    }
    return filename;
}