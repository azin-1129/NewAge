all_correct=False

while not all_correct:
    all_correct=True
    random.shuffle(index_list)

    for i in index_list:
        x=x_train[i]
        y=y_train[i]

        p_out=compute_output(w,x)

        if y!=p_out:
            for j in range(0, len(w)):
                w[j]+=(y*LEARNING_RATE*x[j])
            all_correct=False
            show_learning(w)