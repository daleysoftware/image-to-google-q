include Makefile.common

.PHONY: all build ps logs stop up clean interactive

all: clean build up
	echo
	echo "Success. All systems running. Use \`make logs\` for more detail."

build:
	${COMPOSE} build

ps:
	${COMPOSE} ps

logs:
	${COMPOSE} logs -f

stop:
	${COMPOSE} stop

up:
	${COMPOSE} up -d

clean: stop
	${COMPOSE} rm -fv

interactive:
	docker exec -it ${CONTAINER} bash
