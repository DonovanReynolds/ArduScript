
# ArduScript

**ArduScript** is a simple scripting language designed to compile into Arduino IDE code. The main goal is to make microcontroller programming accessible for beginners by abstracting away complex features and focusing on ease of use.  
> ⚠️ This is not a replacement for the Arduino IDE, but rather a tool to supplement learning for those new to microcontroller programming.

---

## 🧾 Table of Contents

- [Getting Started]
- [Language Features]
  - [Relational Operators]
  - [Mathematical Operators]
  - [Variables]
  - [Global Variables]
  - [Pin Variables]
  - [If Statements]
  - [Loops]
  - [Pin Control]
    - [setPin]
    - [readPin]
    - [togglePin]
  - [Wait]
  - [Print]
  - [Functions]

---

## 🏁 Getting Started

To run an ArduScript file, use the provided shell command in your terminal or command prompt.

### ✅ Usage

```bash
./compile.sh myscript.ard
```

- Replace `myscript.ard` with the name of your ArduScript file.
- The compiler will generate an output file containing equivalent Arduino C++ code.

### 🚀 Uploading to Arduino

The output file can currently be **copy-pasted into the Arduino IDE**. From there, you can upload it directly to your microcontroller.

> ⚠️ Make sure your board and port are correctly selected in the Arduino IDE before uploading.

---

## 🔤 Language Features

### Relational Operators

Compare numbers or variables. Expressions are parsed left to right, with parentheses for precedence.

**Available Operators:**
- `<`  – less than  
- `>`  – greater than  
- `<=` – less than or equal  
- `>=` – greater than or equal  
- `==` – equal to  

**Logical Operators:**
- `and`
- `or`
- `not`

---

### Mathematical Operators

Perform basic arithmetic.

**Available Operators:**
- `+`  – addition  
- `-`  – subtraction  
- `*`  – multiplication  
- `/`  – division  
- `%`  – remainder  

---

### Variables

All variables are **integers** by default. Variables are **scoped** within blocks defined by `begin` and `end`.

**Syntax:**
```plaintext
VARNAME = number or otherVar
```

**Examples:**
```plaintext
variable = x
buttonPin = 27
x = 25 + 7 * 10
```

---

### Global Variables

Make a variable accessible throughout the entire program.

**Syntax:**
```plaintext
GLOBAL VARNAME
```

**Examples:**
```plaintext
GLOBAL counter
GLOBAL variable
```

---

### Pin Variables

Another way of making a variable accessible throughout the entire program. (More clear syntax for using pins on microcontroller).

**Syntax:**
```plaintext
pin VARNAME
```

**Examples:**
```plaintext
pin counter
pin variable
```

---

### If Statements

Control flow based on relational expressions.

**Syntax:**
```plaintext
if RELATIONAL_EXPRESSION begin
  // code
end
else begin
  // code
end
```

**Examples:**
```plaintext
if x == 17 begin
  y = 4
end
else begin
  y = 1
end

if x < 10 and y < 10 begin
  x = x + 1
end
```

---

### Loops

#### While Loop

Runs while a condition is true.

**Syntax:**
```plaintext
while EXPRESSION begin
  // code
end
```

**Example:**
```plaintext
while x < 5 begin
  x = x + 1
end
```

#### Loop (For Loop Equivalent)

Runs a block a specific number of times.

**Syntax:**
```plaintext
loop LENGTH begin
  // code
end
```

**Examples:**
```plaintext
loop 15 begin
  x = x + 1
end

x = 10
loop x begin
  y = y * 2
end
```

---

### Pin Control

#### setPin

Set a pin to high or low.

**Syntax:**
```plaintext
setPin PIN#, high/low/true/false
```

**Examples:**
```plaintext
setPin 5, high
setPin x, low
setPin 10, false
```

#### readPin

Read input from a pin. Can be used in expressions or assignments.

**Syntax:**
```plaintext
readPin PIN#
```

**Examples:**
```plaintext
if readPin 5 == low begin
  x = 10
end

x = readPin 10  // returns 0 (low) or 1 (high)
```

#### togglePin

Toggle a pin's output between high and low.

**Syntax:**
```plaintext
togglePin PIN#
```

**Examples:**
```plaintext
togglePin 5
togglePin buttonPin
```

---

### wait

Pause execution for a specified number of milliseconds.

**Syntax:**
```plaintext
wait MS
```

**Examples:**
```plaintext
wait 500
wait x
```

---

### print

Print to the serial monitor (9600 baud rate).

**Syntax:**
```plaintext
print("text")
print(VARNAME)
```

**Examples:**
```plaintext
print("Hello World!")
print(x)
```

---

### Functions

Define reusable code blocks. These are only blocks that will be repeatable and have no return value

**Syntax:**
```plaintext
function FUNCTIONNAME(args)
```

**Examples:**
```plaintext
function myfunct()begin
  // code
end

function function2(x)begin
  // code
end

function doStuff(x, y, z)begin
  // code
end
```

To execute the functions made use.

**Examples:**
```plaintext
doStuff(x,y,z)
myfunct()
```

