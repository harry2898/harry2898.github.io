import time
highest_fps = 0
lowest_fps = 0
fps_additive_total = 0

def performance_test(loop_start_time, frame_time, frames_rendered):
    current_time = time.time()
    
    frame_number = frames_rendered
    ttrf = frame_time
    ttrf_to_fps = 1 / frame_time
    ttr = current_time - loop_start_time
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