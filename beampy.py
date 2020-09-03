#!/bin/python3
import sys
import os

class UserConfig:
    def __init__(self):
        self.conf_map = {}
        self.conf_map["User"] = ""
        self.conf_map["Colorscheme"] = ""
        self.conf_map["Email"] = ""
        self.conf_map["Company"] = ""
        self.conf_map["Thanks"] = ""

    def AddInfo(self,key,value):
        self.conf_map[key] = value

    def OutputToFile(self,file):
        pass

def ExtractContent(contnet):
   #@TODO
   pass

class Section:
    def __init__(self):
        self.content = []

    def AddContent(self,input):
        self.content.append(input)
    def __str__(self):
        pass

class Slide:
    def __init__(self,file):
        self.layout ={"UL":None , "UR":None ,"DL":None, "DR":None , "L":None, "R":None, "U":None, "D":None}
        self.Heading = ""
        self.file = file
    def Extract(self):
        try:
            with open(self.file) as file:
                data = True
                while data:
                    read_data = file.readline()
                    if not read_data:
                        data = False
                    else:
                        section, item = ExtractContent(read_data)
                        if self.layout[section] == None:
                            self.layout[section] = Section()
                        self.layout[section].AddContent(item)
        except:
            print('Could not open {}'.format(self.file))

class Presentation:
    def __init__(self):
        self.slides = []

    def AddSlideAt(self,slide,slide_pos):
        self.slides.insert(slide_pos,slide)
        pass
    def __str__(self):
        pass


def load_conf(conf_location):
    try:
        #basically read all files and make them into slides and then append them into presentation
    except FileNotFoundError:
        print("Config does not exitst ins location {}".format(conf_location))
        sys.exit(3)

def load_presentation(pres_dir,pres_name):
    try:
        _,_,files=os.walk(pres_dir)

        pres = Presentation()
        slides_it = *range(len(files))
        for (f,pos) in (files,slides):
            sl = Slide(f)
            sl.Extract()
            pres.AddSlideAt(sl,pos)

    except:
        printf("Failed to open dir {}:".format(pres_dir))
        sys.exit(2)

def main():
    sys.argv.pop(0)
    print("Done")

if __name__ == "__main__":
    main()

