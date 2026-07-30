<<<<<<< HEAD
# 🌐 CodeAlpha Internship

# Project-3: Task Automation with Python Scripts

## Task-3: Website Title Extractor

---

## 📌 Project Description

This project is a Python automation script that extracts the title of a fixed webpage automatically.

The program sends a request to the website, retrieves the HTML source code, searches for the webpage title using Regular Expressions (Regex), and saves the extracted title into a professional text report.

---

## 🎯 Objective

The goal of this task is to automate the process of extracting webpage titles without manually opening the website and checking its HTML source.

---

## 🛠️ Technologies Used

- Python 3.14.6
- Visual Studio Code 1.131.0

---

## 📚 Concepts Used

- `requests` Library
  - Sending HTTP GET requests
  - Receiving webpage responses

- `re` Module
  - Searching HTML content using Regular Expressions
  - Extracting required information

- File Handling
  - Reading and writing text files

- Conditional Statements
  - Checking whether a title was found

---

## 📂 Project Structure

```
Task-3-Website-Title-Extractor
│
├── website-title-extractor.py
├── Website-Title.txt
├── README.md
```

---

## ⚙️ How It Works

1. Import required Python modules.

2. Provide the website URL.

3. Send a GET request to the website using the `requests` module.

4. Receive the HTML source code of the webpage.

5. Search for the `<title>` tag using Regex.

6. Extract only the title text.

7. Save the extracted title into `Website-Title.txt`.

8. Display the extraction status.

---

## 🔍 Regex Pattern Used

```regex
<title>(.*)</title>
```

### Explanation:

- `<title>`  
  Finds the opening title tag.

- `(.*)`  
  Captures all characters inside the title tag.

- `</title>`  
  Finds the closing title tag.

The captured group contains only the webpage title.

---

## 📄 Output Example

Generated file:

```
Website-Title.txt
```

Example output:

```
======================================================================
                 Website Title Extraction Report
======================================================================

Website URL:
https://www.python.org/

Website Title:
Welcome to Python.org

======================================================================
                         End of Report
======================================================================
```

---

## 🚀 Features

✅ Automatically extracts webpage titles  
✅ Uses Regex for pattern matching  
✅ Generates a formatted report file  
✅ Simple and beginner-friendly automation script  

---

## 👨‍💻 Author

**Muhammad Ali Haider**

CodeAlpha Internship  
Project-3: Task Automation with Python Scripts

---

## 📅 Date

=======
# 🌐 CodeAlpha Internship

# Project-3: Task Automation with Python Scripts

## Task-3: Website Title Extractor

---

## 📌 Project Description

This project is a Python automation script that extracts the title of a fixed webpage automatically.

The program sends a request to the website, retrieves the HTML source code, searches for the webpage title using Regular Expressions (Regex), and saves the extracted title into a professional text report.

---

## 🎯 Objective

The goal of this task is to automate the process of extracting webpage titles without manually opening the website and checking its HTML source.

---

## 🛠️ Technologies Used

- Python 3.14.6
- Visual Studio Code 1.131.0

---

## 📚 Concepts Used

- `requests` Library
  - Sending HTTP GET requests
  - Receiving webpage responses

- `re` Module
  - Searching HTML content using Regular Expressions
  - Extracting required information

- File Handling
  - Reading and writing text files

- Conditional Statements
  - Checking whether a title was found

---

## 📂 Project Structure

```
Task-3-Website-Title-Extractor
│
├── website-title-extractor.py
├── Website-Title.txt
├── README.md
```

---

## ⚙️ How It Works

1. Import required Python modules.

2. Provide the website URL.

3. Send a GET request to the website using the `requests` module.

4. Receive the HTML source code of the webpage.

5. Search for the `<title>` tag using Regex.

6. Extract only the title text.

7. Save the extracted title into `Website-Title.txt`.

8. Display the extraction status.

---

## 🔍 Regex Pattern Used

```regex
<title>(.*)</title>
```

### Explanation:

- `<title>`  
  Finds the opening title tag.

- `(.*)`  
  Captures all characters inside the title tag.

- `</title>`  
  Finds the closing title tag.

The captured group contains only the webpage title.

---

## 📄 Output Example

Generated file:

```
Website-Title.txt
```

Example output:

```
======================================================================
                 Website Title Extraction Report
======================================================================

Website URL:
https://www.python.org/

Website Title:
Welcome to Python.org

======================================================================
                         End of Report
======================================================================
```

---

## 🚀 Features

✅ Automatically extracts webpage titles  
✅ Uses Regex for pattern matching  
✅ Generates a formatted report file  
✅ Simple and beginner-friendly automation script  

---

## 👨‍💻 Author

**Muhammad Ali Haider**

CodeAlpha Internship  
Project-3: Task Automation with Python Scripts

---

## 📅 Date

>>>>>>> aefc2f7c5a0c4a6c555f06b1b9115337647c29a6
July 28, 2026