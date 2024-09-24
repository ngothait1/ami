def printColored(text, color="blake", size=20):
  return f'<p id="idText" style="font-size: {size}; color: {color} ;"> {text} </p>'

def printGreen(text, size_font=50):
  return printColored(text, "green", size_font)

def printRed(text, size_font=50):
  return printColored(text, "red", size_font)

def printBlue(text, size_font=50):
  return printColored(text, "blue", size_font)