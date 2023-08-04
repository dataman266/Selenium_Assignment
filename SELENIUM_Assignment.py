#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().system('pip install selenium')


# In[19]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[20]:


driver = webdriver.Chrome()


# In[50]:


driver.get('https://www.amazon.in')


# In[ ]:


#Write a python program which searches all the product under a particular product from www.amazon.in. 
#The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. 


# In[9]:





# In[51]:


name = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
product = input('Enter the product: ')
name.send_keys(product)


# In[52]:


search = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[ ]:


#In the above question, now scrape the following details of each product listed in first 3 pages of your search
#results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then
#scrape all the products available under that product name. Details to be scraped are: "Brand Name",
#"Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and
#“Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“. 


# In[24]:


import pandas as pd
df = pd.DataFrame(columns=["Brand Name", "Name of the Product", "Price",  "Return/Exchange", "Expected Delivery", "Availability", "Product URL"])


# In[25]:


df


# In[38]:


brands = []
start = 0
end = 2
for page in range(start,end):
    brand = driver.find_elements(By.CLASS_NAME, "a-size-base po-break-word")
    for i in brand:
        brands.append(i)
    next_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/a[3]")


# In[39]:


len(brands)


# In[40]:


brands


# In[ ]:


#Write a python program to access the search bar and search button on images.google.com and scrape 10
#images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’. 


# In[31]:


driver = webdriver.Chrome()


# In[32]:


driver.get('https://images.google.com')


# In[33]:


input = driver.find_element(By.CLASS_NAME, "gLFyf")
input.send_keys("fruits")


# In[23]:


time.sleep(2)


# In[34]:


search = driver.find_element(By.CLASS_NAME, "wM6W7d")
search.click()


# In[35]:


fruit_images = []
start = 0
end = 10
for image in range(start,end):
    url = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[2]/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
    fruit_images.append(url)


# In[36]:


fruit_images


# In[38]:


driver = webdriver.Chrome()
driver.get('https://images.google.com')
input = driver.find_element(By.CLASS_NAME, "gLFyf")
input.send_keys("cars")


# In[39]:


search = driver.find_element(By.CLASS_NAME, "wM6W7d")
search.click()


# In[42]:


car_images = []
start = 0
end = 10
for image in range(start, end):
    url_elements = driver.find_elements(By.XPATH, "//*[@id='islrg']/div[1]/div[1]/a[1]/div[1]/img")
    for element in url_elements:
        car_images.append(element.get_attribute("src"))


# In[43]:


car_images


# In[ ]:





# In[ ]:




