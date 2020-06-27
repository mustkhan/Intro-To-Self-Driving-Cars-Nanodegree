#include "headers/blur.h"
#include "headers/zeros.h"
#include "headers/normalize.h"

using namespace std;

// OPTIMIZATION: Pass large variable by reference
vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {

	// OPTIMIZATION: window, DX and  DY variables have the 
    // same value each time the function is run.
  	// It's very inefficient to recalculate the vectors
    // every time the function runs. 
    // 
    // The const and/or static operator could be useful.
  	// Define and declare window, DX, and DY using the
    // bracket syntax: vector<int> foo = {1, 2, 3, 4} 
    // instead of calculating these vectors with for loops 
    // and push back

	vector <float> row;
	vector <float> newRow;

	static int height;
	static int width;
	float center, corner, adjacent;

	height = grid.size();
	width = grid[0].size();

	center = 1.0 - blurring;
	corner = blurring / 12.0;
	adjacent = blurring / 6.0;

	int i, j;
	float val;

	static vector<vector<float> > window{{corner, adjacent, corner},
                                  {adjacent, center, adjacent},
                                  {corner, adjacent, corner}};

	static vector <int> DX{-1, 0, 1};
	static vector <int> DY{-1, 0, 1};

	//int dx;
	//int dy;
	//int ii;
	//int jj;
	//int new_i;
	//int new_j;
	//float multiplier;
	//float newVal;

	// OPTIMIZATION: Use your improved zeros function
	vector<vector<float> > newGrid = zeros(height, width);

	for(int i=0; i<height; i++){
        for(int j=0; j<width; j++){
            float grid_val = grid[i][j];
            for(int dx=-1; dx<2; dx++){
                for(int dy=-1; dy<2; dy++){
                    float mult = window[dx+1][dy+1];
                    int new_i = (i + dy + height) % height;
                    int new_j = (j + dx + width) % width;
                    newGrid[new_i][new_j] += mult * grid_val;
                }
            }
        }
	}

	return normalize(newGrid);
}
