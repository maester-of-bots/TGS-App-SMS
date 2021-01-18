import smtplib

import PySimpleGUI as sg

carriers = (
    ['att', '@txt.att.net'],
    ['verizon', '@vtext.com'],
    ['boost', '@myboostmobile.com'],
    ['cricket', '@sms.mycricket.com'],
    ['metropcs', '@mymetropcs.com'],
    ['sprint', '@messaging.sprintpcs.com'],
    ['straighttalk', '@vtext.com'],
    ['tmobile', '@tmomail.net'],
)

carrier_names = []
carrier_extensions = []

for entry in carriers:
    carrier_names.append(entry[0])
    carrier_extensions.append(entry[1])


def e_text(text, justification='c', size=(15, 1), key='--'):
    return sg.Text(text + ':', justification=justification, size=size, key=key)


def e_input(text, justification='c', size=(15, 1), key='--', password_char=None):
    return sg.InputText(text, justification=justification, size=size, key=key, password_char=password_char)


def e_button(text, size=(35, 1), key='--'):
    return sg.Button(text, size=size, key=key)


# Define text labels
text_email = e_text("Email address", key='-text_email-')
text_password = e_text("Password", key='-text_password-')
text_cell = e_text("Cell Phone", key='-text_cell-')

text_msg = e_text("Message to send", key='-text_msg-')
text_count = e_text("Times to send", key='-text_count-')
text_server = e_text("SMTP Server", key='-text_server-')
text_port = e_text("SMTP Port", key='-text_port-')
text_provider = e_text("Providers", key='-text_provider-')

# Define input boxes
input_email = e_input("", key='-input_email-')
input_password = e_input("", password_char="*", key='-input_password-')
input_cell = e_input("", key='-input_cell-')

input_msg = e_input("Thank you for subscribing to Cat Facts!", key='-input_msg-')
input_count = e_input("5", key='-input_count-')
input_server = e_input("smtp.gmail.com", key='-input_server-')
input_port = e_input("587", key='-input_port-')
Combo_provider = sg.Combo(values=carrier_names, size=(15, 1), key='-Combo_provider-', change_submits=True)

# Define button
button_submit = e_button("Send", key='-button_submit-')

# Make up some columns
col1 = sg.Col(layout=[
    [text_email],
    [text_password],
    [text_server],
    [text_port]
])

col2 = sg.Col(layout=[
    [input_email],
    [input_password],
    [input_server],
    [input_port]
])

col3 = sg.Col(layout=[
    [text_cell],
    [text_provider],
    [text_msg],
    [text_count],
])

col4 = sg.Col(layout=[
    [input_cell],
    [Combo_provider],
    [input_msg],
    [input_count],

])

# Make columns into frames
frame_auth = sg.Frame(title="Email Info", layout=[[col1, col2]])
frame_msg = sg.Frame(title="SMS Details", layout=[[col3, col4]])

# Make an output box
output = sg.Output(size=(45, 7), font='Helvetica 10', key='-output-', visible=True)


# Log into Gmail
def gmailLogin(data):
    gmail = smtplib.SMTP(data[2], data[3])
    gmail.starttls()
    gmail.login(data[0], data[1])
    return gmail


# Send some texts
def hello_friend(data):
    gmail = gmailLogin(data)
    count = [0] * int(data[6])
    for x in range(0, len(count)):
        try:
            gmail.sendmail(data[0], data[4], data[5])
            print("Status: Successfully sent message #" + str(x + 1))
        except:
            print("Failed to send.")
    gmail.quit()


layout = [
    [frame_auth],
    [frame_msg],
    [button_submit],
    [output]
]

window = sg.Window(
    'SMS Buddy', layout,
    default_element_size=(30, 2), resizable=True,
    font=('Helvetica', ' 13'),
    icon='images/logo.ico',
    return_keyboard_events=True,

)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    elif event == "-button_submit-":
        data = []
        data.append(values['-input_email-'])  # 0
        data.append(values['-input_password-'])  # 1
        data.append(values['-input_server-'])  # 2
        data.append(values['-input_port-'])  # 3
        data.append(values['-input_cell-'])  # 4
        data.append(values['-input_msg-'])  # 5
        data.append(values['-input_count-'])  # 6
        data.append(values['-Combo_provider-'])  # 7
        loc = carrier_names.index(data[7])
        data[4] = data[4] + carriers[loc][1]
        try:
            hello_friend(data)
        except Exception as e:
            print(e)
