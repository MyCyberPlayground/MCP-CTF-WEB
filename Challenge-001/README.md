# My Cyber Playground - Web CTF 🕷️

Welcome to **My Cyber Playground**, where security meets fun! Test your web hacking skills in our carefully crafted challenges.

## 🚀 Getting Started

### 🎯 Challenge-001: Web Fundamentals
**Difficulty:** 🟢 **Script-Kiddie** (Easy)  
**Points:** 100 per flag (800 + 800 for easter eggs = 1600)  
**Technologies:** HTML, CSS, JavaScript  
**Flags:** 8+4 hidden flags to discover

### Challenge Description
Welcome to your first web security challenge! You've stumbled upon a poorly secured banking website that's hiding several secrets. Your mission is to find all 8 flags using various web exploitation techniques.

**Skills Tested:**
- Source Code Analysis
- Client-Side Security
- Basic Web Exploitation
- Cookie Manipulation
- Hidden Directory Discovery
- API Endpoint Discovery
- Authentication Bypass

---

## Prerequisites: Install Git

### Windows

#### Option 1: Official Git Installer (Recommended)
1. Visit [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the latest Git for Windows installer
3. Run the installer and follow the setup wizard
4. Accept the default settings (recommended for beginners)


### macOS

#### Option 1: Using Homebrew (Recommended)
```bash
# Install Homebrew first if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git
```

#### Option 2: Using MacPorts
```bash
sudo port install git
```

#### Option 3: Official Installer
1. Visit [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
2. Download and install the macOS Git installer


### Linux (Security/Hacking Distributions)

#### Ubuntu/Debian-based Systems
```bash
sudo apt update
sudo apt install git
```

#### Kali Linux
```bash
# Git is usually pre-installed, but if needed:
sudo apt update
sudo apt install git
```

#### Parrot Security OS
```bash
# Git is usually pre-installed, but if needed:
sudo apt update
sudo apt install git
```

#### Arch Linux / BlackArch
```bash
sudo pacman -S git
```

#### Pentoo (Gentoo-based)
```bash
sudo emerge --ask dev-vcs/git
```

#### BackBox / Other Ubuntu-based Security Distros
```bash
sudo apt update
sudo apt install git
```

## Verify Installation

After installation, verify Git is properly installed:

```bash
git --version
```

You should see output similar to:
```
git version 2.34.1
```

## Initial Git Configuration (Optional but Recommended)

Set up your Git identity for commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check your configuration:
```bash
git config --list
```

## Troubleshooting

### Windows
- If Git commands are not recognized, restart your command prompt or PowerShell
- Make sure Git is added to your system PATH during installation

### macOS
- If using Homebrew and getting permission errors, try: `sudo chown -R $(whoami) /usr/local/share/zsh`

### Linux
- If you get permission errors, make sure you have sudo privileges
- For older Linux distributions, you might need to compile Git from source

---

## 🛠️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone --filter=blob:none --sparse https://github.com/MyCyberPlayground/MCP-CTF-WEB.git

   cd MCP-CTF-WEB
   git sparse-checkout set Challenge-001
   cd Challenge-001
   ```

2. **Start the web server:**
   ```bash
   # Option 1: Using the provided Python server (Recommended)
   cd Challenge-001
   python3 setup/server.py
   
   # Option 2: Using Python simple server
   cd Challenge-001/src
   python3 -m http.server 8000
   
   # Option 3: Using PHP
   cd Challenge-001/src
   php -S localhost:8000
   ```

3. **Open your browser:**
   Navigate to `http://localhost:8000`

4. **Start hacking:**
   Explore the website and find all 8 flags and other easter egg flags!

---

## 🚩 Flag Submission

### Submit Your Flags
**[🔒 SUBMIT FLAGS HERE 🔒](https://flags.mycyberplayground.xyz)**

### Flag Format
All flags follow the format: `MCP{flag_content_here}`

**Example:** `MCP{example_flag_content}`

---

## 🛠️ Technical Information

### System Requirements
- **Languages:** HTML5, CSS3, JavaScript
- **Server:** Python 3.x (recommended) or any HTTP server
- **Browser:** Modern web browser with Developer Tools

### Supported Environments
- ✅ Windows 10/11
- ✅ macOS (Intel & Apple Silicon)
- ✅ Linux (Ubuntu, Debian, CentOS)
- ✅ WSL (Windows Subsystem for Linux)

### Browser Compatibility
- ✅ Chrome 
- ✅ Firefox 
- ✅ Safari 
- ✅ Edge 

---

## 🎮 Challenge Difficulty Levels

- 🟢 **Script-Kiddie** (Easy) - Perfect for beginners
- 🟡 **1337 Ninja** (Medium) - For intermediate hackers  
- 🔴 **Elite Hacker** (Hard) - Advanced exploitation
- 🟣 **Digital Overlord** (Very Hard) - Master level challenges

---

## 💡 Getting Started Tips

- Open **Browser Developer Tools** (F12) - your best friend!
- Try **viewing page source** (Ctrl+U or right-click → View Source)
- Check the **Network tab** for API calls
- Inspect **cookies and local storage**
- Don't forget to read **robots.txt**
- Try common credentials like **admin/password**
- Look for **hidden comments** in HTML/CSS/JavaScript
- Use the **Console tab** to run JavaScript commands

---

## 💪 Remember

**Great hackers are made through practice, patience, and curiosity. Don't give up if something seems tricky at first - every expert was once a beginner!**

---

## ⚠️ IMPORTANT DISCLAIMER

**This CTF challenge is designed for educational purposes only.**

- ✅ **Practice ethical hacking techniques**
- ✅ **Learn web security fundamentals**
- ✅ **Develop cybersecurity skills**

**DO NOT:**
- ❌ Use these techniques on websites you don't own
- ❌ Attack real systems without explicit permission
- ❌ Engage in any illegal hacking activities

**Always practice responsible disclosure and ethical hacking principles.**

---


**Ready to start your cybersecurity journey?**

## **[🎯 START CHALLENGE & SUBMIT FLAGS 🎯](https://flags.mycyberplayground.xyz)**

---

**Happy Hacking! 🎭**