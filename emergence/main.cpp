/*
*/

#include <iostream>
#include <string>
#include "world_class.h"

using namespace std;

int main() {
    world small = world(5);
    small.print_map();

    agent test = agent();
    small.insert_agent(1, 1, 1);
    small.print_map();


	return 0;
}
