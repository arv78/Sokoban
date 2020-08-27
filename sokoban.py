import numpy as np
import queue
import timeit
import sys
import math
import random


def copy_matrix(init_state):
    temp = []
    for i in range(len(init_state)):
            temp.append([])
            for j in range(len(init_state[i])):
                temp[i].append(init_state[i][j])
    return temp

def display(temp):
    print("display:")
    for row in range(len(temp)):
        for column in range(len(temp[row])):
            print(temp[row][column], end = " ")
        print()

#successor
def Successor(init_state,x_s,y_s,count_move,count_push):
    result = []
    #move right
    if init_state[x_s][y_s + 1] == "." or init_state[x_s][y_s + 1] == "X":
        count_move += 1
        temp = copy_matrix(init_state)
        temp[x_s][y_s + 1] = "S"
        temp[x_s][y_s] = "."
        result.append(temp)
    
    #move left
    if init_state[x_s][y_s - 1] == "." or init_state[x_s][y_s - 1] == "X":
        count_move += 1
        temp = copy_matrix(init_state)
        temp[x_s][y_s - 1] = "S"
        temp[x_s][y_s] = "."
        result.append(temp)

    #move up
    if init_state[x_s - 1][y_s] == "." or init_state[x_s - 1][y_s] == "X":
        count_move += 1
        temp = copy_matrix(init_state)
        temp[x_s - 1][y_s] = "S"
        temp[x_s][y_s] = "."
        result.append(temp)

    #move down
    if init_state[x_s + 1][y_s] == "." or init_state[x_s + 1][y_s] == "X":
        count_move += 1
        temp = copy_matrix(init_state)
        temp[x_s + 1][y_s] = "S"
        temp[x_s][y_s] = "."
        result.append(temp)

    #move_box right
    if init_state[x_s][y_s + 1] == "@":
        if init_state[x_s][y_s + 2] == "." or init_state[x_s][y_s + 2] == "X":
            count_push += 1
            count_move += 1
            temp = copy_matrix(init_state)
            temp[x_s][y_s + 2] = "@"
            temp[x_s][y_s + 1] = "S"
            temp[x_s][y_s] = "."
            result.append(temp)
    
    #move_box left
    if init_state[x_s][y_s - 1] == "@":
        if init_state[x_s][y_s - 2] == "." or init_state[x_s][y_s - 2] == "X":
            count_push += 1
            count_move += 1
            temp = copy_matrix(init_state)
            temp[x_s][y_s - 2] = "@"
            temp[x_s][y_s - 1] = "S"
            temp[x_s][y_s] = "."
            result.append(temp)

    #move_box up
    if init_state[x_s - 1][y_s] == "@":
        if init_state[x_s - 2][y_s] == "." or init_state[x_s - 2][y_s] == "X":
            count_push += 1
            count_move += 1
            temp = copy_matrix(init_state)
            temp[x_s - 2][y_s] = "@"
            temp[x_s - 1][y_s] = "S"
            temp[x_s][y_s] = "."
            result.append(temp)

    #move_box down
    if init_state[x_s + 1][y_s] == "@":
        if init_state[x_s + 2][y_s] == "." or init_state[x_s + 2][y_s] == "X":
            count_push += 1
            count_move += 1
            temp = copy_matrix(init_state)
            temp[x_s + 2][y_s] = "@"
            temp[x_s + 1][y_s] = "S"
            temp[x_s][y_s] = "."
            result.append(temp)

    return result,count_move,count_push
        
