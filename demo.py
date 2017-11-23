import werobot

robot = werobot.WeRoBot(token='tokenhere');

@robot.text
def hello_world():
    return 'hello world!'

robot.run()