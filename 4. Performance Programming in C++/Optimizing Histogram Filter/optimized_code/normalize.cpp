#include "headers/normalize.h"
using namespace std;

// OPTIMIZATION: Pass variable by reference
vector< vector<float> > normalize(vector< vector <float> > &grid) {

  	// OPTIMIZATION: Avoid declaring and defining 				
   // intermediate variables that are not needed.
	int height = grid.size();
	int width = grid[0].size();

	vector< vector<float> > newGrid(height, vector<float>(width));

	// todo - your code here
	float total = 0.0;
	for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            total += grid[i][j]; //Sum of all the values in the grid
        }
	}

	for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            newGrid[i][j] = grid[i][j]/total; //Normalizing the grid by dividing the total
        }
	}

	return newGrid;
}
