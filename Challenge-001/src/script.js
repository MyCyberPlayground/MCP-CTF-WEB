// File: Challenge-01/src/script.js
// This is CLIENT-SIDE JavaScript that runs in the browser

function showAlert() {
    alert("Welcome to SecureBank! Your security is our priority.");
}

// Fake login function
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (username === 'admin' && password === 'password123') {
        document.cookie = "auth=MCP{c00k13_fl4g_f0und_y0u}; path=/"; // Flag 4
        alert("Login successful! Check your cookies.");
        window.location.href = 'dashboard.html';
    } else {
        alert("Invalid credentials! Hint: Try admin/password123");
    }
}

// Hidden function that might be called from console
function getSecret() {
    return "Secret function called! Check the network tab for API calls.";
}

// Fixed API call function
function makeApiCall() {
    console.log("💻 Making API call to secret endpoint...");
    
    fetch('/api/secret.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('💻 API Response received!');
            console.log('Flag found:', data.ctf_info.discovered_flag);
            console.log('Message:', data.message);
            console.log('Full response:', data);
            alert(`API Secret Found!\n\nFlag: ${data.ctf_info.discovered_flag}\n\nCheck console for full response!`);
        })
        .catch(error => {
            console.error('💻 API Error:', error);
            console.log('💻 Hint: Make sure the server is running and /api/secret.json exists');
        });
}

// Easier API test function for beginners
function testApi() {
    console.log("💻 Testing API endpoint...");
    makeApiCall();
}

// Easter egg for curious users
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.shiftKey && e.key === 'I') {
        console.log("Developer tools detected! Good job, hacker!");
        console.log("Try exploring more...");
    }
});

// Obfuscated flag (Base64 encoded)
const hiddenData = "TUNQe2phdmFzY3JpcHRfZGVjMGQzZF9mbDRnfQ=="; // Flag 5

function decodeSecret() {
    return atob(hiddenData);
}

// Additional debugging functions
function debugInfo() {
    console.log("Debug functions available:");
    console.log("- getSecret()");
    console.log("- decodeSecret()");
    console.log("- makeApiCall()");
    console.log("- testApi()");
    console.log("- help()");
}

// Help function for beginners
function help() {
    console.log("💻 My Cyber Playground - Challenge 001 Help");
    console.log("=" * 40);
    console.log("💻 Goal: Find 5 flags in format MCP{...}");
    console.log("");
    console.log("💻 Available Console Functions:");
    console.log("  • help() - Show this help");
    console.log("  • debugInfo() - List debug functions");
    console.log("  • getSecret() - Get a secret message");
    console.log("  • decodeSecret() - Decode hidden data");
    console.log("  • testApi() - Test the API endpoint");
    console.log("  • makeApiCall() - Make API request");
    console.log("");
    console.log("💻 Things to Try:");
    console.log("  • View page source (Ctrl+U)");
    console.log("  • Check Application tab for cookies/storage");
    console.log("  • Look at CSS files");
    console.log("  • Try logging in with admin/password123");
    console.log("  • Access /api/secret.json directly");
    console.log("  • Visit /help for detailed beginner guide");
    console.log("");
    console.log("Good luck!");
}

// Initialize on page load
window.addEventListener('load', function() {
    console.log("SecureBank application loaded");
    console.log("Try typing help() in console for available functions");
});

// More hidden content for discovery
var developmentMode = true;
if (developmentMode) {
    console.log("Development mode is enabled");
    console.log("Check localStorage for debug information");
    localStorage.setItem('debug_mode', 'enabled');
    localStorage.setItem('developer_notes', 'Remember to remove debug code before production!');
}

// Secret data that might be discovered
window.secretConfig = {
    apiEndpoint: '/api/secret.json',
    debugMode: true,
    version: '1.0.0-beta',
    lastUpdated: '2024-01-15'
};

// Function that could be called from browser console
function showHiddenFeatures() {
    console.log("Hidden features:");
    console.log("1. Admin panel available at /admin/");
    console.log("2. API endpoint at /api/secret.json");
    console.log("3. Debug mode can be toggled");
    console.log("4. Check cookies after successful login");
    console.log("5. Try decoding the hiddenData variable");
    console.log("6. Use help() for beginner guidance");
}

// Simulate some background processes
setInterval(function() {
    if (Math.random() < 0.1) { // 10% chance every interval
        console.log("Background process: Checking for updates...");
    }
}, 30000); // Every 30 seconds

// Add some interactive elements
document.addEventListener('DOMContentLoaded', function() {
    // Add click counter (just for interaction)
    let clickCount = 0;
    document.addEventListener('click', function() {
        clickCount++;
        if (clickCount === 10) {
            console.log("💻 You've clicked 10 times! You're really exploring this site.");
            console.log("💻 Tip: Have you tried the browser's developer tools yet?");
            console.log("💻 Try typing help() in the console!");
        } else if (clickCount === 25) {
            console.log("💻 25 clicks! You're definitely looking for something...");
            console.log("💻 Try examining the page source and JavaScript functions.");
            console.log("💻 Don't forget to test the API: testApi()");
        }
    });
    
    // Add some hover effects via JavaScript
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Fake admin check function
function checkAdminStatus() {
    const authCookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('auth='));
    
    if (authCookie) {
        console.log("Admin session detected!");
        console.log("Cookie found:", authCookie);
        return true;
    } else {
        console.log("No admin session found. Try logging in first.");
        return false;
    }
}

// Function to simulate data fetching
function fetchUserData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (checkAdminStatus()) {
                resolve({
                    username: 'admin',
                    role: 'administrator',
                    lastLogin: new Date().toISOString(),
                    permissions: ['read', 'write', 'delete']
                });
            } else {
                reject(new Error('Unauthorized access'));
            }
        }, 1000);
    });
}

// Console Easter egg for persistent users
let consoleAccessCount = 0;
const originalConsoleLog = console.log;
console.log = function(...args) {
    consoleAccessCount++;
    if (consoleAccessCount === 5) {
        originalConsoleLog("💻 You're really using the console! That's the spirit of a hacker!");
        originalConsoleLog("💻 Try calling some of these functions:");
        originalConsoleLog("   - help()");
        originalConsoleLog("   - debugInfo()");
        originalConsoleLog("   - getSecret()");
        originalConsoleLog("   - decodeSecret()");
        originalConsoleLog("   - testApi()");
    }
    originalConsoleLog.apply(console, args);
};