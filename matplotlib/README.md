# Setting up & running `main.py` 

Make sure to clone the repo/matplotlib using git clone first, then continue with initializing/activating the venv followed by installing required modules (matplotlib) from requirements.txt to the activated venv as follows :

1.  **Create and Activate Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate (ubuntu/linuxdistros)

or .\venv\Scripts\activate (windows)
```
2.  **Install Required Packages**
```sh
pip install -r requirements.txt
```
3.  **Run the Script**
```sh
python main.py

or python3 main.py