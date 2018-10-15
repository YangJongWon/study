
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


a=tf.constant(20,name="a")
b=tf.constant(30,name="b")
mul_op=a*b


# In[3]:


sess=tf.Session()


# In[4]:


tw=tf.summary.FileWriter("log_dir",graph=sess.graph)


# In[5]:


print(sess.run(mul_op))

