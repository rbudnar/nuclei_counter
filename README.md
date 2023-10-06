## **Using the Nuclei Image Processing Program**

This program processes and counts nuclei in images. The following sections detail how to use the various command-line arguments available in the program. You may download the latest windows exectuable from the [releases](https://github.com/rbudnar/nuclei_counter/releases) page, or you may build and run the project from source.

**NOTE:** Due to using pyinstaller to package this code as a windows executable, this file will almost certainly be flagged as a virus or as malware. This is unfortunately common for software built using pyinstaller. If your antivirus blocks the file, you'll need to flag it as safe.

This project uses [Poetry](https://python-poetry.org/docs/) for dependency management. Please follow their official documentation for information on how to install poetry for python. Once you have poetry installed and you have cloned this repository, simply run the following command at the repository's root:

```
poetry install
```

This should install all project dependencies and allow you to run the project as a python script from the command line. If you've downloaded the executable file, replace `python count_nuclei.py` with `count_nuclei.exe`; all command line options remain the same.

### **1. Image Directory (`--img_dir`)**

Specify the directory containing the images you wish to process.

**Usage:**

```
python count_nuclei.py --img_dir "path/to/your/image/directory"
```

### **2. Output Directory (`--output_dir`)**

Defines where the results files should be saved. If not specified, results will be saved in a folder named `results` in the current working directory.

**Usage:**

```
python count_nuclei.py --output_dir "path/to/your/output/directory"
```

### **3. Save Transformed Images (`--save_images`)**

Include this flag if you wish to save the transformed images used during the counting process.

**Usage:**

```
python count_nuclei.py --save_images
```

### **4. Output Count Filename (`--output_count_filename`)**

Specify the filename of the resulting CSV that contains the count of nuclei. If not provided, it will default to `count_results.csv`.

**Usage:**

```
python count_nuclei.py --output_count_filename "your_desired_filename.csv"
```

**Default:**
count_results.csv

### **Full Example**:

To use all the arguments in one command:

```
python count_nuclei.py --img_dir "path/to/images" --output_dir "path/to/output" --save_images --output_count_filename "results.csv"
```
