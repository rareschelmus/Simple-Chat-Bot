import aiml
import time
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("initialize.xml")
kernel.respond("load aiml")

kernel.setBotPredicate("name","Ergo")

# Press CTRL-C to break this loop
while True:
    message=raw_input(""
                      ">> ")

    if message=="quit":
        exit()
    else:
        response=kernel.respond(message)
        time.sleep(len(response)*0.05)
        print response
        topic=kernel.getPredicate("topic")



