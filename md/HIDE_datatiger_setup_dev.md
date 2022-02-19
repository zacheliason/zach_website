## Getting Started with DataTiger
DataTiger is the data management and processing program we use in the Labbott for all our data needs. This tutorial should help you get set up to help with data tasks in the lab such as uploading files and downloading data. If you want to set up a development version of DataTiger (i.e. you will be editing the source code, helping maintain and create new features, debugging problem files) this is the correct tutorial. **If you want to help with data but have no interest in coding, use [this tutorial](HIDE_datatiger_setup) instead (easier and takes less space on your computer).** This is all kind of a pain to get set up but it's nice to have once it's all up and running.

### 1. Download [PyCharm](https://www.jetbrains.com/pycharm/download/)
> PyCharm is an IDE used in computer programming, specifically for the Python programming language.
— Google

PyCharm is a program we use to write python code in one place. It's especially convenient because it lets you run or execute your code in the same place and offers other tools that are nice for debugging your code.

![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.40.03%20AM.png)
Click the black button to download the free, community version. 
### 2. Install Git 
_(Skip to step 3 if you already have Git installed on your computer)_
> Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. 
> — Google

We need to set up DataTiger with Git because although it's a program we use actively in the lab, it's still under constant development and we need a way to coordinate our efforts and especially consolidate differences in code if different people change the same file. 

#### Mac Instructions
1) Open terminal

2) Run the following code:

```console
git --version
 ```
If git isn't installed already, your computer will prompt you to install it. Sometimes this takes a second! 

#### Windows Instructions
1) Download GitBash (a command line application which allows you to run bash commands on Windows) from the link [here](https://git-scm.com/download/win)

![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.40.43%20AM.png)
2) Click the `Click here to download` link to download the most recent version

### 3. Download DataTiger source code from [Github](https://github.com/Populustremuloides/DataTiger2)
This is the code that runs DataTiger! We host it on GitHub, from Labbott alum and DataTiger creator Brian Brown's account.

1) Click the green `Code` button 

2) Make sure the `HTTPS` tab is selected

![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.41.03%20AM.png)
3) Click the copy button to the right of the link to copy to your clipboard

4) Open Terminal/GitBash

5) Navigate to the directory/folder you want to save Data Tiger under. _(i.e., if I have a folder called 'Labbott' under Documents/Work/, I run the following code in Terminal/GitBash to enter that directory from the command line.)_
	
```console
cd Documents/Work/Labbott/
```
	
6) Run the following code to copy the git repository (a kind of cloud storage vault for coding projects) into your folder

```console
git clone PASTE_YOUR_GIT_REPOSITORY_LINK_HERE
```
- Now you're done with Terminal/GitBash :)
### 4. Download [Anaconda](https://www.anaconda.com/products/individual)
> Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.
> — Google

DataTiger uses a lot of different packages or libraries of code that we usually import at the top of `.py` files. In order for python to be able to use those packages, it needs to be able to download and access them. Anaconda lets you create environments that wrap all the libraries you need into a single version of python that we'll use to run our code.

Once you've installed (choose all the default install settings) and opened Anaconda, create a new environment (click the `Create` button at the bottom left of the page) and call it whatever you want. Now you'll need to add some packages to your environment. For each of the following packages, search using the bar in the top right of Anaconda (Make sure the `Installed` dropdown is set to `All` or `Not installed` so that you can see more than the packages you currently have in your environment.) After checking the box next to each package, hit `Apply` in the bottom right corner and wait for a new window to pop up, where you'll hit `Apply` again.

- `pyqt`
- `openpyxl`
- `pandas`
- `seaborn`
- `scikit-learn`

### 5. Download [Box Drive](https://www.box.com/resources/downloads) 
After you install and set up Box Drive, you'll need to get edit access to the drive from a manager. This lets us control who can access/add to the database. Don't abuse these privileges by doing anything stupid (i.e. don't delete any files on Box)

### 6. Configure PyCharm interpreter
Here we're going to set up PyCharm so that it uses the conda environment or version of python we created in step 4. 
1) Open PyCharm
2) Click **File** > **Open** and then navigate to the Data Tiger folder you just downloaded
3) Navigate to **PyCharm** > **Preferences** if you're using a Mac, and **File > Settings** if you're using something else
![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.41.51%20AM.png)
4) Under `Python Interpreter:`, click on `Show All...`
5) Click the `+` in the corner to add a new interpreter 
![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.42.28%20AM.png)

6) Select **Conda Environment** > **Existing environment** and then select the new Anaconda environment you created earlier
### 7. Configure path to database
1) Open `DatabaseName.txt` under the project tab on the left.
2) Edit it to mirror the Path to the database `clean_datAbbase_4-15-2021.db` on your computer through Box Drive

If you have a Mac, your path will look similar to this: `/Users/zacheliason/Library/CloudStorage/Box-Box/AbbottLab/clean_datAbbase_4-15-2021.db`

If you have a PC, your path will look similar to this: `C:\Users\BCBrown\Desktop\C:\Users\BCBrown\Desktop\clean_datAbbase_try_2_again.db`

### 8. Run DataTiger
1) Open `dataTiger.py` from the project tab on the left
2) Right click anywhere in the code on the right and click `Debug 'dataTiger'`
![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.42.55%20AM.png)

### You're done! 