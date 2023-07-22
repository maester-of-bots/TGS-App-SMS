# SMS Buddy

SMS Buddy is a Python-based GUI application for sending SMS messages using email servers such as Gmail.

## Features

- Send SMS messages to multiple mobile network providers
- Customize your SMTP servers
- Send the same message multiple times at once

## Dependencies

SMS Buddy depends on the following Python libraries:

- `smtplib`: Included in standard Python distributions
- `PySimpleGUI`: Can be installed with pip via `pip install PySimpleGUI`

## Usage

1. Run the program.
2. Fill the "Email Info" fields with your email address, email password, SMTP server, and SMTP port (For Gmail users, SMTP server is 'smtp.gmail.com' and SMTP port is '587').
3. Fill the "SMS Details" fields with the cell phone number, select the provider, type the message you want to send and the number of times you want to send it.
4. Press the "Send" button to send the SMS.

## Supported Carriers

Currently, the following mobile network providers are supported:

- Verizon
- AT&T
- Sprint
- T-Mobile
- Boost Mobile
- Cricket
- MetroPCS
- Straight Talk

## Security

This program doesn't store or transmit your email password or any other personal information. The information you provide is used locally to send the messages.

## Troubleshooting

If a message fails to send, check if your email address, password, SMTP server, port, recipient's cell number and provider are entered correctly. For Gmail users, enabling "Less secure apps" in Gmail settings might be necessary. Check Google's support page for more information.

## Contributing

Contributions are welcomed. Open an issue or submit a pull request to contribute.

## License

SMS Buddy is under the MIT License. See `LICENSE` for more information.
