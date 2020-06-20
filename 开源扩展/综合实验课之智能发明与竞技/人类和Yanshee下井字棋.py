#!/usr/bin/python

#coding=utf-8

#监督学习+强化学习 + 左（AI）右（随机策略）手互搏 井字棋游戏；生成参数学习过程的可视化图片，并人机实战演练
'''
开始机器人会等待一个“下棋”的指令，然后开始学习井字棋，然后弹出学习曲线，代表学习完成，当我们关闭学习曲线之后，
井字棋棋盘同时弹出，这时就开始下棋了。人类选手输入行列用逗号隔开之后回车，最后会有三种结果：
机器人AI赢、人类选手赢、和棋。机器人会根据它们做出不同的动作和语音表达，以达到互动的目的。


'''

import RobotApi

import random

import numpy as np

import time

import matplotlib.pyplot as plt

 

def print2():

    print '落子格式 : a,b , 表示棋盘的a行b列'

    L2 = raw_input('玩家 : ')

    return L2

def player0(B,a,b):

    s0_1 = 0.0;s0_2 = 0.0;s0_3 = 0.0;s0_4 = 0.0

    if a != 1 and b != 1:

        s0 = 3.0

    elif a ==1 and b == 1:

        s0 = 4.0

    else:

        s0 = 2.0

    m = 0

    while m<3:

        n = 0

        while n<3:

            if B[m][n] == 1:

                # 同一行

                if m == a:

                    s0_1 = 1.0

                # 同一列

                if n == b:

                    s0_2 = 1.0

                # 对角线

                if m == n and a == b:

                    s0_3 = 1.0

                if (m + n) / 2. == 1 and (a + b) / 2. == 1:

                    s0_4 = 1.0

            n += 1

        m += 1

    return (s0-s0_1-s0_2-s0_3-s0_4)/s0

def player1(B,a,b):

    s1_1 = 0;s1_2 = 0;s1_3 = 0;s1_4 = 0

    m = 0

    while m<3:

        n = 0

        while n<3:

            if B[m][n] == 1:

                # 同一行

                if m == a:

                    s1_1 += 1

                # 同一列

                if n == b:

                    s1_2 += 1

                # 对角线

                if m == n and a == b:

                    s1_3 += 1

                if (m + n) / 2. == 1 and (a + b) / 2. == 1:

                    s1_4 += 1

            n += 1

        m += 1

    return np.max([s1_1,s1_2,s1_3,s1_4])/2.0

def player2(B,a,b):

    s2_1 = 0;s2_2 = 0;s2_3 = 0;s2_4 = 0

    m = 0

    while m < 3:

        n = 0

        while n < 3:

            if B[m][n] == 2:

                # 同一行

                if m == a:

                    s2_1 += 1

                # 同一列

                if n == b:

                    s2_2 += 1

                # 对角线

                if m == n and a == b:

                    s2_3 += 1

                if (m + n) / 2. == 1 and (a + b) / 2. == 1:

                    s2_4 += 1

            n += 1

        m += 1

    return np.max([s2_1,s2_2,s2_3,s2_4])/2.0

def initiate():

    global X, A0, A1, A2, A4

    X = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

    A0 = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

    A1 = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

    A2 = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

    A4 = [[0, 0, 0],[0, 0, 0],[0, 0, 0],]

    return

def calculate():

    global X, A0, A1, A2, A4

    i = 0

    while i < 3:

        j = 0

        while j < 3:

            if X[i][j] == 0:

                A0[i][j] = player0(X, i, j)

                A1[i][j] = player1(X, i, j)

                A2[i][j] = player2(X, i, j)

            else:

                A0[i][j] = -1

                A1[i][j] = -1

                A2[i][j] = -1

            j += 1

        i += 1

    return

# ========================================================================

