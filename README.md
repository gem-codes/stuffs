# Stuffs Factory API

The **Stuffs Factory API** is a Django-based application designed to manage specifications, groups, and components for a fictional that produces various "Stuffs".

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)

## Project Overview

The **Stuffs Factory API** facilitates the management of:
- **Specifications:** Guidelines for creating Stuffs, consisting of Components organized into Groups.
- **Groups:** Organizational units within Specifications.
- **Components:** Building blocks of Stuffs, each assigned a specific Part.
  
The application aims to replace spreadsheet-based workflows with a more efficient RESTful API system.

## Features

- **Specifications Management**:
  - Create, retrieve, update, and delete Specifications.
  - Mark Specifications as completed when all Components have assigned Parts.

- **Groups and Components Management**:
  - Create, retrieve, update, and delete Groups within Specifications.
  - Create, retrieve, update, and delete Components within Groups.
  - Assign Parts to Components.

- **Data Integrity and Security**:
  - Enforcement of business rules such as preventing modifications to completed Specifications.
  - Unique Groups per Specification to maintain data consistency.

## Installation

To run the **Stuffs Factory API** locally, follow these steps:

1. Clone the repository

   ```bash
   git clone https://github.com/gem-codes/stuffs.git
   cd stuffs
   ```

2. Create and activate a virtual environment

  ```bash
  pip install uv
  uv venv
  source .venv/bin/activate
  ```

3. Install dependencies

  ```bash
  uv pip install -r requirements.txt
  ```

4. Apply database migrations

  ```bash
  python manage.py migrate
  ```

5. Run the development server

  ```bash
  python manage.py runserver
  ```

6.  The API should now be accessible at http://localhost:8000/api/v1/. Postman collection is also present in the code for better clearity on endpoints.
