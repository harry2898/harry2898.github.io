#from debugython.debugger_tool import *
#from debugython.utils import *


#openLog = False
#debug_app(calibrateScreen = False, clearScreen = False, tracerOn = False, printDebugLog = True, autoOpenDebugLog = openLog, pathOfTextEditor = r"C:\Program Files (x86)\Notepad++\notepad++.exe")


from debugython.log_formatting import *
newFormat = custom_log_format.create("test_custom_format", "default")
print(newFormat.get_all_settings())
newFormat.print_all_settings()
print("")
print(newFormat.check_if_package_exists())
newFormat.get_package()
newFormat.print_package()
print("")
print(newFormat.name)
newFormat.save()
newFormat.get_package()
newFormat.print_package()
print("")
print(newFormat.name)
print("")
newFormat.save_as("save_as_test_custom_format")
print(newFormat.name)
newFormat.get_package()
newFormat.print_package()