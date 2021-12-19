from launcher.configs.default_launcher_config import *


#A list containing the coordinate pair location/ position of each corner in window:
#window top left corner position = [x, y]
win_top_left_corner_pos = [0,0]
win_tl_corner_pos = [0,0]
win_tlc_pos = [0,0]
#window top right corner position = [x, y]
win_top_right_corner_pos = [WIN_WIDTH, 0]
win_tr_corner_pos = [WIN_WIDTH, 0]
win_trc_pos = [WIN_WIDTH, 0]
#window bottom right corner position = [x, y]
win_bottom_right_corner_pos = [WIN_WIDTH, WIN_HEIGHT]
win_br_corner_pos = [WIN_WIDTH, WIN_HEIGHT]
win_brc_pos = [WIN_WIDTH, WIN_HEIGHT]
#window bottom left corner position = [x, y]
win_bottom_left_corner_pos = [0, WIN_HEIGHT]
win_bl_corner_pos = [0, WIN_HEIGHT]
win_blc_pos = [0, WIN_HEIGHT]
#window all corner positions = [[top left x, top left y], [top right x, top right y], [bottom right x, bottom right y], [bottom left x, bottom left y]]
win_all_corner_pos = [win_top_left_corner_pos, win_top_right_corner_pos, win_bottom_right_corner_pos, win_bottom_left_corner_pos]
win_ac_pos = [win_tlc_pos, win_trc_pos, win_brc_pos, win_blc_pos]

#A list containing the coordinate pair location/ position of each edge's midpoint in window:
#window top edge midpoint position = [x, y]
win_top_midpoint_pos = [WIN_WIDTH / 2, 0]
win_t_mid_pos = [WIN_WIDTH / 2, 0]
win_tmp_pos = [WIN_WIDTH / 2, 0]
#window right edge midpoint position = [x, y]
win_right_midpoint_pos = [WIN_WIDTH, WIN_HEIGHT / 2]
win_r_mid_pos = [WIN_WIDTH, WIN_HEIGHT / 2]
win_rmp_pos = [WIN_WIDTH, WIN_HEIGHT / 2]
#window bottom edge midpoint position = [x, y]
win_bottom_midpoint_pos = [WIN_WIDTH / 2, WIN_HEIGHT]
win_b_mid_pos = [WIN_WIDTH / 2, WIN_HEIGHT]
win_bmp_pos = [WIN_WIDTH / 2, WIN_HEIGHT]
#window left edge midpoint position = [x, y]
win_left_midpoint_pos = [0, WIN_HEIGHT / 2]
win_l_mid_pos = [0, WIN_HEIGHT / 2]
win_lmp_pos = [0, WIN_HEIGHT / 2]
#window all edge midpoint positions = [[top x, top y], [right x, right y], [bottom x, bottom y], [left x, left y]]
win_all_midpoint_pos = [win_top_midpoint_pos, win_right_midpoint_pos, win_bottom_midpoint_pos, win_left_midpoint_pos]
win_all_mid_pos = [win_t_mid_pos, win_r_mid_pos, win_b_mid_pos, win_l_mid_pos]
win_amp_pos = [win_tmp_pos, win_rmp_pos, win_bmp_pos, win_lmp_pos]

#A list containing the coordinate pair location/ position of useful points in window:
#window center position = [x, y]
win_center_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 2]
win_c_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 2]
win_center_midpoint_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 2]
win_c_mid_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 2]
win_cmp_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 2]
#window top center quarter point position = [x, y]
win_top_center_quarter_point_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 4]
win_tcqp_pos = [WIN_WIDTH / 2, WIN_HEIGHT / 4]
#window right center quarter point position = [x, y]
win_right_center_quarter_point_pos = [WIN_WIDTH * .75, WIN_HEIGHT / 2]
win_rcqp_pos = [WIN_WIDTH * .75, WIN_HEIGHT / 2]
#window bottom center quarter point position = [x, y]
win_bottom_center_quarter_point_pos = [WIN_WIDTH / 2, WIN_HEIGHT * .75]
win_bcqp_pos = [WIN_WIDTH / 2, WIN_HEIGHT * .75]
#window left center quarter point position = [x, y]
win_left_center_quarter_point_pos = [WIN_WIDTH / 4, WIN_HEIGHT / 2]
win_lcqp_pos = [WIN_WIDTH / 4, WIN_HEIGHT / 2]

#center third points
#corner third points
#edges third points
#corner quarter points
#edges quarter points
#center fifth points
#corner fifth points
#edges fifth points
#partician screen into 4 tiles {midpoints, half points, 1/2}
#partician screen into 9 tiles {third points, 1/3}
#partician screen into 16 tiles {half midpoints, quarter points, 1/4}
#partician screen into 25 tiles {fifth points, 1/5}


