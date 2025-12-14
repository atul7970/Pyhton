def serve_chai():
    yield "Boil water"
    yield "Steep tea"
    yield "Add milk and sugar"
    yield "Serve chai"

stall = serve_chai()

for step in stall:
    print(step)

print(next(serve_chai()))  # This will print the first step of a new chai preparation