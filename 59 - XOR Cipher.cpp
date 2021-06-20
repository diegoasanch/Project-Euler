/**
 * Project Euler Problem 59 - XOR Decryption
 *
 * Each character on a computer is assigned a unique code and the preferred
 * standard is ASCII (American Standard Code for Information Interchange). For
 * example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
 *
 * A modern encryption method is to take a text file, convert the bytes to ASCII,
 * then XOR each byte with a given value, taken from a secret key. The advantage
 * with the XOR function is that using the same encryption key on the cipher
 * text, restores the plain text; for example, 65 XOR 42 = 107,
 * then 107 XOR 42 = 65.
 *
 * For unbreakable encryption, the key is the same length as the plain text
 * message, and the key is made up of random bytes. The user would keep the
 * encrypted message and the encryption key in different locations, and without
 * both "halves", it is impossible to decrypt the message.
 *
 * Unfortunately, this method is impractical for most users, so the modified
 * method is to use a password as a key. If the password is shorter than the
 * message, which is likely, the key is repeated cyclically throughout the
 * message. The balance for this method is using a sufficiently long password
 * key for security, but short enough to be memorable.
 *
 * Your task has been made easy, as the encryption key consists of three lower
 * case characters. Using p059_cipher.txt (right click and 'Save Link/Target
 * As...'), a file containing the encrypted ASCII codes, and the knowledge that
 * the plain text must contain common English words, decrypt the message and
 * find the sum of the ASCII values in the original text.
 **/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>

using std::cout;
using std::cerr;
using std::cin;
using std::endl;
using std::ifstream;
using std::string;
using std::vector;
using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::milliseconds;

bool areEqual(char toFind[], char current[], int size, int currentIndex);
bool testKey(ifstream &file, char key[3], char toFind[], int toFindSize);
string arrayToString(char arr[], int size);
void insertLastChar(char arr[], int size, int &start, char newChar);
void printDecryptedFile(ifstream &file, char key[3]);
void findKey(ifstream &file, char toFind[], int toFindSize);
void stringToArray(string from, char to[]);

int main() {
    string fileName = "p_059_cipher.txt";
    ifstream file;
    file.open(fileName);
    if (!file) {
        cerr << "Could not open file \"" << fileName << '"' << endl;
        return 1;
    }

    cout << "Type word to find in decrypted file: ";
    string word;
    cin >> word;

    // Timing
    auto start = high_resolution_clock::now();

    char* toFind = new char[word.length()];
    stringToArray(word, toFind);
    findKey(file, toFind, word.length());
    delete[] toFind;
    file.close();

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    float seconds = (float) duration.count() / 1000;
    cout << "Runtime: " << seconds << " seconds." << endl;
}

void stringToArray(string from, char to[]) {
    for (int i = 0; i < from.length(); i++)
        to[i] = from.at(i);
}

string arrayToString(char arr[], int size) {
    string out = "";
    for (int i = 0; i < size; i++)
        out += arr[i];
    return out;
}

void findKey(ifstream &file, char toFind[], int toFindSize) {
    char key[3];
    string foundKey;
    int found = 0;

    for (int i = 97; i < 123; i++) {
        key[0] = i;
        for (int j = 97; j < 123; j++) {
            key[1] = j;
            for (int k = 97; k < 123; k++) {
                key[2] = k;
                if (testKey(file, key, toFind, toFindSize)) {
                    found++;
                    foundKey = arrayToString(key, 3);
                    cout << "\nfound key: \"" << foundKey << "\"\n";

                    printDecryptedFile(file, key);
                }
            }
        }
    }
    cout << "Found: " << found << " Key" << ((found > 1) ? "s" : "") << '\n';
}

bool testKey(ifstream &file, char key[3], char toFind[], int toFindSize) {
    int num;
    int numIndex = 0;
    int currentKey;
    int keyLen = 3;
    char currentChar;
    bool isKey = false;

    char* currentWord = new char[toFindSize];
    int currentWordIndex = 0;

    file.clear();
    file.seekg(0);

    while (!file.eof()) {
        file >> num;
        currentKey = key[numIndex++ % keyLen];
        currentChar = (char) (num ^ currentKey);

        insertLastChar(currentWord, toFindSize, currentWordIndex, currentChar);

        if (areEqual(toFind, currentWord, toFindSize, currentWordIndex)) {
            isKey = true;
            break;
        }
    }
    delete[] currentWord;
    return isKey;
}

// Using the array circularly
void insertLastChar(char arr[], int size, int &start, char newChar) {
    if (start == size - 1)
        start = 0;
    else
        start++;
    int index;
    if (start > 0)
        index = start-1;
    else
        index = size-1;
    arr[index] = newChar;
}

bool areEqual(char toFind[], char current[], int size, int currentIndex) {
    bool eq = true;
    int i = 0;
    while (i < size && eq) {
        eq = toFind[i++] == current[currentIndex++];
        if (currentIndex == size)
            currentIndex = 0;
    }
    return eq;
}

void printDecryptedFile(ifstream &file, char key[3]) {
    int num;
    int numIndex = 0;
    int currentKey;
    int keyLen = 3;
    int XORed;
    char currentChar;

    file.clear();
    file.seekg(0);

    long ascii_sum = 0;

    while (!file.eof()) {
        file >> num;
        currentKey = key[numIndex++ % keyLen];
        XORed = num^currentKey;
        ascii_sum += XORed;
        currentChar = (char) XORed;

        cout << currentChar;
    }
    cout << "\n\nASCII sum: " << ascii_sum << "\n\n\n";
}
