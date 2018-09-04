
# coding: utf-8

# In[337]:

#Next Departure time
def nxtdep (T, Arr, Dest):
    if T == 'T1':
        if Dest[:1] == 'A':
            Dep_Nxt_T1 = Arr + 25
            return Dep_Nxt_T1;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T1 = Arr + 30
            return Dep_Nxt_T1;
        else: 
            Dep_Nxt_T1 = Arr + 35
            return Dep_Nxt_T1;
    elif T == 'T2':
        if Dest[:1] == 'A':
            Dep_Nxt_T2 = Arr + 25
            return Dep_Nxt_T2;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T2 = Arr + 30
            return Dep_Nxt_T2;
        else: 
            Dep_Nxt_T2 = Arr + 35
            return Dep_Nxt_T2;
    elif T == 'T3':
        if Dest[:1] == 'A':
            Dep_Nxt_T3 = Arr + 25
            return Dep_Nxt_T3;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T3 = Arr + 30
            return Dep_Nxt_T3;
        else: 
            Dep_Nxt_T3 = Arr + 35
            return Dep_Nxt_T3;
    elif T == 'T4':
        if Dest[:1] == 'A':
            Dep_Nxt_T4 = Arr + 25
            return Dep_Nxt_T4;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T4 = Arr + 30
            return Dep_Nxt_T4;
        else: 
            Dep_Nxt_T4 = Arr + 35
            return Dep_Nxt_T4;
    elif T == 'T5':
        if Dest[:1] == 'A':
            Dep_Nxt_T5 = Arr + 25
            return Dep_Nxt_T5;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T5 = Arr + 30
            return Dep_Nxt_T5;
        else: 
            Dep_Nxt_T5 = Arr + 35
            return Dep_Nxt_T5;
    elif T == 'T6':
        if Dest[:1] == 'A':
            Dep_Nxt_T6 = Arr + 25
            return Dep_Nxt_T6;
        elif Dest[:1] == 'D': 
            Dep_Nxt_T6 = Arr + 30
            return Dep_Nxt_T6;
        else: 
            Dep_Nxt_T6 = Arr + 35
            return Dep_Nxt_T6;


# In[339]:

#Printing flight schedule
def print_flight_schedule(fn, csv_hdr, flt_sched):
    with open(fn,'wt') as f:
        print(csv_hdr, file=f)
        for s in flt_sched:
            print(','.join(s), file=f)


# In[340]:

# Converting time in 24H format to minutes
def mil_to_min (military_time):
    #Zero padding in front, if the input is not 4 digits
    pad = ('{:04}'.format(military_time))
    min_from_mid_night = (int(str(pad)[:2])*60)+(int(str(pad)[2:]))
    return min_from_mid_night; 


# In[341]:

