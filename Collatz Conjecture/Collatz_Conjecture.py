
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

def update(num, sequence, line):
    line.set_data(range(num+1), sequence[:num+1])
    return line,

def animate_collatz(n):
    sequence = collatz_sequence(n)
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(sequence) - 1)
    ax.set_ylim(0, max(sequence))
    ax.set_title(f"Collatz Conjecture for {n}")
    ax.set_xlabel("Steps")
    ax.set_ylabel("Value")
    
    line, = ax.plot([], [], lw=2)

    ani = animation.FuncAnimation(fig, update, frames=len(sequence), fargs=[sequence, line],
                                  interval=500, blit=True, repeat=False)

    plt.show()

def main():
    try:
        n = int(input("Enter a positive integer: "))
        animate_collatz(n)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
