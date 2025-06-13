#!/usr/bin/env python3
"""
Comprehensive HTTP Server for Challenge-001 CTF
Handles all endpoints and callbacks referenced in script.js
"""

import http.server
import socketserver
import os
import mimetypes
import json
from pathlib import Path

class CTFRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Enhanced request handler for CTF challenge with all callbacks"""
    
    def __init__(self, *args, **kwargs):
        # Add JSON mime type support
        mimetypes.add_type('application/json', '.json')
        super().__init__(*args, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for API requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Handle special CTF endpoints
        if self.path == '/favicon.ico':
            self.send_error(404, "Not Found")
            return
        
        # Handle help endpoint (referenced in script.js help() function)
        if self.path == '/help' or self.path == '/help/':
            self.serve_help_page()
            return
        
        # Handle API requests (referenced in script.js makeApiCall() and testApi())
        if self.path.startswith('/api/'):
            self.handle_api_request()
            return
        
        # Handle debug endpoint (for script.js debugging functions)
        if self.path == '/debug' or self.path == '/debug/':
            self.serve_debug_page()
            return
        
        # Log interesting requests for learning (matches script.js expectations)
        if self.path.startswith('/admin'):
            print(f"[CTF] Admin access attempt: {self.path}")
        elif self.path == '/robots.txt':
            print(f"[CTF] Robots.txt accessed - good reconnaissance!")
        elif self.path.startswith('/api'):
            print(f"[CTF] API endpoint accessed: {self.path}")
        
        # Handle regular file requests
        super().do_GET()
    
    def serve_help_page(self):
        """Serve comprehensive help page """
        help_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF Help - Challenge 001</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        h1 { color: #4a90e2; text-align: center; }
        h2 { color: #4a90e2; border-bottom: 2px solid #4a90e2; padding-bottom: 0.5rem; }
        .tip { background: #f8f9fa; padding: 1rem; border-left: 4px solid #4a90e2; margin: 1rem 0; }
        .flag-format { background: #e7f3ff; padding: 1rem; border-radius: 5px; margin: 1rem 0; }
        .tools { background: #fff3cd; padding: 1rem; border-radius: 5px; margin: 1rem 0; }
        .warning { background: #f8d7da; padding: 1rem; border-radius: 5px; margin: 1rem 0; }
        .console-commands { background: #e8f5e8; padding: 1rem; border-radius: 5px; margin: 1rem 0; }
        code { background: #f4f4f4; padding: 2px 4px; border-radius: 3px; font-family: 'Courier New', monospace; }
        ul { padding-left: 2rem; }
        li { margin-bottom: 0.5rem; }
        .nav-links { text-align: center; margin-top: 2rem; }
        .nav-links a { color: #4a90e2; text-decoration: none; margin: 0 1rem; }
        .nav-links a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💻 My Cyber Playground - CTF Help</h1>
        
        <h2>Challenge Overview</h2>
        <div class="flag-format">
            <strong>Goal:</strong> Find 8 flags in the format: <code>MCP{...}</code> and other easter eggs<br>
            <strong>Difficulty:</strong> Beginner<br>
            <strong>Type:</strong> Web Application Security<br>
            <strong>Skills:</strong> HTML, CSS, JavaScript, Browser DevTools
        </div>

        <h2>Getting Started</h2>
        <ol>
            <li><strong>Explore normally:</strong> Click around the website like a regular user</li>
            <li><strong>View page source:</strong> Right-click and select "View Page Source" (Ctrl+U)</li>
            <li><strong>Open Developer Tools:</strong> Press F12 or right-click and select "Inspect"</li>
            <li><strong>Try logging in:</strong> Look for login functionality and try common credentials</li>
            <li><strong>Check console:</strong> Look for JavaScript messages and try typing commands</li>
        </ol>

        <h2>Essential Browser Tools</h2>
        <div class="tools">
            <ul>
                <li><strong>Developer Tools (F12):</strong> Your most important tool</li>
                <li><strong>Console Tab:</strong> Run JavaScript commands and see debug messages</li>
                <li><strong>Elements Tab:</strong> Inspect HTML and CSS</li>
                <li><strong>Sources Tab:</strong> View JavaScript files and set breakpoints</li>
                <li><strong>Application Tab:</strong> Check cookies, local storage, and sessions</li>
                <li><strong>Network Tab:</strong> Monitor HTTP requests and responses</li>
            </ul>
        </div>

        <h2>Available Console Commands</h2>
        <div class="console-commands">
            Open the browser console (F12 → Console tab) and try these commands:
            <ul>
                <li><code>help()</code> - Show available functions</li>
                <li><code>debugInfo()</code> - List all debug functions</li>
                <li><code>getSecret()</code> - Get a secret message</li>
                <li><code>decodeSecret()</code> - Decode Base64 hidden data</li>
                <li><code>testApi()</code> - Test the API endpoint</li>
                <li><code>makeApiCall()</code> - Make direct API request</li>
                <li><code>showHiddenFeatures()</code> - Show hidden functionality</li>
                <li><code>checkAdminStatus()</code> - Check admin authentication</li>
                <li><code>fetchUserData()</code> - Fetch user data (requires login)</li>
            </ul>
        </div>

        <h2>What to Look For</h2>
        <div class="tip">
            <ul>
                <li><strong>HTML Comments:</strong> Developers often leave notes in <!-- comments --></li>
                <li><strong>JavaScript Variables:</strong> Client-side code may contain secrets</li>
                <li><strong>CSS Files:</strong> Styles can hide information in creative ways</li>
                <li><strong>Cookies:</strong> Authentication tokens and session data</li>
                <li><strong>Encoded Data:</strong> Base64 or other encoding methods</li>
                <li><strong>Hidden Files:</strong> Check robots.txt for interesting directories</li>
                <li><strong>API Endpoints:</strong> Look for AJAX calls and API responses</li>
                <li><strong>localStorage:</strong> Check browser storage for debug info</li>
            </ul>
        </div>

        <h2>Flag Hunting Techniques</h2>
        <div class="tip">
            <strong>Source Code Analysis:</strong>
            <ul>
                <li>View page source (Ctrl+U) and search for "MCP{" or "flag"</li>
                <li>Check all JavaScript files for hardcoded secrets</li>
                <li>Look at CSS files for hidden content</li>
            </ul>
            
            <strong>Authentication Testing:</strong>
            <ul>
                <li>Try common credentials like admin/password123</li>
                <li>Check cookies after successful login</li>
                <li>Look for admin panels and restricted areas</li>
            </ul>
            
            <strong>API Discovery:</strong>
            <ul>
                <li>Check robots.txt for hidden endpoints</li>
                <li>Try accessing /api/secret.json directly</li>
                <li>Use console functions to make API calls</li>
            </ul>
        </div>

        <h2>Common Beginner Mistakes</h2>
        <ul>
            <li>Not checking page source code thoroughly</li>
            <li>Ignoring browser developer tools</li>
            <li>Not trying obvious passwords</li>
            <li>Forgetting to check cookies and localStorage</li>
            <li>Not exploring all pages and links</li>
            <li>Not reading robots.txt file</li>
            <li>Not using browser console commands</li>
            <li>Overlooking Base64 encoded data</li>
        </ul>

        <h2>Stuck? Try This Checklist:</h2>
        <div class="tip">
            <ol>
                <li>Did you view the source of ALL pages?</li>
                <li>Did you check ALL JavaScript files?</li>
                <li>Did you try logging in with admin/password123?</li>
                <li>Did you check cookies after login?</li>
                <li>Did you try the console commands listed above?</li>
                <li>Did you decode any Base64 data you found?</li>
                <li>Did you check robots.txt?</li>
                <li>Did you try accessing /api/secret.json?</li>
                <li>Did you check localStorage and sessionStorage?</li>
                <li>Did you look at CSS files for hidden content?</li>
            </ol>
        </div>

        <h2>Advanced Exploration</h2>
        <div class="tip">
            <ul>
                <li><strong>Network Analysis:</strong> Use F12 → Network tab to see all requests</li>
                <li><strong>JavaScript Debugging:</strong> Set breakpoints in Sources tab</li>
                <li><strong>Console Exploration:</strong> Type commands and explore object properties</li>
                <li><strong>Admin Panel:</strong> Try accessing /admin/ after login</li>
                <li><strong>Hidden Variables:</strong> Check window.secretConfig and other global variables</li>
            </ul>
        </div>

        <div class="warning">
            <strong>Remember:</strong> These techniques are for learning only! Never use them on websites you don't own or without explicit permission. This is a safe learning environment.
        </div>

        <div class="nav-links">
            <a href="/">← Back to Challenge</a> |
            <a href="/robots.txt">robots.txt</a> |
            <a href="/api/secret.json">API</a> |
            <a href="/debug">Debug Info</a>
        </div>
    </div>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(help_content.encode('utf-8'))
        print(f"[CTF] 💻 Help page accessed - guiding the hacker!")

    def serve_debug_page(self):
        """Serve debug information page (for advanced users)"""
        debug_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Debug Info - Challenge 001</title>
    <style>
        body { font-family: 'Courier New', monospace; background: #1a1a1a; color: #00ff00; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { color: #00ff00; text-align: center; }
        .debug-section { background: #2a2a2a; padding: 1rem; margin: 1rem 0; border-radius: 5px; }
        .debug-section h3 { color: #ffff00; }
        code { background: #333; padding: 2px 4px; border-radius: 3px; }
        a { color: #00ffff; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💻 DEBUG MODE - Challenge 001</h1>
        
        <div class="debug-section">
            <h3>System Information</h3>
            <p>Server: CTF Challenge Server v1.0</p>
            <p>Challenge: Web Fundamentals - Challenge 001</p>
            <p>Debug Mode: ENABLED</p>
            <p>API Endpoint: /api/secret.json</p>
        </div>

        <div class="debug-section">
            <h3>Available Console Functions</h3>
            <ul>
                <li><code>help()</code> - Show help information</li>
                <li><code>debugInfo()</code> - List debug functions</li>
                <li><code>getSecret()</code> - Get secret message</li>
                <li><code>decodeSecret()</code> - Decode Base64 data</li>
                <li><code>testApi()</code> - Test API endpoint</li>
                <li><code>showHiddenFeatures()</code> - Show hidden features</li>
                <li><code>checkAdminStatus()</code> - Check admin auth</li>
            </ul>
        </div>

        <div class="debug-section">
            <h3>Flag Locations (SPOILER ALERT!)</h3>
            <p>Flag 1: HTML comments in index.html</p>
            <p>Flag 2: JavaScript variable in index.html</p>
            <p>Flag 3: CSS property in styles.css</p>
            <p>Flag 4: Cookie after login (admin/password123)</p>
            <p>Flag 5: Base64 encoded in script.js</p>
            <p>Flag 6: Access /api/secret.json or call testApi()</p>
            <p>Flag 7: view source of admin page</p>
            <p>Flag 8: Login and access dashboard, view source</p>
            <p>Flag 9-12: Hidden [easter eggs]</p>
        </div>

        <div class="debug-section">
            <h3>Quick Links</h3>
            <p><a href="/">Main Site</a> | <a href="/help">Help</a> | <a href="/api/secret.json">API</a></p>
        </div>
    </div>

    <script>
        console.log("💻 Debug page loaded");
        console.log("💻 All console functions are available here too!");
    </script>
</body>
</html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(debug_content.encode('utf-8'))
        print(f"[CTF] 💻 Debug page accessed - advanced user detected!")

    def handle_api_request(self):
        """Handle API endpoint requests (referenced throughout script.js)"""
        if self.path == '/api/secret' or self.path == '/api/secret.json':
            # Generate JSON response matching script.js expectations
            try:
                secret_data = {
                    "status": "success",
                    "message": "Welcome to SecureBank's secret API! You found it!",
                    "ctf_info": {
                        "challenge_name": "Web Fundamentals - Challenge 001",
                        "difficulty": "Beginner",
                        "flags_total": 8,
                        "easter_eggs": 4,
                        "find_all_flag": "there are a donze flags hidden",
                        "flag_format": "MCP{...}",
                        "discovered_flag": "MCP{4p1_3ndp01nt_d1sc0v3r3d}"
                    },
                    "hints_for_beginners": {
                        "general_tips": [
                            "Always start by looking at the page source (right-click -> View Page Source)",
                            "Press F12 to open Developer Tools - this is your best friend!",
                            "Try common username/password combinations like admin/password123",
                            "Don't forget to check what gets stored in your browser (cookies, localStorage)",
                            "Comments in code often contain useful information"
                        ],
                        "flag_hunting_areas": {
                            "source_code": "HTML comments are often overlooked by developers",
                            "javascript": "Client-side code sometimes contains secrets it shouldn't",
                            "styling": "CSS files can hide things in creative ways",
                            "browser_storage": "Authentication often leaves traces behind",
                            "encoding": "Sometimes data is encoded rather than encrypted (try Base64)"
                        },
                        "console_commands": {
                            "help": "Type help() in console for guidance",
                            "debugInfo": "Type debugInfo() to see available functions",
                            "decodeSecret": "Type decodeSecret() to decode hidden data",
                            "testApi": "Type testApi() to test this API endpoint",
                            "showHiddenFeatures": "Type showHiddenFeatures() for more hints"
                        },
                        "getting_started": {
                            "step_1": "Explore the website normally first",
                            "step_2": "Try to understand what the site does",
                            "step_3": "Look for login functionality and try admin/password123",
                            "step_4": "Open Developer Tools (F12) and poke around",
                            "step_5": "Check if there are any interesting files mentioned in robots.txt"
                        },
                        "tools_beginners_should_know": {
                            "browser_devtools": "Built into every browser - press F12",
                            "view_source": "Right-click -> View Page Source or Ctrl+U",
                            "console": "JavaScript console lets you run commands",
                            "network_tab": "See what requests the page makes",
                            "application_tab": "Check cookies, local storage, session storage",
                            "sources_tab": "View and debug JavaScript files"
                        }
                    },
                    "encouragement": {
                        "stuck": "Don't worry if you get stuck! That's normal for beginners.",
                        "persistence": "Each flag teaches you something new about web security.",
                        "learning": "The goal is to learn, not to solve everything quickly.",
                        "community": "Real hackers help each other - learning together is powerful!"
                    },
                    "easter_eggs": {
                        "console_hint": "Try typing function names in the browser console",
                        "hidden_functions": "Developers sometimes leave debug functions accessible",
                        "click_counter": "Try clicking around the site and watch the console",
                        "keyboard_shortcuts": "Some pages respond to special key combinations",
                        "global_variables": "Check window.secretConfig and other global objects"
                    },
                    "advanced_tips": {
                        "admin_panel": "After login, try accessing /admin/ directory",
                        "localStorage": "Check localStorage for debug information",
                        "network_analysis": "Watch the Network tab for interesting requests",
                        "javascript_debugging": "Use the Sources tab to set breakpoints",
                        "base64_decoding": "Look for strings that might be Base64 encoded"
                    },
                    "warning": "Remember: These techniques are for learning only! Never use them on websites you don't own!",
                    "final_message": "You're doing great! Keep exploring and stay curious!",
                    "next_steps": "Once you find all 8 flags, try exploring more advanced CTF challenges!"
                }
                
                content = json.dumps(secret_data, indent=2, ensure_ascii=False)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
                print(f"[CTF] 💻 API secret endpoint accessed! Flag discovered!")
                
            except Exception as e:
                self.send_error(500, f"Server error: {e}")
        else:
            self.send_error(404, "API endpoint not found")

def create_api_structure():
    """Create API directory and secret.json if they don't exist"""
    api_dir = Path('./api')
    api_dir.mkdir(exist_ok=True)
    
    secret_file = api_dir / 'secret.json'
    if not secret_file.exists():
        try:
            # Create a simple version for file access
            with open(secret_file, 'w', encoding='utf-8') as f:
                f.write('{"status": "success", "flag": "MCP{4p1_3ndp01nt_d1sc0v3r3d}"}')
            print(f"💻 Created {secret_file}")
        except Exception as e:
            print(f"💻 Warning: Could not create API file: {e}")
            print(f"💻 API will still work via dynamic response")

