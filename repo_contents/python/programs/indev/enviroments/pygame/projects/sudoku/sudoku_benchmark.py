import time

from sudoku_solver import solve_sudoku_problem

from sudoku_benchmark_config import *
from sudoku_benchmark_problems import get_sudoku_benchmark_problem
from sudoku_benchmark_problems import get_sudoku_benchmark_solved_problem

class sudoku_benchmark_results:
    def __init__(self, problemNumber, problemIterationNumber, startTime, endTime):
        self.problemNumber = problemNumber
        self.problemIterationNumber = problemIterationNumber
        self.startTime = startTime
        self.endTime = endTime
        self.timeToComplete = self.endTime - self.startTime
    
    def get_problem_number(self):
        return self.problemNumber
    
    def get_problem_iteration_number(self):
        return self.problemIterationNumber
    
    def get_start_time(self):
        return self.startTime
    
    def get_end_time(self):
        return self.endTime
    
    def get_time_to_complete(self):
        return self.timeToComplete
    
    

def benchmark_loop():
    problemNumber = 1
    benchmarkFailed = False
    allBenchmarkResults = []
    benchmarkProblemResultsForEachIteration = []
    while get_sudoku_benchmark_problem(problemNumber) is not False and benchmarkFailed is False:
        for i in range(numberOfTimesToBenchmarkEachSudokuBenchmarkProblems):
            benchmarkProblem = get_sudoku_benchmark_problem(problemNumber)
            benchmarkSolvedProblem = get_sudoku_benchmark_solved_problem(problemNumber)
            
            startTime = time.time()
            #Run benchmark:
            #-----
            returnedBenchmarkSolvedProblem = solve_sudoku_problem(benchmarkProblem)
            #-----
            endTime = time.time()
            
            #Check if returnedBenchmarkSolvedProblem is correct:
            #-----
            if len(benchmarkSolvedProblem) == len(returnedBenchmarkSolvedProblem):
                for i in range(len(benchmarkSolvedProblem)):
                    for j in range(len(benchmarkSolvedProblem[i])):
                        if benchmarkSolvedProblem[i][j] != returnedBenchmarkSolvedProblem[i][j]:
                            benchmarkFailed = True
            else:
                benchmarkFailed = True
            #-----
            
            #Record benchmark problem iteration results:
            #-----
            problemIterationNumber = i + 1
            benchmarkProblemResultsForEachIteration.append(sudoku_benchmark_results(problemNumber, problemIterationNumber, startTime, endTime))
            #-----
        allBenchmarkResults.append(list(benchmarkProblemResultsForEachIteration))
        benchmarkProblemResultsForEachIteration.clear()
        problemNumber += 1
    #Report benchmark results