# Calculator

## Table of Contents
* [ General information ](#general_info)
* [Setup](#setup)
* [Code Description](#code-descript)
  * [runner.py](#runner)
  * [string_scanner.py](#scanner)
  * [string_parser.py](#parser)
  * [string_analyzer.py](#analyzer)
  * [string_interpreter.py](#interpreter)
* [License](#license)

<a name="general_info"></a>
## General Information 
In this repository there is a simple calculator that takes as input an operation and outputs the result of the operation.

For example, given the operation "3 * 6 =" this is a multiplication operation. The result of this operation is 18. The result is printed in the console.

<a name="setup"></a>
## Setup
The code can be run from the runner.py file.
<a name="code-descript"></a>
## Code Description
<a name="runner"></a>
### **1. runner.py**

#### 1.1. Input Format:
Write the operation that you would like to calculate that follows the format:

A.&nbsp; integer operator integer (=) &nbsp;&nbsp;&nbsp;(e.g., 18 % 6 =) 

B.&nbsp; x = 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y = 7&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x + y =

#### 1.2. Constraints:
You can introduce one operator_sign from the list -> [+, -, \*, \/, %]

#### 1.3. Output Format:
The result of the operation is printed on the console.

<br><br />
The code goes through 4 phases: scanning, parsing, analyzing, interpreting.
<a name="scanner"></a>
### **2. string_scanner.py**
The code in this file scans the introduced operation and outputs a list of &nbsp;'ScannerStringSegment'&nbsp; objects. Each object has the attributes:
<br><br />
token = one from the list [Integer, Space, Plus, Minus, Division Sign, Modulo Sign, Equal, Multiplication Sign, Variable] <br />
start_string = the matched string <br />
index and end_string are the numbers where the element begins and ends in the string.

<a name="parser"></a>
### **3. string_parser.py**

The code in this file displays the specific, pre-set BNF Grammar that is followed to match the elements in the scanned list.



*The BNF Grammar for this Calculator is:*

**root** = operation/variable_definition<br />
**operation** = integer operator integer (equal) / variable_symbol operator variable_symbol<br />
**variable_definition** = variable_symbol equal integer<br />
**integer** = non-fractional numbers<br />
**operator** = one element of the list [+, -, \*, \/, %]<br />
**equal** = '='<br />
**variable_symbol** = letters/words<br />
**letter** = [A-Z; a-z]<br />
**word** = any word in the English language<br />

The output after this step is a `'parse tree of grammar production objects'` that reflects the grammar specified above (e.g., Operation(AddExpression(Integer(5), Integer(4))))

<a name="analyzer"></a>
### **4. string_analyzer.py**

The role of the code in this file is to search for, find, and correct semantic mistakes. The semantic mistakes are errors that are grammatically correct, but do not make sense as a whole.

The file takes the 'parse tree of grammar production objects', analyzes each object in the expression, and outputs the analyzed tree.

<a name="interpreter"></a>
### **5. string_interpreter.py**

The role of the code in this file is to interpret the analyzed tree and to output the result of the operation.

## License <a name="license"></a>
This project is licensed under the MIT License - see the LICENSE.md file for details.