def main():
    # Find source directory
    current_dir = Path.cwd()
    src_dir = None
    
    # Check possible locations for src directory
    possible_paths = [
        current_dir / "src",
        current_dir / "Challenge-001" / "src",
        current_dir.parent / "src"
    ]
    
    for path in possible_paths:
        if path.exists() and (path / "index.html").exists():
            src_dir = path
            break
    
    if not src_dir:
        print("💻 Error: Could not find src directory with index.html")
        print("💻 Make sure you're in the Challenge-001 directory")
        print("💻 Or that the src/ folder exists with index.html")
        return
    
    # Change to source directory
    os.chdir(src_dir)
    print(f"💻 Working directory: {src_dir}")
    
    # Create API structure (gracefully handle encoding errors)
    create_api_structure()
    
    # Start server
    port = 8000
    try:
        with socketserver.TCPServer(("", port), CTFRequestHandler) as httpd:
            print("💻 My Cyber Playground - Challenge-001")
            print("=" * 50)
            print(f"💻 Server: http://localhost:{port}")
            print(f"💻 Find 12 flags in format: MCP{{...}}")
            print(f"💻 Use F12 for developer tools")
            print(f"💻 Available endpoints:")
            print(f"   • /help - Comprehensive beginner guide")
            print(f"   • /debug - Debug information")
            print(f"   • /api/secret.json - API with hints and flag")
            print("=" * 50)
            print("💻 Server running! Press Ctrl+C to stop")
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"💻 Port {port} is already in use!")
            print(f"💻 Try: python -m http.server 8080")
        else:
            print(f"💻 Error: {e}")
    except KeyboardInterrupt:
        print("\n💻 Server stopped. Happy hacking!")

if __name__ == "__main__":
    main()