#successor with random
def Successor_random(init_state,x_s,y_s,count_move,count_push):
    rand_if = [1,2,3,4,5,6,7,8]
    random.shuffle(rand_if)
    # print(rand_if)
    temp = 0 

    result = []
    for i in range(len(rand_if)):
        if  1 == rand_if[i]:
            #move down
            if init_state[x_s + 1][y_s] == "." or init_state[x_s + 1][y_s] == "X":
                count_move += 1
                temp = copy_matrix(init_state)
                temp[x_s + 1][y_s] = "S"
                temp[x_s][y_s] = "."
                result.append(temp)

        if 2 == rand_if[i]:
            #move_box down
            if init_state[x_s + 1][y_s] == "@":
                if init_state[x_s + 2][y_s] == "." or init_state[x_s + 2][y_s] == "X":
                    count_push += 1
                    count_move += 1
                    temp = copy_matrix(init_state)
                    temp[x_s + 2][y_s] = "@"
                    temp[x_s + 1][y_s] = "S"
                    temp[x_s][y_s] = "."
                    result.append(temp)

        if 3 == rand_if[i]:
            #move up
            if init_state[x_s - 1][y_s] == "." or init_state[x_s - 1][y_s] == "X":
                count_move += 1
                temp = copy_matrix(init_state)
                temp[x_s - 1][y_s] = "S"
                temp[x_s][y_s] = "."
                result.append(temp)

        if 4 == rand_if[i]:
            #move_box up
            if init_state[x_s - 1][y_s] == "@":
                if init_state[x_s - 2][y_s] == "." or init_state[x_s - 2][y_s] == "X":
                    count_push += 1
                    count_move += 1
                    temp = copy_matrix(init_state)
                    temp[x_s - 2][y_s] = "@"
                    temp[x_s - 1][y_s] = "S"
                    temp[x_s][y_s] = "."
                    result.append(temp)

        if 5 == rand_if[i]:
            #move right
            if init_state[x_s][y_s + 1] == "." or init_state[x_s][y_s + 1] == "X":
                count_move += 1
                temp = copy_matrix(init_state)
                temp[x_s][y_s + 1] = "S"
                temp[x_s][y_s] = "."
                result.append(temp)

        if 6 == rand_if[i]:
            #move_box right
            if init_state[x_s][y_s + 1] == "@":
                if init_state[x_s][y_s + 2] == "." or init_state[x_s][y_s + 2] == "X":
                    count_push += 1
                    count_move += 1
                    temp = copy_matrix(init_state)
                    temp[x_s][y_s + 2] = "@"
                    temp[x_s][y_s + 1] = "S"
                    temp[x_s][y_s] = "."
                    result.append(temp)

        if 7 == rand_if[i]:
            #move left
            if init_state[x_s][y_s - 1] == "." or init_state[x_s][y_s - 1] == "X":
                count_move += 1
                temp = copy_matrix(init_state)
                temp[x_s][y_s - 1] = "S"
                temp[x_s][y_s] = "."
                result.append(temp)

        if 8 == rand_if[i]:
            #move_box left
            if init_state[x_s][y_s - 1] == "@":
                if init_state[x_s][y_s - 2] == "." or init_state[x_s][y_s - 2] == "X":
                    count_push += 1
                    count_move += 1
                    temp = copy_matrix(init_state)
                    temp[x_s][y_s - 2] = "@"
                    temp[x_s][y_s - 1] = "S"
                    temp[x_s][y_s] = "."
                    result.append(temp)
    return result,count_move,count_push

#is_goal function
def is_goal(goal_pos,box_pos):
    check_count = 0
    for i in range(len(goal_pos)):
        for j in range(len(box_pos)):
            if (goal_pos[i] == box_pos[j]):
                check_count += 1
    if check_count == len(goal_pos):
        return True
    return False
            
#finding the agent and box position
def find_pos(state):
    box_x_positions = []
    box_y_positions = []
    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == "S":
                position_x_S,position_y_S = row,column
            if state[row][column] == "@":
                box_x_positions.append(row)
                box_y_positions.append(column)
    return position_x_S,position_y_S,box_x_positions,box_y_positions

