import re
import matplotlib.pyplot as plt

# Open and read the log file
with open('log.txt', 'r') as file:
    log_data = file.read()

# Use regular expressions to extract the loss values
pattern = r'D_A: ([\d.]+) G_A: ([\d.]+) cycle_A: ([\d.]+) idt_A: ([\d.]+) D_B: ([\d.]+) G_B: ([\d.]+) cycle_B: ([\d.]+) idt_B: ([\d.]+)'
matches = re.findall(pattern, log_data)

# Extract individual losses
D_A_loss = [float(match[0]) for match in matches]
G_A_loss = [float(match[1]) for match in matches]
cycle_A_loss = [float(match[2]) for match in matches]
idt_A_loss = [float(match[3]) for match in matches]
D_B_loss = [float(match[4]) for match in matches]
G_B_loss = [float(match[5]) for match in matches]
cycle_B_loss = [float(match[6]) for match in matches]
idt_B_loss = [float(match[7]) for match in matches]

# Generate x-axis values (epochs)
epochs = range(1, len(matches) + 1)

# Plot the losses
plt.figure(figsize=(10, 6))
plt.plot(epochs, D_A_loss, label='D_A Loss')
plt.plot(epochs, G_A_loss, label='G_A Loss')
plt.plot(epochs, cycle_A_loss, label='Cycle_A Loss')
plt.plot(epochs, idt_A_loss, label='Idt_A Loss')
plt.plot(epochs, D_B_loss, label='D_B Loss')
plt.plot(epochs, G_B_loss, label='G_B Loss')
plt.plot(epochs, cycle_B_loss, label='Cycle_B Loss')
plt.plot(epochs, idt_B_loss, label='Idt_B Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss Visualization')
plt.legend()
plt.grid(True)
plt.show()