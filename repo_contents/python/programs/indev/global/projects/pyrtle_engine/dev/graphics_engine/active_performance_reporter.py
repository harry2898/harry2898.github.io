import time
highest_fps = 0
lowest_fps = 0
fps_additive_total = 0

class active_performance_reporter:
    def __init__(self, reportInterval, resolutionAsList, detailedReport = True, includeAcronymInfo = True):
        self.reportInterval = reportInterval
        self.totalFramesRendered = 0
        self.programResolution = resolutionAsList
        self.totalPixelsPerFrame = self.programResolution[0] * self.programResolution[1]
        self.isDetailedReport = detailedReport
        
        self._create_report_structure()
        self._print_report_header(includeAcronymInfo)
        
        self.timeStartOfProgram = time.time()
        self.timeStartOfFrame = self.timeStartOfProgram
    
    def _create_report_structure(self):
        self._set_column_names()
        self._set_report_formatting()
    
    def _set_column_names(self):
        allColumnNames = ["Frame #", "TTR", "TtRF", "FPS", "PPS", "Average FPS", "Average PPS"]
        if self.isDetailedReport is True:
            columnsUsed = []
            for i in range(len(allColumnNames)):
                columnsUsed.append(i)
        else:
            columnsUsed = [0, 1, 3, 5]
        self.columnNames = []
        for i in columnsUsed:
            self.columnNames.append(allColumnNames[i])
    
    def _set_report_formatting(self):
        #[dec places to round to, max num of int digits]
        constantColumnData = [[0, 4, 5], [3, 3, 7], [3, 1, 5], [2, 2, 5], [0, 4, 5], [2, 2, 5], [0, 4, 5]]
        self.columnSeperator = "|"
        self.columnFormatting = []
        for i in enumerate(self.columnNames):
            if len(i[1]) + 2 < 10:
                #[dec places to round to, max num of int digits, max length of number (including leading 0, ',', & '.'), column width]
                self.columnFormatting.append([constantColumnData[i[0]][0], constantColumnData[i[0]][1], constantColumnData[i[0]][2], 10])
            else:
                self.columnFormatting.append([constantColumnData[i[0]][0], constantColumnData[i[0]][1], constantColumnData[i[0]][2], len(i[1]) + 2])    
    
    def _print_report_header(self, includeAcronymInfo):
        if includeAcronymInfo is True:
            self._print_acronym_info()
        print(self._format_column_names())

    def _print_acronym_info(self):
        print("| Acronym |        Definition         |                     Explanations                     |                  FORMULA                   |")
        print("|   TTR   |    Total Time Running     | The total amount of time the engine has been running | TTR     = Current Time - Start Time        |")
        if self.isDetailedReport is True:
            print("|  TtRF   |   Time to Render Frame    | The amount of time required to render THAT frame     | TtRF    = End Time - Start Time            |")
        print("|   FPS   |     Frames Per Second     | FPS of THAT frame based on its TtRF                  | FPS     = 1 / TtRF                         |")
        if self.isDetailedReport is True:
            print("|   PPS   |     Pixels Per Second     | PPS of THAT frame based on its FPS and resolution    | PPS     = FPS * Pixels per Frame           |")
        print("| Avg FPS | Average Frames Per Second | The average number of FPS over the TTR               | Avg FPS = Frame # / TTR                    |")
        if self.isDetailedReport is True:
            print("| Avg PPS | Average Pixels Per Second | The average number of PPS over the TTR               | Avg FPS = Pixels per Frame * Frame # / TTR |")

    def _format_column_names(self):
        line = self.columnSeperator
        for i in enumerate(self.columnNames):
            line = "".join(line + i[1].center(self.columnFormatting[i[0]][3]) + self.columnSeperator)
        return line
    
    def report_performance(self):
        self._update_total_frames_rendered()
        if self._do_report_now() is True:
            self._set_report_values()
            self._print_report_values()
        self.timeStartOfFrame = time.time()
     
    def force_report_performance(self, updateTotalFramesRendered = False, updateTimeStartOfFrame = False):
        if updateTotalFramesRendered is True:
            self._update_total_frames_rendered()
        self._set_report_values()
        self._print_report_values()
        if updateTimeStartOfFrame is True:
            self.timeStartOfFrame = time.time()
     
    def _update_total_frames_rendered(self):
        self.totalFramesRendered += 1
    
    def _do_report_now(self):
        if (self.reportInterval == 0) or (self.totalFramesRendered == 1):
            return True
        elif self.totalFramesRendered % self.reportInterval == 0:
            return True
        else:
            return False            
    
    def _set_report_values(self):
        self.timeEndOfFrame = time.time()
        self.timeLengthOfFrame = self.timeEndOfFrame - self.timeStartOfFrame
        self.fps = 1 / self.timeLengthOfFrame
        self.timeLengthOfProgram = self.timeEndOfFrame - self.timeStartOfProgram
        self.averageFPS = self.totalFramesRendered / self.timeLengthOfProgram
        if self.isDetailedReport is True:
            self.pps = self.fps * self.totalPixelsPerFrame
            self.totalPixelsRendered = self.totalPixelsPerFrame * self.totalFramesRendered
            self.averagePPS = self.totalPixelsRendered / self.timeLengthOfProgram
        if self.totalFramesRendered == 1:
            self.reportValues = []
        self._update_report_values_list()
    
    def _update_report_values_list(self):
        self.reportValues.clear()
        self.reportValues.append(self.totalFramesRendered)
        self.reportValues.append(self.timeLengthOfProgram)
        if self.isDetailedReport is True:
            self.reportValues.append(self.timeLengthOfFrame)
        self.reportValues.append(self.fps)
        if self.isDetailedReport is True:
            self.reportValues.append(self.pps)
        self.reportValues.append(self.averageFPS)
        if self.isDetailedReport is True:
            self.reportValues.append(self.averagePPS)
    
    def _print_report_values(self):
        print(self._format_report_values())
        
    def _format_report_values(self):
        line = self.columnSeperator
        for i in enumerate(self.reportValues):
            if self.columnFormatting[i[0]][0] == 0:
                line = "".join(line + f"{int(i[1]):>{self.columnFormatting[i[0]][2]},}".center(self.columnFormatting[i[0]][3]) + self.columnSeperator)
            else:
                line = "".join(line + (f"{int(i[1]):,}" + "." + f"{i[1] - int(i[1]):{self.columnFormatting[i[0]][0] / 10}f}".split(".", 1)[1]).rjust(self.columnFormatting[i[0]][2]).center(self.columnFormatting[i[0]][3]) + self.columnSeperator)
        return line



