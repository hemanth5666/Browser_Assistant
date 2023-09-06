import PySimpleGUI as sg
import webbrowser
import cv2
from pytesseract import image_to_string
import webbrowser
import cv2



def lens():
    """
    The function `lens()` captures video from the webcam, resizes the frames, converts them to text
    using OCR, and then calls other functions based on the recognized text.
    """
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, frame = cap.read()
        frame = cv2.resize(frame, (1366, 768))
        a = image_to_string(frame)
        if a != None and a != " ":
            edge(a)
            chrome(a)
            duck(a)
            break   

def edge(text):
    """
    The above code defines three functions that open a web browser and perform a search on different
    search engines.
    
    :param text: The "text" parameter is a string that represents the search query or text that you want
    to search for in the respective search engines
    """
    iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
    webbrowser.open("https://www.bing.com/search?q=%s" % text)

def chrome(text):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open("https://google.com/search?q=%s" % text)

def duck(text):
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open("https://duckduckgo.com/?q=%s" % text)


sg.theme("Light Blue 2")

font = ("Times of Roman", 19)
layout = [
        [sg.Text('                   BROWSER ASSISTANT', size=(100, 4), key='-bold-', font=("Merriweather",30))],

        [sg.Text('search', size=(5,0),pad=(30,0),font=font), sg.InputText(font=font)],
        [sg.Button('chrome', pad=(100, 10), size=(8, 2), font=font),sg.Button('edge', pad=(50, 10), size=(8, 2), font=font),sg.Button('duck', pad=(50, 10), size=(8, 2), font=font)],
        [sg.Button('lens',size=(8,2),font=font,pad=(150,45))]
]

window = sg.Window(" ", layout,size=(895,640))

# The code block you provided is the event loop of a PySimpleGUI application. It continuously waits
# for user events and performs corresponding actions based on the event.
while True:  # Event Loop
    event, values = window.read()
    try:
        text=values[0]
        if event == "lens":
            try:
                lens()
            except:
                None
        elif event == "edge":
            if text!=None:
                edge(text)
        elif event == "chrome":
            if text!=None:
                chrome(text)
        elif event == "duck":
            if text !=None:
                duck(text)
    except:
        None

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()

