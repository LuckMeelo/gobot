NAME = pbrain-gomoku-ai

RM = rm -rf

all: $(NAME)

$(NAME):
	ln -s src/app.py $(NAME)
	chmod +x $(NAME)

fclean: clean
	$(RM) $(NAME)

clean:
	$(RM) src/__pycache__
	$(RM) tests/__pycache__

re: fclean re

run_tests:
	pytest

.PHONY: all fclean clean re