
from config import *

class debugger_tool:
    def __init__(self):
        self.doPrintErrors = PRINT_ERRORS
        self.doLogErrors = LOG_ERRORS
        
        self.moduleName = None
        self.className = None
        self.functionName = None
        self.givenToFunction = None #list
        
        self.errorPath = None #list
        self.errorType = None
        self.errorValue = None
        
        self._errorInfoCleared = True
        
    def is_debugger(self):
        return True
        
    def start_new_error(self):
        self.clear_error_info()
        self.clear_error_formatting()
        
    def clear_error_info(self):
        self.moduleName = None
        self.className = None
        self.functionName = None
        self.givenFuncArgsList = None #list
        
        self.errorPath = None #list
        self.errorType = None
        self.errorValue = None
        
        self._errorInfoCleared = True
        
    def clear_error_formatting(self):
        pass
    
    def set_function_info(self, moduleName, functionName, givenArgsAsList, className = None):
        if self.moduleName is None:
            self.moduleName = moduleName
            if className is not None:
                self.className = className
            self.functionName = functionName
            self.givenFuncArgsList = givenArgsAsList
    
    def set_error_info(self, errorType, valueThatCausedError, errorCheckerFunctionNameToAddToPath = None, errorCheckerCompletePath = None):
        if self.errorType is None:
            if errorCheckerFunctionNameToAddToPath is not None:
                self.add_to_error_path(errorCheckerFunctionNameToAddToPath)
            if errorCheckerCompletePath is not None:
                self.errorPath = list(errorCheckerCompletePath)
            self.errorType = errorType
            self.errorValue = valueThatCausedError
        else:
            if errorCheckerFunctionNameToAddToPath is not None:
                self.add_to_error_path(errorCheckerFunctionNameToAddToPath)            
    
    def add_to_error_path(self, errorCheckerFunctionName): 
        if self.errorPath is None:
            self.errorPath = [errorCheckerFunctionName]
        else:
            tempErrorPath = list(self.errorPath)
            self.errorPath.clear()
            self.errorPath.append(errorCheckerFunctionName)
            for i in tempErrorPath:
                self.errorPath.append(i)
        
    def record_error(self):
        if self.doPrintErrors is True:
            self._print_error()
        if self.doLogErrors is True:
            self._log_error()
        self.start_new_error()
    
    def format_error(self):
        pass
    
    def _print_error(self):
        pass
    
    def _log_error(self):
        pass