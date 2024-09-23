import pygame

WIDTH = 550
background_color = (251,247,245)
base_num_color = (53, 31, 151)
grid = [[0 for r in range(9)] for c in range(9)]
win = pygame.display.set_mode((WIDTH, WIDTH))

def main():
    initialize_grid()
    create_grid()
    populate_grid()
    set_difficulty_level()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def initialize_grid():
    pygame.init()
    pygame.font.init()
    win.fill(background_color)
    
    for i in range(10):
        if (i%3 == 0): #bold the dividing lines
            pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 4) #vertical lines
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 4) #horizontal lines
        else:
            pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 2) #vertical lines
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2) #horizontal lines
    
    pygame.display.update()
    pygame.display.set_caption("Adir's Sudoku")

def create_grid():
    print(grid)

def populate_grid():
    numFont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(9):
        for j in range(9):
            value = numFont.render(str(grid[i][j]), True, base_num_color)
            win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

def set_difficulty_level():
    return

def check_correctness():
    return

if __name__ == "__main__":
    main()