#BFS implementation
def BFS(init_state,goal_pos):
    max_size = 1
    count_move = 0
    count_push = 0
    count_successor = 1
    # finding the position of box and agent for the first iteration
    box_x_positions = []
    box_y_positions = []
    for row in range(len(init_state)):
        for column in range(len(init_state[row])):
            if init_state[row][column] == "S":
                position_x_S,position_y_S = row,column
            if init_state[row][column] == "@":
                box_x_positions.append(row)
                box_y_positions.append(column)
    #merge the x and y positons
    box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
    #is_goal
    if (is_goal(goal_pos,box_pos) == True):
        return init_state
    #limited visited list(LVL)
    lvl = queue.Queue()
    lvl.put(init_state)
    #initilaizing queue
    Q = queue.Queue()
    result,count_move,count_push = Successor(init_state,position_x_S,position_y_S,count_move,count_push)
    for i in range(len(result)):
        lvl.put(result[i])
        Q.put(result[i])
        
    while (not(Q.empty())):
        if Q.qsize() > max_size:
            max_size = Q.qsize()
        current_state = Q.get()
        position_x_S,position_y_S,box_x_positions,box_y_positions = find_pos(current_state)
        #merge the x and y positons
        box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
        #is_goal
        if (is_goal(goal_pos,box_pos) == True):
            print("result: \n")
            display(current_state)
            print("\n")
            print("Successor: ",count_successor)
            print("move: ",count_move)
            print("push: ",count_push)
            print("size: ",max_size * sys.getsizeof(init_state)," Bytes")
            print("size lvl: ",lvl.qsize())
            return current_state
        
        result,count_move,count_push = Successor(current_state,position_x_S,position_y_S,count_move,count_push)
        count_successor += 1
        for i in range(len(result)):
            #if they're not visited
            flag = 0
            for j in range(lvl.qsize()):
                if result[i] == lvl.queue[j]:
                    flag = 1
                    break
            if (flag == 0):
##                if (lvl.full() == True):
##                    lvl.get()
##                    lvl.put(result[i])
##                else:
                lvl.put(result[i])
                Q.put(result[i])
#DFS implementation
def DFS(init_state,goal_pos):
    max_size = 1
    count_push = 0
    count_move = 0
    count_successor = 1
    # finding the position of box and agent for the first iteration
    box_x_positions = []
    box_y_positions = []
    for row in range(len(init_state)):
        for column in range(len(init_state[row])):
            if init_state[row][column] == "S":
                position_x_S,position_y_S = row,column
            if init_state[row][column] == "@":
                box_x_positions.append(row)
                box_y_positions.append(column)
    #merge the x and y positons
    box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
    #is_goal
    if (is_goal(goal_pos,box_pos) == True):
        return init_state
    #limited visited list(LVL)
    # limited_size = 200
    lvl = queue.Queue()
    lvl.put(init_state)
    #initilaizing stack
    stack = queue.LifoQueue()
    result,count_move,count_push = Successor_random(init_state,position_x_S,position_y_S,count_move,count_push)
    for i in range(len(result)):
    #    if (lvl.full() == True):
    #        lvl.get()
    #        lvl.put(result[i])
    #        stack.put(result[i])
    #    else:
        lvl.put(result[i])
        stack.put(result[i])
        
    while (not(stack.empty())):
        if stack.qsize() > max_size:
            max_size = stack.qsize()
        current_state = stack.get()
        # display(current_state)
        # a = input("s")

        position_x_S,position_y_S,box_x_positions,box_y_positions = find_pos(current_state)
        #merge the x and y positons
        box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
        #is_goal
        if (is_goal(goal_pos,box_pos) == True):
            print("result: \n")
            display(current_state)
            print("\n")
            print("Successor: ",count_successor)
            print("move: ",count_move)
            print("push: ",count_push)
            print("size: ",max_size * sys.getsizeof(init_state)," Bytes")
            print("size lvl: ",lvl.qsize())
            return current_state
        
        result,count_move,count_push = Successor_random(current_state,position_x_S,position_y_S,count_move,count_push)
        count_successor += 1
        for i in range(len(result)):
             #if they're not visited
             flag = 0
             for j in range(lvl.qsize()):
                 if result[i] == lvl.queue[j]:
                     flag = 1
                     break
             if (flag == 0):
                # if (lvl.full() == True):
                #     lvl.get()
                #     lvl.put(result[i])
                #     stack.put(result[i])
                # else:
                lvl.put(result[i])
                stack.put(result[i])

