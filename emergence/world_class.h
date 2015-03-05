#ifndef WORLD_CLASS_H
#define WORLD_CLASS_H

#include <string>
using namespace std;

class agent {
    public:
        agent();
        string rep;
        int x;
        int y;
        int orientation;
        bool exists;

};

class world {
    public:
        world(int);
        int size;
        agent * map;

        void print_map();
        void insert_agent(int, int, int);




    private:

};


#endif