def step(n,L1,L2):

    global X,A0,A1,A2,A4

    global training_set_inputs,training_set_outputs

    D_step = -1

    ###########################

    if n == 1:

        calculate()

        i = 0

        while i < 3:

            j = 0

            while j < 3:

                A4[i][j] = np.dot([A0[i][j], A1[i][j], A2[i][j]], L1)

                j += 1

            i += 1

        D = np.where(A4 == np.max(A4))

        d = random.randint(1, len(D[0])) - 1

        d1 = D[0][d];d2 = D[1][d]

        training_set_inputs.append([A0[d1][d2], A1[d1][d2], A2[d1][d2]])

        X[d1][d2] = 1

        if A1[d1][d2] == 1:

            D_step = 1

            return D_step

        E = np.where(X == np.int64(0))

        if len(E[0]) == 0:

            D_step = 0

            return D_step

        n = 2

        # print X[0], '\n', X[1], '\n', X[2]

    ###########################

    if n == 2:

        # ++++++++++++++++++++++++++++启用"+++"内的代码，让对抗对手变强，反而学些效果不好++++++++++++++++

        # calculate()

        # i = 0

        # while i < 3:

        #     j = 0

        #     while j < 3:

        #         A4[i][j] = np.dot([A0[i][j], A1[i][j], A2[i][j]], L2.T)

        #         j += 1

        #     i += 1

        # i = 0

        # while i < 3:

        #     j = 0

        #     while j < 3:

        #         if A2[i][j] == 1:

        #             X[i][j] = 2

        #             n = 1

        #             D_step = 2

        #             return D_step

        #         j += 1

        #     i += 1

        # i = 0

        # while i < 3:

        #     j = 0

        #     while j < 3:

        #         if A1[i][j] == 1:

        #             X[i][j] = 2

        #             n = 1

        #         j += 1

        #     i += 1

        # ++++++++++++++++++++++++++++++++++++++++++++不启用则对抗对手随机落子+++++++++++++++++++++++++

        if n == 2:

            # 随机落子

            D = np.where(X == np.int64(0))

            if len(D[0]) == 0:

                D_step = 0

                return D_step

            d = random.randint(1, len(D[0])) - 1

            d1 = D[0][d];d2 = D[1][d]

            X[d1][d2] = 2

            n = 1

        # print X[0], '\n', X[1], '\n', X[2]

    ###########################

    return D_step

# ========================================================================

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

def learn(L,L1,L2):

    I = np.array([L1])

    O = np.array(L2).T

    for i in xrange(5):      #################################### 可以试试 3  5  7  越大越优化，耗时越长

        output = 1 / (1 + np.exp(-(np.dot(I, L))))

        L += np.dot(I.T, (O - output) * output * (1 - output))

    return L

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# ----------------------------------------------------------------

def training():

    global X,A0,A1,A2,A4

    list_K1 = np.random.random((3,1))

    # list_K2 = np.random.random((3))

    list_K2 = [0,0,0]

    for iteration in xrange(100):    ######################################### 可以试试 10 100 1000，越大越优化

        N_train = random.randint(1, 2)

        initiate()

        D_train = -1

        del training_set_inputs[:]

        del training_set_outputs[:]

        while True:

            calculate()

            D_train = step(N_train, list_K1, list_K2)

            N_train = 1

            if D_train != -1:

                plt.scatter(iteration, D_train, s = 3, c='red', marker='o')

                plt.scatter(iteration, list_K1[0][0], s=3, c='g', marker='o')

                plt.scatter(iteration, list_K1[1][0], s=3, c='y', marker='o')

                plt.scatter(iteration, list_K1[2][0], s=3, c='b', marker='o')

            if D_train == 1:

                i_training_set_inputs = training_set_inputs[-1]

                training_set_outputs.append([1])

                list_K1 = learn(list_K1,i_training_set_inputs,training_set_outputs)

                break

            elif D_train == 2:

                i_training_set_inputs = training_set_inputs[-1]

                training_set_outputs.append([0])

                list_K1 = learn(list_K1,i_training_set_inputs,training_set_outputs)

                break

            elif D_train == 0:

                break

    return list_K1

# ==============================

RobotApi.ubtRobotInitialize()                                                                            

ret=RobotApi.ubtRobotConnect("sdk","1", "127.0.0.1")                                                                                                   

if (0 != ret):                                                                                        

         print ("Error --> ubtRobotConnect return value: %d" % ret)                                  

         exit(1)                                                                                  

                                                                                                                                                                                                

#----------------------- block program start ----------------------

RobotApi.ubtVoiceTTS(0,"你好,我是智能机器人Yanshee。")

time.sleep(3)

