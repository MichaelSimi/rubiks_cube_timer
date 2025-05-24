import pygame
import random
import time








# Define possible moves
moves = [
    "R", "L", "U", "D", "F", "B",
    "R'", "L'", "U'", "D'", "F'", "B'",
    "R2", "L2", "U2", "D2", "F2", "B2",
]






def scramble():
    scramble = []
    last_face = None
    for _ in range(20):  # scramble length is 20
        move = random.choice(moves)
        while move[0] == last_face:
            move = random.choice(moves)
        scramble.append(move)
        last_face = move[0]
    return " ".join(scramble)








pygame.init()
font = pygame.font.Font(None, 36)
fontmedium = pygame.font.Font(None, 48)
fontbig = pygame.font.Font(None, 72)
fontHUGE = pygame.font.Font(None, 300)
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rubik's Cube Timer")
clock = pygame.time.Clock()
running = True








# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)






def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return hours, minutes, seconds








def print_elapsed_time(current_time):
    hours, minutes, seconds = format_time(current_time)
    elapsed_time_formatted1 = fontHUGE.render(f"{seconds:.2f}", True, WHITE)
    elapsed_time_formatted2 = fontHUGE.render(f"{minutes}:{seconds:.2f}", True, WHITE)
    elapsed_time_formatted3 = fontHUGE.render(f"{hours}:{minutes}:{seconds:.2f}", True, WHITE)
    if hours == 0 and minutes == 0:
        screen.blit(elapsed_time_formatted1, (WIDTH * 0.42 - 150, HEIGHT // 3))
    elif hours == 0:
        screen.blit(elapsed_time_formatted2, (WIDTH * 0.4 - 150, HEIGHT // 3))
    else:
        screen.blit(elapsed_time_formatted3, (WIDTH * 0.3 - 150, HEIGHT // 3))








is_timing = False
elapsed_time = 0
just_stopped = False
start_time = None




def key(event):
    global is_timing, start_time, just_stopped, elapsed_time, scramble_text, scroll_offset
    # stop the stopwatch on any keydown
    if event.type == pygame.KEYDOWN and is_timing:
        is_timing = False
        elapsed_time = time.time() - start_time
        start_time = None
        print(f"\nStopwatch stopped at {elapsed_time:.2f} seconds.")
        print_elapsed_time(current_time)
        pygame.draw.rect(screen, BLACK, (scramble_text.get_rect(topleft=(WIDTH * 0.2, HEIGHT * 0.0694444444444444))))
        scramble_text = fontmedium.render(scramble(), True, WHITE)
        just_stopped = True
        solve_times.append(elapsed_time)
        update_best_worst()
        update_average()
        # scroll to bottom after new solve
        rounded_numbers = [round(t, 2) for t in solve_times]
        solves_lines = [rounded_numbers[i:i+3] for i in range(0, len(rounded_numbers), 3)]
        rect_y = int(HEIGHT * 0.9)
        line_height = int(0.06 * HEIGHT)
        max_lines = int((rect_y - (HEIGHT * 0.13)) // line_height)
        total_lines = len(solves_lines)
        if total_lines > max_lines:
            scroll_offset = total_lines - max_lines
        else:
            scroll_offset = 0


    # Start the stopwatch on spacebar release
    elif event.type == pygame.KEYUP:
        if not is_timing and not just_stopped:
            is_timing = True
            start_time = time.time()
            print("Stopwatch started!")
        elif just_stopped:
            just_stopped = False  # allow restart after releasing space








# generate text
scramble_text = fontmedium.render(scramble(), True, WHITE)
next_scramble = fontmedium.render("next scramble", True, BLUE)
last_scramble = fontmedium.render("Show times", True, BLUE)




# track solve times
solve_times = []
best_time = None
worst_time = None
averageo5 = None




def update_best_worst():
    global best_time, worst_time
    if solve_times:
        best_time = min(solve_times)
        worst_time = max(solve_times)
    else:
        best_time = None
        worst_time = None




def best_worst(time_val):
    if time_val is None:
        return "--"
    h, m, s = format_time(time_val)
    if h == 0 and m == 0:
        return f"{s:.2f}"
    elif h == 0:
        return f"{m}:{s:.2f}"
    else:
        return f"{h}:{m}:{s:.2f}"
   
def update_average():
    global averageo5
    if solve_times:
        averageo5 = sum(solve_times) / len(solve_times)
    else:
        averageo5 = None




def average(time_val):
    if time_val is None:
        return "--"
    h, m, s = format_time(time_val)
    if h == 0 and m == 0:
        return f"{s:.2f}"
    elif h == 0:
        return f"{m}:{s:.2f}"
    else:
        return f"{h}:{m}:{s:.2f}"




# display best/worst times
best_label = fontbig.render("Best:", True, BLUE)
worst_label = fontbig.render("Worst:", True, BLUE)
average_label = fontbig.render("Average:", True, BLUE)
def draw_best_worst():
    best_str = best_worst(best_time)
    worst_str = best_worst(worst_time)
    best_time_text = fontbig.render(best_str, True, WHITE)
    worst_time_text = fontbig.render(worst_str, True, WHITE)
    screen.blit(best_label, (WIDTH * 0.7, HEIGHT * 0.2))
    screen.blit(best_time_text, (WIDTH * 0.81, HEIGHT * 0.2))
    screen.blit(worst_label, (WIDTH * 0.7, HEIGHT * 0.27))
    screen.blit(worst_time_text, (WIDTH * 0.83, HEIGHT * 0.27))




def draw_average():
    average_str = average(averageo5)
    averageo5_text = fontbig.render(average_str, True, WHITE)
    screen.blit(average_label, (WIDTH * 0.3, HEIGHT * 0.2))
    screen.blit(averageo5_text, (WIDTH * 0.475, HEIGHT * 0.2))
next_scramble_rect = next_scramble.get_rect(topleft=(WIDTH * 0.81, HEIGHT * 0.0027777777777778))
last_scramble_rect = last_scramble.get_rect(topleft=(WIDTH * 0.03, HEIGHT * 0.0027777777777778))
solves_rounded = False
scroll_offset = 0  # scrollng


while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        key(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if next_scramble_rect.collidepoint(mouse_x, mouse_y):
                pygame.draw.rect(screen, BLACK, (scramble_text.get_rect(topleft=(WIDTH * 0.2, HEIGHT * 0.0694444444444444))))
                scramble_text = fontmedium.render(scramble(), True, WHITE)
            elif last_scramble_rect.collidepoint(mouse_x, mouse_y):
                if solve_times:
                    solves_rounded = not solves_rounded
                else:
                    solves_rounded = False
        if solves_rounded and event.type == pygame.MOUSEWHEEL:
            # each scroll step moves by one line
            scroll_offset -= event.y  # event.y is +1 for up, -1 for down


    screen.fill(BLACK)
    screen.blit(scramble_text, (WIDTH * 0.2, HEIGHT * 0.0694444444444444))
    screen.blit(next_scramble, next_scramble_rect.topleft)
    screen.blit(last_scramble, last_scramble_rect.topleft)


    rect_width, rect_height = WIDTH, 50
    rect_x = int(0)
    rect_y = int(HEIGHT * 0.9)
 
    if solves_rounded:
        rounded_numbers = [round(t, 2) for t in solve_times]
        solves_lines = [rounded_numbers[i:i+3] for i in range(0, len(rounded_numbers), 3)]
        line_height = int(0.06 * HEIGHT)
        max_lines = int((rect_y - (HEIGHT * 0.13)) // line_height)
        total_lines = len(solves_lines)
        if scroll_offset < 0:
            scroll_offset = 0
        if scroll_offset > max(0, total_lines - max_lines):
            scroll_offset = max(0, total_lines - max_lines)
        last_time_index = len(rounded_numbers) - 1
        for idx, line in enumerate(solves_lines[scroll_offset:scroll_offset + max_lines]):
            y_pos = HEIGHT * (0.13 + idx * 0.06)
            x_pos = WIDTH * 0.01
            for i, t in enumerate(line):
                global_idx = (scroll_offset + idx) * 3 + i
                color = GREEN if global_idx == last_time_index else RED
                time_surface = fontmedium.render(f"{t:.2f}", True, color)
                screen.blit(time_surface, (x_pos, y_pos))
                x_pos += time_surface.get_width() + 10


    # show press_space only when timer is not running and not just stopped
    if not is_timing and not just_stopped:
        press_space = fontbig.render("Press any key to start the timer", True, WHITE)
        screen.blit(press_space, (WIDTH * 0.2, HEIGHT * 0.7))
    else:
        press_space = fontbig.render("Press any key to stop the timer", True, GREEN)
        screen.blit(press_space, (WIDTH * 0.2, HEIGHT * 0.7))








    # show elapsed time
    if is_timing and start_time is not None:
        current_time = time.time() - start_time
        print_elapsed_time(current_time)
    elif not is_timing and elapsed_time > 0:
        print_elapsed_time(elapsed_time)




    draw_best_worst()
    draw_average()




    pygame.display.flip()
    clock.tick(60)  # limit FPS to 60
pygame.quit()
