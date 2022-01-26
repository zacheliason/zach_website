### Getting Started with Data Tiger
This is all kind of a pain to get set up but it's really nice once you have it up and running!

1. Download [PyCharm](https://www.jetbrains.com/pycharm/download/)
- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.40.03%20AM.png)
- Click the black button to download the free, community version. 
2. (Skip to step 3 if you already have Git installed on your computer)
	- #### Mac
		1. Open terminal
		2. Run the following code:
		```console
		git --version
		 ```
		3. If you don’t have it installed already, it will prompt you to install it
	- #### Windows
		1. Download GitBash (a command line application which allows you to run bash on Windows) from the link [here](https://git-scm.com/download/win)
			- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.40.43%20AM.png)
			- Click the `Click here to download` link to download the most recent version
3. Download Data Tiger source code from [Github](https://github.com/Populustremuloides/DataTiger2)
	1. Click the green `Code` button 
	2. Make sure the `HTTPS` tab is selected
	- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.41.03%20AM.png)
	3. Click the copy button to the right of the link to copy to your clipboard
	4. Open Terminal/GitBash
	5. Navigate to the directory/folder you want to save Data Tiger in 
		- i.e., if I have a folder called 'Labbott' under Documents/Work/, I run the following code to enter that directory from the command line. 
		
	```console
	cd Documents/Work/Labbott/
	```
		
	6. Run the following code to copy the git repository (a kind of cloud storage vault for coding projects) into your folder
	```console
	git clone COPY_YOUR_GIT_REPOSITORY_LINK_HERE
	```
	7. Now you're done with the command line:) 
4. Download [Anaconda](https://www.anaconda.com/products/individual)
	1. Install and open Anaconda
	2. Click the `Import` button at the bottom left of the page
	- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%201.04.39%20PM.png)
	3. Name your environment whatever (DataTiger, dt, etc.)
	4. Select `PATH_TO_YOUR_DATATIGER/DataTiger2/environment.yml` as the source for your environment

5. Download [Box Desktop](https://www.box.com/resources/downloads) 
	- How to check if you have a 32 or 64 bit Windows computer
		1. Select the **Start** button, then select **Settings** > **System** > **About** 
		2. At the right, under **Device specifications,** see **System type**
	- Get edit access to the drive from Zach or another manager

6. Configure PyCharm interpreter
	1. Open PyCharm
	2. Click **File** > **Open** and then navigate to the Data Tiger folder you just downloaded
	3. Navigate to **PyCharm** > **Preferences**
	- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.41.51%20AM.png)
	4. Under `Python Interpreter:`, click on `Show All...`
	5. Click the + in the corner to add a new interpreter 
	- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.42.28%20AM.png)

	6. Select **Conda Environment** > **Existing environment** and then choose the new Anaconda environment you just created
7. Configure path to database
	1. Open `DatabaseName.txt` under the project tab on the left.
	2. Edit it to mirror the Path to the database `clean_datAbbase_4-15-2021.db` on your computer
		1. If you have a Mac, your path will look similar to this: `/Users/zacheliason/Library/CloudStorage/Box-Box/AbbottLab/clean_datAbbase_4-15-2021.db`
		2. If you have a PC, your path will look similar to this: `C:\Users\BCBrown\Desktop\C:\Users\BCBrown\Desktop\clean_datAbbase_try_2_again.db`
8. Run DataTiger
	1. Open `dataTiger.py` from the project tab on the left
	2. Right click anywhere in the code on the right and click `Debug 'dataTiger'`
	- ![](/images/screenshots/Screen%20Shot%202022-01-26%20at%2011.42.55%20AM.png)
	3. I think there are a few more packages you need to install to make DataTiger run but I can't remember off the top of my head which they are

You're done! 