##
## PROJECT 2022
## gobot
## File description:
## Makefile
##

NAME = pbrain-gomoku-ai

RM = rm -rf

all: $(NAME)

$(NAME):
	ln -s src/app.py $(NAME)
	chmod +x $(NAME)

fclean: clean
	$(RM) $(NAME)

clean:
	$(RM) __pycache__

re: fclean re

.PHONY: all fclean clean re