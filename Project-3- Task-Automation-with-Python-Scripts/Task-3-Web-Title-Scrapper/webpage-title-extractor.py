<<<<<<< HEAD
"""
==============================================================================
Task Name    :   Website Title Extractor
Author       :   Muhammad Ali Haider
Date         :   July 30, 2026
Python Ver.  :   Python 3.14.6
VS Code Ver. :   1.131.0

Description  :
Reads the HTML source code of a fixed webpage, extracts the webpage title
using Regular Expressions (Regex), displays a success message, and saves
the extracted title into a professional text report.

Concepts Used:
- requests Library
- Regular Expressions (re)
- File Handling
- Conditional Statements

Output File:
- Website-Title.txt
==============================================================================
"""

import requests
import re

# Website URL
url = "https://www.python.org/"

# Send a GET request to the website
response = requests.get(url)

# Store the HTML source code of the webpage
text = response.text

# Search for the title tag and capture only the title text
result = re.search(r"<title>(.*)</title>", text)

# Check if a title was found
if result:

    print("Website title extracted successfully.")
    print("Website-Title.txt has been created successfully.")
    print("Thank you for using Website Title Extractor!")

    # Create and write the extraction report
    with open("Website-Title.txt", "w") as file:

        file.write("=" * 70 + "\n")
        file.write(f"{'Website Title Extraction Report':^70}\n")
        file.write("=" * 70 + "\n\n")

        file.write(f"Website URL:\n{url}\n\n")

        file.write(f"Website Title:\n{result.group(1)}\n")

        file.write("=" * 70 + "\n")
        file.write(f"{'End of Report':^70}\n")
        file.write("=" * 70 + "\n\n")

# Execute if no title tag is found
else:
=======
"""
==============================================================================
Task Name    :   Website Title Extractor
Author       :   Muhammad Ali Haider
Date         :   July 30, 2026
Python Ver.  :   Python 3.14.6
VS Code Ver. :   1.131.0

Description  :
Reads the HTML source code of a fixed webpage, extracts the webpage title
using Regular Expressions (Regex), displays a success message, and saves
the extracted title into a professional text report.

Concepts Used:
- requests Library
- Regular Expressions (re)
- File Handling
- Conditional Statements

Output File:
- Website-Title.txt
==============================================================================
"""

import requests
import re

# Website URL
url = "https://www.python.org/"

# Send a GET request to the website
response = requests.get(url)

# Store the HTML source code of the webpage
text = response.text

# Search for the title tag and capture only the title text
result = re.search(r"<title>(.*)</title>", text)

# Check if a title was found
if result:

    print("Website title extracted successfully.")
    print("Website-Title.txt has been created successfully.")
    print("Thank you for using Website Title Extractor!")

    # Create and write the extraction report
    with open("Website-Title.txt", "w") as file:

        file.write("=" * 70 + "\n")
        file.write(f"{'Website Title Extraction Report':^70}\n")
        file.write("=" * 70 + "\n\n")

        file.write(f"Website URL:\n{url}\n\n")

        file.write(f"Website Title:\n{result.group(1)}\n")

        file.write("=" * 70 + "\n")
        file.write(f"{'End of Report':^70}\n")
        file.write("=" * 70 + "\n\n")

# Execute if no title tag is found
else:
>>>>>>> aefc2f7c5a0c4a6c555f06b1b9115337647c29a6
    print("Website title could not be found.")