import random

def show_learning(w):
    print('w0=', '%5.2f' % w[0], ',w1=', '%5.2f'  % w[1], 'w2=', '%5.2f'% w[2])

random.seed(7)
LEARNING_RATE=0.1

index_list=[0,1,2,3]

x_train=[(1.0, -1.0, -1.0), (1.0, -1.0, 1.0),
         (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
y_train=[1.0, 1.0, 1.0, -1.0]

w=[0.2, -0.6, 0.25]

show_learning(w)