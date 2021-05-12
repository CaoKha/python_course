import os
def locate_universe_formula():
    path = "/tmp/documents"
    name = "universe-formula"
    for root,dirs,files in os.walk(path):
        if name in files:
            return os.path.join(root,name)
    return None 