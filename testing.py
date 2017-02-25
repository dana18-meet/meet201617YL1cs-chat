import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button
from turtle_chat_widgets import TextInput


class TextBox(TextInput):
  
    def draw_box(self):
        yes = turtle.clone()
        yes.penup()
        yes.goto(self.pos)
        yes.goto(self.width/2,self.height/2)
        yes.pendown()
        yes.goto(-self.width/2,self.height/2)
        yes.goto(-self.width/2,-self.height/2)
        yes.goto(self.width/2,-self.height/2)
        yes.goto(self.width/2,self.height/2) 

    def write_msg(self):
        self.writer.clear()
        self.writer.write(self.get_msg())
        
    def write_msg(self):
        self.writer.clear()
        if len(self.get_msg()) % self.letters_per_line == 0 : 
            self.new_msg=self.new_msg+"\r"
        print (self.get_msg())
        self.writer.write(self.get_msg())
        
class SendButton(Button):
    def __init__(self,my_turtle=None,shape=None,pos=(0,-100),view=None):
        super (SendButton,self).__init__(my_turtle=None,shape=None,pos=(0,-100))
        print('im in this line')
        self.view=View()
        print('this is the view:', self.view)
        
    def fun(self,x=None,y=None):
        self.view.send_msg()

class View:
    _MSG_LOG_LENGTH=5 
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):

        print('st<rted view')
        self.username=username
        self.partner_name=partner_name
        self.my_client=Client()
        turtle.setup(width=SCREEN_WIDTH*2,height=SCREEN_WIDTH*2)
        

        self.msg_queue=[]
        self.EL =[]
        for message in range(_MSG_LOG_LENGTH):
            self.EL.append(turtle.clone())
        
        TBX=TextBox()
        SBTN=SendButton()
        self.TBX=TextBox()
        self.SBTN=SendButton()
        
        self.setup_listeners()

    def send_msg(self):
      
        self.my_client.send(self.TextBox.new_msg)
        self.msg_queue.append(self.TextBox.new_msg)
        self.TextBox.clear_msg()
        self.display_msg()
        
    def get_msg(self):
        return self.textbox.get_msg()
    
    def setup_listeners(self):
        pass
    
    def msg_received(self,msg):
        print(msg) 
        show_this_msg=self.partner_name+' says:\r'+ msg
        self.msg_queue.append(a_msg_string)
        self.display_msg()
    
    def display_msg(self):
        self.me.clear()
        self.me.write(self.msg_queue[5])
        

if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) 
    check()
    turtle.mainloop()
   



SendButton()    
x=TextBox()
        
    
