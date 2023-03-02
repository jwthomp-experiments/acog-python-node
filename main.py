from pyrlang import Node, Atom, GeventEngine # or AsyncioEngine

def main():
    eng = GeventEngine()  # or AsyncioEngine
    node = Node(node_name="py@127.0.0.1", cookie="COOKIE", engine=eng)

    fake_pid = node.register_new_process()

    # To be able to send to Erlang shell by name first give it a
    # registered name: `erlang:register(shell, self()).`
    # To see an incoming message in shell: `flush().`
    node.send(sender=fake_pid,
              receiver=(Atom('erl@127.0.0.1'), Atom('shell')),
              message=Atom('hello'))

    eng.run_forever()

if __name__ == "__main__":
    main()
