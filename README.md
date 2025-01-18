This Python script automates the login process to Instagram using the Selenium framework, Tor as a proxy, and Firefox as the browser. It’s designed for testing purposes to simulate login attempts with multiple passwords. The script uses the Tor network for anonymity, ensuring that each login attempt is routed through the Tor network for increased privacy and security.
Features:

    Tor Network Integration: The script uses Tor as a proxy to anonymize the connection. By routing the requests through Tor, your real IP address is hidden, making the connection more secure and private.
    Selenium WebDriver Automation: Uses Selenium to automate browser interactions (e.g., entering username, password, clicking the login button) to log into Instagram.
    Password Cracking Simulation: Reads a list of passwords from a text file (password.txt) and attempts to log in with each password, making it useful for testing purposes.
    Firefox Browser: The script configures Firefox to use the Tor proxy for the network requests.
    ActionChains for Interaction: Selenium’s ActionChains is used to ensure that the interaction with the login button is smooth and natural.
    Login Success/Failure Feedback: After each attempt, the script checks if the login is successful by looking for Instagram's homepage icon. It reports whether the login attempt was successful or not.
    Delay Between Requests: A random delay is introduced between login attempts to simulate human-like interaction and prevent triggering Instagram's anti-spam systems (though currently commented out).

Requirements:

    Python 3.6+
    Selenium: pip install selenium
    Tor: Download and install the Tor browser and run the Tor service on your machine.
    Geckodriver: Required for Firefox to interact with Selenium. Ensure it’s installed and available in your system’s PATH.
    Stem: pip install stem for Tor network interaction.

Installation:

    Install Tor:
        Download and install the Tor Browser.
        Make sure Tor is running on your machine. It should be running on localhost port 9150 by default.

    Install Python dependencies:

    pip install selenium stem

    Download Geckodriver:
        Download the latest version of Geckodriver (for Firefox) from here.
        Extract the geckodriver binary and add it to your system’s PATH.

    Update the script:
        Place your Instagram username and password list (password.txt) in the same directory as the script.
        Replace 'kikomrn' in the login_to_instagram() function with your actual Instagram username.

Usage:

    Launch Tor:
        Ensure the Tor service is running. You can do this by launching the Tor browser or starting the Tor service from the command line.
    Run the Script:

        Execute the script in a terminal or command prompt:

        python instagram_login_script.py

        The script will try to log in to Instagram with each password from the password.txt file. It will print the result for each login attempt.

Example Output:

Trying password: password1
Login successful!
Trying password: password2
Login unsuccessful.
...

Important Notes:

    Ethical Usage Disclaimer: This script is intended for educational purposes only. Using this script for unauthorized login attempts, password cracking, or any other malicious activities is strictly prohibited and may lead to legal consequences. This script should only be used with accounts you own or have explicit permission to access. By using this script, you agree to take full responsibility for any actions performed with it.
    Tor Usage: Using Tor provides anonymity but can sometimes cause slower response times. Ensure your internet connection is stable for optimal performance.
    Captcha and Anti-Spam Measures: Instagram may trigger CAPTCHA challenges when login attempts are made too quickly or too frequently. This script does not handle CAPTCHA challenges, so use it responsibly and avoid aggressive login attempts.

Customization:

    You can uncomment the line # firefox_options.add_argument('--headless') if you want the browser to run in headless mode (without opening a GUI).
    Adjust the random delay between login attempts by modifying the wait_time line (currently commented out).
    If you want to log in with a different Instagram account, simply replace the login_to_instagram('kikomrn', password) with the desired username.

Contributions:

Feel free to fork this repository and contribute by submitting pull requests. If you have any suggestions or improvements, please open an issue or a pull request.
License:

This repository is licensed under the MIT License.
