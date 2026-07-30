<<<<<<< HEAD
"""
==============================================================================
CodeAlpha Internship

Project-3 : Task Automation with Python Scripts
Task-2    : Email Address Extractor

Author            : Muhammad Ali Haider
Date              : July 28, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
Reads a text file, extracts all valid email addresses using Regular
Expressions (Regex), displays them on the screen, and saves the extracted
email addresses into a new text file named "Extracted-Emails.txt".

Modules Used:
- re (Regular Expressions)
- File Handling
- Loops
- Conditional Statements

Input File:
- emails.txt

Output File:
- Extracted-Emails.txt
==============================================================================
"""


# Import Regular Expression module
import re


# Open and read the input text file
with open("emails.txt", "r") as file:
    
    # Store complete file data
    data = file.read()


# Find all email addresses using Regex pattern
result = re.findall(r"\w+@\w+\.\w+", data)


# Check if email addresses were found
if result:

    print("\nExtracted Email Addresses:\n")


    # Display all extracted email addresses
    for email in result:
        print(email)


    print("\nEmail addresses extracted successfully.")


    # Create output file and save extracted emails
    with open("Extracted-Emails.txt", "w") as file:


        # Write report header
        file.write("=" * 70 + "\n")
        file.write(f"{'Email Extraction Report':^70}\n")
        file.write("=" * 70 + "\n\n")


        # Write extracted email addresses
        file.write("Extracted Email Addresses:\n\n")

        for email in result:
            file.write(email + "\n")


        # Write report footer
        file.write("\n" + "=" * 70 + "\n")
        file.write(f"{'End of Report':^70}\n")
        file.write("=" * 70 + "\n")


    # Display completion message
    print("\nExtracted-Emails.txt has been created successfully.")
    print("Thank you for using Email Extractor!")


# Execute when no emails are found
else:

=======
"""
==============================================================================
CodeAlpha Internship

Project-3 : Task Automation with Python Scripts
Task-2    : Email Address Extractor

Author            : Muhammad Ali Haider
Date              : July 28, 2026
IDE               : Visual Studio Code 1.131.0
Python Version    : Python 3.14.6

Description:
Reads a text file, extracts all valid email addresses using Regular
Expressions (Regex), displays them on the screen, and saves the extracted
email addresses into a new text file named "Extracted-Emails.txt".

Modules Used:
- re (Regular Expressions)
- File Handling
- Loops
- Conditional Statements

Input File:
- emails.txt

Output File:
- Extracted-Emails.txt
==============================================================================
"""


# Import Regular Expression module
import re


# Open and read the input text file
with open("emails.txt", "r") as file:
    
    # Store complete file data
    data = file.read()


# Find all email addresses using Regex pattern
result = re.findall(r"\w+@\w+\.\w+", data)


# Check if email addresses were found
if result:

    print("\nExtracted Email Addresses:\n")


    # Display all extracted email addresses
    for email in result:
        print(email)


    print("\nEmail addresses extracted successfully.")


    # Create output file and save extracted emails
    with open("Extracted-Emails.txt", "w") as file:


        # Write report header
        file.write("=" * 70 + "\n")
        file.write(f"{'Email Extraction Report':^70}\n")
        file.write("=" * 70 + "\n\n")


        # Write extracted email addresses
        file.write("Extracted Email Addresses:\n\n")

        for email in result:
            file.write(email + "\n")


        # Write report footer
        file.write("\n" + "=" * 70 + "\n")
        file.write(f"{'End of Report':^70}\n")
        file.write("=" * 70 + "\n")


    # Display completion message
    print("\nExtracted-Emails.txt has been created successfully.")
    print("Thank you for using Email Extractor!")


# Execute when no emails are found
else:

>>>>>>> aefc2f7c5a0c4a6c555f06b1b9115337647c29a6
    print("No email addresses found.")