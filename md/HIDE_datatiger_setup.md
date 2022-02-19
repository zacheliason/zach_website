## Getting Started with DataTiger
DataTiger is the data management and processing program we use in the Labbott for all our data needs. This tutorial should help you get set up to help with data tasks in the lab such as uploading files and downloading data. **If you want to set up a development version of DataTiger (i.e. you will be editing the source code, helping maintain and create new features, debugging problem files)  use [this tutorial](https://zacheliason.com/#/projects/HIDE_datatiger_setup_dev) instead.** This is all kind of a pain to get set up but it's nice to have once it's all up and running.

### 1. Install Git 
_(Skip to step 2 if you already have Git installed on your computer)_
> Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. 
> — Google

We need to set up DataTiger with Git because although it's a program we use actively in the lab, it's still under constant development and we need a way to coordinate our efforts and especially consolidate differences in code if multiple people change the same file. 

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

### 2. Download DataTiger source code from [Github](https://github.com/Populustremuloides/DataTiger2)
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
### 3. Download [Anaconda](https://www.anaconda.com/products/individual)
> Anaconda is a distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. The distribution includes data-science packages suitable for Windows, Linux, and macOS.
> — Google

DataTiger uses a lot of different packages or libraries of code that we usually import at the top of `.py` files. In order for python to be able to use those packages, it needs to be able to download and access them. Anaconda lets you create environments that wrap all the libraries you need into a single version of python that we'll use to run our code.

1) Install and open Anaconda

2) Click the `Import` button at the bottom left of the page

![](/images/screenshots/Screen%20Shot%202022-01-26%20at%201.04.39%20PM.png)
3) Name your environment whatever you want (DataTiger, dt, etc.)

4) Select `PATH_TO_DATATIGER/DataTiger2/environment.yml` as the source for your environment

### 4. Download [Box Drive](https://www.box.com/resources/downloads) 
After you install and set up Box Drive, you'll need to get edit access to the drive from a manager. This lets us control who can access/add to the database. Don't abuse these privileges by doing anything stupid (i.e. don't delete any files on Box)

### 5. Configure files
#### Update Database name
1) Open the file `DatabaseName.txt` inside your DataTiger folder.
2) Edit its contents to mirror the Path to the database `clean_datAbbase_4-15-2021.db` on your computer through Box Drive

If you have a Mac, your path will look similar to this: `/Users/zacheliason/Library/CloudStorage/Box-Box/AbbottLab/clean_datAbbase_4-15-2021.db`

If you have a PC, your path will look similar to this: `C:\Users\BCBrown\Desktop\C:\Users\BCBrown\Desktop\clean_datAbbase_try_2_again.db`

#### Update DataTiger Path
1) Using a text editor, open the file `dataTiger.command` if you have a Mac and `dataTiger.exe` if you have something else.
2) Edit line 10 to say `DATATIGER_DIRECTORY = ENTER_PATH_TO_YOUR_DATATIGER_HERE`, only subbing out `ENTER_PATH_TO_YOUR_DATATIGER_HERE` with the appropriate path.

### 6. Run DataTiger
1) Double click on the file `dataTiger.command` if you have a Mac and `dataTiger.exe` if you have something else

### You're done! 