#IDS implementation
def IDS(init_state,goal_pos):
    max_size = 1
    count_push = 0
    count_move = 0
    count_successor = 0
    #limited visited list(LVL)
    lvl = queue.Queue()
    lvl.put(init_state)
    
    Q = queue.Queue()
    count = 1
    LDS_num = 1
    # count2 = float(0)
    # count3 = float(0)
    #using count2 and count3 to find an average depth 
    # temp_depth = 1

    Q.put(init_state)
    box_x_positions = []
    box_y_positions = []
    for row in range(len(init_state)):
        for column in range(len(init_state[row])):
            if init_state[row][column] == "S":
                position_x_S,position_y_S = row,column
            if init_state[row][column] == "@":
                box_x_positions.append(row)
                box_y_positions.append(column)
    #merge the x and y positons
    box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
    #is_goal
    if (is_goal(goal_pos,box_pos) == True):
         return init_state
    while(True):
        while(not(Q.empty()) and LDS_num < count):
            if Q.qsize() > max_size:
                max_size = Q.qsize()
            current_state = Q.get()
            position_x_S,position_y_S,box_x_positions,box_y_positions = find_pos(current_state)
            #merge the x and y positons
            box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
            result,count_move,count_push = Successor(current_state,position_x_S,position_y_S,count_move,count_push)
            # temp_depth = len(result)
            count_successor += 1
            LDS_num += 1
            for i in range(len(result)):
                #find position
                position_x_S,position_y_S,box_x_positions,box_y_positions = find_pos(result[i])
                #merge the x and y positons
                box_pos = [[box_x_positions[i], box_y_positions[j]] for i in range(len(box_x_positions)) for j in range(len(box_y_positions)) if i==j]
                #is_goal
                if (is_goal(goal_pos,box_pos) == True):
                    print("result: \n")
                    display(result[i])
                    print("\n")
                    print("Successor: ",count_successor)
                    print("move: ",count_move)
                    print("push: ",count_push)
                    print("size: ",max_size * sys.getsizeof(init_state)," Bytes")
                    print("size lvl: ",lvl.qsize())
                    # final_depth = round((10*count2 + count3)/11)
                    # print("depth: ",final_depth)
                    return result[i]
                #if they're not visited
                flag = 0
                for j in range(lvl.qsize()):
                    if result[i] == lvl.queue[j]:
                        flag = 1
                        break
                if (flag == 0):
##                if (lvl.full() == True):
##                    lvl.get()
##                    lvl.put(result[i])
##                else:
                    lvl.put(result[i])
                    Q.put(result[i])
        count += 1
        # count2 += 1/temp_depth
        # count2 = round(count2)
        # count3 += 1/temp_depth
        # count3 = math.floor(count3)
        

def split_to_char(word): 
    return [char for char in word]  
      
