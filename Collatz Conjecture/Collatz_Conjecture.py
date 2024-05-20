import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import random

def collatz_sequence(n):
    """Returns the Collatz sequence for a given number n."""
    if n <= 0:
        raise ValueError("The number must be positive and greater than zero.")
    
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

def generate_colors(num_colors):
    """Generate a list of distinct colors."""
    colors = []
    for i in range(num_colors):
        colors.append("hsl({}, 100%, 50%)".format(i * 360 // num_colors))
    return colors

def animate_collatz_range(start, end):
    sequences = {n: collatz_sequence(n) for n in range(start, end + 1)}
    max_steps = max(len(seq) for seq in sequences.values())
    colors = generate_colors(len(sequences))
    
    fig = make_subplots(rows=1, cols=1)
    
    
    for idx, (n, sequence) in enumerate(sequences.items()):
        fig.add_trace(go.Scatter(x=[0], y=[sequence[0]], mode="lines+markers", name=f"n={n}", line=dict(color=colors[idx])))
    
    frames = []
    for k in range(1, max_steps):
        frame_data = []
        for idx, (n, sequence) in enumerate(sequences.items()):
            if k < len(sequence):
                frame_data.append(go.Scatter(x=list(range(k + 1)), y=sequence[:k + 1], mode="lines+markers", line=dict(color=colors[idx])))
            else:
                frame_data.append(go.Scatter(x=list(range(len(sequence))), y=sequence, mode="lines+markers", line=dict(color=colors[idx])))
        frames.append(go.Frame(data=frame_data))
    
    fig.update(frames=frames)
    
    fig.update_layout(
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }]
    )
    
    fig.update_layout(
        title=f"Collatz Conjecture for numbers from {start} to {end}",
        xaxis_title="Steps",
        yaxis_title="Value",
        showlegend=True
    )
    
    fig.show()

def main():
    try:
        start = int(input("Enter the start of the range (positive integer): "))
        end = int(input("Enter the end of the range (positive integer): "))
        if start <= 0 or end <= 0 or start > end:
            raise ValueError("The range must consist of positive integers and start should be less than or equal to end.")
        animate_collatz_range(start, end)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

