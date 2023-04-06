import os
import sys
import subprocess
import time
import filecmp
import tabulate
from termcolor import colored

TIMEOUT = 30 # seconds

def main():
    assert len(sys.argv) >= 3, "Usage: python3 evaluate.py <problem> <solver> [solver ...]"
    problem = sys.argv[1]
    solver = sys.argv[2:]
    print ("Evaluating", problem, "with", solver)
    print ("Current working directory: ", os.getcwd())
    if not os.path.exists(problem):
        raise RuntimeError(f"Problem `{problem}` does not exist")
    
    input_path = os.path.join(problem, "input")
    output_path = os.path.join(problem, "output")

    if not os.path.exists(input_path):
        raise RuntimeError(f"Input dir `{input_path}` does not exist")

    if not os.path.exists(output_path):
        raise RuntimeError(f"Output dir `{output_path}` does not exist")

    input_files = [entry for entry in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, entry)) and entry.startswith("input")]
    output_files = [entry for entry in os.listdir(output_path) if os.path.isfile(os.path.join(output_path, entry)) and entry.startswith("output")]
    input_files.sort()
    output_files.sort()
    assert len(input_files) == len(output_files), "Number of input files does not match number of output files"
    for input_file, output_file in zip(input_files, output_files):
        assert input_file[5:] == output_file[6:], "Input file does not match output file"

    prog_output_dir = os.path.join("temp", problem, "output")
    prog_error_dir = os.path.join("temp", problem, "error")

    os.makedirs(prog_output_dir, exist_ok=True)
    os.makedirs(prog_error_dir, exist_ok=True)

    execution_stats = []
    for input_file, output_file in zip(input_files, output_files):
        start_time = time.time()
        input_file_path = os.path.join(input_path, input_file)
        output_file_path = os.path.join(output_path, output_file)
        prog_output_file_path = os.path.join(prog_output_dir, output_file)
        prog_error_file_path = os.path.join(prog_error_dir, output_file)
        status = "Success"
        with open(input_file_path, "r") as input_file, open(prog_output_file_path, "w") as prog_output_file, open(prog_error_file_path, "w") as prog_error_file:
            try:
                result = subprocess.run(solver, stdin=input_file, stdout=prog_output_file, stderr=prog_error_file, timeout=TIMEOUT)
                result.check_returncode()
            except subprocess.TimeoutExpired:
                status = "Timeout"
            except subprocess.CalledProcessError as err:
                status = "Runtime Error"

        if status == "Success" and not filecmp.cmp(output_file_path, prog_output_file_path):
            status = "Wrong Answer"
            
        status = colored(status, "green" if status == "Success" else "red")
        execution_stats += [(input_file_path, status, f"{time.time() - start_time:.3f}s")]

    print("="*80)
    print(f"Execution Stats of {problem} with {solver}")
    print("="*80)
    print(f"program output base path: {prog_output_dir}")
    print(f"program error base path: {prog_error_dir}")
    print(tabulate.tabulate(execution_stats, headers=["Input", "Status", "Time (s)"], tablefmt="grid"))
        
if __name__ == "__main__":
    main()