# 🖼️ JPG File Organizer

A simple Python automation script that automatically organizes all **.jpg** image files by moving them from the **Downloads** folder into a dedicated folder named **JPG Files**.

---

## 📌 Features

- Automatically creates the **JPG Files** folder if it does not exist.
- Detects all `.jpg` image files.
- Moves all JPG files into the destination folder.
- Displays the total number of files moved.
- Displays a message if no JPG files are found.

---

## 🛠 Technologies Used

- Python 3.14.6
- Visual Studio Code 1.131.0

---

## 📂 Project Structure

```
JPG-File-Organizer/
│
├── Downloads/
│   ├── captain-america.jpg
│   ├── iron-man.jpg
│   ├── moon-knight.jpg
│   ├── notes.txt
│   ├── cat.png
│   └── ...
│
├── jpg-file-organizer.py
└── README.md
```

---

## ▶️ How to Run

1. Place your JPG images inside the **Downloads** folder.
2. Open the project in Visual Studio Code.
3. Run:

```bash
python jpg-file-organizer.py
```

4. The program will:
   - Create a folder named **JPG Files** (if it does not already exist).
   - Move all `.jpg` image files into the new folder.
   - Display the total number of files moved.

---

## 📖 Concepts Used

- File and Folder Handling (`os`)
- File Moving (`shutil`)
- Loops
- Conditional Statements
- Path Handling

---

## 📄 Example

### Before

```
Downloads/
│
├── captain-america.jpg
├── iron-man.jpg
├── moon-knight.jpg
├── cat.png
├── notes.txt
```

### After

```
Downloads/
│
├── cat.png
├── notes.txt
│
└── JPG Files/
    ├── captain-america.jpg
    ├── iron-man.jpg
    └── moon-knight.jpg
```

---

## 💻 Example Output

```
7 JPG file(s) moved successfully.
```

or

```
No JPG Files Found!
```

---

## 👨‍💻 Author

**Muhammad Ali Haider**

CodeAlpha Internship – Python Programming