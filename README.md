Using Google-OR tools to solve Knapsack-Problems

1) Solving knapsack with OR-Tools: https://developers.google.com/optimization/bin/knapsack

2) Knapsack test instances: https://github.com/likr/kplib

**How to run?**
1) Clone this repo
```python
git clone https://github.com/HuuPhat125/Solving-Knapsack-Problems-Using-Google-OR-Tools.git
```


```python
cd Solving-Knapsack-Problems-Using-Google-OR-Tools
```

2) Clone repo that contains test case
```python
git clone https://github.com/likr/kplib.git
```
3) Install library
```python
python3 -m pip install --upgrade --user ortools
```
4) Run
```python
python main.py --time_limit 180 --output_dir /kaggle/working/ --idx_begin 0
```

**Parameters:**

--time_limit: Specifies the time limit (in seconds) for the execution of the script. In the provided example, the time limit is set to 180 seconds.

--output_dir: Defines the output directory where the script will save its results. In this example, it's set to /kaggle/working/.

--idx_begin: Indicates the starting index for the test case list within the script. In the given command, the starting index is set to 0.

Make sure to adjust the values of these parameters as needed for your specific use case.

