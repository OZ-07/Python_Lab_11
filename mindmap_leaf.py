import os

class MindMapLeaf:

    def __init__(self,name,shape):
        self.name = name
        self.shape = shape

    def display(self, indent=0):
        if indent == 0:
            print('mindmap\nroot', end='')
        print(' ' * indent + str(self))
        #indent.self = indent
        #print(f"{name}"*indent+str(self))

    def get_mind_map(self, indent=0):
        result = ''
        if indent == 0:
            result += 'mindmap' + os.linesep + 'root'
        result +=' ' * indent + str(self) + os.linesep
        return result

    def __str__(self):
        return self.get_shape_representation().format(name = self.name)

    def get_shape_representation(self):
       shapes= {"circle": "(({name}))",
                "oval": "({name})",
                "square": "[{name}]",
                "cloud": "){name}(",
                "hexagon": "{{{{{name}}}}}",
                "bang": ")){name}(("
                }
       return shapes.get(self.shape,"{name}")


def main():
    mml = MindMapLeaf('trevor','oval')
    mml.display()
    mml.display(indent=4)
if __name__=='__main__':
    main()