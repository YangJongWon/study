
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import tensorflow as tf


# #read csv

# In[54]:


csv=pd.read_csv(r'F:\BigData3\tensorflow\ch5\bmi.csv')


# In[69]:


csv


# #정규화

# In[56]:


csv["height"] = csv["height"]/200
csv["weight"] = csv["weight"]/100


# #레이블

# In[57]:


bclass={"thin":[1,0,0],"normal":[0,1,0],"fat":[0,0,1]}


# In[58]:


csv["label_pat"]=csv["label"].apply(lambda x : np.array(bclass[x]))


# #테스트를 위한 분류

# In[59]:


test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])


# In[72]:


test_pat


# #데이터 플로우 그래프 선언

# ##플레이스홀더

# In[60]:


x=tf.placeholder(tf.float32,[None,2])
y_=tf.placeholder(tf.float32,[None,3])


# ##변수 선언

# In[61]:


W=tf.Variable(tf.zeros([2,3]));
b=tf.Variable(tf.zeros([3]));
y=tf.nn.softmax(tf.matmul(x,W)+b)


# #tf.zeros([3, 4], tf.int32)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# ##모델 훈련

# In[62]:


cross_entropy=-tf.reduce_sum(y_*tf.log(y))
optimizer=tf.train.GradientDescentOptimizer(0.01)
train=optimizer.minimize(cross_entropy)


# #정답률 예측

# In[63]:


predict=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(predict,tf.float32))


# #세션 시작

# In[66]:


sess=tf.Session()
sess.run(tf.global_variables_initializer())


# #학습

# In[67]:


for step in range(3500):
    i = (step*100) % 14000
    rows= csv[1+i:1+i+100]
    x_pat=rows[["weight","height"]]
    y_ans=list(rows["label_pat"])
    fd={x:x_pat,y_:y_ans}
    sess.run(train,feed_dict=fd)
    if step % 500 == 0:
        cre = sess.run(cross_entropy,feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y_:test_ans})
        print("step=",step,"cre=",cre,"acc=",acc)


# #결과

# In[68]:


acc=sess.run(accuracy,feed_dict={x: test_pat, y_: test_ans})
print("정답률=", acc)

