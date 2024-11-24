import os

from mindmap_leaf import MindMapLeaf
from typing import Union

class MindMapComposite:

    def __init__(self,name,shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self,child):
        self.children.append(child)
    def remove(self,child):
        self.children.remove(child)

    def __str__(self):
        return self.get_shape_representation().format(name = self.name)

    def get_mind_map(self,indent=0):
        result = ''
        if indent == 0:
            result+= 'mindmap' + os.linesep + 'root'
        result +=' '*indent +str(self) + os.linesep
        for child in self.children:
            result += child.get_mind_map(indent + 2)
        return result

    def display(self,indent=0):
        if indent == 0:
            print('mindmap\nroot', end='')
        print(' '*indent +str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        shapes = {"circle": "(({name}))",
                  "oval": "({name})",
                  "square": "[{name}]",
                  "cloud": "){name}(",
                  "hexagon": "{{{{{name}}}}}",
                  "bang": ")){name}(("
                  }
        return shapes.get(self.shape, "{name}")


def main():
    tools = MindMapComposite('tools', 'cloud')
    tools.add(MindMapLeaf('mermaid', 'square'))
    tools.add(MindMapLeaf('pen and paper', 'square'))
    mmc = MindMapComposite('mindmap', 'circle')
    mmc.add(tools)
    mmc.add(MindMapLeaf('origin', 'cloud'))
    mmc.add(MindMapLeaf('research','cloud'))
    print(mmc.display())
    #print(mmc.get_mind_map())

if __name__=='__main__':
    main()