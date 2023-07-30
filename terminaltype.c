#include <stdio.h>
#include <ncurses.h>

int main() 
{
     // initialize ncurses    
    initscr();
   
    // check if terminal supports color
    if (has_colors() == FALSE) {
        printf("Terminal does not support color\n");
        return 1;
    }


    start_color();

    //Defines color pairs
    init_pair(1, COLOR_CYAN, COLOR_BLACK);
    
    //Print text
    attron(COLOR_PAIR(1));
    printw("This is a string\n");
    attroff(COLOR_PAIR(1));

    //refreshes screen
    refresh();

    //waits for user input
    getch();

    endwin();

    return 0;
}
