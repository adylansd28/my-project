"""
Assigment: W02 Prove - Tic-Tac-Toe.
Author: Dilan Salas.
"""
import os
import time

game_interface = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def main():
    game_presentation()
    in_game(game_interface)
    game_over()

def game_presentation():
    os.system("cls")
    print("Tic-Tac-Toe")
    print()
    print("Love is a game of tic-tac-toe, Constantly waiting for the next X or O.- Lang Leav -")
    print()
    print("Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, \na column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.")
    print()
    print("Rules")
    print("1. The game is played on a grid that is three squares by three squares.")
    print("2. Player one uses x's. Player two uses o's.")
    print("3. Players take turns putting their marks in empty squares.")
    print("4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.")
    print("5. If all nine squares are full and neither player has three in a row, the game ends in a draw.")
    print()
    ready = input("Are you ready to Play? (Type any letter and press enter)")
    os.system("cls")

def in_game(interface):
    game_ON = True
    someone_won = False
    turn = 1
    square_selected = []

    while game_ON:
        os.system("cls")
        run_interface(interface)
        print()

        if turn > 0:
            playing_symbol = "X"
        elif turn < 0:
            playing_symbol = "O"
        
        square_selection = get_cell_selected(playing_symbol)

        if square_selection in square_selected:
            print("That square has been selected before, please choose other square")
            time.sleep(2)
            continue
        else:
            square_selected.append(square_selection)
            interface = new_interface(game_interface, square_selection, playing_symbol)

        turn = turn * (-1)

        result_review = identify_result(interface, someone_won)

        if len(square_selected) == 9:
            if result_review[1] == True:
                run_interface(interface)
                print(f"{result_review[0]} has won!")
                time.sleep(3)
                game_ON = False
            else:
                run_interface(interface)
                print("The game has finished as a Draw")
                game_ON = False
        elif result_review[1] == True:
            run_interface(interface)
            print(f"{result_review[0]} has won!")
            time.sleep(3)
            game_ON = False

def game_over():
    os.system("cls")
    print("Game Over")

def identify_result(matrix, boolean_result):
    if matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]:
        #1st row analisys
        boolean_result = True
        condition_pair = [matrix[0][0], boolean_result]
    elif matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]:
        #2nd row analisys
        boolean_result = True
        condition_pair = [matrix[1][0], boolean_result]
    elif matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]:
        #3rd row analisys
        boolean_result = True
        condition_pair = [matrix[2][0], boolean_result]
    elif matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
        #1st column analisys
        boolean_result = True
        condition_pair = [matrix[0][0], boolean_result]
    elif matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
        #2nd column analisys
        boolean_result = True
        condition_pair = [matrix[0][1], boolean_result]
    elif matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
        #3rd column analisys
        boolean_result = True
        condition_pair = [matrix[0][2], boolean_result]
    elif matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
        #1st diagonal analisys
        boolean_result = True
        condition_pair = [matrix[0][0], boolean_result]
    elif matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2]:
        #2nd diagonal analisys
        boolean_result = True
        condition_pair = [matrix[2][0], boolean_result]
    else:
        condition_pair = [matrix[0][0], boolean_result]

    return condition_pair

def get_cell_selected(symbol):
    selection = int(input(f"{symbol}'s turn to choose a square (1-9): "))
    return selection

def new_interface(starting_interface, cell_selected, symbol):

    new_interface_matrix = starting_interface

    if cell_selected >=  1 and cell_selected < 4:
        row = 0
        index = cell_selected - 1
    elif cell_selected >=  4 and cell_selected < 7:
        row = 1
        index = cell_selected - 4
    elif cell_selected >=  7 and cell_selected < 10:
        row = 2
        index = cell_selected - 7

    new_interface_matrix[row][index] = symbol

    return new_interface_matrix
    
def run_interface(interface):
    """
    interface_cells_list = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    """
    os.system("cls")
    print("+ - + - + - +")
    print(f"| {interface[0][0]} | {interface[0][1]} | {interface[0][2]} |")
    print("+ - + - + - +")
    print(f"| {interface[1][0]} | {interface[1][1]} | {interface[1][2]} |")
    print("+ - + - + - +")
    print(f"| {interface[2][0]} | {interface[2][1]} | {interface[2][2]} |")
    print("+ - + - + - +")

if __name__ == "__main__":
    main()