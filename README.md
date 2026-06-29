#  NXT
##  Real-Time Endpoint Security Monitor

NXT is  a linux based endpoint security monitoring system developed for the BUILD FOR GOOD HACKATHON. It continuously monitors file system activities and detects suspecious events in real time.
This system provides a live dashboard for monitoring threats and stores security events in a log file for future analysis.

##  Features
- Real-time file system monitoring
- File creation detection
- File deletion detection
- File rename detection
- Suspicious file detection
- Large data copy detection
- Possible ransomware detection
- Live dashboard
- Threat logging

##  Technology Stack
### Backend
- Python
- Flask
- Watchdog
### Frontend
- HTML
- CSS
- JavaScript
### Platform
- Linux (Kali/Ubuntu)

## How It Works
1. NXT starts the watchdog observerto monitor the selected directory.
2. Whenever a file is created, modified,renamed or deleted, Watchdog generates an event.
3. The event is analyzed by NXT to determine its type and severity.
4. Detected threats are displayed on the live dashboard.
5. Every detected event is also saved in logs/threat.log for future analysis.

## Future Scope
The current version of NXT focuses on real-time file system monitoring. In future project can be extended with:
- AI based threat detection
- Process monitoring
- Network Traffic monitoring
- Email and Desktop notifications
- Cloud based monitoring Dashboard
- Cross-platform support(windows & macOS

# Developer
**Vinay Pratap Singh**
B.tech Computer Science and Engineering

Build for Good Hackathon 2026
