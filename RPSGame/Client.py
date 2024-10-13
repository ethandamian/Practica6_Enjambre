from Network import Network  # Make sure the Network class is in a file named 'network.py'

def main():
    net = Network()
    try:
        player = int(net.getPlayer())
        print(player)
        print(f"Connected to the server as player {player}")
        
        print(f"You are player {player}")

        while True:
            move = input("Enter your move (Rock, Paper, Scissors) or 'quit' to exit: ").strip().lower()
            if move == "quit":
                break
            elif move not in ["rock", "paper", "scissors"]:
                print("Invalid move. Please enter Rock, Paper, or Scissors.")
                continue

            response = net.send(move)
            if not response:
                print("Game ended or server error.")
                break

            print("Waiting for the other player...")
            if response.both_moved():
                winner = response.winner()
                if winner == -1:
                    print("It's a tie!")
                elif int(player) == winner:
                    print("You won!")
                else:
                    print("You lost!")

                net.send("reset")
                print("Game reset. Make your move!")
            else:
                print("Waiting for the other player to make a move...")    
        
        net.client.close()
    except Exception as e:
        print(e)
        print("Connection lost.")
        net.client.close()


main()
