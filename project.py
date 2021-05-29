"""
File: project.py
---------------------
This project tries to implement the game of Tic-Tac-Toe
"""

from simpleimage import SimpleImage
from TextGrid import TextGrid, Cell

def main():
    play()
    #get_move("X")
    #x = imageX()
    #o = imageO()

def check_victory(grid, winner):
    # hard coding for 3x3 game board
    print(grid)
    #print(winner)
    c = 1
    for i in range(3):
        
        cell1 = grid.get_cell(i,0)
        cell2 = grid.get_cell(i,1)
        cell3 = grid.get_cell(i,2)
        if cell1.value == winner and cell2.value == winner and cell3.value == winner:
            pos = [cell1.x,cell1.y,cell2.x,cell2.y,cell3.x,cell3.y]
            return [winner,c,pos]
        c = c+1
        cell1 = grid.get_cell(0,i)
        cell2 = grid.get_cell(1,i)
        cell3 = grid.get_cell(2,i)
        if cell1.value == winner and cell2.value == winner and cell3.value == winner:
            pos = [cell1.x,cell1.y,cell2.x,cell2.y,cell3.x,cell3.y]
            return [winner,c,pos]
        c = c+1
    cell1 = grid.get_cell(0,0)
    cell2 = grid.get_cell(1,1)
    cell3 = grid.get_cell(2,2)
    if cell1.value == winner and cell2.value == winner and cell3.value == winner:
        pos = [cell1.x,cell1.y,cell2.x,cell2.y,cell3.x,cell3.y]
        return [winner,c,pos]
    c = c+1
    cell1 = grid.get_cell(0,2)
    cell2 = grid.get_cell(1,1)
    cell3 = grid.get_cell(2,0)
    if cell1.value == winner and cell2.value == winner and cell3.value == winner:
        pos = [cell1.x,cell1.y,cell2.x,cell2.y,cell3.x,cell3.y]
        return [winner,c,pos]
    return ["",0]

def get_move(mark):
    move = input("Enter position to put "+mark+" : ")
    move.strip()
    move = move.split(",")
    while True:
        if len(move)<2:
            print("Wrong input! Input format -> x,y :")
            move = input("Enter position to put "+mark+" : ")
            move.strip()
            move = move.split(",")
        else:
            break
    pos = []
    for ch in move:
        pos.append(int(ch))
    #print(pos)
    return pos

def get_correct_move(mark,grid):
    position = get_move(mark)
    x = position[0] - 1
    y = position[1] - 1
    while True:
        if (x<0 or x>2) and (y<0 or y>2):
            print("Wrong input! Position value can be 1 or 2 or 3. ")
            position = get_move(mark)
            x = position[0] - 1
            y = position[1] - 1
        else: 
            myCell = grid.get_cell(x,y)
            if myCell.value == "X" or myCell.value == "O":
                print("Position already filled, give some other position: ")
                position = get_move(mark)
                x = position[0] - 1
                y = position[1] - 1
            else:
                return [x,y]


def play():
    # prints the welcome texts
    print("Welcome to Tic-Tac-Toe")
    print("Player1 takes X")
    print("Player2 takes 0")
    board = SimpleImage('board_2.jpg')
    pause = input("Check the position and input format. Press enter to procees!")
    board.show()

    """
    Maintaining a word grid corresponding to the game board
    """
    n_rows = 3
    n_cols = 3
    grid = TextGrid.blank(n_rows,n_cols)

    """
    Maintaining a big picture of the game board
    """
    patch_size = 420
    width = n_cols * patch_size
    height = n_rows * patch_size
    final_image = SimpleImage('board_3.jpg')
    

    x = imageX()
    o = imageO()
    image = [x,o]
    winner = ["",0]
    turn = ["X","O"]

    for k in range(n_rows*n_cols):           #n_rows*n_cols
        player = (k%2) + 1
        print("Player"+str(player)+"'s turn ")
        position = get_correct_move(turn[k%2],grid)
        i = position[0]
        j = position[1]
        put_patch(final_image,i*patch_size,j*patch_size,image[k%2])
        myCell = grid.get_cell(i,j)
        myCell.value = turn[k%2]

        final_image.show()
        winner = check_victory(grid,turn[k%2])
        if winner[0] != "":
            print("Player"+str(player)+" is Winner !")
            dummy = input("The Winner played "+winner[0]+". Press Enter : ")
            big_picture(grid,final_image,winner)
            return
    print("It's a Draw! ")


def big_picture(grid,final_board,winner):
    #final_board.show()
    c = winner[1]
    #print(c)
    final_image = SimpleImage.blank(final_board.width,final_board.height)
    for y in range(final_board.height):
        for x in range(final_board.width):
            pixel = final_board.get_pixel(x,y)
            final_image.set_pixel(x,y,pixel)

    if c <= 6:
        if c%2 == 1:
            filename = winner[0]+"b2.jpg"
        else:
            filename = winner[0]+"b4.jpg"
    elif c==7:
        filename = winner[0]+"b1.jpg"
    else:
        filename = winner[0]+"b3.jpg"
    patch1 = SimpleImage(filename)

    #patch1.show()
    final_image.show()
    pos = winner[2]
    patch_size = 420

    put_patch(final_image,pos[0]*patch_size,pos[1]*patch_size,patch1)
    #final_image.show()
    put_patch(final_image,pos[2]*patch_size,pos[3]*patch_size,patch1)
    #final_image.show()
    put_patch(final_image,pos[4]*patch_size,pos[5]*patch_size,patch1)
    final_image.show()

    filename1 = winner[0]+"_trophy.jpg"
    image = SimpleImage(filename1)
    image.show()
    


def put_patch(final_image, start_x, start_y, patch):
    '''
    Implement this function to put a patch on the final combined image.
    It receives the patch image and the location as to where the patch goes.
    Returns the partially patched final image.
    '''
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x,y)
            final_image.set_pixel(x+start_x, y+start_y, pixel)
    

def imageX():
    image = SimpleImage('X.jpg')
    #image.show()
    bordered_img = add_border(image, 10)
    #bordered_img.show()
    return bordered_img

def imageO():
    image = SimpleImage('O.jpg')
    #image.show()
    bordered_img = add_border(image, 10)
    #bordered_img.show()
    return bordered_img


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    new_width = original_img.width + 2*border_size
    new_height = original_img.height + 2*border_size
    image = SimpleImage.blank(new_width,new_height)
    for y in range(new_height):
        for x in range(new_width):
            if x<border_size or y<border_size or x>=border_size+original_img.width or y>=border_size+original_img.height:
                pixel = image.get_pixel(x,y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel = original_img.get_pixel(x-border_size,y-border_size)
                image.set_pixel(x,y,pixel)

    return image


if __name__ == '__main__':
    main()