def main():
    # file input
    start_phase = input("1.BFS(B) 2.DFS(D) 3.IDS(I): ")
    
    if start_phase == "B" or start_phase == "b" or start_phase == "1":
        BFS_input = open("D:\python saving files\sokoban\input_4.txt","r")
        bfs = BFS_input.readline().split()
        column_num = eval(bfs[1])
        row_num = eval(bfs[0])

        BFS_list = []
        BFS_matrix = []
        goal_x_positions = []
        goal_y_positions = []

        #reading each line from input file
        for i in range(row_num):
            BFS_list = np.append(BFS_list,BFS_input.readline().split())

        #assembling the matrix
        for row in range(row_num):
            BFS_matrix.append([]) # Add an empty new row
            split_string = split_to_char(BFS_list[row])# converting each row to splited chars
            for column in range(column_num):
                if split_string[column] == "X":
                   goal_x_positions.append(row)
                   goal_y_positions.append(column)
                BFS_matrix[row].append(split_string[column])
        #merge the x and y positons
        goal_pos = [[goal_x_positions[i], goal_y_positions[j]] for i in range(len(goal_x_positions)) for j in range(len(goal_y_positions)) if i==j]
        #printing the matrix
        for row in range(len(BFS_matrix)):
            for column in range(len(BFS_matrix[row])):
                print(BFS_matrix[row][column], end = " ")
            print() # Print a new line
        print("\n\n")
        #run time calculation
        start = timeit.default_timer()
        BFS(BFS_matrix,goal_pos)
        stop = timeit.default_timer()
        print('BFS_Time: ', stop - start)
        BFS_input.close()

    elif start_phase == "D" or start_phase == "d" or start_phase == "2":
        DFS_input = open("D:\python saving files\sokoban\input_4.txt","r")
        dfs = DFS_input.readline().split()
        column_num = eval(dfs[1])
        row_num = eval(dfs[0])
        
        DFS_list = []
        DFS_matrix = []
        goal_x_positions = []
        goal_y_positions = []

        #reading each line from input file
        for i in range(row_num):
            DFS_list = np.append(DFS_list,DFS_input.readline().split())

        #assembling the matrix
        for row in range(row_num):
            DFS_matrix.append([]) # Add an empty new row
            split_string = split_to_char(DFS_list[row])# converting each row to splited chars
            for column in range(column_num):
                if split_string[column] == "X":
                   goal_x_positions.append(row)
                   goal_y_positions.append(column)
                DFS_matrix[row].append(split_string[column])
                
        #merge the x and y positons
        goal_pos = [[goal_x_positions[i], goal_y_positions[j]] for i in range(len(goal_x_positions)) for j in range(len(goal_y_positions)) if i==j]
        #printing the matrix
        for row in range(len(DFS_matrix)):
            for column in range(len(DFS_matrix[row])):
                print(DFS_matrix[row][column], end = " ")
            print() # Print a new line
        print("\n\n")
        #run time calculation
        start = timeit.default_timer()
        DFS(DFS_matrix,goal_pos)
        stop = timeit.default_timer()
        print('DFS_Time: ', stop - start)
        DFS_input.close()
    elif start_phase == "I" or start_phase == "i" or start_phase == "3":
        IDS_input = open("F:\AI-1\projects\sokoban\input_5.txt","r")
        ids = IDS_input.readline().split()
        column_num = eval(ids[1])
        row_num = eval(ids[0])
        
        IDS_list = []
        IDS_matrix = []
        goal_x_positions = []
        goal_y_positions = []

        #reading each line from input file
        for i in range(row_num):
            IDS_list = np.append(IDS_list,IDS_input.readline().split())

        #assembling the matrix
        for row in range(row_num):
            IDS_matrix.append([]) # Add an empty new row
            split_string = split_to_char(IDS_list[row])# converting each row to splited chars
            for column in range(column_num):
                if split_string[column] == "X":
                   goal_x_positions.append(row)
                   goal_y_positions.append(column)
                IDS_matrix[row].append(split_string[column])

        #merge the x and y positons
        goal_pos = [[goal_x_positions[i], goal_y_positions[j]] for i in range(len(goal_x_positions)) for j in range(len(goal_y_positions)) if i==j]
        #printing the matrix
        for row in range(len(IDS_matrix)):
            for column in range(len(IDS_matrix[row])):
                print(IDS_matrix[row][column], end = " ")
            print() # Print a new line
        #run time calculation
        start = timeit.default_timer()
        IDS(IDS_matrix,goal_pos)
        stop = timeit.default_timer()
        print('IDS_Time: ', stop - start)
        IDS_input.close()
main()
