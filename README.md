
# TestCase Runner

The assignments I would design in university as a TA almost always needed testcases to check students' codes for correctness, and a piece of code to execute the students' code and compare their results to the expected results. This project is that "piece of code".

## Getting Started
to use this testcase runner, run:
```
python3 main.py --exe <path-to-executable> --tests <path-to-tests>
```
while `--tests` specifies the folder containing your testcases, which should be pairs of files with `.in` and `.out` suffixes. The files can be arbitrarily nested inside the specified folder. if there are any command-line arguments you need to pass to the executable you are testing, specify them using --args:
```
python3 main.py --exe <path-to-executable> --tests <path-to-tests> --args "arg1 arg2"
```
This tester checks for 4 conditions, either the result is correct (equal to expected), or incorrect (unequal to expected), or the program returns a non-zero status code, or it takes too long to execute. Internally, the program uses the [Unix diff command](https://man7.org/linux/man-pages/man1/diff.1.html) to compare the results to the expected output and will print the diff output if they differ.

## To Other TA's

If you find this project useful, but need any changes, require new features or have questions, please contact me via email ([seyedahmadpourihosseini@gmail.com](mailto:seyedahmadpourihosseini@gmail.com)) or telegram ([@SAPHosseini](https://telegram.me/SAPHosseini)).

## Authors

* **Ahmad Pourihosseini** - [ahmad-PH](https://github.com/ahmad-PH)
