# 1. Input API

- [1. Input API](#1-input-api)
  - [1.1. A Brief Description of Input API](#11-a-brief-description-of-input-api)
  - [1.2. Basic Usage](#12-basic-usage)
    - [1.2.1. Numerical input](#121-numerical-input)
    - [1.2.2. Clearing the terminal](#122-clearing-the-terminal)
    - [1.2.3. Boolean input](#123-boolean-input)
  - [1.3. Advanced Usage](#13-advanced-usage)
    - [1.3.1. Numbers](#131-numbers)
      - [1.3.1.1. Integers](#1311-integers)
        - [1.3.1.1.1. The newLineInt input](#13111-the-newlineint-input)
        - [1.3.1.1.2. The sameLineInt input](#13112-the-samelineint-input)
        - [1.3.1.1.3. Error treatment and handling](#13113-error-treatment-and-handling)
      - [1.3.1.2. Floating point](#1312-floating-point)
        - [1.3.1.2.1. newLineFloat input](#13121-newlinefloat-input)
        - [1.3.1.2.2. sameLineFloat](#13122-samelinefloat)
        - [1.3.1.2.3. Error treatment and handling](#13123-error-treatment-and-handling)
    - [1.3.2. Strings](#132-strings)
      - [1.3.2.1. newLineStr](#1321-newlinestr)
      - [1.3.2.2. sameLineStr](#1322-samelinestr)
      - [1.3.2.3. Error treatment and handling](#1323-error-treatment-and-handling)
    - [Booleans](#booleans)
      - [yesNo](#yesno)
      - [Error treatment and handling](#error-treatment-and-handling)

## 1.1. A Brief Description of Input API

Input API is a python package made and maintained by Nathan K for the express purpose of making terminal I/O both easier and simpler! When using Input API you are given several options for input, including but not limited to:

- Numbers
  - Both integers and floating point numbers
- Booleans
- Strings
- Menus

## 1.2. Basic Usage

Now for all of the examples of use we will be importing like so:

```python
import inputapi as inp
```

Note: This way of importing is easier for IDE's that don't have an "Auto-Complete" or "AI-assisted dev." feature

When importing Input API we have what is called 'The Basic Library'.
The Basic Library while making usage easier it is also backwards compatible with 1.X versions of Input API without having to rewrite the code.

### 1.2.1. Numerical input

With numerical input you can access both floating point and integer numbers!
An integer input is used as shown:

```python
import inputapi as inp

inp.newLineInt({params})
```

Note: We will cover parameters in [Advanced Usage](#13-advanced-usage)

Floating point numbers can be used as shown:

```python
import inputapi as inp

inp.newLineInt({params})
```

### 1.2.2. Clearing the terminal

If you wish to clear the terminal by using the clearScreen function[^1]:

```python
import inputapi as inp

inp.clearScreen()
```

### 1.2.3. Boolean input

If you need a boolean input we have out yesNo function for that exact reason!

```python
import inputapi as inp

inp.yesNo({params})
```

Fun Fact[^3]: yesNo is the only input to be in the boolean category making it the loneliest function in the package!

## 1.3. Advanced Usage

This style of usage is good for if you need specific input. We will also include the parameters for the inputs with examples.

### 1.3.1. Numbers

#### 1.3.1.1. Integers

Integers serve the purpose of returning integers, integers have two ways to input:

| Type of input |              Best case for use              |
| :------------ | :-----------------------------------------: |
| New Line      |    When there are small amounts of input    |
| Same Line     | When there is a lot of inputs in succession |

##### 1.3.1.1.1. The newLineInt input

There are two ways to use this input:

```python
import inputapi as inp

#This is the basic way of using newLineInt
inp.newLineInt({params})
```

```python
import inputapi as inp

#This is the advanced way of using newLineInt
inp.numerical.integer.newLineInt({params})
```

newLineInt will output the request like this:

```python
#For this example the request string is "Number:"

Number:
>
#The ">" is where the user will input the number
```

The parameters for the input are as follows:

| Parameter     | data type | default               | Purpose it serves                                           |
| :------------ | :-------- | :-------------------- | :---------------------------------------------------------- |
| request       | string    | `"Input an integer:"` | What the user will see when the input is requested          |
| allowNeg      | boolean   | `True`                | Determines if the user can give a negative number           |
| min           | integer   | No limit              | What is the lowest number allowed                           |
| max           | integer   | No limit              | What is the highest number allowed                          |
| clearOnLoad   | boolean   | `False`               | When the function is run, should the terminal be cleared    |
| clearWhenDone | boolean   | `False`               | When the input is retrieved, should the terminal be cleared |

##### 1.3.1.1.2. The sameLineInt input

The sameLineInt has only one way to access the function:

```python
import inputapi as inp

inp.numerical.integer.sameLineInt({params})
```

This is what sameLineInt will output:

```python
#For this example we will have two requests, one will be "X=" and the other will be "Y="

#This is the first request
X=
#And when "X" has been given the next request is shown
Y=

#The user will enter the number at the end of the string
```

You can find the parameters [here](#13111-the-newlineint-input)

##### 1.3.1.1.3. Error treatment and handling

When the inputs face invalid characters, we have error messages to show the user what is allowed and what isn't:

```python
#This error message will appear when the user inputs an invalid character, in this case we will put a decimal in

Number:
>21.6
WARNING: Invalid character ['.'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
```

```python
#This one will be displayed when inputing a negative number when negative numbers are disabled


X=-16
WARNING: Invalid character ['-'], to ensure the program runs correctly please enter only these characters ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

```python
#For this example we will put in a number under the minimum

Y=4
WARNING: Number [4] below minimum [5]
```

For going over the max there are two messages.  
What is picked is depending on the amount of digits for both max and what is entered:

```python
#A number that is greater than max (Same amount of digits as max)

Enter 433724:
>433725
WARNING: Number [433725] above maximum [433724]
```

```python
#We will go above the maximum for this example (More digits than max has)

Enter a 6 digit number:
>581919921
WARNING: Too many characters, maximum amount is [6] characters, you entered [9]
```

#### 1.3.1.2. Floating point

Floating point inputs are great for decimal numbers (e.g. The radius of a circle, width of a box).  
We have two ways for requesting an float:

| Type of input |                            Best use case                             |
| :------------ | :------------------------------------------------------------------: |
| newLineFloat  |                 Small amount of inputs in succession                 |
| sameLineFloat | Multiple inputs with each one after another, or retrieving variables |

##### 1.3.1.2.1. newLineFloat input

Calling the function can be done in two ways:

```python
import inputapi as inp

#Basic usage
inp.newLineFloat({params})
```

```python
import inputapi as inp

#Advanced usage
inp.numerical.float.newLineFloat({params})
```

When using newLineFloat you get an output similar to [newLineInt](#13111-the-newlineint-input)

```python
#This time the request is "Number including decimal:"

Number including decimal:
>
```

The parameters for newLineFloat are very similar to integer inputs but are as follows:

| Parameter     | data type | default               | Purpose it serves                                           |
| :------------ | :-------- | :-------------------- | :---------------------------------------------------------- |
| request       | string    | `"Input an integer:"` | What the user will see when the input is requested          |
| allowNeg      | boolean   | `True`                | Determines if the user can give a negative number           |
| min           | integer   | No limit              | What is the lowest number allowed                           |
| max           | integer   | No limit              | What is the highest number allowed                          |
| clearOnLoad   | boolean   | `False`               | When the function is run, should the terminal be cleared    |
| clearWhenDone | boolean   | `False`               | When the input is retrieved, should the terminal be cleared |

##### 1.3.1.2.2. sameLineFloat

sameLineFloat has only one way to be used:

```python
import inputapi as inp

inp.numerical.float.sameLineFloat({params})
```

The input function outputs like so:

```python
#Request string is "Float="

Float=
```

Parameters are found [here](#1312-floating-point).

##### 1.3.1.2.3. Error treatment and handling

For most of these can be found in [the integer's error handling](#13113-error-treatment-and-handling) except for one error.  
When dealing with decimal points ("."), it can't just be blocked, so we have a solution from the 1.X versions of the Input API:

```python
#The conversion from straight string to float only works if all charecters are numbers and there are no more that one decimal point
#So this is what will happen if we try to break it

Only one decimal point:
>2.2.2
#The result is 2.22
```

How this works is when there is more than one point (e.g. `1.2.3`), it will only acknowledge the first decimal place and remove the others (`1.2.3` -> `1.23`).

### 1.3.2. Strings

Strings works like `input()` but allows for more options and helps with error handling so you don't need something like this copy and pasted 20 times:

```python
while True:
  user = input(request)
  try:
    convert(user)
  except:
    continue
  else:
    break
#convert() is the stand in for what you wan't the string converted to
```

Strings were first introduced in Input API version 1.2.0 as newLineStr, got a bug fix in 1.2.1 (Like an hour after 1.2.0 got built).  
Everything[^4] in the Input API is dependant on the string input since it gives more viability and ease of use. There are two types of string input and they are:

| Type of input |                                                                        Best use case                                                                        |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------: |
| newLineStr    |                                                            Small amount of inputs in succession                                                             |
| sameLineStr   | Multiple inputs with each one after another, getting multiple strings, and replacing the character that sits left of the user input (`>`) with something else |

#### 1.3.2.1. newLineStr

newLineStr has (for the thousandth time) two ways to be used:

```python
import inputapi as inp

#First way
inp.newLineStr({params})
```

```python
import inputapi as inp

#Second way
inp.strings.newLineStr({params})
```

When using the newLineStr the user using the program will have this as the output:

```python
#The request, "String:"

String:
>
```

We have the parameters for newLineStr as:

| Parameter     | data type | default             | Purpose                                                                                 |
| :------------ | :-------- | :------------------ | :-------------------------------------------------------------------------------------- |
| request       | string    | `'Input a string:'` | Is displayed when requesting input                                                      |
| minLength     | integer   | `0`                 | Amount of characters needed for input                                                   |
| maxLength     | integer   | None                | Max amount of characters allowed in input                                               |
| allowOnly     | string    | None                | Only allows an input if all characters are within the string, (Does nothing if default) |
| clearOnLoad   | boolean   | `False`             | Clears terminal before loading input                                                    |
| clearWhenDone | boolean   | `False`             | Clears terminal after getting input                                                     |

#### 1.3.2.2. sameLineStr

sameLineStr has only one way to be used:

```python
import inputapi as inp

#Only way
inp.strings.sameLineStr({params})
```

The output for sameLineStr is:

```python
#The request, "String="
String=
```

The parameters for sameLineStr are:
| Parameter | data type | default | Purpose |
| :------------ | :-------- | :---------- | :-------------------------------------------------------------------------------------- |
| request | string | `'String='` | Is displayed when requesting input |
| minLength | integer | `0` | Amount of characters needed for input |
| maxLength | integer | None | Max amount of characters allowed in input |
| allowOnly | string | None | Only allows an input if all characters are within the string, (Does nothing if default) |
| clearOnLoad | boolean | `False` | Clears terminal before loading input |
| clearWhenDone | boolean | `False` | Clears terminal after getting input |

#### 1.3.2.3. Error treatment and handling

When it comes to error handling on strings, we have three potential errors that can happen:

```python
#This happens when the user inputs less than the minimum amount of characters

Just enter three characters:
>No
WARNING: Input requires [3] characters or more, you entered [2]
```

```python
#This happens when the user inputs more than the maximum amount of characters

Three characters or less:
>Four
WARNING: Input requires [3] characters or less, you entered [4]
```

There are three separate messages related to `allowOnly` depending on length of the amount allowed:

```python
#When there is less than 20 characters allowed
#In this case there is only numbers allowed

Number=Boo!
WARNING: Input has invalid character [B], allowed characters are [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

```python
#When there is more than 30 characters allowed
#In this case there is only letters and numbers allowed

Enter only what a normal person would:
>!@\#$%^&*()_+-=
WARNING: Input has invalid character [!], allowed characters are [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t ... 5, 6, 7, 8, 9]
```

```python
#This is what happens when there is more than 20 but less than 30 characters allowed
#In this case there is only lowercase letters and isn't 'a' allowed

Please don't yell:
>AAAAA
WARNING: Input has invalid character [A], allowed characters are [b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u ... z]
```

### Booleans

The only boolean input there is is `yesNo` which is a boolean input that only allows for `y` or `n` as input. When input is given it will turn it into a boolean value (`True` or `False`).

The Booleans best case use is for when you want to get a yes or no answer from the user. It is also used in the `confirm` input. (Refer to menus for more info about confirming input [Placeholder Link For Menus])

#### yesNo

yesNo has two ways to be used:

```python
import inputapi as inp

#The simple way
inp.yesNo({params})
```

```python
import inputapi as inp

#The hard way
inp.boolean.yesNo({params})
```

yesNo has two different outputs:

```python
#When numeric input is allowed (default)
#This is was added in 2.0.0

#Request is 'Do you breathe air?'
Do you breathe air?
Numeric response allowed (Y=1, n=2)
[Y/n]:
```

```python
#When numeric isn't allowed
#Request is 'Is your fride running'

Is your fridge running?
[Y/n]:
```

The parameters for yesNo are:
| Parameter     | data type | default        | Purpose                              |
| :------------ | :-------- | :------------- | :----------------------------------- |
| request       | string    | `'Yes or no?'` | Is displayed when requesting input   |
| numeric       | boolean   | `True`         | Allows for numeric input (Y=1, n=2)  |
| clearOnLoad   | boolean   | `False`        | Clears terminal before loading input |
| clearWhenDone | boolean   | `False`        | Clears terminal after getting input  |

#### Error treatment and handling

The errors in yesNo mainly happen through the sameLineStr but they are:

```python
#When something not allowed is entered (Numeric allowed)

Did you catch the fridge?
Numeric response allowed (Y=1, n=2)
[Y/n]:Still trying to
WARNING: Input requires [1] characters or less, you entered [15] characters
WARNING: Input has invalid character [S], allowed characters are [Y, N, y, n, 1, 2]
```

```python
#Something not allowed is entered (Numeric not allowed)

Can you see me?
[Y/n]:Murple
WARNING: Input requires [1] characters or less, you entered [6] characters
WARNING: Input has invalid character [M], allowed characters are [y, n]
```

[^1]:
    clearScreen is does not need any information about the OS to work[^2]
    It will automatically tell what OS is running the code and use the command used by the OS to clear the terminal

[^2]: Feature is only supported on Windows, MacOS, and Linux based systems
[^3]: Fun Fact's although being labeled as "Fun" is more fact than fun and could be a "Sad Fact" depending on the fact!
[^4]: Not everything, just what takes input, clearScreen and pause don't rely on it working to function