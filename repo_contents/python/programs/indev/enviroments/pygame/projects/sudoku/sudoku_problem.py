

from config import *
from error_checker_utils import *
from errors import *


class problem:
    def __init__(self):
        self.problem = self._import_problem()
        self._set_debugger_settings()
        
#-------------------------------------------------
#DEBUGGER
    def _set_debugger_settings(self):
        if DEBUG_MODE is True:
            self._useDebugger = True
            self.debugger = debugger_tool()
            self._moduleName = "sudoku_problem.py"
            self._className = "problem"
        else:
            self.debugger = None
            self._useDebugger = False        
    
    def get_debugger(self):
        if self._useDebugger is True:
            return self.debugger
        else:
            return False
    
    def _function_info(self, givenInList, functionName):
        self.debugger.set_function_info(self, givenInList, self._moduleName, functionName, className = self._className)    
#-------------------------------------------------

    def _import_problem(self):
        '''
        TODO
        Import problem from excel
        '''
        return
    
    def get_problem(self):
        return self.problem
    
    def get_row(self, rowNum):
        return self.problem[rowNum]
    
    def get_col(self, colNum):
        pass
    
    def get_block(self, blockNum):
        pass
    
    def get_cell(self, rowNum, colNum):
        return self.problem[rowNum][colNum]
    
    
class solution:
    def __init(self, problem):
        self.givenProblem = problem
        self._create_solution_grid()
        self._set_debugger_settings()

#-------------------------------------------------
#DEBUGGER
    def _set_debugger_settings(self):
        if self.givenProblem.get_debugger() is not False:
            self._useDebugger = True
            self.debugger = self.givenProblem.get_debugger()
            self._moduleName = "sudoku_problem.py"
            self._className = "solution(problem)"
        else:
            self.debugger = None
            self._useDebugger = False
    
    def get_debugger(self):
        if self._useDebugger is True:
            return self.debugger
        else:
            return False
        
    def _function_info(self, givenArgsAsList, functionName):
        self.debugger.set_function_info(self._moduleName, functionName, givenArgsAsList, className = self._className)
        self.debugger.record_error()
#-------------------------------------------------

    def _create_solution_grid(self):
        '''
        Copies problem so it can be modified and turned into the solution
        '''
        self.solution = list(self.givenProblem.get_problem())
    
    def get_solution(self):
        return self.solution
    
    def get_row(self, rowNum):
        return self.solution[rowNum]
    
    def get_col(self, colNum):
        pass
    
    def get_block(self, blockNum):
        pass
    
    def get_cell(self, rowNum, colNum):
        return self.solution[rowNum][colNum]
    
    def get_empty_cells_in_solution(self):
        pass
    
    def get_empty_cells_in_row(self, rowNum):
        pass
    
    def get_empty_cells_in_col(self, colNum):
        pass
    
    def get_empty_cells_in_block(self, blockNum):
        pass
    
    def get_valid_nums_for_cell(self, rowNum, colNum):
        pass
    
    def get_invalid_nums_for_cell(self, rowNum, colNum):
        pass
    
    def set_cell(self, num, rowNum, colNum):
        if are_valid_nums([num, rowNum, colNum], debugMode = self._useDebugger, debuggerTool = self.debugger) is True:
            self.solution[rowNum][colNum] = num
        elif self._useDebugger is True:
            self._function_info(self, [num, rowNum, colNum], "set_cell(num, rowNum, colNum)")