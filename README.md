# Calculator

## Table of Contents
* [General information](#general-info)
* [Setup](#setup)
* [Code Description](#code-descript)
  * [Runner.py](#runner)
  * [StringScanner.py](#scanner)
  * [StringParser.py](#parser)
  * [StringAnalyzer.py](#analyzer)
  * [StringInterpreter.py](#interpreter)
* [License](#license)

## [General Information]
In this repository there is a simple calculator that takes as input an operation and outputs the result of the operation.

For example, given the operation "3 * 6 =" this is a multiplication operation. The result of this operation is 18. The result is printed in the console.


## Setup
The code can be run from the runner.py file.

## Code Description

### **1. Runner.py**

#### 1.1. Input Format:
Write the operation that you would like to calculate that follows the format: int1 operator_sign int2 (equal_sign).

#### 1.2. Constraints:
-∞ < int < ∞
accepted operator_sign is part of the list = [+, -, \*, \/, %]

#### 1.3. Output Format:
The result of the operation is printed on the console.


The fundament of the code consists of 4 files: StringScanner.py, StringParser.py, StringAnalyzer.py, and StringInterpreter.py

### **2. StringScanner.py**
The code in this file scans each element of the operation as a string and outputs a list of tuples under the format (Type_Element, Element, Begin_Number, End_Number)

Type_Element = one from the list [Integer, Space, Plus, Minus, Division Sign, Modulo Sign, Equal, Multiplication Sign]
Element = the element in the string
Begin_Number and End_Number are the numbers where the element begins and ends in the string.


### **3. StringParser.py**

The code in this file follows a specific, pre-set grammar to match the elements in the scanned list (from StringScanner.py).



*The BNF Grammar for this Calculator is:*

root = operation/variable_definition

operation = integer operator integer \*(equal) / variable_symbol operator variable_symbol

variable_definition = variable_symbol equal integer\ variable_symbol equal variable_symbol operator variable_symbol

integer = non-fractional numbers

operator = one element of the list [+, -, \*, \/, %]

equal = '='

variable_symbol = letters/words

letter = [A-Z; a-z]

word = any word in the English language



The output after this step is a `'parse tree of grammar production objects'` that reflects the grammar specified above (e.g., Operation(AddExpression(Integer(5), Integer(4))))


### **4. StringAnalyzer.py**

The role of the code in this file is to search for, find, and correct semantic mistakes. The semantic mistakes are errors that are grammatically correct, but do not make sense as a whole.

The file takes the 'parse tree of grammar production objects', analyzes each object in the expression, and outputs the analyzed  tree.

### **5. StringInterpreter.py**

The role of the code in this file is to interpret the analyzed tree and to output the result of the operation.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details