#A list containing the coordinate pair location/ position of each partition line that subdivides the edge(s)
#window partition edge(the name of the edge that will be partitioned, the number of partitions that the edge will be subdivided into)
#when given only one edge, upon completion, the function will: return {nameOfEdge}PartitionedEdge
#{nameOfEdge}PartitionedEdge = [[partitionLine{1} x, partitionLine{1} y], [partitionLine{2} x, partitionLine{2} y], ..., [partitionLine{numOfPartitions} x, partitionLine{numOfPartitions} y]]
#when given all edges, upon completetion, the function will: return partitionedEdges
#partitionedEdges = [[topPartitionedEdge list], [rightPartitionedEdge list], [bottomPartitionedEdge list], [leftPartitionedEdge list]]
def _win_partition_edge(nameOfEdge, numOfPartitions):
    particianSizeX = WIN_WIDTH / numOfPartitions
    particianSizeY = WIN_HEIGHT / numOfPartitions
    errorOccurred = False
    for i in range(numOfPartitions):
        if nameOfEdge == "top":
            if i == 0:
                topPartitionedEdge = []
            else:
                topPartitionedEdge.append([particianSizeX * i, 0])
                
        elif nameOfEdge == "right":
            if i == 0:
                rightPartitionedEdge = []
            else:
                rightPartitionedEdge.append([WIN_WIDTH, particianSizeY * i])
                
        elif nameOfEdge == "bottom":
            if i == 0:
                bottomPartitionedEdge = []
            else:
                bottomPartitionedEdge.append([particianSizeX * i, WIN_HEIGHT])
                
        elif nameOfEdge == "left":
            if i == 0:
                leftPartitionedEdge = []
            else:
                leftPartitionedEdge.append([0, particianSizeY * i])
                
        elif nameOfEdge == "all":
            if i == 0:
                topPartitionedEdge = []
                rightPartitionedEdge = []
                bottomPartitionedEdge = []
                leftPartitionedEdge = []
                partitionedEdges = []
            else:
                topPartitionedEdge.append([particianSizeX * i, 0])
                rightPartitionedEdge.append([WIN_WIDTH, particianSizeY * i])
                bottomPartitionedEdge.append([particianSizeX * i, WIN_HEIGHT])
                leftPartitionedEdge.append([0, particianSizeY * i])
        else:
            errorOccurred = True
    if errorOccurred is True:
        print("Unkown Error in _win_partition_edge(nameOfEdge, numOfPartitions)")
        print("Was given, nameOfEdge =", nameOfEdge, "which is type:", type(nameOfEdge))
        print("Was given, numOfPartitions =", numOfPartitions, "which is type:", type(numOfPartitions))
    else:
        if nameOfEdge == "top":
            return topPartitionedEdge
        elif nameOfEdge == "right":
            return rightPartitionedEdge
        elif nameOfEdge == "bottom":
            return bottomPartitionedEdge
        elif nameOfEdge == "left":
            return leftPartitionedEdge
        elif nameOfEdge == "all":
            partitionedEdges.append(topPartitionedEdge)
            partitionedEdges.append(rightPartitionedEdge)
            partitionedEdges.append(bottomPartitionedEdge)
            partitionedEdges.append(leftPartitionedEdge)            
            return partitionedEdges
        else:
            print("Unkown Error in _win_partition_edge(nameOfEdge, numOfPartitions)")
            print("Passed errorOccurred check but failed nameOfEdge if checks to return")
            print("Was given, nameOfEdge =", nameOfEdge, "which is type:", type(nameOfEdge))
            print("Was given, numOfPartitions =", numOfPartitions, "which is type:", type(numOfPartitions))            


#A list containing the coordinate pair location/ position of each partition line that subdivides the edge
#window partition top edge(the number of partitions that the top edge will be subdivided into) === return topPartitionedEdge
#topPartitionedEdge = [[top partitionLine{1} x, top partitionLine{1} y], [top partitionLine{2} x, top partitionLine{2} y], ..., [top partitionLine{numOfPartitions} x, top partitionLine{numOfPartitions} y]]
def win_partition_top_edge(numOfPartitions):
    topPartitionedEdge = _win_partition_edge("top", numOfPartitions)
    return topPartitionedEdge

#window partition right edge(the number of partitions that the right edge will be subdivided into) === return rightPartitionedEdge
#rightPartitionedEdge = [[right partitionLine{1} x, right partitionLine{1} y], [right partitionLine{2} x, right partitionLine{2} y], ..., [right partitionLine{numOfPartitions} x, right partitionLine{numOfPartitions} y]]
def win_partition_right_edge(numOfPartitions):
    rightPartitionedEdge = _win_partition_edge("right", numOfPartitions)
    return rightPartitionedEdge

#window partition bottom edge(the number of partitions that the bottom edge will be subdivided into) === return bottomPartitionedEdge
#bottomPartitionedEdge = [[bottom partitionLine{1} x, bottom partitionLine{1} y], [bottom partitionLine{2} x, bottom partitionLine{2} y], ..., [bottom partitionLine{numOfPartitions} x, bottom partitionLine{numOfPartitions} y]]
def win_partition_bottom_edge(numOfPartitions):
    bottomPartitionedEdge = _win_partition_edge("bottom", numOfPartitions)
    return bottomPartitionedEdge

#window partition left edge(the number of partitions that the left edge will be subdivided into) === return leftPartitionedEdge
#leftPartitionedEdge = [[left partitionLine{1} x, left partitionLine{1} y], [left partitionLine{2} x, left partitionLine{2} y], ..., [left partitionLine{numOfPartitions} x, left partitionLine{numOfPartitions} y]]
def win_partition_left_edge(numOfPartitions):
    leftPartitionedEdge = _win_partition_edge("left", numOfPartitions)
    return leftPartitionedEdge

#window partition all edges(the number of partitions that each edge will be subdivided into) === return partitionedEdges
#partitionedEdges = [[topPartitionedEdge list], [rightPartitionedEdge list], [bottomPartitionedEdge list], [leftPartitionedEdge list]]
def win_partition_all_edges(numOfPartitions):
    partitionedEdges = _win_partition_edge("all", numOfPartitions)
    return partitionedEdges

