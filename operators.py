# Operators in Python : Operators are used to perform operations on variables and values.

# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations.

print(10+2)  #Addition
print(10-2)  #Subtraction
print(10*2)  #Multiplication
print(10/2)  #Division
print(10//2) #Floor Division
print(10**2) #Exponentionation
print(10%2)  #Modulus

# Python Assignment Operators:
# Assignment operators are used to assign values to variables

x = 12  #Simple assignment operator
print(x)  

# Add and assign
x = 5
x += 3  # x = x + 3 (5 + 3)
print(x)

# Subtract and assign
x = 5
x -= 4 
print(x)

#  Multiply & Assign (*=)
x = 6
x *= 2  # x = x * 2 (6 × 2)
print(x)

# Divide & Assign (/=)
a = 8
a /= 4  # x = x / 4 = 8/ 4 = 2.0
print(a)

# Floor Divide & Assign (//=)
x = 15
x //= 2  # x = x // 2 (15 ÷ 2 = 7.5, sirf 7 lega)
print(x)

#  Modulus & Assign (%=)
x = 10
x %= 3  # x = x % 3 (10 % 3 = 1)
print(x)

# Exponentiation & Assign (**=)
x = 2
x **= 3  # x = x ** 3 (2³ = 8)
print(x)

# &= (Bitwise AND Assignment Operator)
x = 7  
x &= 3  
print(x)

print(bin(50))  

# |= (Bitwise OR Assignment)
# Ye "OR" operation karta hai aur result variable mein store kar deta hai.

a = 5   # (binary: 0101)
b = 3   # (binary: 0011)

a |= b  # a = a | b
print(a)  

#  ^= (Bitwise XOR Assignment)
# Ye XOR operation karta hai (jo alag values pe 1 deta hai).

x = 6  
y = 4   

x ^= y  # x = x ^ y
print(x)  

# >>= (Right Shift Assignment)
# Ye bits ko right shift karta hai (Matlab 2 se divide karta hai).

p = 16  

p >>= 4  # p = p >> 2 (Right shift by 4)
print(p)  

# <<= (Left Shift Assignment)
# Ye bits ko left shift karta hai (Matlab 2 se multiply karta hai).

q = 5   

q <<= 3  # q = q << 3 (Left shift by 3)
print(q)  

# Walrus Operator (Assign + Use) :=
# User se input lena aur uska length check karna

user_input = input("Enter something: ")  # User input 
length = len(user_input)  

if length > 4:
    print(f"✅ Long text! (Length: {length})")
else:
    print(f"❌ Short text! (Length: {length})")

# Comparison Operators

# 1. Equal to (==)
# ✅ Dono values same hain to True, warna False.

a = 10
b = 10
print(a == b)  # ✅ True 

x = 5
y = 3
print(x == y)  # ❌ False

# 2. Not Equal to (!=)
# ✅ Agar values different hain to True, warna False.

a = 10
b = 5
print(a != b) 

x = 7
y = 7
print(x != y)  

# 3. Greater than (>)
#  Agar pehli value badi hai to True, warna False.

print(10 > 5)  
print(3 > 7)   

# 4. Less than (<)
#  Agar pehli value chhoti hai to True, warna False.

print(5 < 10)  
print(8 < 4)   

# 5. Greater than or Equal to (>=)
#  Agar pehli value badi ya equal hai to True, warna False.

print(12>=10)  #True

# 6. Less than or Equal to (<=)
#  Agar pehli value chhoti ya equal hai to True, warna False.

print(5 <= 10)  
print(8 <= 8)  
print(12 <= 7)  

# Logical Operators 

# 1️. and (Logical AND)
# Jab dono conditions True hongi tabhi result True hoga, warna False hoga.

a = 10
b = 20

print(a > 6 and b < 30)  # True (Dono conditions True hain)

#  or (Logical OR)
# Agar koi ek condition bhi True hogi to result True hoga. Sirf dono False honge tabhi result False hoga.

a = 10
b = 20

print(a > 15 or b < 30)  # True (Ek condition True hai)
print(a > 12 or b > 30)  

# not (Logical NOT)
# Yeh kisi bhi condition ka opposite (invert) kar deta hai.

x = True
y = False

print(not x)  # False (Kyunki x True tha)
print(not y)  # True

# Python mein Identity Operators ka istemal ye check karne ke liye hota hai ke do variables memory mein ek hi object ko refer kar rahe hain ya nahi. Identity Operators is aur is not hain.

# 1. is (Identity Operator)
# Agar dono variables same memory location ko refer karte hain, to is operator True return karega.
# Agar alag alag memory location hain to False return karega.
# 📌 Example:

a = [1, 2, 4]
b = a  

print(a is b)  # True (Dono same object ko refer kar rahe hain)

# is not (Identity Operator)
# Agar dono variables alag memory locations ko refer karte hain, to is not True return karega.
# Agar dono same memory location pe hain, to False return karega.

a = [1, 2, 4]
b = [1, 2, 3]

print(a is not b)  # True (Dono alag objects hain)
print(a != b)      # False (Values same hain)


# a = [1, 2, 4]
# b = [1, 2, 4]

# print(a is not b) 
# print(a != b)  

# is	: Same memory location
# is not: Different memory location

# Python Membership Operators 🔥
# Python mein Membership Operators ka use kisi element ko list, tuple, string, dictionary, ya kisi iterable data structure mein check karne ke liye hota hai. Yeh check karte hain ke koi value kisi object mein exist karti hai ya nahi.

# Membership Operators do tareeke ke hote hain:

# in
# not in

# 1. in Operator (Element Exists or Not)
# Agar koi element kisi sequence (list, tuple, string, dictionary) mein mojood hota hai, to in True return karta hai.
# Agar element nahi hota, to False return karta hai.

#Example with list:
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)   
print("mango" in fruits)   

