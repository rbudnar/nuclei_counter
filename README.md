# **Nuclei Image Processing Program**

This python program processes and counts nuclei in images. The following sections detail how to use the various command-line arguments available in the program. 

## Setup
On windows-based systems, you may use one of the pre-built executable files provided in [releases](https://github.com/rbudnar/nuclei_counter/releases); this does not require installation of python. However, if you wish to modify the code, you must clone this repository and build or run the program from source.

**NOTE:** Due to using pyinstaller to package this code as a windows executable, this file may be flagged as a virus or as malware. This is unfortunately common for software built using pyinstaller. If your antivirus blocks the file, you'll need to flag it as safe when downloading it.

### Requirements
To build or run this program as a python script, ensure you have [python 3.10](https://www.python.org/downloads/) or later installed on your system. Then clone this repository by downloading and extracting the zip file or by using git. 

### Project installation
This library uses a [PEP-518](https://peps.python.org/pep-0518/) compliant pyproject.toml file to manage project dependencies. To install this library locally, you may use your preferred python package manager (e.g., [poetry](https://python-poetry.org/)) or run the following from the repository root:

```
pip install -e .
```

This will install all project dependencies and allow you to run the project as a python script from the command line. If you've downloaded the executable file, replace `python count_nuclei.py` with `count_nuclei.exe`; all command line options remain the same.

## Program usage
To use this program, open a terminal and change your working directory into `\nuclei_counter` where `count_nuclei.py` exists. You may run the python program with the  command line arguments as described; note that only `--img_dir` is required; other arguments may be omitted.

### **1. Image Directory (`--img_dir`) (REQUIRED)**

Specify the directory containing the images you wish to process.

**Usage:**

```
python count_nuclei.py --img_dir "path/to/your/image/directory"
```

### **2. Output Directory (`--output_dir`) (OPTIONAL)**

Defines where the results files should be saved. If not specified, results will be saved in a folder named `results` in the current working directory.

**Usage:**

```
python count_nuclei.py --img_dir "path/to/your/image/directory" --output_dir "path/to/your/output/directory"
```

### **3. Save Transformed Images (`--save_images`) (OPTIONAL)**

Include this flag if you wish to save the transformed images used during the counting process. This flag is optional and excluding it will not save a copy of the transformed images.

**Usage:**

```
python count_nuclei.py --img_dir "path/to/your/image/directory" --save_images
```

### **4. Output Count Filename (`--output_count_filename`) (OPTIONAL)**

Specify the filename of the resulting CSV that contains the count of nuclei. If not provided, it will default to `count_results.csv`.

**Usage:**

```
python count_nuclei.py --img_dir "path/to/your/image/directory" --output_count_filename "your_desired_filename.csv"
```

**Default:**
count_results.csv

### **Full Example**:

To use all the arguments in one command:

```
python count_nuclei.py --img_dir "path/to/images" --output_dir "path/to/output" --save_images --output_count_filename "results.csv"
```

# License
See the [LICENSE](/LICENSE) file for license rights and limitations (MIT).