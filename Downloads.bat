@echo off
curl -L -o login.py https://gist.githubusercontent.com/elfarid09/79681e2ef3b8f1e16310fe9fda7f69a8/raw/8431186fdc787b91c35a00bf0cdf872292560a1f/login.py
curl -L -o loop.bat https://www.dropbox.com/scl/fi/vji7ekyslpbovokpqeay3/loop.bat?rlkey=876nfzm3qdmyqhc1jckgqjcld&dl=0
curl -L -o show.bat https://raw.githubusercontent.com/elfarid09/rdp2/refs/heads/main/show.bat
certutil -urlcache -split -f "https://github.com/rustdesk/rustdesk/releases/download/1.2.1/rustdesk-1.2.1-x86_64.exe" rustdesk.exe
pip install pyautogui --quiet
pip install psutil --quiet
curl -s -L -o time.py https://www.dropbox.com/scl/fi/ox42qglbf6fsnm9erf8cw/timelimit.py?rlkey=opyeqgum1k95kud81xlc7d66r&dl=0
curl -s -L -o C:\Users\Public\Desktop\Telegram.exe https://telegram.org/dl/desktop/win64
curl -s -L -o C:\Users\Public\Desktop\Winrar.exe https://www.rarlab.com/rar/winrar-x64-621.exe
powershell -Command "Invoke-WebRequest 'https://github.com/chieunhatnang/VM-QuickConfig/releases/download/1.6.1/VMQuickConfig.exe' -OutFile 'C:\Users\Public\Desktop\VMQuickConfig.exe'"
C:\Users\Public\Desktop\Telegram.exe /VERYSILENT /NORESTART
del C:\Users\Public\Desktop\Telegram.exe
C:\Users\Public\Desktop\Winrar.exe /S
del C:\Users\Public\Desktop\Winrar.exe
del /f "C:\Users\Public\Desktop\Epic Games Launcher.lnk" > errormsg.txt 2>&1
del /f "C:\Users\Public\Desktop\Unity Hub.lnk" > errormsg.txt 2>&1
start "" "rustdesk.exe"
python login.py
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\HideDesktopIcons\NewStartPanel" /v "{20D04FE0-3AEA-1069-A2D8-08002B30309D}" /t REG_DWORD /d 0 /f
tzutil /s "Sri Lanka Standard Time"
