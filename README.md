# Python Mini Projects Collection 🐍🚀

This repository contains a collection of Python mini-projects built to practice core programming concepts, data handling, database integration, and problem-solving.

---

## 📋 Table of Contents
1. [YouTube Manager App](#1-youtube-manager-app)
2. [AI Python Chatbot](#2-ai-python-chatbot)
3. [Python Expense Tracker](#3-python-expense-tracker)
4. [How to Run](#4-how-to-run)

---

### 1. YouTube Manager App 🎥
A command-line interface (CLI) application built with Python and SQLite database to manage a collection of YouTube videos with full CRUD functionality and persistent local data storage.

* **Features:**
  * **List Videos:** View all saved YouTube videos along with their duration/time from the database.
  * **Add Videos:** Insert new video records with names and timestamps into the SQLite database.
  * **Update Videos:** Modify existing video titles and timestamps using their unique video ID.
  * **Delete Videos:** Remove unwanted video records from the database by ID.
* **Tech Stack:** Python 3, SQLite3 (`youtube_videos.db`)
* **Concepts Used:** Database integration, raw SQL queries, parameterized statements, and exception handling.

---

### 2. AI Python Chatbot 🤖
A rule-based command-line chatbot built with Python that greets users based on the time of day, matches keywords using a custom dictionary-based memory system, and provides automated responses.

* **Features:**
  * **Time-Aware Dynamic Greetings:** Automatically fetches the system time and greets the user accordingly (Good Morning, Afternoon, Evening, Night).
  * **Dictionary-Based Keyword Matching:** Scans user queries against a predefined response dictionary to provide relevant answers.
  * **Fallback Handling:** Gracefully handles unknown queries with a default learning mode response.
  * **Interactive Session Loop:** Runs continuously until the user types `"bye"` to exit.
* **Tech Stack:** Python 3
* **Concepts Used:** `datetime` module, string manipulation (`.lower()`), conditional logic, and loops.

---

### 3. Python Expense Tracker 💰
A practical financial management tool built with Python to log, manage, and track daily personal expenses efficiently using in-memory data structures.

* **Features:**
  * **Add Expense:** Record detailed expenses including date, category (Food, Travel, Shopping), description/reason, and monetary amount.
  * **View Expenses:** Display a clean, numbered list of all recorded transactions with complete details.
  * **View Total Spending:** Automatically calculate and display the cumulative sum of all logged expenses.
* **Tech Stack:** Python 3
* **Concepts Used:** Lists, Dictionaries, user input validation, and accumulator logic.
## 4. How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ms1018807-debug/your-repository-name.git
  

  
