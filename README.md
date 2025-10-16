# Study Reminder System

This project is a study reminder system for students. It allows you to add students, schedule personalized reminders for them at their preferred times, and log all reminders sent.

## Features

- **Add students** with name, email, course, and preferred reminder time.
- **List all students** currently registered.
- **Send reminders manually** to all students.
- **Schedule automatic reminders** at each student's preferred time (using the `schedule` library).
- **Log all reminders** sent, with timestamp, to `reminder_log.txt`.

## File Overview

- `main.py` - Main menu and user interface.
- `students.py` - Core module for in-memory management of students (add, remove, retrieve).
- `students_manager.py` - Handles loading, saving, and managing students with JSON storage, and uses the `Students` class internally.
- `reminder_generator.py` - Generates personalized reminder messages.
- `reminder_sender.py` - Simulates sending reminders (prints to console).
- `logger.py` - Logs reminders to `reminder_log.txt`.
- `scheduler.py` - Schedules reminders at preferred times.
- `students.json` - Stores student data persistently.
- `reminder_log.txt` - Log file for sent reminders.

## How It Works

- All student management (add, remove, retrieve) is handled by the `Students` class in `students.py`.
- Persistent storage (saving/loading students) is handled by `students_manager.py`, which wraps the `Students` class and stores data in `students.json`.
- The main program (`main.py`) uses `StudentsManager` for all student operations, ensuring both in-memory management and file persistence.
- Reminders are generated, sent (simulated), and logged using their respective modules.
- The scheduler runs in the background and sends reminders at each student's preferred time.

## Installation and Usage

### 1. Install the package locally

From the project root folder, run:

```bash
pip install .
```

### 2. Run the program

After installation, you can start the program with:

```bash
study-reminder
```

Or, if you want to run directly without installing:

```bash
python3 main.py
```

### 3. Menu Options

- **1. List students** – Shows all students and their info.
- **2. Add student** – Add a new student (time format: `HH:MM`, 24-hour clock, e.g. `08:00`).
- **3. Send reminders now** – Immediately sends reminders to all students.
- **4. Start scheduler** – Starts automatic reminders at each student's preferred time.
- **5. Exit** – Quit the program.

### 4. Time Format

When adding a student, enter the preferred time as `HH:MM` (e.g., `14:30` for 2:30 PM).  
**Do not use AM/PM.**

### 5. Log File

All reminders sent (manually or scheduled) are logged in `reminder_log.txt` with a timestamp.

## Example

```
1. List students
2. Add student
3. Send reminders now
4. Start scheduler
5. Exit
Choose an option: 2

Add a new student
Name: Alex
Email: alex@example.com
Course: ACIT 4420
Preferred time (e.g., 08:00): 20:00
```

## Notes

- The scheduler will only print/send reminders when the system time matches a student's preferred time.
- You can stop the scheduler with `Ctrl+C`.
- All student data is saved in `students.json` and managed in memory using the `Students` class.

## Author

- Alex Bazo

---