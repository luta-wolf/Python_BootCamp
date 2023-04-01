
def fix_wiring():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    for c in fix_wiring(cables, sockets, plugs):
        print(c)




if __name__ == "__main__":
    fix_wiring()