# Practical-Harmonic-Ananlysis-Solver
> This is a beta version & might get updates to improve/add more features to tackle the problem. <br>For Contributing, reach out to me sukhmani1303@gmail.com
<br>

## INTRODUCTION <BR>
  This Python Application can solve Practical Harmonic Analysis Maths Problems with ***100% accuracy*** in no time for you. All you have to do, is feed the ***X*** & ***F(x)*** Values and get the answer in one click. This app aims to help every Math student/teacher in _Verifying answers_ or _Getting answers_ without the need of internet with a ***highly interactive interface***.<br><p>_A SAMPLE PROBLEM_ :</p><img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlbPfF2T13vJi2vNwUzElPWofurOldSeQ5jiPI-4unHNiZZ5AIsnuZPpYA0LqCA3I6cw&usqp=CAU" width = "500px"><br><br>
  
## DEPENDENCIES <BR>
  There are 3 elements without which this application won't work<br>
  1. **Python** <br>
    The code being written in python, needs the same to run successfully. One can download & install the latest version of Python from [here](https://www.python.org/downloads/) <br>
  - Add pip to System Environment Variables, [how to do it ?](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command)<br>
  
  2. **Tkinter Python Library** <br>
    This Library is not pre-installed, thus we need to install it externally. The simplest method to install Tkinter is :<br><br>
    1. Open CMD <br>
    2. ```pip install tkinter``` , this might take a while but will get installed eventually <br>
  ***To use pip, make sure you complete step 1***<br>
  
  3. **Math Python Library** <br>
    This is a pre-installed Python Library <br><br>
  
## CHANGING FILE PATH <br>
  You need to change the file path before running the script.
  ***Change app icon on line 7 to respective function.png file on your device*** <br><br>
  
## HOW TO USE <br>
  
  ### Step 1  - Enter **X** values<br>
  <img src='https://www.linkpicture.com/q/entr_x_val.png' type='image'><p>Pressing X button once, you can input as many values of X you want. After entering one value, press ENTER on the app.</p><br>
  
  ### Step 2 - Enter **Y** values<br>
  <img src='https://www.linkpicture.com/q/entr_y_val.png' type='image'><p>Once, all the Values of X are fed, you can start feeding same number of Y values.<br>Pressing Y button once, you can input as many values of Y you want. After entering one value, press ENTER on the app.</p><br>
  
  ### Step 3 - Enter number of **Harmonics** you want to find<br>
  <img src='https://www.linkpicture.com/q/entr_har_val.png' type='image'><p>Pressing Har Button, you are supposed to enter only 1 value. This must be any natural number (1,2,3,4,5...).<br>After typing the number, press ENTER on the app to save it</p><br>
  
  ### Step 4 - Viewing the Answer (a<sub>0</sub> , a<sub>n</sub> & b<sub>n</sub>)<br>
  <img src='https://www.linkpicture.com/q/answers.png' type='image'><br>
  - **a<sub>0</sub>** : For a<sub>0</sub> , you need to click **a0** button which will display the decimal value of a0.<br>
  - **a<sub>n</sub>** : You will have as many a<sub>n</sub> values as the number of Harmonics you entered. So, to view each value you need to click **an** button.<br> For viewing the next a<sub>n</sub> value you simple press **an** button again and so on. 
  - **b<sub>n</sub>** : Again, You will have as many b<sub>n</sub> values as the number of Harmonics you entered. So, to view each value you need to click **bn** button.<br> For viewing the next b<sub>n</sub> value you simple press **bn** button again and so on. 
  
  ```
  NOTE : THIS APPLICATION ONLY TAKES X VALUES IN DEGREES
  ```
