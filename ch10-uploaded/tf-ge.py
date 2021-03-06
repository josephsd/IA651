import numpy as np
import tensorflow as tf

n_inputs = 2  
n_outputs = 2

X = tf.placeholder(tf.float32, shape=(None, n_inputs), name="X")
y = tf.placeholder(tf.float32, shape=(None, n_outputs), name="y")

# Construct model
W = tf.Variable(tf.zeros([n_inputs,n_outputs]))
b = tf.Variable(tf.zeros([n_outputs]), name="bias")
Z = tf.matmul(X, W) + b
pred = tf.nn.softmax(Z)
# Minimize error using cross entropy
loss = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))

learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()

n_epochs = 10000
with tf.Session() as sess:
    X_batch = [[8.5, 9.1],[3,3], [7.6, 5.2], [0.2, 6.8], [6.6, 6.6], [4.2, 2.4],[3.0,3.1],[9.9,9.9],[2.0,2.2]]
    y_batch = [[0,1],[0,1],[0, 1],[1, 0],[0, 1],[0, 1],[1,0],[0,1],[1,0]]
    
    init.run()
    for epoch in range(n_epochs):
        loss_val, _=sess.run([loss, training_op], feed_dict={X: X_batch, y: y_batch})
        #print("loss: ", loss_val)

    X_new = [[6, 4], [1, 1], [1,6],[4,6]]
    y_pred = pred.eval(feed_dict={X: X_new})
    y_actuals = [1, 1, 0, 0]

    print("Predicted classes:", np.argmax(y_pred,1))
    print("Actual classes:   ", y_actuals)
