# The-Ravens-Eye 🐦‍⬛🧿
Python script for a hostname resolver and a port scanner for a given hostname or IP Address from the end-user

![Alt text](Images/Screenshot_20260902_121242_Termux.jpg)

Requirements:
* Ensure the latest version of python is installed in your terminal (python 3.x)

Recommendations:
* Use a VPN while using this tool (Proton or Mullvad are encouraged)
* Enable TOR in your terminal
* Run proxychains4 while executing the software (This comes pre-installed with Kali-Linux)

Key Terminology:
* Pecking - When the software is actively performing a port scan or resolving a hostname
* Chirping - When the act of port scanning results in the discovery of open ports or resolving a hostname is successful

Installation & Execution:
* To install, simply type "git clone https://github.com/RavenTheBird789/The-Ravens-Eye" in your terminals command line
* To run, simply type "python3 ravens_eye.py" in your terminals command line or use the alias command to create a shortcut to run the program in your terminal such as "alias run="python3 ravens_eye.py""

Global Execution (Optional)
* Alternatively, you can run the program globally by simply typing "ravenseye" from anywhere in your terminal, follow these steps (For macOS and Linux):
  1. Make the file executable by typing "chmod +x ravens_eye.py" in your terminal
  2. Copy the file to a new name using "cp ravens_eye.py ravenseye" then make that executable too with "chmod +x ravenseye"
  3. Create a local bin folder if you don't already have one using "mkdir -p ~/.local/bin"
  4. Move the file into it using "mv ravenseye ~/.local/bin/"
  5. Make sure that folder is in your PATH by adding "export PATH="HOME/.local/bin:PATH"" to your ~/.bashrc (or ~/.zshrc if you use zsh)
  6. Reload your terminal config using "source ~/.bashrc" (or ~/.zshrc)
  7. Type "ravenseye" from anywhere to run the program

* For Windows
  1. Make sure Python is added to your PATH (check by typing "python --version" in Command Prompt. If it shows a version number, you're set)
  2. Create a folder to hold your global scripts, such as "C:\Scripts" (You can make this anywhere, just don't forget the path)
  3. Copy "ravens_eye.py" into that folder and rename the copy "ravenseye.py"
  4. In the same folder, create a new text file named "ravenseye.bat"
  5. Open "ravenseye.bat" in Notepad and add this single line "@python "%~dp0ravenseye.py" %*"
  6. Save and close the file
  7. Add your folder to your PATH: press the Windows key, search "Environment Variables", click "Edit the system environment variables", click "Environment Variables", under "User variables" select "Path", click "Edit", click "New", then paste in your folder path (e.g. "C:\Scripts")
  8. Click OK on all the windows to save
  9. Close and reopen Command Prompt or Powershell
  10. Type "ravenseye" from anywhere to run the program

Note:
* If the input fields for the start and end ports are empty the default values for the port scan with be 1 and 1024 respectively

Updates:
* Built-in python os library utilized to document findings from both resolving hostnames (or IP Addresses) and port scanning processes locally