while True:

    RobotApi.ubtSetRobotLED("button", "yellow", "blink")

    ret = RobotApi.ubtDetectVoiceMsg("下棋",20)

    if ret == 0:

        break

RobotApi.ubtVoiceTTS(0,"开始学习井字棋游戏。")

# ----------------------------------------------------------------

# X为棋盘，空格为0，玩家1(AI)的落子为1，玩家2的落子为2

initiate()

# ----------------------------------------------------------------

training_set_inputs = []

training_set_outputs = []

time_s = time.time()

K = training()

time_e = time.time()

print '训练时间：',time_e-time_s,'秒'

print K

k_A0 = K[0][0]

k_A1 = K[1][0]

k_A2 = K[2][0]

RobotApi.ubtVoiceTTS(0,"学习完毕，用时"+str(int(time_e-time_s))+"秒。")

plt.show()

RobotApi.ubtVoiceTTS(0,"开始下棋。")

# ----------------------------------------------------------------

initiate()

print X[0],'\n',X[1],'\n',X[2]

N = random.randint(1,2)

L = []

if N==2 :

    while True:

        RobotApi.ubtVoiceTTS(0, "请落子。")

        L = print2();L = L.strip(' ').split(',')

        L[0] = int(L[0]) - 1;L[1] = int(L[1]) - 1

        if X[L[0]][L[1]] == 0:

            break

    X[L[0]][L[1]] = 2

    N = 1

while True:

    print X[0],'\n',X[1],'\n',X[2]

    calculate()

    # print A0[0],'\n',A0[1],'\n',A0[2]

    # print A1[0],'\n',A1[1],'\n',A1[2]

    # print A2[0],'\n',A2[1],'\n',A2[2]

    i = 0

    while i<3:

        j = 0

        while j<3:

            A4[i][j] = k_A0*A0[i][j]+k_A1*A1[i][j]+k_A2*A2[i][j]

            j += 1

        i += 1

    if N == 1:

        D = np.where(A4==np.max(A4))

        d = random.randint(1,len(D[0]))-1

        d1 = D[0][d];d2 = D[1][d]

        X[d1][d2] = 1

        RobotApi.ubtVoiceTTS(0, "我选第"+str(d1+1)+"行，第"+str(d2+1)+"列。")

        if A1[d1][d2] == 1:

            print X[0], '\n', X[1], '\n', X[2]

            print 'AI win!'

            RobotApi.ubtSetRobotMotion("come on", "left", 3, 1)

            RobotApi.ubtVoiceTTS(0, "多谢承让！")

            # =============================================================

            RobotApi.ubtStopRobotAction ()

            #----------------------- block program end ----------------------                                                                                                                                            

            RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                           

            RobotApi.ubtRobotDeinitialize()

            exit()

        E = np.where(X == np.int64(0))

        if len(E[0]) == 0:

            print X[0], '\n', X[1], '\n', X[2]

            print 'Draw!'

            RobotApi.ubtSetRobotMotion("crouch", "left", 2, 1)

            RobotApi.ubtVoiceTTS(0, "棋逢对手！")

            # =============================================================

            RobotApi.ubtStopRobotAction ()

            #----------------------- block program end ----------------------                                                                                                                                            

            RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                           

            RobotApi.ubtRobotDeinitialize()

            exit()

        N = 2

 

    print X[0], '\n', X[1], '\n', X[2]

 

    while True:

        L = print2();L = L.strip(' ').split(',')

        L[0] = int(L[0]) - 1;L[1] = int(L[1]) - 1

        if X[L[0]][L[1]] == 0:

            break

        else:

            print 'There is already employed. Remove, please.'

    X[L[0]][L[1]] = 2

    N = 1

    if A2[L[0]][L[1]] == 1:

        print X[0], '\n', X[1], '\n', X[2]

        print 'Player win!'

        RobotApi.ubtSetRobotMotion("bow", "", 1, 1)

        RobotApi.ubtVoiceTTS(0, "不胜棋力，甘拜下风！")

        # =============================================================

        RobotApi.ubtStopRobotAction ()

        #----------------------- block program end ----------------------                                                                                                                                

        RobotApi.ubtRobotDisconnect("sdk", "1", "127.0.0.1")                                                                                            

        RobotApi.ubtRobotDeinitialize()

        exit()