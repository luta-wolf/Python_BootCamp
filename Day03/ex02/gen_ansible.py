import yaml
from yaml import Loader, Dumper

with open("todo.yml") as file:
    param = file.read()
    pars = yaml.load(param, Loader=Loader)

# print(pars)
play_book = []
play_book.append({
    "name": "Install packages",
    "ansible.builtin.apt": {
        "pkg": pars['server']['install_packages']
    }
})

for a in pars["server"]["exploit_files"]:
    play_book.append({
        "name": "Copy over files " + a,
        "ansible.builtin.copy": {
            "src": a,
            "dest": "/tmp/" + a
        }
    })

play_book.append({
    "name": "Run files on a remote server with a Python interpreter, specifying corresponding arguments",
    "aansible.builtin.command": "python3 /tmp/consumer.py -e {}".format(",".join(pars['bad_guys']))
})

output = yaml.dump(play_book, Dumper=Dumper, sort_keys=False)
print(play_book)
with open("deploy.yml", "w") as file:
    file.write(output)

