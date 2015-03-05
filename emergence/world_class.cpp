/*
	Alexandra Nilles
*/

#include "world_class.h"
#include <iostream>
#include <string>

using namespace std;

//constructor
world::world(int sz) {
    size = sz;
    //map = static_cast<agent*> (::operator new (sizeof(agent[size*size])));
    map = new agent[size*size]();
    int i;
    for(i=0; i<size*size; ++i) {
        map[i] = NULL;
    }
}

void world::print_map() {
    int i,j;
    for (i=0; i < size; ++i) {
        for (j=0; j < size; ++j) {
            cout << map[i*size + j].rep;
        }
        cout << endl;
    }

}

void world::insert_agent(int x, int y, int orientation) {
    agent * new_agent = new agent();
    map[x*size + y] = new_agent;
    map[x*size + y].exists = true;
    map[x*size + y].rep = "x";
    map[x*size + y].x = x;
    map[x*size + y].y = y;
    map[x*size + y].orientation = orientation;



}

agent::agent() {
    rep = "_";
    exists = false;
};
