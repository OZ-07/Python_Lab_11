
from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite
from jinja2 import Environment, FileSystemLoader

def get_mindmap_html(root):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('templates/mindmap.j2')
    output = template.render(mindmap=root.get_mind_map())
    return output

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
    print(get_mindmap_html(mmc))

    with open('mindmaps/mindmap.html','w') as file:
        file.write(get_mindmap_html(mmc))

if __name__=='__main__':
    main()