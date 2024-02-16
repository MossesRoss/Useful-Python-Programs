import pyperclip

def write_selected_text(filename="selecteds.txt"):
  """
  Copies selected text from the clipboard and writes it to a file.

  Args:
    filename: The name of the file to write the text to (default: "selecteds.txt").
  """

  try:
    selected_text = pyperclip.paste()
    with open(filename, "a") as f:
      f.write(selected_text + "\n")
    print(f"Selected text written to {filename}")
  except Exception as e:
    print(f"Error writing text: {e}")

while True:
  current_text = pyperclip.paste()
  previous_text = ""

  while current_text != previous_text:
    write_selected_text()
    previous_text = current_text

  time.sleep(0.1)
