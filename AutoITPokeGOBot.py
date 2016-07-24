import win32api
import win32com.client
import win32gui
import time



coordinates=[(44.799763, 20.449119),(44.804723, 20.463614), (44.809446, 20.470598), 
			(44.816795, 20.461275), (44.820695, 20.452080), (44.824135, 20.463034)]

duration = 2 #How much will bot run on a given location
rest = 400 #Give it a rest so when location gets changed, you don't get softbanned


for locs in coordinates:
	shell = win32com.client.Dispatch("WScript.Shell")
	shell.Run('cmd /K "C:\Users\Stefan\Documents\GO.Bot.v0-0-4\GO Bot.exe"')

	win32api.Sleep(100)
	#shell.AppActivate('cmd /K "C:\Users\Stefan\Documents\GO.Bot.v0-0-4\GO Bot.exe"')
	win32api.Sleep(4000)
	hwnd= win32gui.FindWindow(0,'GO Bot v0.0.4 [BETA]')


	win32gui.SetForegroundWindow(hwnd)
	shell.SendKeys("{TAB}")
	shell.SendKeys("{RIGHT}")
	shell.SendKeys("{TAB}")
	shell.SendKeys(str(locs[0]))
	shell.SendKeys("{TAB}")
	shell.SendKeys(str(locs[1]))
	win32api.Sleep(2000)
	shell.SendKeys("{TAB}{TAB}{TAB}")
	shell.SendKeys("{LEFT}")
	shell.SendKeys("{TAB}{TAB}{TAB}")


	shell.SendKeys("{ENTER}") #Start Go BOt
	time.sleep(duration) #Duration of current session

	shell.SendKeys("%{F4}") #Close GO Bot
	win32api.Sleep(4000) #Wait for cmd to switch back to and close (milliseconds)
	shell.SendKeys("exit {ENTER}") #Send Exit command

	time.sleep(rest) #Give it a rest


