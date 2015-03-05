all : main


main : main.o world_class.o
	g++ -o main main.o world_class.o

main.o : main.cpp
	g++ -c main.cpp

world_class.o : world_class.cpp
	g++ -c world_class.cpp
