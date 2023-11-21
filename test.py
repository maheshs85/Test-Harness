import os
import subprocess

class TestResult:
    def __init__(self, name, result, expected, got):
        self.name = name
        self.result = result
        self.expected = expected
        self.got = got

    def __str__(self):
        return f"FAIL: {self.name} failed ({self.result})"

    def output(self):
        return f"      expected:\n{self.expected}\n\n           got:\n{self.got}"

def run_single_test(program_name, test_name, command):
    
    test_results = []
    input_path = f"test/{program_name}.{test_name}.in"
    expected_output_path = f"test/{program_name}.{test_name}.out"
    arg_output_path = f"test/{program_name}.{test_name}.arg.out"

    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    program_output, _ = process.communicate(input=open(input_path).read())

    if os.path.exists(expected_output_path):
        expected_output = open(expected_output_path).read()
        if program_output == expected_output:
            result = "OK"
        else:
            result = "TestResult.OutputMismatch"
        test_results.append(TestResult(test_name, result, expected_output, program_output))
    else:
        result = "MissingExpectedOutput"
        test_results.append(TestResult(test_name, result, "", program_output))
    
    # Run the command with input as a command-line argument
    process = subprocess.Popen(command + [input_path], stdout=subprocess.PIPE, text=True)
    arg_output, _ = process.communicate()

    # Check if the argument output matches the expected argument output
    if os.path.exists(arg_output_path):
        expected_arg_output = open(arg_output_path).read()
        if arg_output == expected_arg_output:
            result = "OK"
        else:
            result = "TestResult.OutputMismatch"
        test_results.append(TestResult(f"{test_name} (arg)", result, expected_arg_output, arg_output))
    else:
        result = "MissingExpectedArgOutput"
        test_results.append(TestResult(f"{test_name} (arg)", result, "", arg_output))
    
    return test_results

def run_all_tests():
    all_test_results = []

    # commands for different tests
    commands = {
        # "wc.multiple_files": ["python3", "/prog/wc.py", "multiple_file_1", "multiple_file_2"],
        "wc.basic": ["python3", f"./prog/wc.py"],
        "wc.flags": ["python3", f"./prog/wc.py", "-lw"],
        "ungron.basic": ["python3", f"./prog/ungron.py"],
        "gron.basic": ["python3", f"./prog/gron.py"],
        # "gron.base": ["python3", f"/prog/wc.py"]
    }

    for test_file, command in commands.items():
        program_name = os.path.splitext(test_file)[0]
        test_name = os.path.splitext(test_file)[1][1:]
        test_results = run_single_test(program_name, test_name, command)
        if test_results:
            all_test_results.extend(test_results)

    return all_test_results

def print_test_results(test_results):
    total_tests = len(test_results)
    passed_tests = sum(1 for result in test_results if result.result == "OK")
    failed_tests = total_tests - passed_tests

    print(f"OK: {passed_tests}")
    print(f"output mismatch: {failed_tests}")
    print(f"total: {total_tests}")

    for result in test_results:
        if result.result != "OK":
            print(result)
            print(result.output())

if __name__ == "__main__":
    all_test_results = run_all_tests()
    print_test_results(all_test_results)
