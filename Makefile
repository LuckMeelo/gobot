NAME = pbrain-gomoku-ai

RM = rm -rf

all: $(NAME)

$(NAME):
	ln -s src/app.py $(NAME)
	chmod +x $(NAME)

fclean: clean
	$(RM) $(NAME)

clean:
	$(RM) $(shell find . -type d -name "__pycache__")
	$(RM) .pytest_cache

re: fclean all

tests_run:
	pytest

.PHONY: all fclean clean re