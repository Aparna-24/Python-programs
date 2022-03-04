class change:
    def __init__(self,name):
        self.name=name
    def change_name(self,new_name):
        print(self.name," has a new name and that is ",new_name.name)

ori=change("harry")
new=change("peerter")
ori.change_name(new)



