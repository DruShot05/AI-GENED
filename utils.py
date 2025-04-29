def select_move():
    from moves import player_moves
    print("\nChoose your move:")
    for idx, move in enumerate(player_moves):
        print(f"{idx+1}. {move}")

    choice = int(input("Enter move number: ")) - 1
    if 0 <= choice < len(player_moves):
        return player_moves[choice]
    else:
        print("Invalid move, choosing Jab by default.")
        return "Jab"