#Converting time in minutes to 24H format
def min_to_mil (minutes_from_mid_night):
    military_time = str('{:02}'.format(minutes_from_mid_night//60))+str('{:02}'.format(minutes_from_mid_night%60))
    return military_time;


# In[342]:

#Converting initial schedule in integer to military time by zero padding
def pad (Time):
    #Zero padding in front, if the input is not 4 digits
    Time = ('{:04}'.format(Time))
    return Time;


# In[343]:

#Replacing the gate details with the origin/ destination cities:
def location (Gate):
    if Gate[:1] == 'A':
        Loc = 'AUS'
        return Loc;
    elif Gate[:1] == 'D':
        Loc = 'DAL'
        return Loc;
    elif Gate[:1] == 'H':
        Loc = 'HOU'
        return Loc;


# In[344]:

#Calculating next arrival time
def nxtarr (T, AG_I, DG1_I, DG2_I, HG1_I, HG2_I, HG3_I, Dep_Nxt, Ori):
    #Convert Dep_Nxt to integer to parse it as an input to "mil_to_min" function
    Dep_Nxt = int(Dep_Nxt)
    #Convert the time in 24H format to minutes for time comparisons within the function
    Dep_Nxt = mil_to_min(Dep_Nxt)
    AG_I = mil_to_min(AG_I)
    DG1_I = mil_to_min(DG1_I)
    DG2_I = mil_to_min(DG2_I)
    HG1_I = mil_to_min(HG1_I)
    HG2_I = mil_to_min(HG2_I)
    HG3_I = mil_to_min(HG3_I)
    if T == 'T1':
        if Ori[:1] == 'A':
            Inc = 1
            while (Inc<36):
                if Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'DG1'
                    return Arr_Nxt_T1_Dest; 
                elif Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG3'
                    return Arr_Nxt_T1_Dest; 
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG1'
                    return Arr_Nxt_T1_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG2'
                    return Arr_Nxt_T1_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'DG2'
                    return Arr_Nxt_T1_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while (Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'AG'
                    return Arr_Nxt_T1_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG1'
                    return Arr_Nxt_T1_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG2'
                    return Arr_Nxt_T1_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'HG3'
                    return Arr_Nxt_T1_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        else:
            Inc = 1
            while (Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'AG'
                    return Arr_Nxt_T1_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'DG1'
                    return Arr_Nxt_T1_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T1_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T1 = min_to_mil(Arr_Nxt_T1_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T1_Dest = Arr_Nxt_T1 + 'DG2'
                    return Arr_Nxt_T1_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
    elif T == 'T2':
        if Ori[:1] == 'A':
            Inc = 1
            while (Inc<36):
                if Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG3'
                    return Arr_Nxt_T2_Dest;
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG1'
                    return Arr_Nxt_T2_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG2'
                    return Arr_Nxt_T2_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'DG2'
                    return Arr_Nxt_T2_Dest;
                elif Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'DG1'
                    return Arr_Nxt_T2_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while (Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'AG'
                    return Arr_Nxt_T2_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG1'
                    return Arr_Nxt_T2_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG2'
                    return Arr_Nxt_T2_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'HG3'
                    return Arr_Nxt_T2_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        else:
            Inc = 1
            while (Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'AG'
                    return Arr_Nxt_T2_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'DG1'
                    return Arr_Nxt_T2_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T2_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T2 = min_to_mil(Arr_Nxt_T2_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T2_Dest = Arr_Nxt_T2 + 'DG2'
                    return Arr_Nxt_T2_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
    elif T == 'T3':
        if Ori[:1] == 'A':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'DG1'
                    return Arr_Nxt_T3_Dest; 
                elif Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG3'
                    return Arr_Nxt_T3_Dest;
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG1'
                    return Arr_Nxt_T3_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG2'
                    return Arr_Nxt_T3_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'DG2'
                    return Arr_Nxt_T3_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while (Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'AG'
                    return Arr_Nxt_T3_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG1'
                    return Arr_Nxt_T3_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG2'
                    return Arr_Nxt_T3_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'HG3'
                    return Arr_Nxt_T3_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        else:
            Inc = 1
            while(Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'AG'
                    return Arr_Nxt_T3_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'DG1'
                    return Arr_Nxt_T3_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T3_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T3 = min_to_mil(Arr_Nxt_T3_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T3_Dest = Arr_Nxt_T3 + 'DG2'
                    return Arr_Nxt_T3_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
    elif T == 'T4':
        if Ori[:1] == 'A':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG3'
                    return Arr_Nxt_T4_Dest;
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG1'
                    return Arr_Nxt_T4_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG2'
                    return Arr_Nxt_T4_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'DG2'
                    return Arr_Nxt_T4_Dest;
                elif Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'DG1'
                    return Arr_Nxt_T4_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'AG'
                    return Arr_Nxt_T4_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG1'
                    return Arr_Nxt_T4_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG2'
                    return Arr_Nxt_T4_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'HG3'
                    return Arr_Nxt_T4_Dest;  
        else:
            Inc = 1
            while (Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'AG'
                    return Arr_Nxt_T4_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'DG1'
                    return Arr_Nxt_T4_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T4_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T4 = min_to_mil(Arr_Nxt_T4_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T4_Dest = Arr_Nxt_T4 + 'DG2'
                    return Arr_Nxt_T4_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
    elif T == 'T5':
        if Ori[:1] == 'A':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'DG1'
                    return Arr_Nxt_T5_Dest; 
                elif Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG3'
                    return Arr_Nxt_T5_Dest;
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG1'
                    return Arr_Nxt_T5_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG2'
                    return Arr_Nxt_T5_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'DG2'
                    return Arr_Nxt_T5_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'AG'
                    return Arr_Nxt_T5_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG1'
                    return Arr_Nxt_T5_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG2'
                    return Arr_Nxt_T5_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'HG3'
                    return Arr_Nxt_T5_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        else:
            Inc = 1
            while(Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'AG'
                    return Arr_Nxt_T5_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'DG1'
                    return Arr_Nxt_T5_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T5_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T5 = min_to_mil(Arr_Nxt_T5_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T5_Dest = Arr_Nxt_T5 + 'DG2'
                    return Arr_Nxt_T5_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
    else:
        if Ori[:1] == 'A':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+45 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG3'
                    return Arr_Nxt_T6_Dest;
                elif Dep_Nxt+45 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG1'
                    return Arr_Nxt_T6_Dest;
                elif Dep_Nxt+45 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG2'
                    return Arr_Nxt_T6_Dest; 
                elif Dep_Nxt+50 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'DG2'
                    return Arr_Nxt_T6_Dest;
                elif Dep_Nxt+50 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'DG1'
                    return Arr_Nxt_T6_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        elif Ori[:1] == 'D':
            Inc = 1
            while(Inc<36):
                if Dep_Nxt+50 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 50 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'AG'
                    return Arr_Nxt_T6_Dest;  
                elif Dep_Nxt+65 > HG1_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG1'
                    return Arr_Nxt_T6_Dest;  
                elif Dep_Nxt+65 > HG2_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG2'
                    return Arr_Nxt_T6_Dest;  
                elif Dep_Nxt+65 > HG3_I+35:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'HG3'
                    return Arr_Nxt_T6_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1
        else:
            Inc = 1
            while(Inc<31):
                if Dep_Nxt+45 > AG_I+25:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 45 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'AG'
                    return Arr_Nxt_T6_Dest;  
                elif Dep_Nxt+65 > DG1_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'DG1'
                    return Arr_Nxt_T6_Dest;  
                elif Dep_Nxt+65 > DG2_I+30:
                    #Convert departure time in 24H format to minutes and add the flight time
                    Arr_Nxt_T6_min = Dep_Nxt + 65 
                    #Convert next arrival time in minutes to 24H format
                    Arr_Nxt_T6 = min_to_mil(Arr_Nxt_T6_min)
                    #Appending the destination with the next arrival time
                    Arr_Nxt_T6_Dest = Arr_Nxt_T6 + 'DG2'
                    return Arr_Nxt_T6_Dest;
                else:
                    #Increment ground time by 1 min
                    Dep_Nxt = Dep_Nxt + 1
                    Inc = Inc + 1


# In[345]:

#Recalculating the next departure time based on the incremented ground time
def incdep(Ori_T, Dest_T, Arr_Nxt):
    Arr_Nxt = int(Arr_Nxt)
    Arr_Nxt = mil_to_min (Arr_Nxt)
    if((Ori_T=='HOU' and Dest_T=='AUS')or(Ori_T=='AUS' and Dest_T=='HOU')):
        Dep_Nxt = Arr_Nxt - 45
        Dep_Nxt = min_to_mil(Dep_Nxt)
        return Dep_Nxt;
    elif((Ori_T=='DAL' and Dest_T=='AUS')or(Ori_T=='AUS' and Dest_T=='DAL')):
        Dep_Nxt = Arr_Nxt - 50
        Dep_Nxt = min_to_mil(Dep_Nxt)
        return Dep_Nxt;
    elif((Ori_T=='DAL' and Dest_T=='HOU')or(Ori_T=='HOU' and Dest_T=='DAL')):
        Dep_Nxt = Arr_Nxt - 65
        Dep_Nxt = min_to_mil(Dep_Nxt)
        return Dep_Nxt;


# In[346]:

#Tail Numbers
Tail_Number = ['T1','T2','T3','T4','T5','T6']

#Current Origin
O_T1 = 'HG1'
O_T2 = 'AG'
O_T3 = 'HG2'
O_T4 = 'HG3'
O_T5 = 'DG1'
O_T6 = 'DG2'

#Current Destination
D_T1 = 'AG'
D_T2 = 'HG1'
D_T3 = 'DG1'
D_T4 = 'DG2'
D_T5 = 'HG2'
D_T6 = 'HG3'

#Next Origin (Not required)
O_Nxt_T1 = D_T1
O_Nxt_T2 = D_T2
O_Nxt_T3 = D_T3
O_Nxt_T4 = D_T4
O_Nxt_T5 = D_T5
O_Nxt_T6 = D_T6

#Next Destination


#Current departure time
Dep_Now_T1 = 600
Dep_Now_T2 = 600
Dep_Now_T3 = 600
Dep_Now_T4 = 600
Dep_Now_T5 = 600
Dep_Now_T6 = 600

#Current arrival time
Arr_Now_T1 = 645
Arr_Now_T2 = 645
Arr_Now_T3 = 705
Arr_Now_T4 = 705
Arr_Now_T5 = 705
Arr_Now_T6 = 705

#Initial departure time in 24H format
Dep_Now_T1_ini = pad (Dep_Now_T1)
Dep_Now_T2_ini = pad (Dep_Now_T2)
Dep_Now_T3_ini = pad (Dep_Now_T3)
Dep_Now_T4_ini = pad (Dep_Now_T4)
Dep_Now_T5_ini = pad (Dep_Now_T5)
Dep_Now_T6_ini = pad (Dep_Now_T6)


#Initial arrival time in 24H format
Arr_Now_T1_ini = pad (Arr_Now_T1)
Arr_Now_T2_ini = pad (Arr_Now_T2)
Arr_Now_T3_ini = pad (Arr_Now_T3)
Arr_Now_T4_ini = pad (Arr_Now_T4)
Arr_Now_T5_ini = pad (Arr_Now_T5)
Arr_Now_T6_ini = pad (Arr_Now_T6)


#Initial gate arrival time
AG = 645
HG1 = 645
DG1 = 705
DG2 = 705
HG2 = 705
HG3 = 705


#Flight legs
Leg = 1



# In[347]:

#Converting initial origin gates to the respective city code
Ori_T1_ini = location(O_T1)
Ori_T2_ini = location(O_T2)
Ori_T3_ini = location(O_T3)
Ori_T4_ini = location(O_T4)
Ori_T5_ini = location(O_T5)
Ori_T6_ini = location(O_T6)

#Converting initial destination gates to the respective city code
Dest_T1_ini = location(D_T1)
Dest_T2_ini = location(D_T2)
Dest_T3_ini = location(D_T3)
Dest_T4_ini = location(D_T4)
Dest_T5_ini = location(D_T5)
Dest_T6_ini = location(D_T6)

Flight_Schedule = [[Tail_Number[0], Ori_T1_ini, Dest_T1_ini, Dep_Now_T1_ini, Arr_Now_T1_ini],
           [Tail_Number[1], Ori_T2_ini, Dest_T2_ini, Dep_Now_T2_ini, Arr_Now_T2_ini],
           [Tail_Number[2], Ori_T3_ini, Dest_T3_ini, Dep_Now_T3_ini, Arr_Now_T3_ini],
           [Tail_Number[3], Ori_T4_ini, Dest_T4_ini, Dep_Now_T4_ini, Arr_Now_T4_ini],
           [Tail_Number[4], Ori_T5_ini, Dest_T5_ini, Dep_Now_T5_ini, Arr_Now_T5_ini],
           [Tail_Number[5], Ori_T6_ini, Dest_T6_ini, Dep_Now_T6_ini, Arr_Now_T6_ini]]


# In[348]:

#print (Flight_Schedule)
while (Leg<11):
    #print ("Leg:", Leg)
    for T in Tail_Number:
        if T == 'T1':
            #print ("T1")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T1_min = mil_to_min (Arr_Now_T1)
            #Calculate next departure time in minutes
            Dep_Nxt_T1_min = nxtdep(T, Arr_Now_T1_min, D_T1)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T1 = min_to_mil(Dep_Nxt_T1_min)
            #print (Dep_Nxt_T1)
            O_T1 = D_T1
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T1_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T1, O_T1)
            #print (Arr_Nxt_T1_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T1 = Arr_Nxt_T1_Dest[0:4]
            #print (Arr_Nxt_T1)
            Dest_upd_T1 = Arr_Nxt_T1_Dest[4:]
            #print (Dest_upd_T1)
            #Assigning the updated destination as the current destination
            D_T1 = Dest_upd_T1
            #Assigning the next arrival time as current arrival time
            Arr_Now_T1 = int(Arr_Nxt_T1)
            #Assign arrival time to the respective gates
            if Dest_upd_T1 == 'AG':
                AG = int(Arr_Nxt_T1)
            #    print ("AG:", AG)
            elif Dest_upd_T1 == 'DG1':
                DG1 = int(Arr_Nxt_T1)
            #    print ("DG1:", DG1)
            elif Dest_upd_T1 == 'DG2':
                DG2 = int(Arr_Nxt_T1)
            #    print ("DG2:", DG2)
            elif Dest_upd_T1 == 'HG1':
                HG1 = int(Arr_Nxt_T1)
            #    print ("HG1:", HG1)
            elif Dest_upd_T1 == 'HG2':
                HG2 = int(Arr_Nxt_T1)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T1)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T1 = location(O_T1)
            Dest_T1 = location(D_T1)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T1 = incdep(Ori_T1, Dest_T1, Arr_Nxt_T1)
            #Flight Schedule
            Schedule_T1 = [T, Ori_T1, Dest_T1, Dep_Nxt_T1, Arr_Nxt_T1]
            #print (Schedule_T1)
        elif T == 'T2':
            #print ("T2")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T2_min = mil_to_min (Arr_Now_T2)
            #Calculate next departure time in minutes
            Dep_Nxt_T2_min = nxtdep(T, Arr_Now_T2_min, D_T2)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T2 = min_to_mil(Dep_Nxt_T2_min)
            #print (Dep_Nxt_T2)
            O_T2 = D_T2
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T2_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T2, O_T2)
            #print (Arr_Nxt_T2_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T2 = Arr_Nxt_T2_Dest[0:4]
            #print (Arr_Nxt_T2)
            Dest_upd_T2 = Arr_Nxt_T2_Dest[4:]
            #print (Dest_upd_T2)
            #Assigning the updated destination as the current destination
            D_T2 = Dest_upd_T2
            #Assigning the next arrival time as current arrival time
            Arr_Now_T2 = int(Arr_Nxt_T2)
            #Assign arrival time to the respective gates
            if Dest_upd_T2 == 'AG':
                AG = int(Arr_Nxt_T2)
            #    print ("AG:", AG)
            elif Dest_upd_T2 == 'DG1':
                DG1 = int(Arr_Nxt_T2)
            #    print ("DG1:", DG1)
            elif Dest_upd_T2 == 'DG2':
                DG2 = int(Arr_Nxt_T2)
            #    print ("DG2:", DG2)
            elif Dest_upd_T2 == 'HG1':
                HG1 = int(Arr_Nxt_T2)
            #    print ("HG1:", HG1)
            elif Dest_upd_T2 == 'HG2':
                HG2 = int(Arr_Nxt_T2)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T2)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T2 = location(O_T2)
            Dest_T2 = location(D_T2)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T2 = incdep(Ori_T2, Dest_T2, Arr_Nxt_T2)
            #Flight Schedule
            Schedule_T2 = [T, Ori_T2, Dest_T2, Dep_Nxt_T2, Arr_Nxt_T2]
            #print (Schedule_T2)
        elif T == 'T3':
            #print ("T3")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T3_min = mil_to_min (Arr_Now_T3)
            #Calculate next departure time in minutes
            Dep_Nxt_T3_min = nxtdep(T, Arr_Now_T3_min, D_T3)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T3 = min_to_mil(Dep_Nxt_T3_min)
            #print (Dep_Nxt_T3)
            O_T3 = D_T3
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T3_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T3, O_T3)
            #print (Arr_Nxt_T3_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T3 = Arr_Nxt_T3_Dest[0:4]
            #print (Arr_Nxt_T3)
            Dest_upd_T3 = Arr_Nxt_T3_Dest[4:]
            #print (Dest_upd_T3)
            #Assigning the updated destination as the current destination
            D_T3 = Dest_upd_T3
            #Assigning the next arrival time as current arrival time
            Arr_Now_T3 = int(Arr_Nxt_T3)
            #Assign arrival time to the respective gates
            if Dest_upd_T3 == 'AG':
                AG = int(Arr_Nxt_T3)
            #    print ("AG:", AG)
            elif Dest_upd_T3 == 'DG1':
                DG1 = int(Arr_Nxt_T3)
            #    print ("DG1:", DG1)
            elif Dest_upd_T3 == 'DG2':
                DG2 = int(Arr_Nxt_T3)
            #    print ("DG2:", DG2)
            elif Dest_upd_T3 == 'HG1':
                HG1 = int(Arr_Nxt_T3)
            #    print ("HG1:", HG1)
            elif Dest_upd_T3 == 'HG2':
                HG2 = int(Arr_Nxt_T3)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T3)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T3 = location(O_T3)
            Dest_T3 = location(D_T3)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T3 = incdep(Ori_T3, Dest_T3, Arr_Nxt_T3)
            #Flight Schedule
            Schedule_T3 = [T, Ori_T3, Dest_T3, Dep_Nxt_T3, Arr_Nxt_T3]
            #print (Schedule_T3)
        elif T == 'T4':
            #print ("T4")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T4_min = mil_to_min (Arr_Now_T4)
            #Calculate next departure time in minutes
            Dep_Nxt_T4_min = nxtdep(T, Arr_Now_T4_min, D_T4)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T4 = min_to_mil(Dep_Nxt_T4_min)
            #print (Dep_Nxt_T4)
            O_T4 = D_T4
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T4_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T4, O_T4)
            #print (Arr_Nxt_T4_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T4 = Arr_Nxt_T4_Dest[0:4]
            #print (Arr_Nxt_T4)
            Dest_upd_T4 = Arr_Nxt_T4_Dest[4:]
            #print (Dest_upd_T4)
            #Assigning the updated destination as the current destination
            D_T4 = Dest_upd_T4
            #Assigning the next arrival time as current arrival time
            Arr_Now_T4 = int(Arr_Nxt_T4)
            #Assign arrival time to the respective gates
            if Dest_upd_T4 == 'AG':
                AG = int(Arr_Nxt_T4)
            #    print ("AG:", AG)
            elif Dest_upd_T4 == 'DG1':
                DG1 = int(Arr_Nxt_T4)
            #    print ("DG1:", DG1)
            elif Dest_upd_T4 == 'DG2':
                DG2 = int(Arr_Nxt_T4)
            #    print ("DG2:", DG2)
            elif Dest_upd_T4 == 'HG1':
                HG1 = int(Arr_Nxt_T4)
            #    print ("HG1:", HG1)
            elif Dest_upd_T4 == 'HG2':
                HG2 = int(Arr_Nxt_T4)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T4)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T4 = location(O_T4)
            Dest_T4 = location(D_T4)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T4 = incdep(Ori_T4, Dest_T4, Arr_Nxt_T4)
            #Flight Schedule
            Schedule_T4 = [T, Ori_T4, Dest_T4, Dep_Nxt_T4, Arr_Nxt_T4]
            #print (Schedule_T4)
        elif T == 'T5':
            #print ("T5")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T5_min = mil_to_min (Arr_Now_T5)
            #Calculate next departure time in minutes
            Dep_Nxt_T5_min = nxtdep(T, Arr_Now_T5_min, D_T5)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T5 = min_to_mil(Dep_Nxt_T5_min)
            #print (Dep_Nxt_T5)
            O_T5 = D_T5
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T5_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T5, O_T5)
            #print (Arr_Nxt_T5_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T5 = Arr_Nxt_T5_Dest[0:4]
            #print (Arr_Nxt_T5)
            Dest_upd_T5 = Arr_Nxt_T5_Dest[4:]
            #print (Dest_upd_T5)
            #Assigning the updated destination as the current destination
            D_T5 = Dest_upd_T5
            #Assigning the next arrival time as current arrival time
            Arr_Now_T5 = int(Arr_Nxt_T5)
            #Assign arrival time to the respective gates
            if Dest_upd_T5 == 'AG':
                AG = int(Arr_Nxt_T5)
            #    print ("AG:", AG)
            elif Dest_upd_T5 == 'DG1':
                DG1 = int(Arr_Nxt_T5)
            #    print ("DG1:", DG1)
            elif Dest_upd_T5 == 'DG2':
                DG2 = int(Arr_Nxt_T5)
            #    print ("DG2:", DG2)
            elif Dest_upd_T5 == 'HG1':
                HG1 = int(Arr_Nxt_T5)
            #    print ("HG1:", HG1)
            elif Dest_upd_T5 == 'HG2':
                HG2 = int(Arr_Nxt_T5)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T5)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T5 = location(O_T5)
            Dest_T5 = location(D_T5)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T5 = incdep(Ori_T5, Dest_T5, Arr_Nxt_T5)
            #Flight Schedule
            Schedule_T5 = [T, Ori_T5, Dest_T5, Dep_Nxt_T5, Arr_Nxt_T5]
            #print (Schedule_T5)
        else:
            #print ("T6")
            #Convert arrival time from 24H format to minutes
            Arr_Now_T6_min = mil_to_min (Arr_Now_T6)
            #print ("Arr_Now_T6:", Arr_Now_T6)
            #print ("Arr_Now_T6_min:", Arr_Now_T6_min)
            #print ("D_T6:", D_T6)
            #Calculate next departure time in minutes
            Dep_Nxt_T6_min = nxtdep(T, Arr_Now_T6_min, D_T6)
            #Convert next departure time in minutes to 24H format
            Dep_Nxt_T6 = min_to_mil(Dep_Nxt_T6_min)
            #print (Dep_Nxt_T6)
            O_T6 = D_T6
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Calculate next arrival time
            Arr_Nxt_T6_Dest = nxtarr (T, AG, DG1, DG2, HG1, HG2, HG3, Dep_Nxt_T6, O_T6)
            #print (Arr_Nxt_T6_Dest)
            #print ("@@@@@@@@@@@@@@@@@@@@@@@@@")
            #Splitting next arrival time and corresponding updated destination gate 
            Arr_Nxt_T6 = Arr_Nxt_T6_Dest[0:4]
            #print (Arr_Nxt_T6)
            Dest_upd_T6 = Arr_Nxt_T6_Dest[4:]
            #print (Dest_upd_T6)
            #Assigning the updated destination as the current destination
            D_T6 = Dest_upd_T6
            #Assigning the next arrival time as current arrival time
            Arr_Now_T6 = int(Arr_Nxt_T6)
            #Assign arrival time to the respective gates
            if Dest_upd_T6 == 'AG':
                AG = int(Arr_Nxt_T6)
            #    print ("AG:", AG)
            elif Dest_upd_T6 == 'DG1':
                DG1 = int(Arr_Nxt_T6)
            #    print ("DG1:", DG1)
            elif Dest_upd_T6 == 'DG2':
                DG2 = int(Arr_Nxt_T6)
            #    print ("DG2:", DG2)
            elif Dest_upd_T6 == 'HG1':
                HG1 = int(Arr_Nxt_T6)
            #    print ("HG1:", HG1)
            elif Dest_upd_T6 == 'HG2':
                HG2 = int(Arr_Nxt_T6)
            #    print ("HG2:", HG2)
            else:
                HG3 = int(Arr_Nxt_T6)
            #    print ("HG3:", HG3)
            #Origin/ Destination location conversion
            Ori_T6 = location(O_T6)
            Dest_T6 = location(D_T6)
            #Updated departure time calculation after incrementing ground time
            Dep_Nxt_T6 = incdep(Ori_T6, Dest_T6, Arr_Nxt_T6)
            #Flight Schedule
            Schedule_T6 = [T, Ori_T6, Dest_T6, Dep_Nxt_T6, Arr_Nxt_T6]
            #print (Schedule_T6)
    Leg = Leg + 1
    Schedule = [Schedule_T1, Schedule_T2, Schedule_T3, Schedule_T4, Schedule_T5, Schedule_T6]
    #print (Schedule)
    Flight_Schedule = Flight_Schedule + Schedule
    print(Flight_Schedule)
    csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
    file_name = 'flight_schedule.csv'
    # TO Sort based on tail_number and departure_time
    Flight_Schedule = sorted(Flight_Schedule, key = lambda x: x[0] + x[3])
    print_flight_schedule(file_name, csv_header, Flight_Schedule)


# In[268]:

Schedule


# In[269]:

print (Schedule)


# In[225]:




# In[229]:




# In[170]:

Arr_Now_T6


# In[159]:

type(Arr_Nxt_T6_Dest)


# In[179]:

Arr_Nxt_T6_Dest


# In[182]:

D_T5


# In[67]:

type(Dep_Nxt_T1)


# In[183]:

D_T6


# In[162]:

Arr_Nxt_T6


# In[180]:

Arr_Now_T6


# In[176]:

Arr_Now_T6_min


# In[178]:

O_T6


# In[169]:

O_T5


# In[198]:

1115//60


# In[199]:

1115%60


# In[ ]:



