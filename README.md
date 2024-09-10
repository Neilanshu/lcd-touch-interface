# lcd-touch-interface

## Project Overview

The **LCD Touch Interface** is a Python application designed for use with an LCD screen featuring a touch interface. This project demonstrates a user-friendly login system and a dashboard with simulated sensor data. The application includes a registration screen, login screen, and a dashboard displaying data such as temperature, flow rate, color sensor readings, and current time.

## Features

- **Login Screen**: Allows users to log in with a user ID and password.
- **Registration Screen**: Users can create a new user ID and password.
- **Dashboard**: Displays simulated data for temperature, flow rate, color sensor readings, and current time.
- **On-Screen Keyboard**: Provides an interface for text input on the login and registration screens.
- **Logo Display**: Shows a logo on the login screen.

## Requirements

- Python 3.x
- `PIL` (Pillow)
- `tkinter` (usually included with Python)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Neilanshu/lcd-touch-interface.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd lcd-touch-interface
    ```

3. **Install Required Packages**:
    ```bash
    pip install pillow
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```

2. **Registration**:
    - Enter a user ID and password on the registration screen.
    - Confirm the password and click "Register."

3. **Login**:
    - Enter your registered user ID and password on the login screen.
    - Click "Login" to access the dashboard.

4. **Dashboard**:
    - View simulated sensor data for temperature, flow rate, color sensor readings, and current time.
    - Use the "Logout" button to return to the login screen.

## Simulated Data

Since real sensors were not available, the dashboard uses mock data generated by the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
