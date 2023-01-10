# import modules
from dotenv import load_dotenv
from pathlib import Path
from tabnews import Client
import os

global bestPosts; bestPosts = []

class bot:
   def __init__(self):
      # config dotenv path
      dotenv_path = Path('../.env')
      load_dotenv(dotenv_path=dotenv_path)

      #get email and password of file [.env]
      self.email_tabnews    = os.getenv('email_tabnews')
      self.password_tabnews = os.getenv('password_tabnews')
      #print(f'email:{self.email_tabnews} | pass:{self.password_tabnews}')

      # start functions
      self.create_connection_tabnews()
      self.get_post()


   def create_connection_tabnews(self):
      self.client = Client(self.email_tabnews, self.password_tabnews, save_session=False, use_preview_tabnews_host=False)
      self.user   = self.client.get_user()

      print(f'tabnews conected with: {self.user.username}')


   def get_post(self):
      posts = self.client.get_relevant_posts()
      
      for i in range(0, len(posts)):
         if posts[i]['tabcoins'] > 10 or posts[i]['children_deep_count'] > 5:
            print(posts[i])
            print(' ')
            

         

   


if "__main__" == __name__:
   bot()