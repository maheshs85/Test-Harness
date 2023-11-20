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


def run_tests():
    program_directory = "prog"
    test_directory = "test"
    test_results = []
    for test_file in os.listdir(test_directory):
        if test_file.endswith(".in"):
            program_name = test_file.split('.')[0]
            test_name = os.path.splitext(test_file)[0]
            program_path = os.path.join(program_directory, f"{program_name}.py")
            input_path = os.path.join(test_directory, f"{test_file}")
            expected_output_path = os.path.join(test_directory, f"{test_name}.out")
            arg_output_path = os.path.join(test_directory, f"{test_name}.arg.out")
            
            # Run the program with input from the file
            process = subprocess.Popen(["python3", program_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            program_output, _ = process.communicate(input=open(input_path).read())
            
            # Check if the output matches the expected output
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

            # Run the program with input as a command-line argument
            process = subprocess.Popen(["python3", program_path, input_path], stdout=subprocess.PIPE, text=True)
            arg_output, _ = process.communicate()

            # Check if the argument output matches the expected argument output
            print(os.path.exists(arg_output_path))
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
    run_tests()