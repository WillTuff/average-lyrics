# Average Lyrics

## Readme

Please note - If you are running this program on a Mac or Linux distribution you can skip steps 3 - 7. You can open a terminal window, navigate to the project folder and complete steps 8 onwards.

1. Download the source code directly from the repository then unzip the files
2. Download the community edition of PyCharm: 
    https://www.jetbrains.com/pycharm/download
3. Install PyCharm
4. When running PyCharm for the first time, choose the following options:
    * Do not import settings
    * Choose 'Dont Send' to Data Sharing
    * When the first 'Customize PyCharm' box appears, choose 'Skip Remaining and Set Defaults'

5. Choose 'Open' from the options then navigate to the project folder.
6. Next, please configure a Python interpreter. This can be completed by following the instructions found here: 
    https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
7. Click on 'Terminal' in the bottom left hand corner.
8. You'll then need to ensure Pip is installed on your PC. This can be achieved by running the following command into the terminal window you've opened in PyCharm: 
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
9. Once pip is installed, please run: 
    pip install --user --requirement requirements.txt
10. Then right click on 'main.py' on choose Run Main.py (alternatively, if you have Python installed on your machine you can run python main.py)
11. The program should start automatically and ask for the name of an artist to search.