"|"
x = "5"
x = x + "6"


'''
def OLD_report_performance(graphicsEngineStartTime, frame_time, frames_rendered):
    current_time = time.time()
    
    frame_number = frames_rendered
    ttrf = frame_time
    ttrf_to_fps = 1 / frame_time
    ttr = current_time - graphicsEngineStartTime
    avg_fps = frames_rendered / ttr
    
    if(frame_number == 1): 
        print("Acronym:       Definition                                     ---  Explanations                                          ---  FORMULA")
        print("TtRF:          Time to Render Frame                           ---  The amount of time required to render THAT frame.     ---  FORMULA: TtRF    = End Time - Start Time")
        print("TtRF to FPS:   Time to Render Frame   to   Frames Per Second  ---  The equivalent FPS of THAT frame based on its TtRF.   ---  FORMULA: FPS     = 1 / TtRF")
        print("TTR:           Total Time Running                             ---  The total amount of time the engine has been running  ---  FORMULA: TTR     = Current Time - Start Time")
        print("Avg FPS:       Average Frames Per Second                      ---  The average number of FPS over the TTR                ---  FORMULA: Avg FPS = Frame Number / TTR")
        print("|   Frame #   |    TtRF    |   TtRF to FPS   |    TTR     |   Avg FPS   |")
    if(frame_number < 10):  
        if(ttr < 10):
            print("|     ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    |  ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(10 <= ttr < 100):
            print("|     ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    |  ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(ttr >= 100):
            print("|     ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
    if(9 < frame_number < 100):
        if(ttr < 10):
            print("|    ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    |  ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(10 <= ttr < 100):
            print("|    ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(ttr >= 100):
            print("|    ", frame_number, "     |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")        
    if(99 < frame_number < 1000):
        if(ttr < 10):
            print("|    ", frame_number, "    |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    |  ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(10 <= ttr < 100):
            print("|    ", frame_number, "    |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(ttr >= 100):
            print("|    ", frame_number, "    |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), " |  ", "%.4f" % round(avg_fps,4), "  |")        
    if(frame_number > 999):
        if(ttr < 10):
            print("|    ", frame_number, "   |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    |  ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(10 <= ttr < 100):
            print("|    ", frame_number, "   |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), "  |  ", "%.4f" % round(avg_fps,4), "  |")
        if(ttr >= 100):
            print("|    ", frame_number, "   |  ", "%.4f" % round(ttrf,4), "  |     ", "%.4f" % round(ttrf_to_fps,4), "    | ", "%.4f" % round(ttr,4), " |  ", "%.4f" % round(avg_fps,4), "  |")        
    return
'''