# 2. not in Operator (Element Does Not Exist)
# Agar element sequence mein nahi hota, to not in True return karega.
# Agar element mojood hoga, to False return karega.

#Example with dictionary ( keys only )
student = {"name": "Amna", "age": 20, "city": "Karachi"}

print("marks" not in student) 
print("name" not in student)    

# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers

# 1.  & (Bitwise AND)
# Dono bits 1 honi chahiye, tabhi result 1 hoga.
# Agar koi ek ya dono bits 0 hain, to result 0 hoga.

a = 5  
b = 3  

print(a & b)  

# 2. | (Bitwise OR)
# Agar koi bhi ek bit 1 hogi, to result 1 hoga.
# Dono bits 0 honi chahiye tabhi result 0 hoga.

a = 4
b = 3  

print(a | b) 

# 3. ^ (Bitwise XOR)
# Dono bits different honi chahiye (1 aur 0 ya 0 aur 1) tabhi result 1 hoga.
# Agar dono same hain (0-0 ya 1-1) to result 0 hoga.

a = 5  
b = 2  

print(a ^ b)  

# 4. ~ (Bitwise NOT)
# Yeh 1s Complement nikalta hai, yani sab bits ko ulta kar deta hai.
# Python mein negative numbers 2's complement format mein store hote hain, is wajah se result negative ata hai.

a = 8

print(~a)  

# 5. << (Left Shift)
# Bits ko left shift karta hai aur right side se 0 add karta hai.
# Har shift se number 2x barhta hai.

a = 8 # 0b0101

print(a << 1)  
print(a << 2)  

# 6. >> (Right Shift)
# Bits ko right shift karta hai aur left side se 0 add karta hai.
# Har shift se number 2 se divide hota hai.

a = 2 

print(a >> 1)
print(a >> 4)  


# Operator Precedence (priority of operators) 
# Python mein jab ek expression mein multiple operators hotay hain, to Operator Precedence decide karta hai ke kaunsa operator pehle evaluate hoga.

result = (10 + 6) * 4
print(result)  


# 🎯 Key Takeaways
# Operators ki priority predefined hoti hai.
# Parentheses () sabse zyada priority rakhte hain.
# Multiplication, Division pehle hoti hai Addition, Subtraction se.
# Exponentiation (**) right to left associativity follow karta hai.
# Bitwise operators arithmetic operations se kam priority rakhte hain.
# Logical not highest priority, phir and, phir or aata hai.