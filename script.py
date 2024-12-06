import time
import math
import os
import csv
import subprocess

def water_consumption_task(splits, runtime_memory, ephemeral_storage):
    """Executes the 'water-consumption.py' script with the given parameters and measures execution time."""
    start_time = time.time()
    
    script_path = 'water-consumption.py'
    
    # Build the command to execute the script with specified arguments
    command = [
        'python3.9', script_path, 
        '--splits', str(splits),
        '--runtime_memory', str(runtime_memory),
        '--ephemeral_storage', str(ephemeral_storage)
    ]
    
    # Execute the command and capture stdout and stderr
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    end_time = time.time()
    exec_time = end_time - start_time
    
    # Check if the script executed successfully
    if result.returncode != 0:
        print(f"Error ejecutando water-consumption.py: {result.stderr}")
        raise Exception(f"Script execution failed with return code {result.returncode}")
    
    # Print the results of the script execution
    print(f"Execution with splits={splits}, runtime_memory={runtime_memory}, ephemeral_storage={ephemeral_storage}:")
    print("----- stdout -----")
    print(result.stdout)
    print("----- stderr -----")
    print(result.stderr)
    print("\n")
    
    return {'exec_time': exec_time}

def main():
    """Main function to execute the water consumption task with different configurations."""
    num_repeats = 2  # Number of times to repeat each configuration
    splits_values = [2, 3, 4, 5, 6]  # List of splits to test
    configurations = [
        {'runtime_memory': 2000, 'ephemeral_storage': 1024},  # Configuration settings
    ]
    
    output_file = 'water_consumption_dsa_results.csv'  # Output CSV file name
    fieldnames = [
        'execution_number',
        'splits',
        'runtime_memory_mb',
        'ephemeral_storage_mb',
        'vcpus',
        'total_exec_time_s',
    ]
    
    # Check if the output file already exists
    file_exists = os.path.isfile(output_file)
    
    # Open the CSV file in append mode
    with open(output_file, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Write the header if the file doesn't exist
        if not file_exists:
            writer.writeheader()
        
        execution_number = 0  # Initialize execution counter
        # Iterate over each configuration
        for config in configurations:
            # Iterate over each splits value
            for splits in splits_values:
                # Repeat the execution based on num_repeats
                for _ in range(num_repeats):
                    execution_number += 1

                    # Calculate the number of vCPUs based on runtime memory
                    vcpus = round(config['runtime_memory'] / 1769, 2)

                    try:
                        # Execute the water consumption task
                        result = water_consumption_task(splits, config['runtime_memory'], config['ephemeral_storage'])
                        elapsed = result['exec_time']

                        # Write the results to the CSV file
                        writer.writerow({
                            'execution_number': execution_number,
                            'splits': splits,
                            'runtime_memory_mb': config['runtime_memory'],
                            'ephemeral_storage_mb': config['ephemeral_storage'],
                            'vcpus': vcpus,
                            'total_exec_time_s': elapsed,
                        })

                        # Print summary of the execution
                        print(f"Execution {execution_number} completed.")
                        print(f"Splits: {splits}")
                        print(f"Total execution time: {elapsed:.2f} s")
                        print("-" * 40)
                    
                    except Exception as e:
                        # Handle any exceptions during execution
                        print(f"Execution {execution_number} failed with error: {e}")
                        print(f"Skipping to next configuration.")
                        print("-" * 40)

    # Indicate that data collection is complete
    print(f"Data collection complete. Results saved to {output_file}.")

if __name__ == "__main__":
    main()
