#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?

# In Python, you can add comments to your code to provide explanations, notes, or to temporarily disable specific lines of code. Comments are not executed by the Python interpreter, and they are intended for human readers to understand the code better.
# 
# To add comments in Python, you use the hash symbol (#) followed by the comment text. Anything after the # on the same line will be considered a comment and will not be executed.

# Q2. What are variables in Python? How do you declare and assign values to variables?

# Variables are used to store data values. A variables is like a container that holds the values and gives its a name.
# To declare and assign values to variables in Python you simple use the assignment operator("=")

# Q3. How do you convert one data type to another in Python?

# Convert one data type to another in Python can be done using type conversion function.Python provides built in  functions to perform type conversion.
# int()
# float()
# bool()

# Q4. How do you write and execute a Python script from the command line?

# Step 1: Open a text editor or an Integrated Development Environment (IDE) to write your Python script. You can use any text editor like Notepad (Windows), TextEdit (Mac), or any code-specific IDE like Visual Studio Code, PyCharm, or IDLE.
# 
# Step 2: Write your Python code in the text editor and save the file with a .py extension. For example, you can save your script as my_script.py

# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[2]:


my_list = [1,2,3,4,5]
my_list[1:3]


# Q6. What is a complex number in mathematics, and how is it represented in Python?

# In mathematics, a complex number is a number of the form a + bi, where a and b are real numbers, and i is the imaginary unit, defined as the square root of -1. The real part a represents the standard real numbers, while the imaginary part b represents multiples of the imaginary unit i.
# In python, complex numbers are supported as a built in data types.To represent a complex number in python , we use "j".

# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[3]:


age = 25


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
# belong to?

# In[4]:


price = 9.99


# In[5]:


type(price)


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

# In[6]:


name = "Mayur Dilipbhai Nayak"
print(name)


# Q10. Given the string "Hello, World!", extract the substring "World".

# In[7]:


s = "Hello, World!"
s_s = s[7:12]
print(s_s)


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.

# In[8]:


is_student = False


# In[9]:


is_student


# In[ ]:




