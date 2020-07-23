
# TestCase Runner

This is a light-weight project that checks a given program against the given test cases and provides a summary of how many of the tests passed. A test case consists of a pair of files, one that specifies the input, and one that specifies the expected output when that particular input is fed to the program.

## Getting Started
to use this testcase runner, run:
```
python3 main.py --exe <path-to-executable> --tests <path-to-tests>
```
while `--tests` specifies the folder containing your testcases, which should be pairs of files with `.in` and `.out` suffixes. The files can be arbitrarily nested inside the specified folder. if there are any command-line arguments you need to pass to the executable you are testing, specify them using --args:
```
python3 main.py --exe <path-to-executable> --tests <path-to-tests> --args "arg1 arg2"
```
* Note: the arguments passed via `--args` are directly fed to the executable, so if they contain file addresses, they will be interpreted with respect to the folder containing the executable being tested, **not** the tester script. If you are unsure, use absolute paths to make sure the program will work.

This tester checks for 4 conditions, either the result is equal to the expected result (`correct`), or unequal (`incorrect`), or the program returns a non-zero exit code (`bad_exit_code`), or it takes too long to execute (`timed_out`). Internally, the program uses the [Unix diff command](https://man7.org/linux/man-pages/man1/diff.1.html) to compare the results to the expected output and will print the diff output if they differ.

## To Other TA's

If you find this project useful, but need any changes, require new features or have questions, please contact me via email ([seyedahmadpourihosseini@gmail.com](mailto:seyedahmadpourihosseini@gmail.com)) or telegram ([@SAPHosseini](https://telegram.me/SAPHosseini)).

## Authors

* **Ahmad Pourihosseini** - [ahmad-PH](https://github.com/ahmad-PH)
