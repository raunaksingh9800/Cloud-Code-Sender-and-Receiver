# Cloud-Code-Sender-and-Receiver
Python Script for Pushing and Retrieving Code to/from Firebase Storage

## Overview

This Python script streamlines the process of pushing code to a Firebase Storage bucket, retrieving it on another device, and running it, with optional compilation for different programming languages. It's ideal for sharing and executing code across multiple devices seamlessly.

## Key Features

- **File Handling:** Uploads and downloads code files to/from Firebase Storage.
- **Command-Line Arguments:** Supports four modes for distinct actions:
    - `Sender`: Initializes the sending process, prompts for file name and Global Access Code (GAC), uploads the file, and creates a `data.txt` file for future reference.
    - `Receiver`: Initializes the receiving process, prompts for file name and GAC, downloads the file, creates a `data.txt` file, and runs the code (defaulting to clang++ compilation for C++, but customizable for other languages).
    - `push`: Reads GAC and file name from `data.txt` and pushes the code to the cloud.
    - `get`: Reads GAC and file name from `data.txt`, retrieves the code from the cloud, compiles it (if applicable), and runs it.
- **Customizable Compilation:** Allows users to adjust the compilation command for their preferred programming language.

## Usage

1. **Install Required Libraries:**
   ```bash
   pip install firebase-admin 
   ```
2. **Provide Firebase Credentials:**
   - Create a Firebase project and download a service account key JSON file.
   - Place the JSON file in the same directory as the script.
3. **Run the Script:**
   ```bash
   python main.py <mode>
   ```
   Replace `<mode>` with `Sender`, `Receiver`, `push`, or `get`.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests.

