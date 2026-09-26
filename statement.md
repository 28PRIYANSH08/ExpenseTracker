# Project Statement

## Project Title

Expense Tracker

## Problem Statement

Students often make small daily expenses such as food, travel, stationery, and other personal purchases. When these expenses are not recorded properly, it becomes difficult to understand where money is being spent and how much is still available from a monthly budget.

The Expense Tracker is designed to provide a simple way for students to record and manage their expenses while keeping track of their monthly budget.

## Project Scope

The project focuses on recording personal expenses, managing a monthly budget, and generating a basic spending report.

The application is designed as a simple Python-based application using SQLite for storing data.

## Target Users

The primary users of the application are:

- Students
- Individuals who want to track personal expenses
- Beginners who want a simple expense management system

## Objectives

The main objectives of the project are:

1. Allow users to record their expenses.
2. Allow users to view their saved expenses.
3. Allow users to edit and delete expenses.
4. Allow users to set and view a monthly budget.
5. Calculate total spending.
6. Calculate the remaining budget.
7. Show spending grouped by category.
8. Store expense information reliably using a database.

## Functional Requirements

### 1. Expense Management

The system should allow users to:

- Add expenses
- View expenses
- Edit expenses
- Delete expenses

### 2. Budget Management

The system should allow users to:

- Set a monthly budget
- View the current budget

### 3. Expense Reporting

The system should:

- Calculate total expenses
- Calculate remaining budget
- Group expenses by category
- Display an expense report

## Non-Functional Requirements

### Usability
The application should have a simple menu-based interface that is easy for users to understand.

### Reliability
Expense information should be stored in SQLite so that data remains available after the program is closed.

### Error Handling
The application should handle invalid numerical inputs and prevent the program from crashing because of common user input errors.

### Maintainability
The project is divided into separate Python modules for database management, expenses, budgeting, reports, and the main program.

## Technologies Used

- Python
- SQLite
- Pytest
- VS Code
- Git and GitHub

## High-Level Features

- Expense management
- Monthly budget management
- Expense reports
- Category-wise spending
- SQLite data storage
- Automated testing