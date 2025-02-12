# Setting up & running `main.py` 

NP :- commands written to run on linux distros specifically ubuntu

Make sure to clone the repo and cd into matplotlib using git clone first, then continue with initializing/activating the venv followed by installing required modules (matplotlib) from requirements.txt to the activated venv as follows :
```sh
git clone https://github.com/aaromalonline/aaromalanil_horizon_s2.git
cd ./aaromalanil_horizon_s2/matplotlib
```

1.  **Create and Activate Virtual Environment**
```sh
python3 -m venv venv
source ../venv/bin/activate
```
2.  **Install Required Packages**
```sh
pip3 install -r requirements.txt
sudo apt-get install python3-tk
```
3.  **Run the Script**
```sh
python3 main.py
```