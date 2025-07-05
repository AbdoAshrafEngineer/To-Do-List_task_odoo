# 📝 To-Do List Module for Odoo 18

This module provides a simple To-Do list management system for Odoo 18, allowing users to create, view, and manage tasks efficiently.

## 📋 Features

- **To-Do Model**
  - A custom model `todo.task` to represent tasks in the To-Do list.
  - Fields included:
    - `Task Name`
    - `Assign To`
    - `Description`
    - `Due Date`
    - `Status` (New, In Progress, Completed)

- **List View**
  - Menu: Added under the main menu **"To-Do"** as **"All Tasks"**
  - Displays all tasks with their key details.

- **Form View**
  - Allows adding and editing tasks.
  - Includes fields for `Task Name`, `Assign To`, `Description`, `Due Date`, and `Status`.

- **Search View**
  - Search filters for `Status`, with default group by `Assign To`, `Status`, and `Due Date`.
  - Additional search on `Task Name` and `Assign To`.

---

## 🚀 Added Features

- **📌 Lines**
  - Added field to `todo.task` model: `Estimated Time`.
  - Timesheet lines related to the task, allowing users to record all their timesheets within the task.
  - Validates that total times in related lines **do not exceed the estimated time**.

- **📁 Archiving Technique**
  - Added archiving feature to `todo.task` model to manage obsolete tasks.

- **⚙️ Server Action**
  - Added a server action named **"Close"** to close tickets (works for single and multiple records).

- **⏳ Cron Job**
  - Automated action to notify users of late tasks based on the **Due Date** field.
  - Colors late records in the tree view for easy identification.

- **🖨️ Report Action**
  - Allows users to print any task in a predefined layout.

