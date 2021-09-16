from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.network.urlrequest import UrlRequest

import threading
from kivymd_extensions.akivymd.uix.loaders import AKLabelLoader, AKImageLoader

KV = '''
MDScreen:
    
    MDBoxLayout:
        orientation: 'vertical'
        
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: '24dp'
                spacing: '24dp'
                adaptive_height: True
                
                LoaderCard:
                    id: user1
                
                LoaderCard:
                    id: user2
                    
        
        MDBoxLayout:
            adaptive_height: True
            padding: '5dp'
            spacing: '5dp'
            
            MDRaisedButton:
                text: 'Get Online Data'
                on_release: app.get_data()
            
            MDRaisedButton:
                text: 'Clear Data'
                on_release: app.clear_data()

<LoaderCard@MDCard>:
    padding: '8dp'
    size_hint: None, None
    size: '280dp', '140dp'
    pos_hint: {'center_x': .5, 'center_y': .5}
    name: ''
    email: ''
    website: ''
    avatar: ''
    
    MDBoxLayout:
        
        MDFloatLayout:
            size_hint_x: 0.3
            
            AKImageLoader:
                size_hint: None, None
                size: '50dp', '50dp'
                pos_hint: {'center_x': .5, 'center_y': 0.5}
                source: root.avatar
        
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.7
            padding: '10dp'
            spacing: '10dp'
            
            # Name
            DataLoaderLabel:
                text: root.name
            
            MDSeparator:
            
            # Email
            DataLoaderLabel:
                text: root.email
            
            MDSeparator:
            
            # Website
            DataLoaderLabel:
                text: root.website
            
            MDSeparator:
            
            
<DataLoaderLabel@AKLabelLoader>:
    size_hint_y: None
    height: '20dp'
    theme_text_color: 'Primary'
    halign: 'left'  
            
'''


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # get data
    def get_data(self, *args):
        print('Getting Data')
        t = threading.Thread(target=self.send_request)
        t.start()
        print('Finished!')

    # Set the first user
    def set_user1(self, *args):
        user1 = args[1]
        self.root.ids.user1.avatar = 'https://images.unsplash.com/photo-1631761326704-510e0f81237b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=400&q=80'
        self.root.ids.user1.name = user1['name']
        self.root.ids.user1.email = user1['email']
        self.root.ids.user1.website = user1['website']

    # Set the second user
    def set_user2(self, *args):
        user1 = args[1]
        self.root.ids.user2.avatar = 'https://images.unsplash.com/photo-1631731552291-b19fbd77282b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80'
        self.root.ids.user2.name = user1['name']
        self.root.ids.user2.email = user1['email']
        self.root.ids.user2.website = user1['website']

    # request data from the web
    def send_request(self):
        url = 'https://jsonplaceholder.typicode.com/'

        UrlRequest(url + 'users/1', self.set_user1, on_error=self.got_error, timeout=4)
        UrlRequest(url + 'users/2', self.set_user2, on_error=self.got_error, timeout=4)
        return True

    # Error
    def got_error(self):
        print('Got an error!')

    # Clear the data
    def clear_data(self):
        self.root.ids.user1.name = ''
        self.root.ids.user1.email = ''
        self.root.ids.user1.website = ''
        self.root.ids.user1.avatar = ''

        self.root.ids.user2.name = ''
        self.root.ids.user2.email = ''
        self.root.ids.user2.website = ''
        self.root.ids.user2.avatar = ''


if __name__ == '__main__':
    MainApp().run()
