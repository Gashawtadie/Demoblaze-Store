# Demoblaze-Store
![image](https://user-images.githubusercontent.com/113560142/216850462-5898f827-c684-48cb-8c10-0ebff288df46.png)


Title - Demoblza Store E-commerce website


Description of the system and its purpose

This project is consisting of different modules(directory) login page, sign up, add to cart, about us and, contact us. each modules have its own tests class with functions and at the end i created another class on tests module(directory) to dispaly all test in one time by using of multiple inheritance so its posibbl to run all type of tests.  
The purpose of the system is to bring for users to connect with their accounts and create a new accounts with sign up modules system and provide online shopping 


Dependencies:

the project is done with selenium python on windows 11


Executing program:

i will explain how to run the program step by step
- before all there is graphical acticterure design to test the website that leads how and where the program runs
![image](https://user-images.githubusercontent.com/113560142/216849548-f0599f8d-4e69-4674-819c-473efe3dc91c.png)

- first of all i created Base pags: the use of base page is minimize the unwanted longer and salad code to make shorttly ad netly, i put all of them on one class in different functions and each function are retun when i use in any code 
example: find, click, send to keys, wait, assertion etc all are that i use repeatdly so if i want to use i just call it the functions

- Locators: locatrs are the paths of the webelemnt of the website and all locators are under a class and  i call it on other class by using single inheritance
- Page object: in page bjects there is a different kind of modules of website and each tests fiels are owns the code 
- Tests: tests are the final class that gather all class and using of multiple class i just make object functions and call all page object class functions and run it


Help:
in tests i already created Final report directory and if someone who want to run use it 
 allure serve Final_report
 ![Screenshot_20230205_012653](https://user-images.githubusercontent.com/113560142/216850427-9d2c4218-16cb-4f99-b940-61c82b0664da.png)

 
Author - Gashaw Tadie

Version History:
version-1 initial release
