## **Using the Nuclei Image Processing Program**

This program processes and counts nuclei in images. The following sections detail how to use the various command-line arguments available in the program.

### **1. Image Directory (`--img_dir`)**

Specify the directory containing the images you wish to process. 

**Usage:**
python my_program.py --img_dir "path/to/your/image/directory"

### **2. Output Directory (`--output_dir`)**

Defines where the results files should be saved. If not specified, results will be saved in a folder named `results` in the current working directory.

**Usage:**
python my_program.py --output_dir "path/to/your/output/directory"
<current_working_directory>/results


### **3. Save Transformed Images (`--save_images`)**

Include this flag if you wish to save the transformed images used during the counting process.

**Usage:**
python my_program.py --save_images

### **4. Output Count Filename (`--output_count_filename`)**

Specify the filename of the resulting CSV that contains the count of nuclei. If not provided, it will default to `count_results.csv`.

**Usage:**
python my_program.py --output_count_filename "your_desired_filename.csv"

**Default:**
count_results.csv


### **Full Example**:

To use all the arguments in one command:

python my_program.py --img_dir "path/to/images" --output_dir "path/to/output" --save_images --output_count_filename "results.csv"