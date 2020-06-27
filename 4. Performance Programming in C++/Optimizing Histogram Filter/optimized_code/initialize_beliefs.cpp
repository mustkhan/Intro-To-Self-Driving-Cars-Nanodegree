#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	int i, j, height, width;
  	float prob_per_cell;
  
  	vector < vector <float> > newGrid;
  	//newGrid.reserve(height);
	vector <float> newRow;
  	//newRow.reserve(width);
  	
  //Note: It appears that reserving space increases 
  	//the time it takes to run this function after testing

	height = grid.size();
	width = grid[0].size();
 

  	prob_per_cell = 1.0 / ( (float) height * width) ;

  	// OPTIMIZATION: Is there a way to get the same results 	// without nested for loops?  	
  	for (int j = 0; j < width; j++) {
        newRow.push_back(prob_per_cell);
    }
    
    for (int i = 0; i < height; i++) {
        newGrid.push_back(newRow);
    }
  
    return newGrid;
}